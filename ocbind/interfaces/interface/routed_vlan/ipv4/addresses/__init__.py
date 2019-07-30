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

from . import address
class addresses(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/routed-vlan/ipv4/addresses. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for address list
  """
  __slots__ = ('_path_helper', '_extmethods', '__address',)

  _yang_name = 'addresses'

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
    self.__address = YANGDynClass(base=YANGListType("ip",address.address, yang_name="address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)

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
      return ['interfaces', 'interface', 'routed-vlan', 'ipv4', 'addresses']

  def _get_address(self):
    """
    Getter method for address, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address (list)

    YANG Description: The list of configured IPv4 addresses on the interface.
    """
    return self.__address
      
  def _set_address(self, v, load=False):
    """
    Setter method for address, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.

    YANG Description: The list of configured IPv4 addresses on the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ip",address.address, yang_name="address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ip",address.address, yang_name="address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)""",
        })

    self.__address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address(self):
    self.__address = YANGDynClass(base=YANGListType("ip",address.address, yang_name="address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)

  address = __builtin__.property(_get_address, _set_address)


  _pyangbind_elements = OrderedDict([('address', address), ])


from . import address
class addresses(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/routed-vlan/ipv4/addresses. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for address list
  """
  __slots__ = ('_path_helper', '_extmethods', '__address',)

  _yang_name = 'addresses'

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
    self.__address = YANGDynClass(base=YANGListType("ip",address.address, yang_name="address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)

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
      return ['interfaces', 'interface', 'routed-vlan', 'ipv4', 'addresses']

  def _get_address(self):
    """
    Getter method for address, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address (list)

    YANG Description: The list of configured IPv4 addresses on the interface.
    """
    return self.__address
      
  def _set_address(self, v, load=False):
    """
    Setter method for address, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.

    YANG Description: The list of configured IPv4 addresses on the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ip",address.address, yang_name="address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ip",address.address, yang_name="address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)""",
        })

    self.__address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address(self):
    self.__address = YANGDynClass(base=YANGListType("ip",address.address, yang_name="address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)

  address = __builtin__.property(_get_address, _set_address)


  _pyangbind_elements = OrderedDict([('address', address), ])


from . import address
class addresses(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/routed-vlan/ipv4/addresses. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enclosing container for address list
  """
  __slots__ = ('_path_helper', '_extmethods', '__address',)

  _yang_name = 'addresses'

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
    self.__address = YANGDynClass(base=YANGListType("ip",address.address, yang_name="address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)

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
      return ['interfaces', 'interface', 'routed-vlan', 'ipv4', 'addresses']

  def _get_address(self):
    """
    Getter method for address, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address (list)

    YANG Description: The list of configured IPv4 addresses on the interface.
    """
    return self.__address
      
  def _set_address(self, v, load=False):
    """
    Setter method for address, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.

    YANG Description: The list of configured IPv4 addresses on the interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ip",address.address, yang_name="address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ip",address.address, yang_name="address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)""",
        })

    self.__address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address(self):
    self.__address = YANGDynClass(base=YANGListType("ip",address.address, yang_name="address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ip', extensions=None), is_container='list', yang_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='list', is_config=True)

  address = __builtin__.property(_get_address, _set_address)


  _pyangbind_elements = OrderedDict([('address', address), ])

