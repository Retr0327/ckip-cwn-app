import json
import asyncio
from models import redis_cli
from typing import List, Union
from utils import WordSegmentation, add_multiple_textsubscripts


async def dump_to_redis(ws_result) -> None:
    """The dump_to_redis function writes the stringified `ws_result` to Redis.

    Args:
        ws_result (list): the result of word segmentation
    """
    key = "ws"
    ttl = 3
    dump_result = json.dumps(ws_result)
    redis_cli.hset(key, mapping={"data": dump_result})
    redis_cli.expire(name=key, time=ttl)


async def create_result(ws_result) -> List[Union[str, int]]:
    """The create_result function runs two asynchronous operations (i.e.
    `add_multiple_textsubscripts` and `dump_to_redis`).

    Args:
        ws_result (list): the result of word segmentation
    """
    return await asyncio.gather(
        *[
            add_multiple_textsubscripts("ws", ws_result),
            dump_to_redis(ws_result),
        ]
    )


def handle_word_segmentation(sentence_list: List[str]) -> List[str]:
    """The handle_word_segmentation function handles the request that deals with word
    segmentation.

    Args:
        sentence_list (list): a list of sentences
    Returns:
        a list of strings
    """
    ws_result = WordSegmentation(sentence_list).segment()
    ws_span_tags, redis_result = asyncio.run(create_result(ws_result))

    return ws_span_tags
