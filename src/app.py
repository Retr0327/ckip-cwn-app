import streamlit as st
from pathlib import Path
from configs import download_ckip_drivers, ckip_path
from views import create_data_form, visualize_side_bar, create_data_card


def run_app() -> None:
    while not Path(ckip_path).exists():
        with st.spinner("Downloading ckip models ..."):
            download_ckip_drivers()

    st.title("LOPE")
    input_data = create_data_form()
    active_visualizers = visualize_side_bar()

    if "input_data" in st.session_state and input_data:
        for visualizer in active_visualizers:
            create_data_card(visualizer, st.session_state["input_data"])


if __name__ == "__main__":
    run_app()
