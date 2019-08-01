#!/bin/bash

cd $(dirname $0)

export PYBINDPLUGIN=`python3 -c 'import pyangbind; import os; print ("%s/plugin" % os.path.dirname(pyangbind.__file__));'`

pyang --plugindir $PYBINDPLUGIN -f pybind \
        --use-xpathhelper --split-class-dir ../ocbind \
     openconfig-interfaces@*.yang \
     openconfig-if-ip@*.yang \
     openconfig-lacp@*.yang \
     openconfig-platform@*.yang \
     openconfig-platform-linecard@*.yang \
     openconfig-platform-port@*.yang \
     openconfig-platform-transceiver@*.yang \
     openconfig-vlan@*.yang \
     openconfig-system@*.yang

#    openconfig-hercules-platform-linecard@*.yang \
#    openconfig-hercules-qos@*.yang \
#    openconfig-hercules-platform@*.yang \
#    openconfig-hercules-platform-chassis@*.yang \
#    openconfig-hercules-platform-port@*.yang \
#    openconfig-hercules@*.yang \
#    openconfig-hercules-interfaces@*.yang \
#    openconfig-hercules-platform-node@*.yang \

