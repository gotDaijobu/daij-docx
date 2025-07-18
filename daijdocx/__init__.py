# encoding: utf-8

from daijdocx.api import Document  # noqa

__version__ = 'daij_0.1' 


# register custom Part classes with opc package reader

from daijdocx.opc.constants import CONTENT_TYPE as CT, RELATIONSHIP_TYPE as RT
from daijdocx.opc.part import PartFactory
from daijdocx.opc.parts.coreprops import CorePropertiesPart

from daijdocx.parts.document import DocumentPart
from daijdocx.parts.hdrftr import FooterPart, HeaderPart
from daijdocx.parts.image import ImagePart
from daijdocx.parts.numbering import NumberingPart
from daijdocx.parts.settings import SettingsPart
from daijdocx.parts.styles import StylesPart
from daijdocx.parts.comments import CommentsPart
from daijdocx.parts.footnotes import FootnotesPart


def part_class_selector(content_type, reltype):
    if reltype == RT.IMAGE:
        return ImagePart
    return None


PartFactory.part_class_selector = part_class_selector
PartFactory.part_type_for[CT.WML_COMMENTS] = CommentsPart
PartFactory.part_type_for[CT.OPC_CORE_PROPERTIES] = CorePropertiesPart
PartFactory.part_type_for[CT.WML_DOCUMENT_MAIN] = DocumentPart
PartFactory.part_type_for[CT.WML_FOOTER] = FooterPart
PartFactory.part_type_for[CT.WML_HEADER] = HeaderPart
PartFactory.part_type_for[CT.WML_NUMBERING] = NumberingPart
PartFactory.part_type_for[CT.WML_SETTINGS] = SettingsPart
PartFactory.part_type_for[CT.WML_STYLES] = StylesPart
PartFactory.part_type_for[CT.WML_FOOTNOTES] = FootnotesPart

del (
    CT,
    CorePropertiesPart,
    DocumentPart,
    FooterPart,
    HeaderPart,
    FootnotesPart,
    CommentsPart,
    NumberingPart,
    PartFactory,
    SettingsPart,
    StylesPart,
    part_class_selector,
)
