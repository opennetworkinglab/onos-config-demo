# onos-config-demo
Simple application to demonstrate how to interact with µONOS configuration subsystem.

This is still work in progress. There are two separate experiments here, but they are not yet integrated.
This requires Python 3.7.4 or greater. You will also need to make sure that the requirements have been 
installed as well via:

```pip3 install -r requirements.txt```

### Python gNMI client
Allows get, set and delete of values from command-line now (drawn from the deprecated gnxi repo), but serves
as a demonstration of how to establish a gNMI connection to the onos-config service.

Here is an example usage of a get request against locally running `onos-config` gNMI northbound.
```
export CP=$HOME/go/src/github.com/onosproject/onos-config/test/certs
python3 py_gnmicli.py -e localhost:5150 -pkey $CP/client1.key -cchain $CP/client1.crt -rcert $CP/onf.cacrt \
    -t localhost-1 -x /system/
```

### Python OpenConfig bindings
A relevant subset of the OpenConfig YANG models have been checked in under the `yang` directory and a set of 
Python bindings were generated via the `compile-yang.sh` script, which uses the pyangbind plugin.
The generated bindings are checked-in under the `ocbind` directory.

A modified version of Rob Shakir's example script `rs-demo.py` is available and shows how one can manipulate 
OpenConfig compliant structures in Python and how such structures can be encoded/decoded to/from JSON.