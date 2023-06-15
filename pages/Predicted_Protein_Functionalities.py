import streamlit as st
import requests
import shutil
import configuration
from stmol import showmol
import py3Dmol
import biotite.structure.io as bsio
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

def update_table():

    st.subheader('Predicted GO Terms')

    data_df = pd.read_csv('go_terms.csv')

    st.data_editor(
        data_df,
        column_config={
            'Graph': st.column_config.ImageColumn(
                "Graph Preview Image", help="Streamlit app preview screenshots"
            )
        },
        hide_index=False,
        width=800
    )

update_table()
