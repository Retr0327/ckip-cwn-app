from .textsubscript import add_multiple_textsubscripts
from .text_color import create_entity_color, create_pos_color
from .cwn_helper import disambiguate_word_sense, create_cwn_sense_tags
from .ckip_helper import PosTagging, WordSegmentation, chunk_multiple_entities


__all__ = [
    "disambiguate_word_sense",
    "PosTagging",
    "WordSegmentation",
    "chunk_multiple_entities",
    "create_cwn_sense_tags",
    "add_multiple_textsubscripts",
    "create_entity_color",
    "create_pos_color",
]
