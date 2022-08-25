import asyncio
from typing import List
from utils import (
    disambiguate_word_sense,
    create_cwn_sense_tags,
    add_multiple_textsubscripts,
)


async def create_tags(segmented_result):
    """The create_tags function runs two asynchronous operations (i.e.
    `add_multiple_textsubscripts` and `create_cwn_sense_tags`).

    Args:
        segmented_result (list)
    """

    return await asyncio.gather(
        *[
            add_multiple_textsubscripts("cwn", segmented_result),
            create_cwn_sense_tags(segmented_result),
        ]
    )


def handle_cwn_sense_tag(sentence_list: List[str]) -> List[str]:
    segmented_result = asyncio.run(disambiguate_word_sense(sentence_list))
    span_tags, cwn_tags = asyncio.run(create_tags(segmented_result))

    return span_tags, cwn_tags
