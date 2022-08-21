import streamlit as st
from typing import Optional


def add_text_area(
    title: str,
    placeholder: Optional[str] = "",
    height: Optional[int] = None,
    key: Optional[str] = None,
):
    return st.text_area(title, placeholder=placeholder, height=height, key=key)
