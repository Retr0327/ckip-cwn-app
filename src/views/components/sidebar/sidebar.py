import streamlit as st
from ..form import form_controller
from .options import MODEL_OPTIONS, CKIP_VISUALIZERS, CWN_VISUALIZERS


def remove_input_data():
    if "input_data" in st.session_state:
        del st.session_state["input_data"]


def visualize_side_bar():
    with st.sidebar:
        st.image(
            "https://avatars.githubusercontent.com/u/21136511?s=200&v=4", width=100
        )

        model_options = form_controller(
            control="select-box",
            title="NLP 模型",
            options=MODEL_OPTIONS,
            on_change=remove_input_data,
        )

        visualizers = CKIP_VISUALIZERS if model_options == "CKIP" else CWN_VISUALIZERS

        active_visualizers = form_controller(
            control="multi-select", title="Visualizers", options=visualizers
        )
        
        return active_visualizers
