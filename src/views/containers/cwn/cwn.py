from typing import List
from ...services import request
from .block import DistilTagBlock, CWNSenseTagBlock


def create_block(visualizer, sentence_list):
    distil_tags, cwn_tags = request("distil_tag", sentence_list)

    visualizer_factories = {
        "DistilTag": DistilTagBlock(visualizer, distil_tags).visualize,
        "CwnSenseTag": CWNSenseTagBlock(visualizer, sentence_list, cwn_tags).visualize,
    }

    return visualizer_factories[visualizer]()


def display_cwn(visualizers: str, sentence_list: List[str]):
    for visualizer in visualizers:
        create_block(visualizer, sentence_list)
