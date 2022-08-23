from dataclasses import dataclass
from typing import List, Union, Tuple, Optional
from ckip_transformers.nlp.util import NerToken


def add_textsubscript(
    ner_token_list: List[NerToken],
) -> List[List[Union[str, Tuple[int]]]]:
    """The add_textsubscript method combines the token word and the NER-tag, and
    specifies the NER-tag to be displayed as subscript.

    Args:
        ner_token_list (NerToken): a list of NerToken
    Returns:
        a list: [
            ["<span>傅達仁<sub style='margin-right: 0.1rem'>PERSON</sub></span>", (0, 3)]
            ...
        ]
    """

    combine = lambda value: [
        f"<span>{value.word}<sub style='margin-right: 0.1rem'>{value.ner}</sub></span>",
        value.idx,
    ]
    return list(map(combine, ner_token_list))


def modify_sentence(
    span_list: List[List[Union[str, Tuple[int]]]],
    sentence: str,
    increased_len: Optional[int] = 0,
) -> str:
    if len(span_list) == 1:
        modified_word, index = span_list[0]
        start_index, end_index = index
        start_index += increased_len
        end_index += increased_len
        return "".join((sentence[:start_index], modified_word, sentence[end_index:]))

    modified_word, index = span_list.pop(0)
    start_index, end_index = index

    if increased_len:
        start_index += increased_len
        end_index += increased_len

    original_word = sentence[start_index:end_index]
    modified_sentence = "".join(
        (sentence[:start_index], modified_word, sentence[end_index:])
    )

    index_gap = len(modified_word) - len(original_word)

    return modify_sentence(span_list, modified_sentence, increased_len + index_gap)


def replace_entities(sentence: str, ner_token_list: List[NerToken]) -> str:
    """The replace_entities function replaces words that are recognized
    as the token words with opening and closing span tags.

    Args:
        sentence (str): the orignal sentence
        ner_token_list (NerToken): a list of NerToken
    Returns:
        a str
    """
    modified_ner_token_list = add_textsubscript(ner_token_list)
    return modify_sentence(modified_ner_token_list, sentence)
