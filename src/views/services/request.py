import streamlit as st
from typing import Union
from controllers.ckip import (
    handle_pos_tagging,
    handle_ner_chunker,
    handle_word_segmentation,
)
from controllers.cwn import handle_cwn_sense_tag

TEN_MINUTES = 60 * 10


@st.cache(ttl=TEN_MINUTES, show_spinner=True)
def request(method: str, *args, **kwargs):
    """The fetch function fetch the data in the database based on the `method`."""

    methods = {
        "ws": handle_word_segmentation,
        "pos": handle_pos_tagging,
        "ner": handle_ner_chunker,
        "cwn": handle_cwn_sense_tag,
    }

    return methods[method](*args, **kwargs)
