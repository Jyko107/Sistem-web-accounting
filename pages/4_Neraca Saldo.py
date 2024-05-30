import streamlit as st
import pandas as pd
from navigation import make_sidebar

def skip_bad_lines(bad_lines):

    return [], bad_lines

st.sidebar.success("Pilih Menu Diatas ini.")
make_sidebar()
#header
with st.container():
    st.title("Laporan Posisi Keuangan")
    st.subheader("UMKM Soto Mie Bogor - Periode April 2024")
    st.write("---")
    df = pd.read_csv("dataset/nrcafx.csv")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    st.subheader ("Neraca Saldo")
    st.dataframe(df, width= 10000, height= 350)    
    st.write("---")
 
