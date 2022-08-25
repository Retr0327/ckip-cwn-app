import asyncio
import streamlit as st
from pathlib import Path
from configs import ckip_path, download_ckip_drivers


initial_drivers = [
    ckip_path / "albert-base_drivers.pickle",
    ckip_path / "albert-tiny_drivers.pickle",
    ckip_path / "bert-base_drivers.pickle",
    ckip_path / "bert-tiny_drivers.pickle",
]


def dowload_ckip_package():
    while not all(list(map(lambda path: Path(path).exists(), initial_drivers))):
        with st.spinner("Downloading CKIP models ..."):
            asyncio.run(download_ckip_drivers())
            
        if all(list(map(lambda path: Path(path).exists(), initial_drivers))):
            break
