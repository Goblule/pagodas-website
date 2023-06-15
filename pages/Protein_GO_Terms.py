import streamlit as st
import requests
import shutil
import configuration
from stmol import showmol
import py3Dmol
import biotite.structure.io as bsio
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

go_id='3A1904659'

def update_table():
    st.subheader('Predicted GO Terms')

    apps = [ 'https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{ids}/chart?ids=GO%'+go_id,
            'https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{ids}/chart?ids=GO%'+go_id,
            'https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{ids}/chart?ids=GO%'+go_id,
            'https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{ids}/chart?ids=GO%'+go_id
    ]

    dicto = {'Name' : ['<name>','<name>','<name>','<name>'],
            'Weighted Probability' : ['<weighted_probability>','<weighted_probability>','<weighted_probability>','<weighted_probability>'],
            'Graph' : apps,}

    data_df = pd.DataFrame(dicto,index=[f'GO:{go_id}',f'GO:{go_id}',f'GO:{go_id}',f'GO:{go_id}'])

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
