import streamlit as st
from pathlib import Path
from configs import download_cwn_models, cwn_model_path


def download_cwn_drivers(upgrade):
    cwn_drivers = [
        cwn_model_path / "cwn-graph-v.2022.08.01.pyobj",
        cwn_model_path / "manifest.json",
        cwn_model_path / "cwn-wsd-model",
        cwn_model_path / "tagmodel",
    ]

    while not all(list(map(lambda path: Path(path).exists(), cwn_drivers))):
        with st.spinner("Downloading CWN models ..."):
            download_cwn_models(upgrade)

        if all(list(map(lambda path: Path(path).exists(), cwn_drivers))):
            break


def run_app(ckip_nlp_models, cwn_upgrade) -> None:
    # need to download first because CWN packages will first check whether
    # there is .cwn_graph folder in the root directory.
    download_cwn_drivers(cwn_upgrade)

    from views import (
        display_cwn,
        display_ckip,
        create_data_form,
        visualize_side_bar,
        dowload_ckip_package,
    )

    dowload_ckip_package(ckip_nlp_models)

    st.title("LOPE")
    input_data = create_data_form()
    model, pipeline, active_visualizers = visualize_side_bar(ckip_nlp_models)
    display_factories = {"CKIP": display_ckip, "CWN": display_cwn}

    if "input_data" in st.session_state:
        display_factories[pipeline](
            model, active_visualizers, st.session_state["input_data"]
        )


if __name__ == "__main__":
    ckip_nlp_models = ["bert-base", "albert-tiny", "bert-tiny", "albert-base"]
    run_app(ckip_nlp_models, cwn_upgrade=False)
