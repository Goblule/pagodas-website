import streamlit as st
import requests
import shutil
import configuration
from stmol import showmol
import py3Dmol
import biotite.structure.io as bsio
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

txt = open("seq.txt", "r").read()

# stmol
def render_mol(pdb):
    pdbview = py3Dmol.view()
    pdbview.addModel(pdb,'pdb')
    pdbview.setStyle({'cartoon':{'color':'spectrum'}})
    pdbview.setBackgroundColor('white')#('0xeeeeee')
    pdbview.zoomTo()
    pdbview.zoom(1.5, 800)
    pdbview.spin(True)
    showmol(pdbview, height = 600,width=800)


# ESMfold
def update_pdb(sequence=txt):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence)

    pdb_string = response.content.decode('utf-8')

    with open('predicted.pdb', 'w') as f:
        f.write(pdb_string)

    # Display protein structure
    st.subheader('Visualization of Predicted Protein Structure')
    render_mol(pdb_string)

update_pdb(txt)

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


button_go_terms = st.button(':green[Check out functionalities]')

if button_go_terms:
    switch_page("Protein_Functionalities")
