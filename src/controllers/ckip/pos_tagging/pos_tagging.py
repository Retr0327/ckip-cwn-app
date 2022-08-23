import asyncio
from typing import List
from utils import Segmenter


async def add_textsubscript(segmented_list: List[str]) -> str:
    create = (
        lambda value: f"<span>{value[0]}<sub style='margin-right: 0.1rem'>{value[1]}</sub></span>"
    )
    return "".join(list(map(create, segmented_list)))


async def add_multiple_textsubscripts(segmented_result: List[List[str]]) -> List[str]:
    return await asyncio.gather(*list(map(add_textsubscript, segmented_result)))


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
