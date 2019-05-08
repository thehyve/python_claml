from abc import abstractmethod
from typing import Sequence, Optional
from xml.dom import Node

CDATA = str
ID = str
IDREF = str
IDREFS = Sequence[IDREF]
NMTOKEN = str


class PCDATA:
    @property
    @abstractmethod
    def data(self) -> CDATA:
        pass


class NodeWrapper:
    @abstractmethod
    def toxml(self) -> CDATA:
        pass

    @abstractmethod
    def toDOM(self) -> Node:
        pass


class Meta:
    @property
    @abstractmethod
    def name(self) -> CDATA:
        pass

    @property
    @abstractmethod
    def value(self) -> CDATA:
        pass

    @property
    @abstractmethod
    def variants(self) -> IDREFS:
        pass


class Identifier:
    @property
    @abstractmethod
    def authority(self) -> NMTOKEN:
        pass

    @property
    @abstractmethod
    def uid(self) -> CDATA:
        pass


class Title(PCDATA):
    @property
    @abstractmethod
    def name(self) -> NMTOKEN:
        pass

    @property
    @abstractmethod
    def version(self) -> CDATA:
        pass

    @property
    @abstractmethod
    def date(self) -> CDATA:
        pass


class Author(PCDATA):
    @property
    @abstractmethod
    def name(self) -> ID:
        pass


class Authors:
    @property
    @abstractmethod
    def Author(self) -> Sequence[Author]:
        pass


class History(PCDATA):
    @property
    @abstractmethod
    def author(self) -> IDREF:
        pass

    @property
    @abstractmethod
    def date(self) -> NMTOKEN:
        pass


class Label(NodeWrapper):
    @property
    @abstractmethod
    def variants(self) -> IDREFS:
        pass


class Rubric:
    @property
    @abstractmethod
    def id(self) -> ID:
        pass

    @property
    @abstractmethod
    def kind(self) -> IDREF:
        pass

    @property
    @abstractmethod
    def usage(self) -> IDREF:
        pass

    @property
    @abstractmethod
    def Label(self) -> Sequence[Label]:
        pass

    @property
    @abstractmethod
    def History(self) -> Sequence[History]:
        pass


class Variant(PCDATA):
    @property
    @abstractmethod
    def name(self) -> ID:
        pass


class Variants:
    @property
    @abstractmethod
    def Variant(self) -> Sequence[Variant]:
        pass


class ClassKind:
    @property
    @abstractmethod
    def name(self) -> str:
        pass


class ClassKinds:
    @property
    @abstractmethod
    def ClassKind(self) -> Sequence[ClassKind]:
        pass


class UsageKind:
    @property
    @abstractmethod
    def name(self) -> ID:
        pass

    @property
    @abstractmethod
    def mark(self) -> CDATA:
        pass


class UsageKinds:
    @property
    @abstractmethod
    def UsageKind(self) -> Sequence[UsageKind]:
        pass


class RubricKind:
    @property
    @abstractmethod
    def name(self) -> ID:
        pass

    @property
    @abstractmethod
    def inherited(self) -> str:
        pass


class RubricKinds:
    @property
    @abstractmethod
    def RubricKind(self) -> Sequence[RubricKind]:
        pass


class SuperClass:
    @property
    @abstractmethod
    def code(self) -> NMTOKEN:
        pass

    @property
    @abstractmethod
    def variants(self) -> IDREFS:
        pass


class SubClass(SuperClass):
    pass


class Modifier:
    @property
    @abstractmethod
    def code(self) -> NMTOKEN:
        pass

    @property
    @abstractmethod
    def variants(self) -> IDREFS:
        pass

    @property
    @abstractmethod
    def Meta(self) -> Sequence[Meta]:
        pass

    @property
    @abstractmethod
    def SubClass(self) -> Sequence[SubClass]:
        pass

    @property
    @abstractmethod
    def Rubric(self) -> Sequence[Rubric]:
        pass

    @property
    @abstractmethod
    def History(self) -> Sequence[History]:
        pass


class ModifierClass(Modifier):
    @property
    @abstractmethod
    def modifier(self) -> NMTOKEN:
        pass

    @property
    @abstractmethod
    def usage(self) -> IDREF:
        pass

    @property
    @abstractmethod
    def SuperClass(self) -> SuperClass:
        pass


class ValidModifierClass:
    pass


class ModifiedBy:
    pass


class ExcludeModifier:
    pass


class Class(Modifier):
    @property
    @abstractmethod
    def kind(self) -> IDREF:
        pass

    @property
    @abstractmethod
    def usage(self) -> IDREF:
        pass

    @property
    @abstractmethod
    def SuperClass(self) -> Sequence[SuperClass]:
        pass

    @property
    @abstractmethod
    def ModifiedBy(self) -> Sequence[ModifiedBy]:
        pass

    @property
    @abstractmethod
    def ExcludeModifier(self) -> Sequence[ExcludeModifier]:
        pass


class ClaML:
    @property
    @abstractmethod
    def Meta(self) -> Meta:
        pass

    @property
    @abstractmethod
    def Identifier(self) -> Sequence[Identifier]:
        pass

    @property
    @abstractmethod
    def Title(self) -> Title:
        pass

    @property
    @abstractmethod
    def Authors(self) -> Optional[Authors]:
        pass

    @property
    @abstractmethod
    def Variants(self) -> Optional[Variants]:
        pass

    @property
    @abstractmethod
    def ClassKinds(self) -> ClassKinds:
        pass

    @property
    @abstractmethod
    def UsageKinds(self) -> Optional[UsageKinds]:
        pass

    @property
    @abstractmethod
    def RubricKinds(self) -> RubricKinds:
        pass

    @property
    @abstractmethod
    def Modifier(self) -> Sequence[Modifier]:
        pass

    @property
    @abstractmethod
    def ModifierClass(self) -> Sequence[ModifierClass]:
        pass

    @property
    @abstractmethod
    def Class(self) -> Sequence[Class]:
        pass
