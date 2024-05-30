import streamlit as st
import pandas as pd
from navigation import make_sidebar

def skip_bad_lines(bad_lines):

    return [], bad_lines


st.sidebar.success("Pilih Menu Diatas ini.")
make_sidebar()
#header
with st.container():
    st.title("Laporan Keuangan")
    st.subheader("UMKM Soto Mie Bogor - Periode April 2024")
    st.write("---")
    df = pd.read_csv("dataset/lapkeu3.csv")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    st.subheader ("Laporan Laba Rugi")
    st.dataframe(df, width= 10000, height= 350)    
    st.write("---")
    
    df = pd.read_csv("dataset/lapkeu2.csv")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    st.subheader ("Laporan Perubahan Modal")
    st.dataframe(df, width= 10000, height= 170)    
    st.write("---")
   
    df = pd.read_csv("dataset/lapkeu1.csv")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    st.subheader ("Laporan Posisi Keuangan")
    st.dataframe(df, width= 10000, height= 140)    
    st.write("---")
