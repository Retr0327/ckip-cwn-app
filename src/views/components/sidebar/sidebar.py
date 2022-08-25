import streamlit as st
from typing import Dict, Union
from ..form import form_controller
from configs import download_ckip_drivers
from .options import MODEL_OPTIONS, PIPELINE_OPTIONS, CKIP_VISUALIZERS, CWN_VISUALIZERS


def remove_input_data():
    if "input_data" in st.session_state:
        del st.session_state["input_data"]


def format_option(option: Union[str, Dict[str, str]]) -> str:
    """The format_options function formats each option in a list of options.
    If `option` is a dict, the function will extract the value from the dict.

    Args:
        option (str or dict)
    Returns:
        a str
    """

    if isinstance(option, dict):
        return list(option.values())[0]

    return option


def visualize_side_bar():
    with st.sidebar:
        st.image(
            "https://avatars.githubusercontent.com/u/21136511?s=200&v=4", width=100
        )

        pipeline_options = form_controller(
            control="select-box",
            title="中文 NLP 管線處理：",
            options=PIPELINE_OPTIONS,
            on_change=remove_input_data,
        )

        model_options = None
        if pipeline_options == "CKIP":
            model_options = form_controller(
                control="select-box",
                title="NLP 模型：",
                options=MODEL_OPTIONS,
                key="model",
            )

        visualizers = (
            CKIP_VISUALIZERS if pipeline_options == "CKIP" else CWN_VISUALIZERS
        )

        active_visualizers = form_controller(
            control="multi-select",
            title="功能：",
            options=visualizers,
            format_func=format_option,
        )

        return model_options, pipeline_options, active_visualizers
