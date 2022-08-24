import asyncio
from typing import List
from itertools import chain
from utils import disambiguate_word_sense, create_cwn_sense_tags


async def add_textsubscript(segmented_list) -> str:
    create = (
        lambda value: f"<span>{value[0]}<sub style='margin-right: 0.1rem'>{value[1]}</sub></span>"
    )
    return "".join(list(map(create, chain(*segmented_list))))


async def add_multiple_textsubscripts(segmented_result):
    return await asyncio.gather(*list(map(add_textsubscript, segmented_result)))


def handle_cwn_sense_tag(sentence_list: List[str]) -> List[str]:
    segmented_result = disambiguate_word_sense(sentence_list)
    span_tags = asyncio.run(add_multiple_textsubscripts(segmented_result))
    cwn_tags = create_cwn_sense_tags(segmented_result)

    return span_tags, cwn_tags
