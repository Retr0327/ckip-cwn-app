import asyncio
from typing import List
from utils import Segmenter, add_multiple_textsubscripts


def handle_pos_tagging(sentence_list: List[str]):
    """The handle_pos_tagging function handles the request that deals with pos-tagging.

    Args:
        sentence_list (list): a list of sentences
    Returns:
        a list of strings
    """
    segmented_result = Segmenter(sentence_list).segment()
    result = asyncio.run(add_multiple_textsubscripts(segmented_result))
    return result
