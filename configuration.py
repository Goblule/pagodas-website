import streamlit as st
import requests
import shutil
from stmol import showmol
import py3Dmol
import biotite.structure.io as bsio
from streamlit_option_menu import option_menu


def home_app():
    st.title("Home")

def page_set_up():

    # Page configuration
    st.set_page_config(
        page_title="🏯 Pagodas", # => Quick reference - Streamlit
        page_icon="🏯",
        layout="centered", # wide
        initial_sidebar_state="auto") # collapsed


    apps =[{"func": home_app, "title": "Home", "icon": "house"}]

    # titles = [app["title"] for app in apps]
    # titles_lower = [title.lower() for title in titles]
    # icons = [app["icon"] for app in apps]


    params = st.experimental_get_query_params()

    if "page" in params:
        default_index = int(titles_lower.index(params["page"][0].lower()))
    else:
        default_index = 0

    with st.sidebar:
        # selected = option_menu(
        #     "Main Menu",
        #     options=titles,
        #     icons=icons,
        #     menu_icon="cast",
        #     default_index=default_index,
        # )

        st.sidebar.title("About")
        st.sidebar.info(
            """
            Source code: <https://github.com/Goblule/pagodas-website>

            This interface uses the following API:

            - [*ESMFold*](https://esmatlas.com/about). The ESMFold API is an end-to-end single sequence protein structure predictor based on the ESM-2 language model.
            - [*QuickGO API*](https://www.ebi.ac.uk/QuickGO/api/). The QuickGO REST API provides access to key biological data from QuickGO and GOA.
        """
        )
#            For more information, read the [research article](https://www.biorxiv.org/content/10.1101/2022.07.20.500902v2) and the [news article](https://www.nature.com/articles/d41586-022-03539-1) published in *Nature*.
