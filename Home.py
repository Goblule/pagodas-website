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

configuration.page_set_up()

######################## LAYOUT ##########################

st.markdown('''# Pagodas''')
st.markdown('''## Protein Annotation _by_ Gene Ontology _through_ Deep _learning_ Automated System''')

# Protein sequence input
# default seq Apical meristem formation protein-related
st.info('🧬 Enter your protein sequence 🧬')

DEFAULT_SEQ = "MTMDKSELVQKAKLAEQAERYDDMAAAMKAVTEQGHELSNEERNLLSVAYKNVVGARRSSWRVISSIEQKTERNEKKQQMGKEYREKIEAELQDICNDVLELLDKYLILNATQAESKVFYLKMKGDYFRYLSEVASGENKQTTVSNSQQAYQEAFEISKKEMQPTHPIRLGLALNFSVFYYEILNSPEKACSLAKTAFDEAIAELDTLNEESYKDSTLIMQLLRDNLTLWTSENQGDEGDAGEGEN"
txt = st.text_area('Input sequence', DEFAULT_SEQ, height=275)

button_predict = st.button(':violet[Predict]')

if button_predict:
    with open('seq.txt', 'w') as f:
        f.write(txt)

    #txt = open("seq.txt", "r").read()

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
    data_df.to_csv('go_terms.csv',index=False)

    switch_page("Protein_Structure")
