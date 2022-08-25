import asyncio
from typing import List, Tuple
from DistilTag import DistilTag
from CwnSenseTagger import senseTag


# --------------------------------------------------------------------
# distil tag

tagger = DistilTag()


async def tag_values(value):
    return tagger.tag(value)


async def disambiguate_word_sense(sentence_list: List[str]) -> List[Tuple[str]]:
    """The disambiguate_word_sense function disambiuates the word sense.

    Args:
        sentence_list (list): a list of sentences
    Returns:
        a list of tuples.
    """

    return await asyncio.gather(*list(map(tag_values, sentence_list)))


# --------------------------------------------------------------------
# CWN sense tag


async def sense_value(value):
    return senseTag(value)


async def create_cwn_sense_tags(disambiguated_list: List[List[List[tuple]]]):
    return await asyncio.gather(*list(map(sense_value, disambiguated_list)))
