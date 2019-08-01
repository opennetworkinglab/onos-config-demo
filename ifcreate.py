#!/usr/local/bin/python3

import pyangbind.lib.pybindJSON as pybindJSON
import pyangbind.lib.xpathhelper as xpathhelper

import ocbind

def ifcreate(ifname):
    ph = xpathhelper.YANGPathHelper()

    src_ocif = ocbind.openconfig_interfaces(path_helper=ph)

    src_ocif.interfaces.interface.add(ifname)
    newif = src_ocif.interfaces.interface[ifname]

    newif.config.description = "Linux " + ifname + " interface"
    newif.config.enabled = True
    newif.ethernet.config.duplex_mode = "FULL"
    newif.ethernet.config.auto_negotiate = True

    newif.subinterfaces.subinterface.add(0)
    subint0 = newif.subinterfaces.subinterface[0]
    subint0.config.description = "Primary public IP address"
    subint0.ipv4.addresses.address.add("192.0.2.1")

    nsub = subint0.ipv4.addresses.address["192.0.2.1"]
    nsub.config.prefix_length = 24

    # Serialise the entire object
    # print(pybindJSON.dumps(src_ocif))
    return pybindJSON.dumps(src_ocif)
