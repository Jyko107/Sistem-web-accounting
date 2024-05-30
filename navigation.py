import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages

st.set_page_config(page_title="Sistem Informasi Soto Mie Bogor", page_icon=":🍲:", layout="wide", initial_sidebar_state="expanded")


def get_current_page_name():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise RuntimeError("Couldn't get script context")

    pages = get_pages("")
    return pages[ctx.page_script_hash]["page_name"]



def make_sidebar():
    with st.sidebar:
        st.title("SITOMB")
        st.write("")
        st.write("")

        if st.session_state.get("logged_in", False):

            st.write("")
            st.write("")

            if st.button("Log out"):
                logout()

        elif get_current_page_name() != "Home":
            # If anyone tries to access a secret page without being logged in,
            # redirect them to the home page
            st.warning("You must be logged in to access this page.")
            st.experimental_rerun()  # Re-run to redirect


def logout():
    st.session_state.logged_in = False
    st.info("Logged out successfully!")
    sleep(0.5)
    st.experimental_rerun()  # Re-run to redirect to home


# Sample usage:
make_sidebar()

# Dummy content to demonstrate the sidebar
st.write("Welcome to the SITOMB application!")
if st.session_state.get("logged_in", False):
    st.write("You are logged in.")
else:
    st.write("Please log in to access more features.")

