import json
import asyncio
from typing import List
from models import redis_cli
from utils import add_multiple_textsubscripts, PosTagging


def handle_pos_tagging(nlp_model: str, sentence_list: List[str]):
    """The handle_pos_tagging function handles the request that deals with pos-tagging.

    Args:
        sentence_list (list): a list of sentences
    Returns:
        a list of strings
    """
    ws_result = json.loads(redis_cli.hgetall("ws")["data"])
    segmented_result = PosTagging(nlp_model, ws_result).tag()
    return asyncio.run(add_multiple_textsubscripts("pos", segmented_result))
