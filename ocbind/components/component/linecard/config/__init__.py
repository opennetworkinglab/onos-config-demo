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

class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/linecard/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for linecards
  """
  __slots__ = ('_path_helper', '_extmethods', '__power_admin_state',)

  _yang_name = 'config'

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
    self.__power_admin_state = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'POWER_ENABLED': {}, 'POWER_DISABLED': {}},), default=six.text_type("POWER_ENABLED"), is_leaf=True, yang_name="power-admin-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/linecard', defining_module='openconfig-platform-linecard', yang_type='oc-platform-types:component-power-type', is_config=True)

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
      return ['components', 'component', 'linecard', 'config']

  def _get_power_admin_state(self):
    """
    Getter method for power_admin_state, mapped from YANG variable /components/component/linecard/config/power_admin_state (oc-platform-types:component-power-type)

    YANG Description: Enable or disable power to the linecard
    """
    return self.__power_admin_state
      
  def _set_power_admin_state(self, v, load=False):
    """
    Setter method for power_admin_state, mapped from YANG variable /components/component/linecard/config/power_admin_state (oc-platform-types:component-power-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_power_admin_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_power_admin_state() directly.

    YANG Description: Enable or disable power to the linecard
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'POWER_ENABLED': {}, 'POWER_DISABLED': {}},), default=six.text_type("POWER_ENABLED"), is_leaf=True, yang_name="power-admin-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/linecard', defining_module='openconfig-platform-linecard', yang_type='oc-platform-types:component-power-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """power_admin_state must be of a type compatible with oc-platform-types:component-power-type""",
          'defined-type': "oc-platform-types:component-power-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'POWER_ENABLED': {}, 'POWER_DISABLED': {}},), default=six.text_type("POWER_ENABLED"), is_leaf=True, yang_name="power-admin-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/linecard', defining_module='openconfig-platform-linecard', yang_type='oc-platform-types:component-power-type', is_config=True)""",
        })

    self.__power_admin_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_power_admin_state(self):
    self.__power_admin_state = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'POWER_ENABLED': {}, 'POWER_DISABLED': {}},), default=six.text_type("POWER_ENABLED"), is_leaf=True, yang_name="power-admin-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/linecard', defining_module='openconfig-platform-linecard', yang_type='oc-platform-types:component-power-type', is_config=True)

  power_admin_state = __builtin__.property(_get_power_admin_state, _set_power_admin_state)


  _pyangbind_elements = OrderedDict([('power_admin_state', power_admin_state), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/linecard/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for linecards
  """
  __slots__ = ('_path_helper', '_extmethods', '__power_admin_state',)

  _yang_name = 'config'

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
    self.__power_admin_state = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'POWER_ENABLED': {}, 'POWER_DISABLED': {}},), default=six.text_type("POWER_ENABLED"), is_leaf=True, yang_name="power-admin-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/linecard', defining_module='openconfig-platform-linecard', yang_type='oc-platform-types:component-power-type', is_config=True)

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
      return ['components', 'component', 'linecard', 'config']

  def _get_power_admin_state(self):
    """
    Getter method for power_admin_state, mapped from YANG variable /components/component/linecard/config/power_admin_state (oc-platform-types:component-power-type)

    YANG Description: Enable or disable power to the linecard
    """
    return self.__power_admin_state
      
  def _set_power_admin_state(self, v, load=False):
    """
    Setter method for power_admin_state, mapped from YANG variable /components/component/linecard/config/power_admin_state (oc-platform-types:component-power-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_power_admin_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_power_admin_state() directly.

    YANG Description: Enable or disable power to the linecard
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'POWER_ENABLED': {}, 'POWER_DISABLED': {}},), default=six.text_type("POWER_ENABLED"), is_leaf=True, yang_name="power-admin-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/linecard', defining_module='openconfig-platform-linecard', yang_type='oc-platform-types:component-power-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """power_admin_state must be of a type compatible with oc-platform-types:component-power-type""",
          'defined-type': "oc-platform-types:component-power-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'POWER_ENABLED': {}, 'POWER_DISABLED': {}},), default=six.text_type("POWER_ENABLED"), is_leaf=True, yang_name="power-admin-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/linecard', defining_module='openconfig-platform-linecard', yang_type='oc-platform-types:component-power-type', is_config=True)""",
        })

    self.__power_admin_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_power_admin_state(self):
    self.__power_admin_state = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'POWER_ENABLED': {}, 'POWER_DISABLED': {}},), default=six.text_type("POWER_ENABLED"), is_leaf=True, yang_name="power-admin-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/linecard', defining_module='openconfig-platform-linecard', yang_type='oc-platform-types:component-power-type', is_config=True)

  power_admin_state = __builtin__.property(_get_power_admin_state, _set_power_admin_state)


  _pyangbind_elements = OrderedDict([('power_admin_state', power_admin_state), ])


class config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-platform - based on the path /components/component/linecard/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for linecards
  """
  __slots__ = ('_path_helper', '_extmethods', '__power_admin_state',)

  _yang_name = 'config'

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
    self.__power_admin_state = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'POWER_ENABLED': {}, 'POWER_DISABLED': {}},), default=six.text_type("POWER_ENABLED"), is_leaf=True, yang_name="power-admin-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/linecard', defining_module='openconfig-platform-linecard', yang_type='oc-platform-types:component-power-type', is_config=True)

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
      return ['components', 'component', 'linecard', 'config']

  def _get_power_admin_state(self):
    """
    Getter method for power_admin_state, mapped from YANG variable /components/component/linecard/config/power_admin_state (oc-platform-types:component-power-type)

    YANG Description: Enable or disable power to the linecard
    """
    return self.__power_admin_state
      
  def _set_power_admin_state(self, v, load=False):
    """
    Setter method for power_admin_state, mapped from YANG variable /components/component/linecard/config/power_admin_state (oc-platform-types:component-power-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_power_admin_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_power_admin_state() directly.

    YANG Description: Enable or disable power to the linecard
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'POWER_ENABLED': {}, 'POWER_DISABLED': {}},), default=six.text_type("POWER_ENABLED"), is_leaf=True, yang_name="power-admin-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/linecard', defining_module='openconfig-platform-linecard', yang_type='oc-platform-types:component-power-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """power_admin_state must be of a type compatible with oc-platform-types:component-power-type""",
          'defined-type': "oc-platform-types:component-power-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'POWER_ENABLED': {}, 'POWER_DISABLED': {}},), default=six.text_type("POWER_ENABLED"), is_leaf=True, yang_name="power-admin-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/linecard', defining_module='openconfig-platform-linecard', yang_type='oc-platform-types:component-power-type', is_config=True)""",
        })

    self.__power_admin_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_power_admin_state(self):
    self.__power_admin_state = YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'POWER_ENABLED': {}, 'POWER_DISABLED': {}},), default=six.text_type("POWER_ENABLED"), is_leaf=True, yang_name="power-admin-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/platform/linecard', defining_module='openconfig-platform-linecard', yang_type='oc-platform-types:component-power-type', is_config=True)

  power_admin_state = __builtin__.property(_get_power_admin_state, _set_power_admin_state)


  _pyangbind_elements = OrderedDict([('power_admin_state', power_admin_state), ])


