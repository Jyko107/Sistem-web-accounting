import streamlit as st
import pandas as pd
import numpy as np


def skip_bad_lines(bad_lines):

    return [], bad_lines

st.set_page_config(page_title="Transaksi", page_icon=":bar_chart:", layout="wide")

st.sidebar.success("Pilih Menu Diatas ini.")

#header
with st.container():
    st.title("Transaksi")
    st.subheader("UMKM Soto Mie Bogor - Periode April 2024")
    st.write("---")
    df = pd.read_csv("dataset/Transaksi.csv")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.loc[:, ~df.columns.str.contains('^None')]
    st.dataframe(df, width=10000, height=5000)
    st.write("---")
