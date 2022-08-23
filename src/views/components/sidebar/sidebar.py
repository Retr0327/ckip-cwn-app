from typing import Dict
from ..form import form_controller
from streamlit import sidebar, image, session_state
from .options import MODEL_OPTIONS, CKIP_VISUALIZERS, CWN_VISUALIZERS


def remove_input_data():
    if "input_data" in session_state:
        del session_state["input_data"]


def format_option(option: Dict[str, str]) -> str:
    """The format_options function gets the value of a dict."""
    return list(option.values())[0]


def visualize_side_bar():
    with sidebar:
        image("https://avatars.githubusercontent.com/u/21136511?s=200&v=4", width=100)

        model_options = form_controller(
            control="select-box",
            title="NLP 模型",
            options=MODEL_OPTIONS,
            on_change=remove_input_data,
        )

        visualizers = CKIP_VISUALIZERS if model_options == "CKIP" else CWN_VISUALIZERS

        active_visualizers = form_controller(
            control="multi-select",
            title="Visualizers",
            options=visualizers,
            format_func=format_option,
        )

        return model_options, active_visualizers
