import asyncio
import pandas as pd
import streamlit as st
from .base import Block
from typing import List
from dataclasses import dataclass


@dataclass
class CWNSenseTagBlock(Block):
    """
    The CWNSenseTagBlock object visualizes the cwn sense tags.
    """

    title: str
    sentence_list: List[str]
    cwn_tags: List[List[List[tuple]]]

    async def create_data_frame(self, data: List[tuple]):
        return list(map(lambda value: pd.DataFrame(value), data))

    async def create_multiple_df(self, cwn_tags: List[List[List[tuple]]]):
        return await asyncio.gather(*list(map(self.create_data_frame, cwn_tags)))

    def visualize(self) -> None:
        st.subheader(self.title)
        data_frames = asyncio.run(self.create_multiple_df(self.cwn_tags))
        table_result = zip(self.sentence_list, data_frames)

        for sentence, tables in table_result:
            with st.expander(sentence, expanded=True):
                for table in tables:
                    st.table(table)
