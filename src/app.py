from views import (
    display_cwn,
    display_ckip,
    create_data_form,
    visualize_side_bar,
    dowload_ckip_package,
)
import streamlit as st


def run_app() -> None:
    dowload_ckip_package()

    st.title("LOPE")
    input_data = create_data_form()
    model, pipeline, active_visualizers = visualize_side_bar()
    display_factories = {"CKIP": display_ckip, "CWN": display_cwn}

    if "input_data" in st.session_state:
        display_factories[pipeline](
            model, active_visualizers, st.session_state["input_data"]
        )


if __name__ == "__main__":
    run_app()
