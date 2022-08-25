import asyncio
from typing import List


async def add_pos_textsubscript(data_list: List[str]) -> str:
    create = (
        lambda value: f"<span>{value[0]}<sub style='margin-right: 0.1rem'>{value[1]}</sub></span>"
    )
    return "".join(list(map(create, data_list)))


async def add_ws_textsubscript(data_list: List[str]) -> str:
    create = lambda value: f"<span style='margin-right: 1rem'>{value}</span>"
    return "".join(list(map(create, data_list)))


async def add_multiple_textsubscripts(
    target: str, list_of_lists: List[List[str]]
) -> List[str]:

    textsubscript_factories = {
        "ws": add_ws_textsubscript,
        "pos": add_pos_textsubscript,
    }

    return await asyncio.gather(
        *list(map(textsubscript_factories[target], list_of_lists))
    )
