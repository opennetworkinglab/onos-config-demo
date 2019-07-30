from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
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
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-e', '--endpoint', type=str, help='gNMI address:port endpoint', required=True)
    parser.add_argument('-t', '--target', type=str, help='gNMI target', required=True)
    parser.add_argument('-m', '--mode', choices=['get', 'set', 'delete'], help='get, set or delete', default='get')
    parser.add_argument('-val', '--value', type=str, help='value', required=False)
    parser.add_argument('-pkey', '--private_key', type=str, help='Private key file path', required=True)
    parser.add_argument('-rcert', '--root_cert', type=str, help='Root CA file path', required=True)
    parser.add_argument('-cchain', '--cert_chain', type=str, help='Certificate file path', required=True)
    parser.add_argument('-x', '--xpath', type=str, help='gNMI path', required=True)
    return parser


def _path_names(xpath):
    if not xpath or xpath == '/':  # A blank xpath was provided at CLI.
        return []
    return xpath.strip().strip('/').split('/')  # Remove leading and trailing '/'.


def _parse_path(target, p_names):
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
    for key, value in kwargs.items():
        if value:
            kwargs[key] = six.moves.builtins.open(value, 'rb').read()
    return kwargs


def _create_stub(certs, endpoint):
    creds = gnmi_pb2_grpc.grpc.ssl_channel_credentials(
                        root_certificates=certs['root_cert'],
                        private_key=certs['private_key'],
                        certificate_chain=certs['cert_chain'])
    channel = gnmi_pb2_grpc.grpc.secure_channel(endpoint, creds)
    return gnmi_pb2_grpc.gNMIStub(channel)


def _format_type(json_value):
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
    val = gnmi_pb2.TypedValue()
    coerced_val = _format_type(json_value)
    type_to_value = {bool: 'bool_val', int: 'int_val', float: 'float_val', str: 'string_val'}
    value_type = type_to_value.get(type(coerced_val))
    if value_type:
        setattr(val, value_type, coerced_val)
    return val

def main():
    args = vars(_create_parser().parse_args())

    kwargs = {'root_cert': args['root_cert'], 'cert_chain': args['cert_chain'], 'private_key': args['private_key']}
    certs = _open_certs(**kwargs)
    stub = _create_stub(certs, args['endpoint'])
    paths = _parse_path(args['target'], _path_names(args['xpath']))

    mode = args['mode']
    if mode == 'get':
        response = stub.Get(gnmi_pb2.GetRequest(path=[paths], encoding='JSON_IETF'))
        print(response)
    elif mode == 'set':
        response = stub.Set(gnmi_pb2.SetRequest(update=[gnmi_pb2.Update(path=paths, val=_get_val(args['value']), )]))
        print(response)
    elif mode == 'delete':
        response = stub.Set(gnmi_pb2.SetRequest(delete=[paths]))
        print(response)

if __name__ == '__main__':
    main()
