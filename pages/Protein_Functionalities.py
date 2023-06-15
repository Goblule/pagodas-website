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

txt = open("seq.txt", "r").read()
url='https://pagodas-74s6w3h4cq-od.a.run.app/predict?protein_sequence='+txt
response = requests.get(url)
dicto = response.json()

df = pd.DataFrame(dicto).T
df['weighted_probability'] = df['weighted_probability'].map(lambda x : round(x,2))
df = df.drop(columns=['probability']).rename(columns={'function_name' : 'Function Name','weighted_probability' : 'Weighted Probability'})
df['Function Name'] = df['Function Name'].map(lambda x :x.capitalize())

base_url = 'https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{ids}/chart?ids=GO%3A'
apps = [base_url + go_id[3:] for go_id in list(df.index)]

df['Graph'] = apps

data_df = df[df['Weighted Probability'] > 0.05].sample(10)
# data_df.to_csv('go_terms.csv',index=False)

def update_table():

    st.subheader('✅ Predicted Protein Functionalities')

    #data_df = pd.read_csv('go_terms.csv')

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
