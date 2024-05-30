import streamlit as st
import pandas as pd
from navigation import make_sidebar

def skip_bad_lines(bad_lines):

    return [], bad_lines

st.sidebar.success("Pilih Menu Diatas ini.")
make_sidebar()
#header
with st.container():
    st.title("Buku Besar")
    st.subheader("UMKM Soto Mie Bogor - Periode April 2024")
    st.write("---")
    df = pd.read_csv("dataset/bukbes1.csv")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    st.subheader ("1. Akun Kas")
    st.dataframe(df, width= 10000, height= 870)    
    st.write("---")
    
    df = pd.read_csv("dataset/bukbes2.csv")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    st.subheader ("2. Akun Modal Awal")
    st.dataframe(df, width= 10000, height= 50)    
    st.write("---")
    
    df = pd.read_csv("dataset/bukbes3.csv")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    st.subheader ("3. Akun Pembelian Bahan Baku")
    st.dataframe(df, width= 10000, height= 350)    
    st.write("---")
    
    df = pd.read_csv("dataset/bukbes4.csv")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    st.subheader ("4. Akun Penjualan")
    st.dataframe(df, width= 10000, height= 350)    
    st.write("---")
    
    df = pd.read_csv("dataset/bukbes5.csv")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    st.subheader ("5. Akun Beban Listrik")
    st.dataframe(df, width= 10000, height= 100)    
    st.write("---")
    
    df = pd.read_csv("dataset/bukbes6.csv")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    st.subheader ("6. Akun Beban Air")
    st.dataframe(df, width= 10000, height= 50)    
    st.write("---")
    
    df = pd.read_csv("dataset/bukbes7.csv")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    st.subheader ("7. Akun Beban Sewa")
    st.dataframe(df, width= 10000, height= 50)    
    st.write("---")
    
    df = pd.read_csv("dataset/bukbes8.csv")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    st.subheader ("8. Akun Beban Gaji")
    st.dataframe(df, width= 10000, height= 50)    
    st.write("---")

    
