import streamlit as st
from pathlib import Path
from typing import Callable


def load_package(pkg_path: Path, pkg_name: str, dowload: Callable) -> None:
    """The load_package function loads the package.

    Args:
        pkg_path (Path): the package path
        pkg_name (str): the package name
        download (Callable): the download function
    """

    while not Path(pkg_path).exists():
        with st.spinner(f"Downloading {pkg_name} models ..."):
            dowload()
