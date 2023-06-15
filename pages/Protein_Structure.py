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

button_go_terms = st.button(':green[Check out functionalities]')

if button_go_terms:
    switch_page("Protein_Functionalities")
