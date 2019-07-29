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

from . import selectors
class console(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/logging/console. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for data related to console-based
logging
  """
  __slots__ = ('_path_helper', '_extmethods', '__selectors',)

  _yang_name = 'console'

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
    self.__selectors = YANGDynClass(base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

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
      return ['system', 'logging', 'console']

  def _get_selectors(self):
    """
    Getter method for selectors, mapped from YANG variable /system/logging/console/selectors (container)

    YANG Description: Enclosing container 
    """
    return self.__selectors
      
  def _set_selectors(self, v, load=False):
    """
    Setter method for selectors, mapped from YANG variable /system/logging/console/selectors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_selectors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_selectors() directly.

    YANG Description: Enclosing container 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """selectors must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__selectors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_selectors(self):
    self.__selectors = YANGDynClass(base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

  selectors = __builtin__.property(_get_selectors, _set_selectors)


  _pyangbind_elements = OrderedDict([('selectors', selectors), ])


from . import selectors
class console(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/logging/console. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for data related to console-based
logging
  """
  __slots__ = ('_path_helper', '_extmethods', '__selectors',)

  _yang_name = 'console'

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
    self.__selectors = YANGDynClass(base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

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
      return ['system', 'logging', 'console']

  def _get_selectors(self):
    """
    Getter method for selectors, mapped from YANG variable /system/logging/console/selectors (container)

    YANG Description: Enclosing container 
    """
    return self.__selectors
      
  def _set_selectors(self, v, load=False):
    """
    Setter method for selectors, mapped from YANG variable /system/logging/console/selectors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_selectors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_selectors() directly.

    YANG Description: Enclosing container 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """selectors must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__selectors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_selectors(self):
    self.__selectors = YANGDynClass(base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

  selectors = __builtin__.property(_get_selectors, _set_selectors)


  _pyangbind_elements = OrderedDict([('selectors', selectors), ])


from . import selectors
class console(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-system - based on the path /system/logging/console. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level container for data related to console-based
logging
  """
  __slots__ = ('_path_helper', '_extmethods', '__selectors',)

  _yang_name = 'console'

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
    self.__selectors = YANGDynClass(base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

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
      return ['system', 'logging', 'console']

  def _get_selectors(self):
    """
    Getter method for selectors, mapped from YANG variable /system/logging/console/selectors (container)

    YANG Description: Enclosing container 
    """
    return self.__selectors
      
  def _set_selectors(self, v, load=False):
    """
    Setter method for selectors, mapped from YANG variable /system/logging/console/selectors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_selectors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_selectors() directly.

    YANG Description: Enclosing container 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """selectors must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)""",
        })

    self.__selectors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_selectors(self):
    self.__selectors = YANGDynClass(base=selectors.selectors, is_container='container', yang_name="selectors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='container', is_config=True)

  selectors = __builtin__.property(_get_selectors, _set_selectors)


  _pyangbind_elements = OrderedDict([('selectors', selectors), ])


