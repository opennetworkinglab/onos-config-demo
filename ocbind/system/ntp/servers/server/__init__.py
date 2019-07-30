# -*- coding: utf-8 -*-
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
elif six.PY2:
  import __builtin__

from . import config
from . import state
class server(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/ntp/servers/server. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of NTP servers to use for system clock
synchronization.  If '/system/ntp/enabled'
is 'true', then the system will attempt to
contact and utilize the specified NTP servers.
  """
  __slots__ = ('_path_helper', '_extmethods', '__address','__config','__state',)

  _yang_name = 'server'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
    else:
      self._path_helper = False

    self._extmethods = False
    self.__address = YANGDynClass(base=ReferenceType(referenced_path='../config/address', caller=self._path() + ['address'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['system', 'ntp', 'servers', 'server']

  def _get_address(self):
    """
    Getter method for address, mapped from YANG variable /system/ntp/servers/server/address (leafref)

    YANG Description: References the configured address or hostname of the
NTP server.
    """
    return self.__address
      
  def _set_address(self, v, load=False):
    """
    Setter method for address, mapped from YANG variable /system/ntp/servers/server/address (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.

    YANG Description: References the configured address or hostname of the
NTP server.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ReferenceType(referenced_path='../config/address', caller=self._path() + ['address'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=ReferenceType(referenced_path='../config/address', caller=self._path() + ['address'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)""",
        })

    self.__address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address(self):
    self.__address = YANGDynClass(base=ReferenceType(referenced_path='../config/address', caller=self._path() + ['address'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /system/ntp/servers/server/config (container)

    YANG Description: Configuration data for an NTP server.
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /system/ntp/servers/server/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for an NTP server.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /system/ntp/servers/server/state (container)

    YANG Description: Operational state data for an NTP server.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /system/ntp/servers/server/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data for an NTP server.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

  address = __builtin__.property(_get_address, _set_address)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)


  _pyangbind_elements = OrderedDict([('address', address), ('config', config), ('state', state), ])


from . import config
from . import state
class server(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/ntp/servers/server. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of NTP servers to use for system clock
synchronization.  If '/system/ntp/enabled'
is 'true', then the system will attempt to
contact and utilize the specified NTP servers.
  """
  __slots__ = ('_path_helper', '_extmethods', '__address','__config','__state',)

  _yang_name = 'server'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
    else:
      self._path_helper = False

    self._extmethods = False
    self.__address = YANGDynClass(base=ReferenceType(referenced_path='../config/address', caller=self._path() + ['address'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['system', 'ntp', 'servers', 'server']

  def _get_address(self):
    """
    Getter method for address, mapped from YANG variable /system/ntp/servers/server/address (leafref)

    YANG Description: References the configured address or hostname of the
NTP server.
    """
    return self.__address
      
  def _set_address(self, v, load=False):
    """
    Setter method for address, mapped from YANG variable /system/ntp/servers/server/address (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.

    YANG Description: References the configured address or hostname of the
NTP server.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ReferenceType(referenced_path='../config/address', caller=self._path() + ['address'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=ReferenceType(referenced_path='../config/address', caller=self._path() + ['address'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)""",
        })

    self.__address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address(self):
    self.__address = YANGDynClass(base=ReferenceType(referenced_path='../config/address', caller=self._path() + ['address'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /system/ntp/servers/server/config (container)

    YANG Description: Configuration data for an NTP server.
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /system/ntp/servers/server/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for an NTP server.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /system/ntp/servers/server/state (container)

    YANG Description: Operational state data for an NTP server.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /system/ntp/servers/server/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data for an NTP server.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

  address = __builtin__.property(_get_address, _set_address)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)


  _pyangbind_elements = OrderedDict([('address', address), ('config', config), ('state', state), ])


from . import config
from . import state
class server(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/ntp/servers/server. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of NTP servers to use for system clock
synchronization.  If '/system/ntp/enabled'
is 'true', then the system will attempt to
contact and utilize the specified NTP servers.
  """
  __slots__ = ('_path_helper', '_extmethods', '__address','__config','__state',)

  _yang_name = 'server'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
    else:
      self._path_helper = False

    self._extmethods = False
    self.__address = YANGDynClass(base=ReferenceType(referenced_path='../config/address', caller=self._path() + ['address'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return ['system', 'ntp', 'servers', 'server']

  def _get_address(self):
    """
    Getter method for address, mapped from YANG variable /system/ntp/servers/server/address (leafref)

    YANG Description: References the configured address or hostname of the
NTP server.
    """
    return self.__address
      
  def _set_address(self, v, load=False):
    """
    Setter method for address, mapped from YANG variable /system/ntp/servers/server/address (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.

    YANG Description: References the configured address or hostname of the
NTP server.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ReferenceType(referenced_path='../config/address', caller=self._path() + ['address'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address must be of a type compatible with leafref""",
          'defined-type': "leafref",
          'generated-type': """YANGDynClass(base=ReferenceType(referenced_path='../config/address', caller=self._path() + ['address'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)""",
        })

    self.__address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address(self):
    self.__address = YANGDynClass(base=ReferenceType(referenced_path='../config/address', caller=self._path() + ['address'], path_helper=self._path_helper, require_instance=True), is_leaf=True, yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='leafref', is_config=True)


  def _get_config(self):
    """
    Getter method for config, mapped from YANG variable /system/ntp/servers/server/config (container)

    YANG Description: Configuration data for an NTP server.
    """
    return self.__config
      
  def _set_config(self, v, load=False):
    """
    Setter method for config, mapped from YANG variable /system/ntp/servers/server/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration data for an NTP server.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_config(self):
    self.__config = YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)


  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /system/ntp/servers/server/state (container)

    YANG Description: Operational state data for an NTP server.
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /system/ntp/servers/server/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Operational state data for an NTP server.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

  address = __builtin__.property(_get_address, _set_address)
  config = __builtin__.property(_get_config, _set_config)
  state = __builtin__.property(_get_state, _set_state)


  _pyangbind_elements = OrderedDict([('address', address), ('config', config), ('state', state), ])

