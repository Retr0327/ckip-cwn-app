import asyncio
from typing import List, Tuple, Union
from .ner_modifier import replace_entities
from ckip_transformers.nlp.util import NerToken


async def chunk_entities(zip_value: Tuple[Union[str, NerToken]]) -> str:
    sentence, ner_token_list = zip_value
    return replace_entities(sentence, ner_token_list)


async def chunk_multiple_entities(data: zip) -> List[str]:
    return await asyncio.gather(*list(map(chunk_entities, data)))
