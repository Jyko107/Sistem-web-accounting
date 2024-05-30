import streamlit as st
import pandas as pd
import numpy as np
from navigation import make_sidebar


def skip_bad_lines(bad_lines):

    return [], bad_lines

st.sidebar.success("Pilih Menu Diatas ini.")
make_sidebar()
#header
with st.container():
    st.title("Jurnal Umum")
    st.subheader("UMKM Soto Mie Bogor - Periode April 2024")
    st.write("---")
    df = pd.read_csv("dataset/awok2.csv")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.loc[:, ~df.columns.str.contains('^None')]
    st.dataframe(df, width=10000, height=1750)
    st.write("---")

