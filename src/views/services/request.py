import streamlit as st
from typing import Union
from controllers.cwn import handle_cwn_sense_tag
from controllers.ckip import handle_pos_tagging, handle_ner_chunker

TEN_MINUTES = 60 * 10


@st.cache(ttl=TEN_MINUTES, show_spinner=False)
def request(method: str, *args, **kwargs) -> Union[str, tuple]:
    """The fetch function fetch the data in the database based on the `method`."""

    methods = {
        "pos": handle_pos_tagging,
        "ner": handle_ner_chunker,
        "distil_tag": handle_cwn_sense_tag,
    }

    return methods[method](*args, **kwargs)
