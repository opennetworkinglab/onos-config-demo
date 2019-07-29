#!/usr/local/bin/python3

import os

import pyangbind.lib.pybindJSON as pybindJSON
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.serialise import pybindJSONDecoder

import json
import ocbind

ph = xpathhelper.YANGPathHelper()

src_ocif = ocbind.openconfig_interfaces(path_helper=ph)

src_ocif.interfaces.interface.add("eth0")
eth0 = src_ocif.interfaces.interface["eth0"]

eth0.config.description = "Linux eth0 interface"
eth0.config.enabled = True
eth0.ethernet.config.duplex_mode = "FULL"
eth0.ethernet.config.auto_negotiate = True

eth0.subinterfaces.subinterface.add(0)
subint0 = eth0.subinterfaces.subinterface[0]
subint0.config.description = "Primary public IP address"
subint0.ipv4.addresses.address.add("192.0.2.1")

nsub = subint0.ipv4.addresses.address["192.0.2.1"]
nsub.config.prefix_length = 24

# Serialise the entire object
# print(pybindJSON.dumps(src_ocif))
pybindJSON.dump(src_ocif, "/tmp/ocif.json")

# Deserialisation from a JSON file
# Arguments are:
#   path to JSON file
#   Python module to find the class in
#   The name of the class
dst_ocif = pybindJSON.load("/tmp/ocif.json", ocbind, "openconfig_interfaces", path_helper=ph)
# print(pybindJSON.dumps(dst_ocif))

src_ocif_json = json.load(open("/tmp/ocif.json", 'r'))

# Deserialisation from a JSON string
# Arguments are:
#   Loaded JSON object
#   Python module to find the class in
#   Name of the class

# In pyangbind 0.3.0 - pybindJSONDecoder becomes a static method - previously
# this should be specified as pybindJSONDecoder().load_json.
dst_ocif_str = pybindJSONDecoder.load_json(src_ocif_json, ocbind, "openconfig_interfaces", path_helper=ph)

# Serialise a particular list entry
# print(pybindJSON.dumps(src_ocif.interfaces.interface["eth0"]))
if not os.path.exists("/tmp/ocifs"):
    os.makedirs("/tmp/ocifs")
pybindJSON.dump(src_ocif.interfaces.interface["eth0"], "/tmp/ocifs/eth0.json")

# Load JSON files within a directory into a list, using the filename as the key
nph = xpathhelper.YANGPathHelper()
new_ocif = ocbind.openconfig_interfaces(path_helper=nph)
for fn in os.listdir("/tmp/ocifs"):
    k = fn.split(".")[0]
    # Create the list entry, since load_json needs the base object to exist
    if not k in new_ocif.interfaces.interface:
        new_ocif.interfaces.interface.add(k)
    target = new_ocif.interfaces.interface[k]
    #
    # Arguments are:
    #     JSON object to load from
    #     Target pyangbind class
    #     Base module (may be False if loading to an existing object)
    #     obj=Existing object
    #
    # Note that this load is not very clean, since we're really optimised for loading
    # entire objects, one might want to create wrappers inside pybindJSON to make this
    # nicer.
    pybindJSONDecoder.load_json(json.load(open("/tmp/ocifs/" + fn, 'r')), target, False, obj=target, path_helper=nph)
print(pybindJSON.dumps(new_ocif))