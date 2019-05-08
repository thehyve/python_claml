# ./claml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2019-04-05 19:48:40.632175 by PyXB version 1.2.6 using Python 3.6.7.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0c295e4a-57cb-11e9-80c6-e86a649bf8c8')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import pyxb.binding.xml_

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 121, 16)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.true = STD_ANON._CF_enumeration.addEnumeration(unicode_value='true', tag='true')
STD_ANON.false = STD_ANON._CF_enumeration.addEnumeration(unicode_value='false', tag='false')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 194, 16)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.true = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='true', tag='true')
STD_ANON_.false = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='false', tag='false')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 276, 16)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.item = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='item', tag='item')
STD_ANON_2.list = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='list', tag='list')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 24, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Variants uses Python identifier Variants
    __Variants = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Variants'), 'Variants', '__AbsentNamespace0_CTD_ANON_Variants', False, pyxb.utils.utility.Location('ClaML.xsd', 41, 4), )


    Variants = property(__Variants.value, __Variants.set, None, None)


    # Element Meta uses Python identifier Meta
    __Meta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Meta'), 'Meta', '__AbsentNamespace0_CTD_ANON_Meta', True, pyxb.utils.utility.Location('ClaML.xsd', 53, 4), )


    Meta = property(__Meta.value, __Meta.set, None, None)


    # Element Identifier uses Python identifier Identifier
    __Identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), 'Identifier', '__AbsentNamespace0_CTD_ANON_Identifier', True, pyxb.utils.utility.Location('ClaML.xsd', 60, 4), )


    Identifier = property(__Identifier.value, __Identifier.set, None, None)


    # Element Title uses Python identifier Title
    __Title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Title'), 'Title', '__AbsentNamespace0_CTD_ANON_Title', False, pyxb.utils.utility.Location('ClaML.xsd', 66, 4), )


    Title = property(__Title.value, __Title.set, None, None)


    # Element Authors uses Python identifier Authors
    __Authors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Authors'), 'Authors', '__AbsentNamespace0_CTD_ANON_Authors', False, pyxb.utils.utility.Location('ClaML.xsd', 73, 4), )


    Authors = property(__Authors.value, __Authors.set, None, None)


    # Element ClassKinds uses Python identifier ClassKinds
    __ClassKinds = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClassKinds'), 'ClassKinds', '__AbsentNamespace0_CTD_ANON_ClassKinds', False, pyxb.utils.utility.Location('ClaML.xsd', 85, 4), )


    ClassKinds = property(__ClassKinds.value, __ClassKinds.set, None, None)


    # Element RubricKinds uses Python identifier RubricKinds
    __RubricKinds = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RubricKinds'), 'RubricKinds', '__AbsentNamespace0_CTD_ANON_RubricKinds', False, pyxb.utils.utility.Location('ClaML.xsd', 92, 4), )


    RubricKinds = property(__RubricKinds.value, __RubricKinds.set, None, None)


    # Element UsageKinds uses Python identifier UsageKinds
    __UsageKinds = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UsageKinds'), 'UsageKinds', '__AbsentNamespace0_CTD_ANON_UsageKinds', False, pyxb.utils.utility.Location('ClaML.xsd', 99, 4), )


    UsageKinds = property(__UsageKinds.value, __UsageKinds.set, None, None)


    # Element Modifier uses Python identifier Modifier
    __Modifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Modifier'), 'Modifier', '__AbsentNamespace0_CTD_ANON_Modifier', True, pyxb.utils.utility.Location('ClaML.xsd', 142, 4), )


    Modifier = property(__Modifier.value, __Modifier.set, None, None)


    # Element ModifierClass uses Python identifier ModifierClass
    __ModifierClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ModifierClass'), 'ModifierClass', '__AbsentNamespace0_CTD_ANON_ModifierClass', True, pyxb.utils.utility.Location('ClaML.xsd', 154, 4), )


    ModifierClass = property(__ModifierClass.value, __ModifierClass.set, None, None)


    # Element Class uses Python identifier Class
    __Class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Class'), 'Class', '__AbsentNamespace0_CTD_ANON_Class', True, pyxb.utils.utility.Location('ClaML.xsd', 169, 4), )


    Class = property(__Class.value, __Class.set, None, None)


    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_CTD_ANON_version', pyxb.binding.datatypes.anySimpleType, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 38, 12)
    __version._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 38, 12)

    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __Variants.name() : __Variants,
        __Meta.name() : __Meta,
        __Identifier.name() : __Identifier,
        __Title.name() : __Title,
        __Authors.name() : __Authors,
        __ClassKinds.name() : __ClassKinds,
        __RubricKinds.name() : __RubricKinds,
        __UsageKinds.name() : __UsageKinds,
        __Modifier.name() : __Modifier,
        __ModifierClass.name() : __ModifierClass,
        __Class.name() : __Class
    })
    _AttributeMap.update({
        __version.name() : __version
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 42, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Variant uses Python identifier Variant
    __Variant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Variant'), 'Variant', '__AbsentNamespace0_CTD_ANON__Variant', True, pyxb.utils.utility.Location('ClaML.xsd', 48, 4), )


    Variant = property(__Variant.value, __Variant.set, None, None)

    _ElementMap.update({
        __Variant.name() : __Variant
    })
    _AttributeMap.update({

    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type MIXED
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 49, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_2_name', pyxb.binding.datatypes.ID, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 50, 12)
    __name._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 50, 12)

    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 54, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_3_name', pyxb.binding.datatypes.anySimpleType, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 55, 12)
    __name._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 55, 12)

    name = property(__name.value, __name.set, None, None)


    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_CTD_ANON_3_value', pyxb.binding.datatypes.anySimpleType, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 56, 12)
    __value._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 56, 12)

    value_ = property(__value.value, __value.set, None, None)


    # Attribute variants uses Python identifier variants
    __variants = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variants'), 'variants', '__AbsentNamespace0_CTD_ANON_3_variants', pyxb.binding.datatypes.IDREFS)
    __variants._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 57, 12)
    __variants._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 57, 12)

    variants = property(__variants.value, __variants.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __name.name() : __name,
        __value.name() : __value,
        __variants.name() : __variants
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 61, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute authority uses Python identifier authority
    __authority = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'authority'), 'authority', '__AbsentNamespace0_CTD_ANON_4_authority', pyxb.binding.datatypes.NMTOKEN)
    __authority._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 62, 12)
    __authority._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 62, 12)

    authority = property(__authority.value, __authority.set, None, None)


    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__AbsentNamespace0_CTD_ANON_4_uid', pyxb.binding.datatypes.anySimpleType, required=True)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 63, 12)
    __uid._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 63, 12)

    uid = property(__uid.value, __uid.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __authority.name() : __authority,
        __uid.name() : __uid
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type MIXED
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 67, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_5_name', pyxb.binding.datatypes.NMTOKEN, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 68, 12)
    __name._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 68, 12)

    name = property(__name.value, __name.set, None, None)


    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_CTD_ANON_5_version', pyxb.binding.datatypes.anySimpleType)
    __version._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 69, 12)
    __version._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 69, 12)

    version = property(__version.value, __version.set, None, None)


    # Attribute date uses Python identifier date
    __date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date'), 'date', '__AbsentNamespace0_CTD_ANON_5_date', pyxb.binding.datatypes.anySimpleType)
    __date._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 70, 12)
    __date._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 70, 12)

    date = property(__date.value, __date.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __name.name() : __name,
        __version.name() : __version,
        __date.name() : __date
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 74, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Author uses Python identifier Author
    __Author = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Author'), 'Author', '__AbsentNamespace0_CTD_ANON_6_Author', True, pyxb.utils.utility.Location('ClaML.xsd', 80, 4), )


    Author = property(__Author.value, __Author.set, None, None)

    _ElementMap.update({
        __Author.name() : __Author
    })
    _AttributeMap.update({

    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type MIXED
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 81, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_7_name', pyxb.binding.datatypes.ID, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 82, 12)
    __name._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 82, 12)

    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 86, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element ClassKind uses Python identifier ClassKind
    __ClassKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClassKind'), 'ClassKind', '__AbsentNamespace0_CTD_ANON_8_ClassKind', True, pyxb.utils.utility.Location('ClaML.xsd', 106, 4), )


    ClassKind = property(__ClassKind.value, __ClassKind.set, None, None)

    _ElementMap.update({
        __ClassKind.name() : __ClassKind
    })
    _AttributeMap.update({

    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 93, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element RubricKind uses Python identifier RubricKind
    __RubricKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RubricKind'), 'RubricKind', '__AbsentNamespace0_CTD_ANON_9_RubricKind', True, pyxb.utils.utility.Location('ClaML.xsd', 114, 4), )


    RubricKind = property(__RubricKind.value, __RubricKind.set, None, None)

    _ElementMap.update({
        __RubricKind.name() : __RubricKind
    })
    _AttributeMap.update({

    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 100, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element UsageKind uses Python identifier UsageKind
    __UsageKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UsageKind'), 'UsageKind', '__AbsentNamespace0_CTD_ANON_10_UsageKind', True, pyxb.utils.utility.Location('ClaML.xsd', 130, 4), )


    UsageKind = property(__UsageKind.value, __UsageKind.set, None, None)

    _ElementMap.update({
        __UsageKind.name() : __UsageKind
    })
    _AttributeMap.update({

    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 107, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Display uses Python identifier Display
    __Display = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Display'), 'Display', '__AbsentNamespace0_CTD_ANON_11_Display', True, pyxb.utils.utility.Location('ClaML.xsd', 136, 4), )


    Display = property(__Display.value, __Display.set, None, None)


    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_11_name', pyxb.binding.datatypes.ID, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 111, 12)
    __name._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 111, 12)

    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        __Display.name() : __Display
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 131, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_12_name', pyxb.binding.datatypes.ID, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 132, 12)
    __name._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 132, 12)

    name = property(__name.value, __name.set, None, None)


    # Attribute mark uses Python identifier mark
    __mark = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'mark'), 'mark', '__AbsentNamespace0_CTD_ANON_12_mark', pyxb.binding.datatypes.anySimpleType, required=True)
    __mark._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 133, 12)
    __mark._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 133, 12)

    mark = property(__mark.value, __mark.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __name.name() : __name,
        __mark.name() : __mark
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type MIXED
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 137, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_CTD_ANON_13_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang, required=True)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 138, 12)

    lang = property(__lang.value, __lang.set, None, None)


    # Attribute variants uses Python identifier variants
    __variants = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variants'), 'variants', '__AbsentNamespace0_CTD_ANON_13_variants', pyxb.binding.datatypes.IDREF)
    __variants._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 139, 12)
    __variants._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 139, 12)

    variants = property(__variants.value, __variants.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __variants.name() : __variants
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 143, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Meta uses Python identifier Meta
    __Meta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Meta'), 'Meta', '__AbsentNamespace0_CTD_ANON_14_Meta', True, pyxb.utils.utility.Location('ClaML.xsd', 53, 4), )


    Meta = property(__Meta.value, __Meta.set, None, None)


    # Element Rubric uses Python identifier Rubric
    __Rubric = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rubric'), 'Rubric', '__AbsentNamespace0_CTD_ANON_14_Rubric', True, pyxb.utils.utility.Location('ClaML.xsd', 217, 4), )


    Rubric = property(__Rubric.value, __Rubric.set, None, None)


    # Element History uses Python identifier History
    __History = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'History'), 'History', '__AbsentNamespace0_CTD_ANON_14_History', True, pyxb.utils.utility.Location('ClaML.xsd', 236, 4), )


    History = property(__History.value, __History.set, None, None)


    # Element SubClass uses Python identifier SubClass
    __SubClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubClass'), 'SubClass', '__AbsentNamespace0_CTD_ANON_14_SubClass', True, pyxb.utils.utility.Location('ClaML.xsd', 248, 4), )


    SubClass = property(__SubClass.value, __SubClass.set, None, None)


    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_14_code', pyxb.binding.datatypes.NMTOKEN, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 150, 12)
    __code._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 150, 12)

    code = property(__code.value, __code.set, None, None)


    # Attribute variants uses Python identifier variants
    __variants = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variants'), 'variants', '__AbsentNamespace0_CTD_ANON_14_variants', pyxb.binding.datatypes.IDREFS)
    __variants._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 151, 12)
    __variants._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 151, 12)

    variants = property(__variants.value, __variants.set, None, None)

    _ElementMap.update({
        __Meta.name() : __Meta,
        __Rubric.name() : __Rubric,
        __History.name() : __History,
        __SubClass.name() : __SubClass
    })
    _AttributeMap.update({
        __code.name() : __code,
        __variants.name() : __variants
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 155, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Meta uses Python identifier Meta
    __Meta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Meta'), 'Meta', '__AbsentNamespace0_CTD_ANON_15_Meta', True, pyxb.utils.utility.Location('ClaML.xsd', 53, 4), )


    Meta = property(__Meta.value, __Meta.set, None, None)


    # Element Rubric uses Python identifier Rubric
    __Rubric = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rubric'), 'Rubric', '__AbsentNamespace0_CTD_ANON_15_Rubric', True, pyxb.utils.utility.Location('ClaML.xsd', 217, 4), )


    Rubric = property(__Rubric.value, __Rubric.set, None, None)


    # Element History uses Python identifier History
    __History = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'History'), 'History', '__AbsentNamespace0_CTD_ANON_15_History', True, pyxb.utils.utility.Location('ClaML.xsd', 236, 4), )


    History = property(__History.value, __History.set, None, None)


    # Element SuperClass uses Python identifier SuperClass
    __SuperClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SuperClass'), 'SuperClass', '__AbsentNamespace0_CTD_ANON_15_SuperClass', False, pyxb.utils.utility.Location('ClaML.xsd', 242, 4), )


    SuperClass = property(__SuperClass.value, __SuperClass.set, None, None)


    # Element SubClass uses Python identifier SubClass
    __SubClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubClass'), 'SubClass', '__AbsentNamespace0_CTD_ANON_15_SubClass', True, pyxb.utils.utility.Location('ClaML.xsd', 248, 4), )


    SubClass = property(__SubClass.value, __SubClass.set, None, None)


    # Attribute modifier uses Python identifier modifier
    __modifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modifier'), 'modifier', '__AbsentNamespace0_CTD_ANON_15_modifier', pyxb.binding.datatypes.NMTOKEN, required=True)
    __modifier._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 163, 12)
    __modifier._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 163, 12)

    modifier = property(__modifier.value, __modifier.set, None, None)


    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_15_code', pyxb.binding.datatypes.NMTOKEN, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 164, 12)
    __code._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 164, 12)

    code = property(__code.value, __code.set, None, None)


    # Attribute usage uses Python identifier usage
    __usage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'usage'), 'usage', '__AbsentNamespace0_CTD_ANON_15_usage', pyxb.binding.datatypes.IDREF)
    __usage._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 165, 12)
    __usage._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 165, 12)

    usage = property(__usage.value, __usage.set, None, None)


    # Attribute variants uses Python identifier variants
    __variants = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variants'), 'variants', '__AbsentNamespace0_CTD_ANON_15_variants', pyxb.binding.datatypes.IDREFS)
    __variants._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 166, 12)
    __variants._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 166, 12)

    variants = property(__variants.value, __variants.set, None, None)

    _ElementMap.update({
        __Meta.name() : __Meta,
        __Rubric.name() : __Rubric,
        __History.name() : __History,
        __SuperClass.name() : __SuperClass,
        __SubClass.name() : __SubClass
    })
    _AttributeMap.update({
        __modifier.name() : __modifier,
        __code.name() : __code,
        __usage.name() : __usage,
        __variants.name() : __variants
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 170, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Meta uses Python identifier Meta
    __Meta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Meta'), 'Meta', '__AbsentNamespace0_CTD_ANON_16_Meta', True, pyxb.utils.utility.Location('ClaML.xsd', 53, 4), )


    Meta = property(__Meta.value, __Meta.set, None, None)


    # Element ModifiedBy uses Python identifier ModifiedBy
    __ModifiedBy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ModifiedBy'), 'ModifiedBy', '__AbsentNamespace0_CTD_ANON_16_ModifiedBy', True, pyxb.utils.utility.Location('ClaML.xsd', 186, 4), )


    ModifiedBy = property(__ModifiedBy.value, __ModifiedBy.set, None, None)


    # Element ExcludeModifier uses Python identifier ExcludeModifier
    __ExcludeModifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExcludeModifier'), 'ExcludeModifier', '__AbsentNamespace0_CTD_ANON_16_ExcludeModifier', True, pyxb.utils.utility.Location('ClaML.xsd', 205, 4), )


    ExcludeModifier = property(__ExcludeModifier.value, __ExcludeModifier.set, None, None)


    # Element Rubric uses Python identifier Rubric
    __Rubric = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rubric'), 'Rubric', '__AbsentNamespace0_CTD_ANON_16_Rubric', True, pyxb.utils.utility.Location('ClaML.xsd', 217, 4), )


    Rubric = property(__Rubric.value, __Rubric.set, None, None)


    # Element History uses Python identifier History
    __History = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'History'), 'History', '__AbsentNamespace0_CTD_ANON_16_History', True, pyxb.utils.utility.Location('ClaML.xsd', 236, 4), )


    History = property(__History.value, __History.set, None, None)


    # Element SuperClass uses Python identifier SuperClass
    __SuperClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SuperClass'), 'SuperClass', '__AbsentNamespace0_CTD_ANON_16_SuperClass', True, pyxb.utils.utility.Location('ClaML.xsd', 242, 4), )


    SuperClass = property(__SuperClass.value, __SuperClass.set, None, None)


    # Element SubClass uses Python identifier SubClass
    __SubClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubClass'), 'SubClass', '__AbsentNamespace0_CTD_ANON_16_SubClass', True, pyxb.utils.utility.Location('ClaML.xsd', 248, 4), )


    SubClass = property(__SubClass.value, __SubClass.set, None, None)


    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_16_code', pyxb.binding.datatypes.NMTOKEN, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 180, 12)
    __code._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 180, 12)

    code = property(__code.value, __code.set, None, None)


    # Attribute kind uses Python identifier kind
    __kind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kind'), 'kind', '__AbsentNamespace0_CTD_ANON_16_kind', pyxb.binding.datatypes.IDREF, required=True)
    __kind._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 181, 12)
    __kind._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 181, 12)

    kind = property(__kind.value, __kind.set, None, None)


    # Attribute usage uses Python identifier usage
    __usage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'usage'), 'usage', '__AbsentNamespace0_CTD_ANON_16_usage', pyxb.binding.datatypes.IDREF)
    __usage._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 182, 12)
    __usage._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 182, 12)

    usage = property(__usage.value, __usage.set, None, None)


    # Attribute variants uses Python identifier variants
    __variants = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variants'), 'variants', '__AbsentNamespace0_CTD_ANON_16_variants', pyxb.binding.datatypes.IDREFS)
    __variants._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 183, 12)
    __variants._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 183, 12)

    variants = property(__variants.value, __variants.set, None, None)

    _ElementMap.update({
        __Meta.name() : __Meta,
        __ModifiedBy.name() : __ModifiedBy,
        __ExcludeModifier.name() : __ExcludeModifier,
        __Rubric.name() : __Rubric,
        __History.name() : __History,
        __SuperClass.name() : __SuperClass,
        __SubClass.name() : __SubClass
    })
    _AttributeMap.update({
        __code.name() : __code,
        __kind.name() : __kind,
        __usage.name() : __usage,
        __variants.name() : __variants
    })
_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 206, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_17_code', pyxb.binding.datatypes.NMTOKEN, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 207, 12)
    __code._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 207, 12)

    code = property(__code.value, __code.set, None, None)


    # Attribute variants uses Python identifier variants
    __variants = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variants'), 'variants', '__AbsentNamespace0_CTD_ANON_17_variants', pyxb.binding.datatypes.IDREFS)
    __variants._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 208, 12)
    __variants._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 208, 12)

    variants = property(__variants.value, __variants.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __code.name() : __code,
        __variants.name() : __variants
    })
_module_typeBindings.CTD_ANON_17 = CTD_ANON_17


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 212, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_18_code', pyxb.binding.datatypes.NMTOKEN, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 213, 12)
    __code._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 213, 12)

    code = property(__code.value, __code.set, None, None)


    # Attribute variants uses Python identifier variants
    __variants = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variants'), 'variants', '__AbsentNamespace0_CTD_ANON_18_variants', pyxb.binding.datatypes.IDREFS)
    __variants._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 214, 12)
    __variants._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 214, 12)

    variants = property(__variants.value, __variants.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __code.name() : __code,
        __variants.name() : __variants
    })
_module_typeBindings.CTD_ANON_18 = CTD_ANON_18


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 218, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Label uses Python identifier Label
    __Label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Label'), 'Label', '__AbsentNamespace0_CTD_ANON_19_Label', True, pyxb.utils.utility.Location('ClaML.xsd', 228, 4), )


    Label = property(__Label.value, __Label.set, None, None)


    # Element History uses Python identifier History
    __History = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'History'), 'History', '__AbsentNamespace0_CTD_ANON_19_History', True, pyxb.utils.utility.Location('ClaML.xsd', 236, 4), )


    History = property(__History.value, __History.set, None, None)


    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_CTD_ANON_19_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 223, 12)
    __id._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 223, 12)

    id = property(__id.value, __id.set, None, None)


    # Attribute kind uses Python identifier kind
    __kind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kind'), 'kind', '__AbsentNamespace0_CTD_ANON_19_kind', pyxb.binding.datatypes.IDREF, required=True)
    __kind._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 224, 12)
    __kind._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 224, 12)

    kind = property(__kind.value, __kind.set, None, None)


    # Attribute usage uses Python identifier usage
    __usage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'usage'), 'usage', '__AbsentNamespace0_CTD_ANON_19_usage', pyxb.binding.datatypes.IDREF)
    __usage._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 225, 12)
    __usage._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 225, 12)

    usage = property(__usage.value, __usage.set, None, None)

    _ElementMap.update({
        __Label.name() : __Label,
        __History.name() : __History
    })
    _AttributeMap.update({
        __id.name() : __id,
        __kind.name() : __kind,
        __usage.name() : __usage
    })
_module_typeBindings.CTD_ANON_19 = CTD_ANON_19


# Complex type [anonymous] with content type MIXED
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 229, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reference'), 'Reference', '__AbsentNamespace0_CTD_ANON_20_Reference', True, pyxb.utils.utility.Location('ClaML.xsd', 254, 4), )


    Reference = property(__Reference.value, __Reference.set, None, None)


    # Element Para uses Python identifier Para
    __Para = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Para'), 'Para', '__AbsentNamespace0_CTD_ANON_20_Para', True, pyxb.utils.utility.Location('ClaML.xsd', 264, 4), )


    Para = property(__Para.value, __Para.set, None, None)


    # Element Fragment uses Python identifier Fragment
    __Fragment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Fragment'), 'Fragment', '__AbsentNamespace0_CTD_ANON_20_Fragment', True, pyxb.utils.utility.Location('ClaML.xsd', 270, 4), )


    Fragment = property(__Fragment.value, __Fragment.set, None, None)


    # Element Include uses Python identifier Include
    __Include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Include'), 'Include', '__AbsentNamespace0_CTD_ANON_20_Include', True, pyxb.utils.utility.Location('ClaML.xsd', 285, 4), )


    Include = property(__Include.value, __Include.set, None, None)


    # Element IncludeDescendants uses Python identifier IncludeDescendants
    __IncludeDescendants = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IncludeDescendants'), 'IncludeDescendants', '__AbsentNamespace0_CTD_ANON_20_IncludeDescendants', True, pyxb.utils.utility.Location('ClaML.xsd', 291, 4), )


    IncludeDescendants = property(__IncludeDescendants.value, __IncludeDescendants.set, None, None)


    # Element List uses Python identifier List
    __List = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'List'), 'List', '__AbsentNamespace0_CTD_ANON_20_List', True, pyxb.utils.utility.Location('ClaML.xsd', 297, 4), )


    List = property(__List.value, __List.set, None, None)


    # Element Table uses Python identifier Table
    __Table = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Table'), 'Table', '__AbsentNamespace0_CTD_ANON_20_Table', True, pyxb.utils.utility.Location('ClaML.xsd', 317, 4), )


    Table = property(__Table.value, __Table.set, None, None)


    # Element Term uses Python identifier Term
    __Term = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Term'), 'Term', '__AbsentNamespace0_CTD_ANON_20_Term', True, pyxb.utils.utility.Location('ClaML.xsd', 380, 4), )


    Term = property(__Term.value, __Term.set, None, None)


    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__AbsentNamespace0_CTD_ANON_20_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang, required=True)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 231, 12)

    lang = property(__lang.value, __lang.set, None, None)


    # Attribute {http://www.w3.org/XML/1998/namespace}space uses Python identifier space
    __space = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'space'), 'space', '__AbsentNamespace0_CTD_ANON_20_httpwww_w3_orgXML1998namespacespace', pyxb.binding.xml_.STD_ANON_space, unicode_default='default')
    __space._DeclarationLocation = None
    __space._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 232, 12)

    space = property(__space.value, __space.set, None, None)


    # Attribute variants uses Python identifier variants
    __variants = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variants'), 'variants', '__AbsentNamespace0_CTD_ANON_20_variants', pyxb.binding.datatypes.IDREFS)
    __variants._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 233, 12)
    __variants._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 233, 12)

    variants = property(__variants.value, __variants.set, None, None)

    _ElementMap.update({
        __Reference.name() : __Reference,
        __Para.name() : __Para,
        __Fragment.name() : __Fragment,
        __Include.name() : __Include,
        __IncludeDescendants.name() : __IncludeDescendants,
        __List.name() : __List,
        __Table.name() : __Table,
        __Term.name() : __Term
    })
    _AttributeMap.update({
        __lang.name() : __lang,
        __space.name() : __space,
        __variants.name() : __variants
    })
_module_typeBindings.CTD_ANON_20 = CTD_ANON_20


# Complex type [anonymous] with content type MIXED
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 237, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute author uses Python identifier author
    __author = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'author'), 'author', '__AbsentNamespace0_CTD_ANON_21_author', pyxb.binding.datatypes.IDREF, required=True)
    __author._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 238, 12)
    __author._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 238, 12)

    author = property(__author.value, __author.set, None, None)


    # Attribute date uses Python identifier date
    __date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date'), 'date', '__AbsentNamespace0_CTD_ANON_21_date', pyxb.binding.datatypes.NMTOKEN, required=True)
    __date._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 239, 12)
    __date._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 239, 12)

    date = property(__date.value, __date.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __author.name() : __author,
        __date.name() : __date
    })
_module_typeBindings.CTD_ANON_21 = CTD_ANON_21


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 243, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_22_code', pyxb.binding.datatypes.NMTOKEN, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 244, 12)
    __code._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 244, 12)

    code = property(__code.value, __code.set, None, None)


    # Attribute variants uses Python identifier variants
    __variants = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variants'), 'variants', '__AbsentNamespace0_CTD_ANON_22_variants', pyxb.binding.datatypes.IDREFS)
    __variants._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 245, 12)
    __variants._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 245, 12)

    variants = property(__variants.value, __variants.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __code.name() : __code,
        __variants.name() : __variants
    })
_module_typeBindings.CTD_ANON_22 = CTD_ANON_22


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 249, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_23_code', pyxb.binding.datatypes.NMTOKEN, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 250, 12)
    __code._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 250, 12)

    code = property(__code.value, __code.set, None, None)


    # Attribute variants uses Python identifier variants
    __variants = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variants'), 'variants', '__AbsentNamespace0_CTD_ANON_23_variants', pyxb.binding.datatypes.IDREFS)
    __variants._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 251, 12)
    __variants._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 251, 12)

    variants = property(__variants.value, __variants.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __code.name() : __code,
        __variants.name() : __variants
    })
_module_typeBindings.CTD_ANON_23 = CTD_ANON_23


# Complex type [anonymous] with content type MIXED
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 255, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__AbsentNamespace0_CTD_ANON_24_class', pyxb.binding.datatypes.anySimpleType)
    __class._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 256, 12)
    __class._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 256, 12)

    class_ = property(__class.value, __class.set, None, None)


    # Attribute authority uses Python identifier authority
    __authority = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'authority'), 'authority', '__AbsentNamespace0_CTD_ANON_24_authority', pyxb.binding.datatypes.NMTOKEN)
    __authority._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 257, 12)
    __authority._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 257, 12)

    authority = property(__authority.value, __authority.set, None, None)


    # Attribute uid uses Python identifier uid
    __uid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'uid'), 'uid', '__AbsentNamespace0_CTD_ANON_24_uid', pyxb.binding.datatypes.NMTOKEN)
    __uid._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 258, 12)
    __uid._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 258, 12)

    uid = property(__uid.value, __uid.set, None, None)


    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_24_code', pyxb.binding.datatypes.NMTOKEN)
    __code._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 259, 12)
    __code._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 259, 12)

    code = property(__code.value, __code.set, None, None)


    # Attribute usage uses Python identifier usage
    __usage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'usage'), 'usage', '__AbsentNamespace0_CTD_ANON_24_usage', pyxb.binding.datatypes.IDREF)
    __usage._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 260, 12)
    __usage._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 260, 12)

    usage = property(__usage.value, __usage.set, None, None)


    # Attribute variants uses Python identifier variants
    __variants = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variants'), 'variants', '__AbsentNamespace0_CTD_ANON_24_variants', pyxb.binding.datatypes.IDREFS)
    __variants._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 261, 12)
    __variants._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 261, 12)

    variants = property(__variants.value, __variants.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __class.name() : __class,
        __authority.name() : __authority,
        __uid.name() : __uid,
        __code.name() : __code,
        __usage.name() : __usage,
        __variants.name() : __variants
    })
_module_typeBindings.CTD_ANON_24 = CTD_ANON_24


# Complex type [anonymous] with content type MIXED
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 265, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reference'), 'Reference', '__AbsentNamespace0_CTD_ANON_25_Reference', True, pyxb.utils.utility.Location('ClaML.xsd', 254, 4), )


    Reference = property(__Reference.value, __Reference.set, None, None)


    # Element Term uses Python identifier Term
    __Term = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Term'), 'Term', '__AbsentNamespace0_CTD_ANON_25_Term', True, pyxb.utils.utility.Location('ClaML.xsd', 380, 4), )


    Term = property(__Term.value, __Term.set, None, None)


    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__AbsentNamespace0_CTD_ANON_25_class', pyxb.binding.datatypes.anySimpleType)
    __class._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 267, 12)
    __class._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 267, 12)

    class_ = property(__class.value, __class.set, None, None)

    _ElementMap.update({
        __Reference.name() : __Reference,
        __Term.name() : __Term
    })
    _AttributeMap.update({
        __class.name() : __class
    })
_module_typeBindings.CTD_ANON_25 = CTD_ANON_25


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 286, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__AbsentNamespace0_CTD_ANON_26_class', pyxb.binding.datatypes.anySimpleType)
    __class._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 287, 12)
    __class._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 287, 12)

    class_ = property(__class.value, __class.set, None, None)


    # Attribute rubric uses Python identifier rubric
    __rubric = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rubric'), 'rubric', '__AbsentNamespace0_CTD_ANON_26_rubric', pyxb.binding.datatypes.IDREF, required=True)
    __rubric._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 288, 12)
    __rubric._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 288, 12)

    rubric = property(__rubric.value, __rubric.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __class.name() : __class,
        __rubric.name() : __rubric
    })
_module_typeBindings.CTD_ANON_26 = CTD_ANON_26


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 292, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_27_code', pyxb.binding.datatypes.NMTOKEN, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 293, 12)
    __code._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 293, 12)

    code = property(__code.value, __code.set, None, None)


    # Attribute kind uses Python identifier kind
    __kind = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kind'), 'kind', '__AbsentNamespace0_CTD_ANON_27_kind', pyxb.binding.datatypes.IDREF, required=True)
    __kind._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 294, 12)
    __kind._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 294, 12)

    kind = property(__kind.value, __kind.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __code.name() : __code,
        __kind.name() : __kind
    })
_module_typeBindings.CTD_ANON_27 = CTD_ANON_27


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 298, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element ListItem uses Python identifier ListItem
    __ListItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ListItem'), 'ListItem', '__AbsentNamespace0_CTD_ANON_28_ListItem', True, pyxb.utils.utility.Location('ClaML.xsd', 305, 4), )


    ListItem = property(__ListItem.value, __ListItem.set, None, None)


    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__AbsentNamespace0_CTD_ANON_28_class', pyxb.binding.datatypes.anySimpleType)
    __class._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 302, 12)
    __class._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 302, 12)

    class_ = property(__class.value, __class.set, None, None)

    _ElementMap.update({
        __ListItem.name() : __ListItem
    })
    _AttributeMap.update({
        __class.name() : __class
    })
_module_typeBindings.CTD_ANON_28 = CTD_ANON_28


# Complex type [anonymous] with content type MIXED
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 306, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reference'), 'Reference', '__AbsentNamespace0_CTD_ANON_29_Reference', True, pyxb.utils.utility.Location('ClaML.xsd', 254, 4), )


    Reference = property(__Reference.value, __Reference.set, None, None)


    # Element Para uses Python identifier Para
    __Para = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Para'), 'Para', '__AbsentNamespace0_CTD_ANON_29_Para', True, pyxb.utils.utility.Location('ClaML.xsd', 264, 4), )


    Para = property(__Para.value, __Para.set, None, None)


    # Element Include uses Python identifier Include
    __Include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Include'), 'Include', '__AbsentNamespace0_CTD_ANON_29_Include', True, pyxb.utils.utility.Location('ClaML.xsd', 285, 4), )


    Include = property(__Include.value, __Include.set, None, None)


    # Element List uses Python identifier List
    __List = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'List'), 'List', '__AbsentNamespace0_CTD_ANON_29_List', True, pyxb.utils.utility.Location('ClaML.xsd', 297, 4), )


    List = property(__List.value, __List.set, None, None)


    # Element Table uses Python identifier Table
    __Table = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Table'), 'Table', '__AbsentNamespace0_CTD_ANON_29_Table', True, pyxb.utils.utility.Location('ClaML.xsd', 317, 4), )


    Table = property(__Table.value, __Table.set, None, None)


    # Element Term uses Python identifier Term
    __Term = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Term'), 'Term', '__AbsentNamespace0_CTD_ANON_29_Term', True, pyxb.utils.utility.Location('ClaML.xsd', 380, 4), )


    Term = property(__Term.value, __Term.set, None, None)


    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__AbsentNamespace0_CTD_ANON_29_class', pyxb.binding.datatypes.anySimpleType)
    __class._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 314, 12)
    __class._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 314, 12)

    class_ = property(__class.value, __class.set, None, None)

    _ElementMap.update({
        __Reference.name() : __Reference,
        __Para.name() : __Para,
        __Include.name() : __Include,
        __List.name() : __List,
        __Table.name() : __Table,
        __Term.name() : __Term
    })
    _AttributeMap.update({
        __class.name() : __class
    })
_module_typeBindings.CTD_ANON_29 = CTD_ANON_29


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 318, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Caption uses Python identifier Caption
    __Caption = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Caption'), 'Caption', '__AbsentNamespace0_CTD_ANON_30_Caption', False, pyxb.utils.utility.Location('ClaML.xsd', 328, 4), )


    Caption = property(__Caption.value, __Caption.set, None, None)


    # Element THead uses Python identifier THead
    __THead = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'THead'), 'THead', '__AbsentNamespace0_CTD_ANON_30_THead', False, pyxb.utils.utility.Location('ClaML.xsd', 334, 4), )


    THead = property(__THead.value, __THead.set, None, None)


    # Element TBody uses Python identifier TBody
    __TBody = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TBody'), 'TBody', '__AbsentNamespace0_CTD_ANON_30_TBody', False, pyxb.utils.utility.Location('ClaML.xsd', 342, 4), )


    TBody = property(__TBody.value, __TBody.set, None, None)


    # Element TFoot uses Python identifier TFoot
    __TFoot = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TFoot'), 'TFoot', '__AbsentNamespace0_CTD_ANON_30_TFoot', False, pyxb.utils.utility.Location('ClaML.xsd', 350, 4), )


    TFoot = property(__TFoot.value, __TFoot.set, None, None)


    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__AbsentNamespace0_CTD_ANON_30_class', pyxb.binding.datatypes.anySimpleType)
    __class._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 325, 12)
    __class._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 325, 12)

    class_ = property(__class.value, __class.set, None, None)

    _ElementMap.update({
        __Caption.name() : __Caption,
        __THead.name() : __THead,
        __TBody.name() : __TBody,
        __TFoot.name() : __TFoot
    })
    _AttributeMap.update({
        __class.name() : __class
    })
_module_typeBindings.CTD_ANON_30 = CTD_ANON_30


# Complex type [anonymous] with content type MIXED
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 329, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reference'), 'Reference', '__AbsentNamespace0_CTD_ANON_31_Reference', True, pyxb.utils.utility.Location('ClaML.xsd', 254, 4), )


    Reference = property(__Reference.value, __Reference.set, None, None)


    # Element Term uses Python identifier Term
    __Term = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Term'), 'Term', '__AbsentNamespace0_CTD_ANON_31_Term', True, pyxb.utils.utility.Location('ClaML.xsd', 380, 4), )


    Term = property(__Term.value, __Term.set, None, None)


    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__AbsentNamespace0_CTD_ANON_31_class', pyxb.binding.datatypes.anySimpleType)
    __class._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 331, 12)
    __class._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 331, 12)

    class_ = property(__class.value, __class.set, None, None)

    _ElementMap.update({
        __Reference.name() : __Reference,
        __Term.name() : __Term
    })
    _AttributeMap.update({
        __class.name() : __class
    })
_module_typeBindings.CTD_ANON_31 = CTD_ANON_31


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 335, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Row uses Python identifier Row
    __Row = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Row'), 'Row', '__AbsentNamespace0_CTD_ANON_32_Row', True, pyxb.utils.utility.Location('ClaML.xsd', 358, 4), )


    Row = property(__Row.value, __Row.set, None, None)


    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__AbsentNamespace0_CTD_ANON_32_class', pyxb.binding.datatypes.anySimpleType)
    __class._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 339, 12)
    __class._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 339, 12)

    class_ = property(__class.value, __class.set, None, None)

    _ElementMap.update({
        __Row.name() : __Row
    })
    _AttributeMap.update({
        __class.name() : __class
    })
_module_typeBindings.CTD_ANON_32 = CTD_ANON_32


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_33 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 343, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Row uses Python identifier Row
    __Row = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Row'), 'Row', '__AbsentNamespace0_CTD_ANON_33_Row', True, pyxb.utils.utility.Location('ClaML.xsd', 358, 4), )


    Row = property(__Row.value, __Row.set, None, None)


    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__AbsentNamespace0_CTD_ANON_33_class', pyxb.binding.datatypes.anySimpleType)
    __class._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 347, 12)
    __class._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 347, 12)

    class_ = property(__class.value, __class.set, None, None)

    _ElementMap.update({
        __Row.name() : __Row
    })
    _AttributeMap.update({
        __class.name() : __class
    })
_module_typeBindings.CTD_ANON_33 = CTD_ANON_33


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_34 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 351, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Row uses Python identifier Row
    __Row = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Row'), 'Row', '__AbsentNamespace0_CTD_ANON_34_Row', True, pyxb.utils.utility.Location('ClaML.xsd', 358, 4), )


    Row = property(__Row.value, __Row.set, None, None)


    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__AbsentNamespace0_CTD_ANON_34_class', pyxb.binding.datatypes.anySimpleType)
    __class._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 355, 12)
    __class._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 355, 12)

    class_ = property(__class.value, __class.set, None, None)

    _ElementMap.update({
        __Row.name() : __Row
    })
    _AttributeMap.update({
        __class.name() : __class
    })
_module_typeBindings.CTD_ANON_34 = CTD_ANON_34


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_35 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 359, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Cell uses Python identifier Cell
    __Cell = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Cell'), 'Cell', '__AbsentNamespace0_CTD_ANON_35_Cell', True, pyxb.utils.utility.Location('ClaML.xsd', 366, 4), )


    Cell = property(__Cell.value, __Cell.set, None, None)


    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__AbsentNamespace0_CTD_ANON_35_class', pyxb.binding.datatypes.anySimpleType)
    __class._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 363, 12)
    __class._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 363, 12)

    class_ = property(__class.value, __class.set, None, None)

    _ElementMap.update({
        __Cell.name() : __Cell
    })
    _AttributeMap.update({
        __class.name() : __class
    })
_module_typeBindings.CTD_ANON_35 = CTD_ANON_35


# Complex type [anonymous] with content type MIXED
class CTD_ANON_36 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 367, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reference'), 'Reference', '__AbsentNamespace0_CTD_ANON_36_Reference', True, pyxb.utils.utility.Location('ClaML.xsd', 254, 4), )


    Reference = property(__Reference.value, __Reference.set, None, None)


    # Element Para uses Python identifier Para
    __Para = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Para'), 'Para', '__AbsentNamespace0_CTD_ANON_36_Para', True, pyxb.utils.utility.Location('ClaML.xsd', 264, 4), )


    Para = property(__Para.value, __Para.set, None, None)


    # Element Include uses Python identifier Include
    __Include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Include'), 'Include', '__AbsentNamespace0_CTD_ANON_36_Include', True, pyxb.utils.utility.Location('ClaML.xsd', 285, 4), )


    Include = property(__Include.value, __Include.set, None, None)


    # Element List uses Python identifier List
    __List = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'List'), 'List', '__AbsentNamespace0_CTD_ANON_36_List', True, pyxb.utils.utility.Location('ClaML.xsd', 297, 4), )


    List = property(__List.value, __List.set, None, None)


    # Element Table uses Python identifier Table
    __Table = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Table'), 'Table', '__AbsentNamespace0_CTD_ANON_36_Table', True, pyxb.utils.utility.Location('ClaML.xsd', 317, 4), )


    Table = property(__Table.value, __Table.set, None, None)


    # Element Term uses Python identifier Term
    __Term = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Term'), 'Term', '__AbsentNamespace0_CTD_ANON_36_Term', True, pyxb.utils.utility.Location('ClaML.xsd', 380, 4), )


    Term = property(__Term.value, __Term.set, None, None)


    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__AbsentNamespace0_CTD_ANON_36_class', pyxb.binding.datatypes.anySimpleType)
    __class._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 375, 12)
    __class._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 375, 12)

    class_ = property(__class.value, __class.set, None, None)


    # Attribute rowspan uses Python identifier rowspan
    __rowspan = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rowspan'), 'rowspan', '__AbsentNamespace0_CTD_ANON_36_rowspan', pyxb.binding.datatypes.anySimpleType)
    __rowspan._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 376, 12)
    __rowspan._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 376, 12)

    rowspan = property(__rowspan.value, __rowspan.set, None, None)


    # Attribute colspan uses Python identifier colspan
    __colspan = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'colspan'), 'colspan', '__AbsentNamespace0_CTD_ANON_36_colspan', pyxb.binding.datatypes.anySimpleType)
    __colspan._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 377, 12)
    __colspan._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 377, 12)

    colspan = property(__colspan.value, __colspan.set, None, None)

    _ElementMap.update({
        __Reference.name() : __Reference,
        __Para.name() : __Para,
        __Include.name() : __Include,
        __List.name() : __List,
        __Table.name() : __Table,
        __Term.name() : __Term
    })
    _AttributeMap.update({
        __class.name() : __class,
        __rowspan.name() : __rowspan,
        __colspan.name() : __colspan
    })
_module_typeBindings.CTD_ANON_36 = CTD_ANON_36


# Complex type [anonymous] with content type MIXED
class CTD_ANON_37 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 381, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__AbsentNamespace0_CTD_ANON_37_class', pyxb.binding.datatypes.anySimpleType)
    __class._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 382, 12)
    __class._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 382, 12)

    class_ = property(__class.value, __class.set, None, None)

    _ElementMap.update({

    })
    _AttributeMap.update({
        __class.name() : __class
    })
_module_typeBindings.CTD_ANON_37 = CTD_ANON_37


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_38 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 115, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Display uses Python identifier Display
    __Display = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Display'), 'Display', '__AbsentNamespace0_CTD_ANON_38_Display', True, pyxb.utils.utility.Location('ClaML.xsd', 136, 4), )


    Display = property(__Display.value, __Display.set, None, None)


    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_CTD_ANON_38_name', pyxb.binding.datatypes.ID, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 119, 12)
    __name._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 119, 12)

    name = property(__name.value, __name.set, None, None)


    # Attribute inherited uses Python identifier inherited
    __inherited = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'inherited'), 'inherited', '__AbsentNamespace0_CTD_ANON_38_inherited', _module_typeBindings.STD_ANON, unicode_default='true')
    __inherited._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 120, 12)
    __inherited._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 120, 12)

    inherited = property(__inherited.value, __inherited.set, None, None)

    _ElementMap.update({
        __Display.name() : __Display
    })
    _AttributeMap.update({
        __name.name() : __name,
        __inherited.name() : __inherited
    })
_module_typeBindings.CTD_ANON_38 = CTD_ANON_38


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_39 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 187, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Meta uses Python identifier Meta
    __Meta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Meta'), 'Meta', '__AbsentNamespace0_CTD_ANON_39_Meta', True, pyxb.utils.utility.Location('ClaML.xsd', 53, 4), )


    Meta = property(__Meta.value, __Meta.set, None, None)


    # Element ValidModifierClass uses Python identifier ValidModifierClass
    __ValidModifierClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ValidModifierClass'), 'ValidModifierClass', '__AbsentNamespace0_CTD_ANON_39_ValidModifierClass', True, pyxb.utils.utility.Location('ClaML.xsd', 211, 4), )


    ValidModifierClass = property(__ValidModifierClass.value, __ValidModifierClass.set, None, None)


    # Attribute code uses Python identifier code
    __code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'code'), 'code', '__AbsentNamespace0_CTD_ANON_39_code', pyxb.binding.datatypes.NMTOKEN, required=True)
    __code._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 192, 12)
    __code._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 192, 12)

    code = property(__code.value, __code.set, None, None)


    # Attribute all uses Python identifier all
    __all = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'all'), 'all', '__AbsentNamespace0_CTD_ANON_39_all', _module_typeBindings.STD_ANON_, unicode_default='true')
    __all._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 193, 12)
    __all._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 193, 12)

    all = property(__all.value, __all.set, None, None)


    # Attribute position uses Python identifier position
    __position = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'position'), 'position', '__AbsentNamespace0_CTD_ANON_39_position', pyxb.binding.datatypes.anySimpleType)
    __position._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 201, 12)
    __position._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 201, 12)

    position = property(__position.value, __position.set, None, None)


    # Attribute variants uses Python identifier variants
    __variants = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'variants'), 'variants', '__AbsentNamespace0_CTD_ANON_39_variants', pyxb.binding.datatypes.IDREFS)
    __variants._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 202, 12)
    __variants._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 202, 12)

    variants = property(__variants.value, __variants.set, None, None)

    _ElementMap.update({
        __Meta.name() : __Meta,
        __ValidModifierClass.name() : __ValidModifierClass
    })
    _AttributeMap.update({
        __code.name() : __code,
        __all.name() : __all,
        __position.name() : __position,
        __variants.name() : __variants
    })
_module_typeBindings.CTD_ANON_39 = CTD_ANON_39


# Complex type [anonymous] with content type MIXED
class CTD_ANON_40 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('ClaML.xsd', 271, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element Reference uses Python identifier Reference
    __Reference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Reference'), 'Reference', '__AbsentNamespace0_CTD_ANON_40_Reference', True, pyxb.utils.utility.Location('ClaML.xsd', 254, 4), )


    Reference = property(__Reference.value, __Reference.set, None, None)


    # Element Term uses Python identifier Term
    __Term = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Term'), 'Term', '__AbsentNamespace0_CTD_ANON_40_Term', True, pyxb.utils.utility.Location('ClaML.xsd', 380, 4), )


    Term = property(__Term.value, __Term.set, None, None)


    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__AbsentNamespace0_CTD_ANON_40_class', pyxb.binding.datatypes.anySimpleType)
    __class._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 273, 12)
    __class._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 273, 12)

    class_ = property(__class.value, __class.set, None, None)


    # Attribute usage uses Python identifier usage
    __usage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'usage'), 'usage', '__AbsentNamespace0_CTD_ANON_40_usage', pyxb.binding.datatypes.IDREF)
    __usage._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 274, 12)
    __usage._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 274, 12)

    usage = property(__usage.value, __usage.set, None, None)


    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_CTD_ANON_40_type', _module_typeBindings.STD_ANON_2, unicode_default='item')
    __type._DeclarationLocation = pyxb.utils.utility.Location('ClaML.xsd', 275, 12)
    __type._UseLocation = pyxb.utils.utility.Location('ClaML.xsd', 275, 12)

    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __Reference.name() : __Reference,
        __Term.name() : __Term
    })
    _AttributeMap.update({
        __class.name() : __class,
        __usage.name() : __usage,
        __type.name() : __type
    })
_module_typeBindings.CTD_ANON_40 = CTD_ANON_40


ClaML = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClaML'), CTD_ANON, location=pyxb.utils.utility.Location('ClaML.xsd', 23, 4))
Namespace.addCategoryObject('elementBinding', ClaML.name().localName(), ClaML)

Variants = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Variants'), CTD_ANON_, location=pyxb.utils.utility.Location('ClaML.xsd', 41, 4))
Namespace.addCategoryObject('elementBinding', Variants.name().localName(), Variants)

Variant = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Variant'), CTD_ANON_2, location=pyxb.utils.utility.Location('ClaML.xsd', 48, 4))
Namespace.addCategoryObject('elementBinding', Variant.name().localName(), Variant)

Meta = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Meta'), CTD_ANON_3, location=pyxb.utils.utility.Location('ClaML.xsd', 53, 4))
Namespace.addCategoryObject('elementBinding', Meta.name().localName(), Meta)

Identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), CTD_ANON_4, location=pyxb.utils.utility.Location('ClaML.xsd', 60, 4))
Namespace.addCategoryObject('elementBinding', Identifier.name().localName(), Identifier)

Title = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Title'), CTD_ANON_5, location=pyxb.utils.utility.Location('ClaML.xsd', 66, 4))
Namespace.addCategoryObject('elementBinding', Title.name().localName(), Title)

Authors = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Authors'), CTD_ANON_6, location=pyxb.utils.utility.Location('ClaML.xsd', 73, 4))
Namespace.addCategoryObject('elementBinding', Authors.name().localName(), Authors)

Author = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Author'), CTD_ANON_7, location=pyxb.utils.utility.Location('ClaML.xsd', 80, 4))
Namespace.addCategoryObject('elementBinding', Author.name().localName(), Author)

ClassKinds = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClassKinds'), CTD_ANON_8, location=pyxb.utils.utility.Location('ClaML.xsd', 85, 4))
Namespace.addCategoryObject('elementBinding', ClassKinds.name().localName(), ClassKinds)

RubricKinds = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RubricKinds'), CTD_ANON_9, location=pyxb.utils.utility.Location('ClaML.xsd', 92, 4))
Namespace.addCategoryObject('elementBinding', RubricKinds.name().localName(), RubricKinds)

UsageKinds = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UsageKinds'), CTD_ANON_10, location=pyxb.utils.utility.Location('ClaML.xsd', 99, 4))
Namespace.addCategoryObject('elementBinding', UsageKinds.name().localName(), UsageKinds)

ClassKind = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClassKind'), CTD_ANON_11, location=pyxb.utils.utility.Location('ClaML.xsd', 106, 4))
Namespace.addCategoryObject('elementBinding', ClassKind.name().localName(), ClassKind)

UsageKind = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UsageKind'), CTD_ANON_12, location=pyxb.utils.utility.Location('ClaML.xsd', 130, 4))
Namespace.addCategoryObject('elementBinding', UsageKind.name().localName(), UsageKind)

Display = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Display'), CTD_ANON_13, location=pyxb.utils.utility.Location('ClaML.xsd', 136, 4))
Namespace.addCategoryObject('elementBinding', Display.name().localName(), Display)

Modifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Modifier'), CTD_ANON_14, location=pyxb.utils.utility.Location('ClaML.xsd', 142, 4))
Namespace.addCategoryObject('elementBinding', Modifier.name().localName(), Modifier)

ModifierClass = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ModifierClass'), CTD_ANON_15, location=pyxb.utils.utility.Location('ClaML.xsd', 154, 4))
Namespace.addCategoryObject('elementBinding', ModifierClass.name().localName(), ModifierClass)

Class = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Class'), CTD_ANON_16, location=pyxb.utils.utility.Location('ClaML.xsd', 169, 4))
Namespace.addCategoryObject('elementBinding', Class.name().localName(), Class)

ExcludeModifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExcludeModifier'), CTD_ANON_17, location=pyxb.utils.utility.Location('ClaML.xsd', 205, 4))
Namespace.addCategoryObject('elementBinding', ExcludeModifier.name().localName(), ExcludeModifier)

ValidModifierClass = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValidModifierClass'), CTD_ANON_18, location=pyxb.utils.utility.Location('ClaML.xsd', 211, 4))
Namespace.addCategoryObject('elementBinding', ValidModifierClass.name().localName(), ValidModifierClass)

Rubric = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rubric'), CTD_ANON_19, location=pyxb.utils.utility.Location('ClaML.xsd', 217, 4))
Namespace.addCategoryObject('elementBinding', Rubric.name().localName(), Rubric)

Label = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Label'), CTD_ANON_20, location=pyxb.utils.utility.Location('ClaML.xsd', 228, 4))
Namespace.addCategoryObject('elementBinding', Label.name().localName(), Label)

History = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'History'), CTD_ANON_21, location=pyxb.utils.utility.Location('ClaML.xsd', 236, 4))
Namespace.addCategoryObject('elementBinding', History.name().localName(), History)

SuperClass = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SuperClass'), CTD_ANON_22, location=pyxb.utils.utility.Location('ClaML.xsd', 242, 4))
Namespace.addCategoryObject('elementBinding', SuperClass.name().localName(), SuperClass)

SubClass = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubClass'), CTD_ANON_23, location=pyxb.utils.utility.Location('ClaML.xsd', 248, 4))
Namespace.addCategoryObject('elementBinding', SubClass.name().localName(), SubClass)

Reference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reference'), CTD_ANON_24, location=pyxb.utils.utility.Location('ClaML.xsd', 254, 4))
Namespace.addCategoryObject('elementBinding', Reference.name().localName(), Reference)

Para = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Para'), CTD_ANON_25, location=pyxb.utils.utility.Location('ClaML.xsd', 264, 4))
Namespace.addCategoryObject('elementBinding', Para.name().localName(), Para)

Include = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Include'), CTD_ANON_26, location=pyxb.utils.utility.Location('ClaML.xsd', 285, 4))
Namespace.addCategoryObject('elementBinding', Include.name().localName(), Include)

IncludeDescendants = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IncludeDescendants'), CTD_ANON_27, location=pyxb.utils.utility.Location('ClaML.xsd', 291, 4))
Namespace.addCategoryObject('elementBinding', IncludeDescendants.name().localName(), IncludeDescendants)

List = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'List'), CTD_ANON_28, location=pyxb.utils.utility.Location('ClaML.xsd', 297, 4))
Namespace.addCategoryObject('elementBinding', List.name().localName(), List)

ListItem = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ListItem'), CTD_ANON_29, location=pyxb.utils.utility.Location('ClaML.xsd', 305, 4))
Namespace.addCategoryObject('elementBinding', ListItem.name().localName(), ListItem)

Table = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Table'), CTD_ANON_30, location=pyxb.utils.utility.Location('ClaML.xsd', 317, 4))
Namespace.addCategoryObject('elementBinding', Table.name().localName(), Table)

Caption = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Caption'), CTD_ANON_31, location=pyxb.utils.utility.Location('ClaML.xsd', 328, 4))
Namespace.addCategoryObject('elementBinding', Caption.name().localName(), Caption)

THead = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'THead'), CTD_ANON_32, location=pyxb.utils.utility.Location('ClaML.xsd', 334, 4))
Namespace.addCategoryObject('elementBinding', THead.name().localName(), THead)

TBody = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TBody'), CTD_ANON_33, location=pyxb.utils.utility.Location('ClaML.xsd', 342, 4))
Namespace.addCategoryObject('elementBinding', TBody.name().localName(), TBody)

TFoot = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TFoot'), CTD_ANON_34, location=pyxb.utils.utility.Location('ClaML.xsd', 350, 4))
Namespace.addCategoryObject('elementBinding', TFoot.name().localName(), TFoot)

Row = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Row'), CTD_ANON_35, location=pyxb.utils.utility.Location('ClaML.xsd', 358, 4))
Namespace.addCategoryObject('elementBinding', Row.name().localName(), Row)

Cell = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cell'), CTD_ANON_36, location=pyxb.utils.utility.Location('ClaML.xsd', 366, 4))
Namespace.addCategoryObject('elementBinding', Cell.name().localName(), Cell)

Term = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Term'), CTD_ANON_37, location=pyxb.utils.utility.Location('ClaML.xsd', 380, 4))
Namespace.addCategoryObject('elementBinding', Term.name().localName(), Term)

RubricKind = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RubricKind'), CTD_ANON_38, location=pyxb.utils.utility.Location('ClaML.xsd', 114, 4))
Namespace.addCategoryObject('elementBinding', RubricKind.name().localName(), RubricKind)

ModifiedBy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ModifiedBy'), CTD_ANON_39, location=pyxb.utils.utility.Location('ClaML.xsd', 186, 4))
Namespace.addCategoryObject('elementBinding', ModifiedBy.name().localName(), ModifiedBy)

Fragment = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Fragment'), CTD_ANON_40, location=pyxb.utils.utility.Location('ClaML.xsd', 270, 4))
Namespace.addCategoryObject('elementBinding', Fragment.name().localName(), Fragment)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Variants'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('ClaML.xsd', 41, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Meta'), CTD_ANON_3, scope=CTD_ANON, location=pyxb.utils.utility.Location('ClaML.xsd', 53, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Identifier'), CTD_ANON_4, scope=CTD_ANON, location=pyxb.utils.utility.Location('ClaML.xsd', 60, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Title'), CTD_ANON_5, scope=CTD_ANON, location=pyxb.utils.utility.Location('ClaML.xsd', 66, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Authors'), CTD_ANON_6, scope=CTD_ANON, location=pyxb.utils.utility.Location('ClaML.xsd', 73, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClassKinds'), CTD_ANON_8, scope=CTD_ANON, location=pyxb.utils.utility.Location('ClaML.xsd', 85, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RubricKinds'), CTD_ANON_9, scope=CTD_ANON, location=pyxb.utils.utility.Location('ClaML.xsd', 92, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UsageKinds'), CTD_ANON_10, scope=CTD_ANON, location=pyxb.utils.utility.Location('ClaML.xsd', 99, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Modifier'), CTD_ANON_14, scope=CTD_ANON, location=pyxb.utils.utility.Location('ClaML.xsd', 142, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ModifierClass'), CTD_ANON_15, scope=CTD_ANON, location=pyxb.utils.utility.Location('ClaML.xsd', 154, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Class'), CTD_ANON_16, scope=CTD_ANON, location=pyxb.utils.utility.Location('ClaML.xsd', 169, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 26, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 27, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ClaML.xsd', 29, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ClaML.xsd', 30, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ClaML.xsd', 32, 16))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 34, 16))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 35, 16))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 36, 16))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Meta')), pyxb.utils.utility.Location('ClaML.xsd', 26, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Identifier')), pyxb.utils.utility.Location('ClaML.xsd', 27, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Title')), pyxb.utils.utility.Location('ClaML.xsd', 28, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Authors')), pyxb.utils.utility.Location('ClaML.xsd', 29, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Variants')), pyxb.utils.utility.Location('ClaML.xsd', 30, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClassKinds')), pyxb.utils.utility.Location('ClaML.xsd', 31, 16))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UsageKinds')), pyxb.utils.utility.Location('ClaML.xsd', 32, 16))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RubricKinds')), pyxb.utils.utility.Location('ClaML.xsd', 33, 16))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Modifier')), pyxb.utils.utility.Location('ClaML.xsd', 34, 16))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ModifierClass')), pyxb.utils.utility.Location('ClaML.xsd', 35, 16))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Class')), pyxb.utils.utility.Location('ClaML.xsd', 36, 16))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Variant'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('ClaML.xsd', 48, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Variant')), pyxb.utils.utility.Location('ClaML.xsd', 44, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_3()




CTD_ANON_6._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Author'), CTD_ANON_7, scope=CTD_ANON_6, location=pyxb.utils.utility.Location('ClaML.xsd', 80, 4)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 76, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_6._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Author')), pyxb.utils.utility.Location('ClaML.xsd', 76, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_6._Automaton = _BuildAutomaton_4()




def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_5()




CTD_ANON_8._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClassKind'), CTD_ANON_11, scope=CTD_ANON_8, location=pyxb.utils.utility.Location('ClaML.xsd', 106, 4)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_8._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClassKind')), pyxb.utils.utility.Location('ClaML.xsd', 88, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_6()




CTD_ANON_9._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RubricKind'), CTD_ANON_38, scope=CTD_ANON_9, location=pyxb.utils.utility.Location('ClaML.xsd', 114, 4)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_9._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RubricKind')), pyxb.utils.utility.Location('ClaML.xsd', 95, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_7()




CTD_ANON_10._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UsageKind'), CTD_ANON_12, scope=CTD_ANON_10, location=pyxb.utils.utility.Location('ClaML.xsd', 130, 4)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_10._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UsageKind')), pyxb.utils.utility.Location('ClaML.xsd', 102, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_8()




CTD_ANON_11._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Display'), CTD_ANON_13, scope=CTD_ANON_11, location=pyxb.utils.utility.Location('ClaML.xsd', 136, 4)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 109, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_11._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Display')), pyxb.utils.utility.Location('ClaML.xsd', 109, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_9()




def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_10()




CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Meta'), CTD_ANON_3, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('ClaML.xsd', 53, 4)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rubric'), CTD_ANON_19, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('ClaML.xsd', 217, 4)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'History'), CTD_ANON_21, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('ClaML.xsd', 236, 4)))

CTD_ANON_14._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubClass'), CTD_ANON_23, scope=CTD_ANON_14, location=pyxb.utils.utility.Location('ClaML.xsd', 248, 4)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 145, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 146, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 147, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 148, 16))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Meta')), pyxb.utils.utility.Location('ClaML.xsd', 145, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubClass')), pyxb.utils.utility.Location('ClaML.xsd', 146, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Rubric')), pyxb.utils.utility.Location('ClaML.xsd', 147, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_14._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'History')), pyxb.utils.utility.Location('ClaML.xsd', 148, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_11()




CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Meta'), CTD_ANON_3, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('ClaML.xsd', 53, 4)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rubric'), CTD_ANON_19, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('ClaML.xsd', 217, 4)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'History'), CTD_ANON_21, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('ClaML.xsd', 236, 4)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SuperClass'), CTD_ANON_22, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('ClaML.xsd', 242, 4)))

CTD_ANON_15._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubClass'), CTD_ANON_23, scope=CTD_ANON_15, location=pyxb.utils.utility.Location('ClaML.xsd', 248, 4)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 157, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 159, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 160, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 161, 16))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Meta')), pyxb.utils.utility.Location('ClaML.xsd', 157, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SuperClass')), pyxb.utils.utility.Location('ClaML.xsd', 158, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubClass')), pyxb.utils.utility.Location('ClaML.xsd', 159, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Rubric')), pyxb.utils.utility.Location('ClaML.xsd', 160, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_15._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'History')), pyxb.utils.utility.Location('ClaML.xsd', 161, 16))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_12()




CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Meta'), CTD_ANON_3, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('ClaML.xsd', 53, 4)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ModifiedBy'), CTD_ANON_39, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('ClaML.xsd', 186, 4)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExcludeModifier'), CTD_ANON_17, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('ClaML.xsd', 205, 4)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rubric'), CTD_ANON_19, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('ClaML.xsd', 217, 4)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'History'), CTD_ANON_21, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('ClaML.xsd', 236, 4)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SuperClass'), CTD_ANON_22, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('ClaML.xsd', 242, 4)))

CTD_ANON_16._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubClass'), CTD_ANON_23, scope=CTD_ANON_16, location=pyxb.utils.utility.Location('ClaML.xsd', 248, 4)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 172, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 173, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 174, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 175, 16))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 176, 16))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 177, 16))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 178, 16))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Meta')), pyxb.utils.utility.Location('ClaML.xsd', 172, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SuperClass')), pyxb.utils.utility.Location('ClaML.xsd', 173, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubClass')), pyxb.utils.utility.Location('ClaML.xsd', 174, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ModifiedBy')), pyxb.utils.utility.Location('ClaML.xsd', 175, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExcludeModifier')), pyxb.utils.utility.Location('ClaML.xsd', 176, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Rubric')), pyxb.utils.utility.Location('ClaML.xsd', 177, 16))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_16._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'History')), pyxb.utils.utility.Location('ClaML.xsd', 178, 16))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_13()




CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Label'), CTD_ANON_20, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('ClaML.xsd', 228, 4)))

CTD_ANON_19._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'History'), CTD_ANON_21, scope=CTD_ANON_19, location=pyxb.utils.utility.Location('ClaML.xsd', 236, 4)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 221, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Label')), pyxb.utils.utility.Location('ClaML.xsd', 220, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_19._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'History')), pyxb.utils.utility.Location('ClaML.xsd', 221, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_14()




CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reference'), CTD_ANON_24, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('ClaML.xsd', 254, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Para'), CTD_ANON_25, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('ClaML.xsd', 264, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Fragment'), CTD_ANON_40, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('ClaML.xsd', 270, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Include'), CTD_ANON_26, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('ClaML.xsd', 285, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IncludeDescendants'), CTD_ANON_27, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('ClaML.xsd', 291, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'List'), CTD_ANON_28, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('ClaML.xsd', 297, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Table'), CTD_ANON_30, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('ClaML.xsd', 317, 4)))

CTD_ANON_20._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Term'), CTD_ANON_37, scope=CTD_ANON_20, location=pyxb.utils.utility.Location('ClaML.xsd', 380, 4)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 230, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ClaML.xsd', 6, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reference')), pyxb.utils.utility.Location('ClaML.xsd', 7, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Term')), pyxb.utils.utility.Location('ClaML.xsd', 8, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Para')), pyxb.utils.utility.Location('ClaML.xsd', 15, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Include')), pyxb.utils.utility.Location('ClaML.xsd', 16, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IncludeDescendants')), pyxb.utils.utility.Location('ClaML.xsd', 17, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Fragment')), pyxb.utils.utility.Location('ClaML.xsd', 18, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'List')), pyxb.utils.utility.Location('ClaML.xsd', 19, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_20._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Table')), pyxb.utils.utility.Location('ClaML.xsd', 20, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_15()




def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_16()




def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_17()




CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reference'), CTD_ANON_24, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('ClaML.xsd', 254, 4)))

CTD_ANON_25._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Term'), CTD_ANON_37, scope=CTD_ANON_25, location=pyxb.utils.utility.Location('ClaML.xsd', 380, 4)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 266, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ClaML.xsd', 6, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reference')), pyxb.utils.utility.Location('ClaML.xsd', 7, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_25._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Term')), pyxb.utils.utility.Location('ClaML.xsd', 8, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_18()




CTD_ANON_28._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ListItem'), CTD_ANON_29, scope=CTD_ANON_28, location=pyxb.utils.utility.Location('ClaML.xsd', 305, 4)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_28._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ListItem')), pyxb.utils.utility.Location('ClaML.xsd', 300, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_19()




CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reference'), CTD_ANON_24, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('ClaML.xsd', 254, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Para'), CTD_ANON_25, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('ClaML.xsd', 264, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Include'), CTD_ANON_26, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('ClaML.xsd', 285, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'List'), CTD_ANON_28, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('ClaML.xsd', 297, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Table'), CTD_ANON_30, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('ClaML.xsd', 317, 4)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Term'), CTD_ANON_37, scope=CTD_ANON_29, location=pyxb.utils.utility.Location('ClaML.xsd', 380, 4)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 307, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ClaML.xsd', 6, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reference')), pyxb.utils.utility.Location('ClaML.xsd', 7, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Term')), pyxb.utils.utility.Location('ClaML.xsd', 8, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Para')), pyxb.utils.utility.Location('ClaML.xsd', 309, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Include')), pyxb.utils.utility.Location('ClaML.xsd', 310, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'List')), pyxb.utils.utility.Location('ClaML.xsd', 311, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Table')), pyxb.utils.utility.Location('ClaML.xsd', 312, 16))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_29._Automaton = _BuildAutomaton_20()




CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Caption'), CTD_ANON_31, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('ClaML.xsd', 328, 4)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'THead'), CTD_ANON_32, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('ClaML.xsd', 334, 4)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TBody'), CTD_ANON_33, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('ClaML.xsd', 342, 4)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TFoot'), CTD_ANON_34, scope=CTD_ANON_30, location=pyxb.utils.utility.Location('ClaML.xsd', 350, 4)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ClaML.xsd', 320, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ClaML.xsd', 321, 16))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ClaML.xsd', 322, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ClaML.xsd', 323, 16))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Caption')), pyxb.utils.utility.Location('ClaML.xsd', 320, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'THead')), pyxb.utils.utility.Location('ClaML.xsd', 321, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TBody')), pyxb.utils.utility.Location('ClaML.xsd', 322, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TFoot')), pyxb.utils.utility.Location('ClaML.xsd', 323, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_30._Automaton = _BuildAutomaton_21()




CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reference'), CTD_ANON_24, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('ClaML.xsd', 254, 4)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Term'), CTD_ANON_37, scope=CTD_ANON_31, location=pyxb.utils.utility.Location('ClaML.xsd', 380, 4)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 330, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ClaML.xsd', 6, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reference')), pyxb.utils.utility.Location('ClaML.xsd', 7, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Term')), pyxb.utils.utility.Location('ClaML.xsd', 8, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_31._Automaton = _BuildAutomaton_22()




CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Row'), CTD_ANON_35, scope=CTD_ANON_32, location=pyxb.utils.utility.Location('ClaML.xsd', 358, 4)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Row')), pyxb.utils.utility.Location('ClaML.xsd', 337, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_32._Automaton = _BuildAutomaton_23()




CTD_ANON_33._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Row'), CTD_ANON_35, scope=CTD_ANON_33, location=pyxb.utils.utility.Location('ClaML.xsd', 358, 4)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_33._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Row')), pyxb.utils.utility.Location('ClaML.xsd', 345, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_33._Automaton = _BuildAutomaton_24()




CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Row'), CTD_ANON_35, scope=CTD_ANON_34, location=pyxb.utils.utility.Location('ClaML.xsd', 358, 4)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Row')), pyxb.utils.utility.Location('ClaML.xsd', 353, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_34._Automaton = _BuildAutomaton_25()




CTD_ANON_35._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Cell'), CTD_ANON_36, scope=CTD_ANON_35, location=pyxb.utils.utility.Location('ClaML.xsd', 366, 4)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 361, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_35._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Cell')), pyxb.utils.utility.Location('ClaML.xsd', 361, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_35._Automaton = _BuildAutomaton_26()




CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reference'), CTD_ANON_24, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('ClaML.xsd', 254, 4)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Para'), CTD_ANON_25, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('ClaML.xsd', 264, 4)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Include'), CTD_ANON_26, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('ClaML.xsd', 285, 4)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'List'), CTD_ANON_28, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('ClaML.xsd', 297, 4)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Table'), CTD_ANON_30, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('ClaML.xsd', 317, 4)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Term'), CTD_ANON_37, scope=CTD_ANON_36, location=pyxb.utils.utility.Location('ClaML.xsd', 380, 4)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 368, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ClaML.xsd', 6, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reference')), pyxb.utils.utility.Location('ClaML.xsd', 7, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Term')), pyxb.utils.utility.Location('ClaML.xsd', 8, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Para')), pyxb.utils.utility.Location('ClaML.xsd', 370, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Include')), pyxb.utils.utility.Location('ClaML.xsd', 371, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'List')), pyxb.utils.utility.Location('ClaML.xsd', 372, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Table')), pyxb.utils.utility.Location('ClaML.xsd', 373, 16))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_36._Automaton = _BuildAutomaton_27()




def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_37._Automaton = _BuildAutomaton_28()




CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Display'), CTD_ANON_13, scope=CTD_ANON_38, location=pyxb.utils.utility.Location('ClaML.xsd', 136, 4)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 117, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Display')), pyxb.utils.utility.Location('ClaML.xsd', 117, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_38._Automaton = _BuildAutomaton_29()




CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Meta'), CTD_ANON_3, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('ClaML.xsd', 53, 4)))

CTD_ANON_39._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ValidModifierClass'), CTD_ANON_18, scope=CTD_ANON_39, location=pyxb.utils.utility.Location('ClaML.xsd', 211, 4)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 189, 16))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 190, 16))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Meta')), pyxb.utils.utility.Location('ClaML.xsd', 189, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_39._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ValidModifierClass')), pyxb.utils.utility.Location('ClaML.xsd', 190, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_39._Automaton = _BuildAutomaton_30()




CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Reference'), CTD_ANON_24, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('ClaML.xsd', 254, 4)))

CTD_ANON_40._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Term'), CTD_ANON_37, scope=CTD_ANON_40, location=pyxb.utils.utility.Location('ClaML.xsd', 380, 4)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('ClaML.xsd', 272, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('ClaML.xsd', 6, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Reference')), pyxb.utils.utility.Location('ClaML.xsd', 7, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_40._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Term')), pyxb.utils.utility.Location('ClaML.xsd', 8, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_40._Automaton = _BuildAutomaton_31()

