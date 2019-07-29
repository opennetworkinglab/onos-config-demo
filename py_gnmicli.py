from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import json
import os
import re
import sys

import six

sys.path.append(os.path.join(os.path.dirname(__file__), "gnmi"))

try:
    import gnmi_pb2
    import gnmi_pb2_grpc
except ImportError:
    print('ERROR: Install dependencies from requirements.txt\n')

__version__ = '0.9'

_RE_PATH_COMPONENT = re.compile(r'''
^
(?P<pname>[^[]+)  # gNMI path name
(\[(?P<key>\w+)   # gNMI path key
=
(?P<value>.*)    # gNMI path value
\])?$
''', re.VERBOSE)


class Error(Exception):
    """Module-level Exception class."""


class XpathError(Error):
    """Error parsing xpath provided."""


class ValError(Error):
    """Error parsing provided val from CLI."""


class JsonReadError(Error):
    """Error parsing provided JSON file."""


class FindTypeError(Error):
    """Error identifying type of provided value."""


def _create_parser():
    """Create parser for arguments passed into the program from the CLI.

    Returns:
      Argparse object.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter, epilog='\nExample'
                                                                     ' GetRequest without user/password and over-riding Target certificate CN:'
                                                                     '\npython py_gnmicli.py -t 127.0.0.1 -p 8080 -x \'/access-points/'
                                                                     'access-point[hostname=test-ap]/\' -rcert ~/certs/target-cert.crt -o '
                                                                     'openconfig.example.com')
    parser.add_argument('-a', '--address', type=str, help='gNMI address', required=True)
    parser.add_argument('-p', '--port', type=str, help='gNMI port', required=True)
    parser.add_argument('-t', '--target', type=str, help='gNMI target', required=True)
    parser.add_argument('-m', '--mode',
                        choices=['get', 'set-update', 'set-replace', 'set-delete', 'subscribe'],
                        help='Mode of operation when interacting with network element.'
                             ' Default=get. If set, it can be either value \nor JSON '
                             'file (prepend filename with "@")', default='get')
    parser.add_argument('-val', '--value', type=str,
                        help='Value for SetRequest.'
                             '\nCan be Leaf value or JSON file. If JSON file, prepend'
                             ' with "@"; eg "@interfaces.json".',
                        required=False)
    parser.add_argument('-pkey', '--private_key', type=str, help='Private key file path', required=True)
    parser.add_argument('-rcert', '--root_cert', type=str, help='Root CA file path', required=True)
    parser.add_argument('-cchain', '--cert_chain', type=str, help='Certificate file path', required=True)
    parser.add_argument('-x', '--xpath', type=str, help='gNMI path', required=True)
    parser.add_argument('-f', '--format', type=str, action='store',
                        help='json or protobuff; default json',
                        choices=['json', 'protobuff'], default='json', required=False)
    parser.add_argument('-V', '--version', help='Print program version',
                        action='store_true', required=False)
    return parser


def _path_names(xpath):
    """Parses the xpath names.

    This takes an input string and converts it to a list of gNMI Path names. Those
    are later turned into a gNMI Path Class object for use in the Get/SetRequests.
    Args:
      xpath: (str) xpath formatted path.

    Returns:
      list of gNMI path names.
    """
    if not xpath or xpath == '/':  # A blank xpath was provided at CLI.
        return []
    return xpath.strip().strip('/').split('/')  # Remove leading and trailing '/'.


def _parse_path(target, p_names):
    """Parses a list of path names for path keys.

    Args:
      p_names: (list) of path elements, which may include keys.

    Returns:
      a gnmi_pb2.Path object representing gNMI path elements.

    Raises:
      XpathError: Unable to parse the xpath provided.
    """
    gnmi_elems = []
    for word in p_names:
        word_search = _RE_PATH_COMPONENT.search(word)
        if not word_search:  # Invalid path specified.
            raise XpathError('xpath component parse error: %s' % word)
        if word_search.group('key') is not None:  # A path key was provided.
            tmp_key = {}
            for x in re.findall(r'\[([^]]*)\]', word):
                tmp_key[x.split("=")[0]] = x.split("=")[-1]
            gnmi_elems.append(gnmi_pb2.PathElem(name=word_search.group(
                'pname'), key=tmp_key))
        else:
            gnmi_elems.append(gnmi_pb2.PathElem(name=word, key={}))
    return gnmi_pb2.Path(target=target, elem=gnmi_elems)


def _open_certs(**kwargs):
    """Opens provided certificate files.

    Args:
      root_cert: (str) Root certificate file to use in the gRPC channel.
      cert_chain: (str) Certificate chain file to use in the gRPC channel.
      private_key: (str) Private key file to use in the gRPC channel.

    Returns:
      root_cert: (str) Root certificate to use in the gRPC channel.
      cert_chain: (str) Certificate chain to use in the gRPC channel.
      private_key: (str) Private key to use in the gRPC channel.
    """
    for key, value in kwargs.items():
        if value:
            kwargs[key] = six.moves.builtins.open(value, 'rb').read()
    return kwargs


def _create_stub(certs, address, port):
    creds = gnmi_pb2_grpc.grpc.ssl_channel_credentials(
        root_certificates=certs['root_cert'], private_key=certs['private_key'],
        certificate_chain=certs['cert_chain'])
    channel = gnmi_pb2_grpc.grpc.secure_channel(address + ':' + port, creds)
    return gnmi_pb2_grpc.gNMIStub(channel)


def _format_type(json_value):
    """Helper to determine the Python type of the provided value from CLI.

    Args:
      json_value: (str) Value providing from CLI.

    Returns:
      json_value: The provided input coerced into proper Python Type.
    """
    if (json_value.startswith('-') and json_value[1:].isdigit()) or (
            json_value.isdigit()):
        return int(json_value)
    if (json_value.startswith('-') and json_value[1].isdigit()) or (
            json_value[0].isdigit()):
        return float(json_value)
    if json_value.capitalize() == 'True':
        return True
    if json_value.capitalize() == 'False':
        return False
    return json_value  # The value is a string.


def _get_val(json_value):
    """Get the gNMI val for path definition.

    Args:
      json_value: (str) JSON_IETF or file.

    Returns:
      gnmi_pb2.TypedValue()
    """
    val = gnmi_pb2.TypedValue()
    if '@' in json_value:
        try:
            set_json = json.loads(six.moves.builtins.open(
                json_value.strip('@'), 'rb').read())
        except (IOError, ValueError) as e:
            raise JsonReadError('Error while loading JSON: %s' % str(e))
        val.json_ietf_val = json.dumps(set_json).encode()
        return val
    coerced_val = _format_type(json_value)
    type_to_value = {bool: 'bool_val', int: 'int_val', float: 'float_val',
                     str: 'string_val'}
    if type_to_value.get(type(coerced_val)):
        setattr(val, type_to_value.get(type(coerced_val)), coerced_val)
    return val


def _get(stub, paths):
    """Create a gNMI GetRequest.

    Args:
      stub: (class) gNMI Stub used to build the secure channel.
      paths: gNMI Path

    Returns:
      a gnmi_pb2.GetResponse object representing a gNMI GetResponse.
    """
    return stub.Get(gnmi_pb2.GetRequest(path=[paths], encoding='JSON_IETF'))


def _set(stub, paths, set_type, json_value):
    """Create a gNMI SetRequest.

    Args:
      stub: (class) gNMI Stub used to build the secure channel.
      paths: gNMI Path
      set_type: (str) Type of gNMI SetRequest.
      json_value: (str) JSON_IETF or file.

    Returns:
      a gnmi_pb2.SetResponse object representing a gNMI SetResponse.
    """
    if json_value:  # Specifying ONLY a path is possible (eg delete).
        val = _get_val(json_value)
        path_val = gnmi_pb2.Update(path=paths, val=val, )

    kwargs = {}
    if set_type == 'delete':
        return stub.Set(gnmi_pb2.SetRequest(delete=[paths]), **kwargs)
    elif set_type == 'update':
        return stub.Set(gnmi_pb2.SetRequest(update=[path_val]), **kwargs)
    return stub.Set(gnmi_pb2.SetRequest(replace=[path_val]), **kwargs)


def main():
    argparser = _create_parser()
    args = vars(argparser.parse_args())
    if args['version']:
        print(__version__)
        sys.exit()

    mode = args['mode']
    address = args['address']
    port = args['port']

    root_cert = args['root_cert']
    cert_chain = args['cert_chain']
    private_key = args['private_key']

    target = args['target']
    xpath = args['xpath']
    json_value = args['value']

    form = args['format']
    paths = _parse_path(target, _path_names(xpath))

    kwargs = {'root_cert': root_cert, 'cert_chain': cert_chain, 'private_key': private_key}
    certs = _open_certs(**kwargs)
    stub = _create_stub(certs, address, port)

    if mode == 'get':
        print('Performing GetRequest, encoding=JSON_IETF', 'to', address,
              ' with the following gNMI Path\n', '-' * 25, '\n', paths)
        response = _get(stub, paths)
        print('The GetResponse is below\n' + '-' * 25 + '\n')
        if form == 'protobuff':
            print(response)
        elif response.notification[0].update[0].val.json_ietf_val:
            print(json.dumps(json.loads(response.notification[0].update[0].val.json_ietf_val), indent=2))
        else:
            print('JSON Format specified, but gNMI Response was not json_ietf_val')
            print(response)
    elif mode == 'set-update':
        print('Performing SetRequest Update, encoding=JSON_IETF', ' to ', address,
              ' with the following gNMI Path\n', '-' * 25, '\n', paths, json_value)
        response = _set(stub, paths, 'update', json_value)
        print('The SetRequest response is below\n' + '-' * 25 + '\n', response)
    elif mode == 'set-replace':
        print('Performing SetRequest Replace, encoding=JSON_IETF', ' to ', address,
              ' with the following gNMI Path\n', '-' * 25, '\n', paths)
        response = _set(stub, paths, 'replace', json_value)
        print('The SetRequest response is below\n' + '-' * 25 + '\n', response)
    elif mode == 'set-delete':
        print('Performing SetRequest Delete, encoding=JSON_IETF', ' to ', address,
              ' with the following gNMI Path\n', '-' * 25, '\n', paths)
        response = _set(stub, paths, 'delete', json_value)
        print('The SetRequest response is below\n' + '-' * 25 + '\n', response)
    elif mode == 'subscribe':
        print('This mode not available in this version')
        sys.exit()


if __name__ == '__main__':
    main()
