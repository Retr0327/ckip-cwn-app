from typing import List
from ...services import request
from streamlit import expander, markdown

divider_tag = "<hr style='margin-top: 1rem;margin-bottom: 1rem;border: 0;border-top: 1px solid rgba(0,0,0,.1);'/>"


def create_data_card(visualizer: str, sentence_list: List[str]):
    fetch_method = list(visualizer.keys())[0]
    title = visualizer[fetch_method]
    html_tags = request(fetch_method, sentence_list)
    html_string = divider_tag.join(html_tags)

    with expander(title, expanded=True):
        markdown(html_string, unsafe_allow_html=True)
