import streamlit as st
import pandas as pd
import numpy as np

from navigation import make_sidebar

# Set the page configuration
st.set_page_config(page_title="UMKM Soto Mie Bogor - Transaksi", page_icon=":chart_with_upwards_trend:")

def skip_bad_lines(bad_lines):
    return [], bad_lines

# Create the sidebar
st.sidebar.success("Pilih Menu Diatas ini.")
make_sidebar()

# Header
with st.container():
    st.title("Transaksi")
    st.subheader("UMKM Soto Mie Bogor - Periode April 2024")
    st.write("---")
    
    # Debug: Check if file path is correct and file is readable
    try:
        df = pd.read_csv("dataset/Transaksi.csv", error_bad_lines=False)
        st.write("File read successfully.")
    except FileNotFoundError:
        st.error("File not found. Please check the file path.")
        st.stop()
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")
        st.stop()
    
    # Process DataFrame
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.loc[:, ~df.columns.str.contains('^None')]
    
    # Debug: Display the DataFrame
    st.write("Original DataFrame:")
    st.dataframe(df)
    
    # Display the editable table
    try:
        edited_df = st.data_editor(
            df,
            num_rows="dynamic",
            column_config={  # Format columns as needed
                "price": st.column_config.NumberColumn(format="$%.2f"),
            },
            key="transactions_table"
        )
    except Exception as e:
        st.error(f"An error occurred while displaying the editable table: {e}")
        st.stop()
    
    # Check for uncommitted changes
    has_uncommitted_changes = any(len(v) for v in st.session_state.transactions_table.values())
    
    # Debug: Display state of changes
    st.write("Session state changes:")
    st.json(st.session_state.transactions_table)
    
    # Button to save changes
    if st.button("Save Changes", type="primary", disabled=not has_uncommitted_changes):
        try:
            edited_df.to_csv("dataset/Transaksi.csv", index=False)
            st.success("Changes saved to dataset/Transaksi.csv")
        except Exception as e:
            st.error(f"An error occurred while saving the file: {e}")
    
    st.write("---")
