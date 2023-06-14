import streamlit as st
import requests

from stmol import showmol
import py3Dmol
import biotite.structure.io as bsio


# Page configuration
st.set_page_config(
    page_title="🏯 Pagodas", # => Quick reference - Streamlit
    page_icon="🏯",
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed





######################## LAYOUT ##########################


st.markdown('''
# Pagodas
''')


st.markdown('''
## Protein Annotation by Gene Ontology through Deep learning Automated System
''')


# st.sidebar.title('Pagodas')
st.write('[*ESMFold*](https://esmatlas.com/about) is an end-to-end single sequence protein structure predictor based on the ESM-2 language model. For more information, read the [research article](https://www.biorxiv.org/content/10.1101/2022.07.20.500902v2) and the [news article](https://www.nature.com/articles/d41586-022-03539-1) published in *Nature*.')



# stmol
def render_mol(pdb):
    pdbview = py3Dmol.view()
    pdbview.addModel(pdb,'pdb')
    pdbview.setStyle({'cartoon':{'color':'spectrum'}})
    pdbview.setBackgroundColor('white')#('0xeeeeee')
    pdbview.zoomTo()
    pdbview.zoom(2, 800)
    pdbview.spin(True)
    showmol(pdbview, height = 500,width=800)

# Protein sequence input
# default seq Apical meristem formation protein-related
st.info('🧬 Enter your protein sequence 🧬')

DEFAULT_SEQ = "MEDDDAAYDLIKHELLYSEDEVIISRYLKGMVVNGDSWPDHFIEDANVFTKNPDKVFNSERPRFVIVKPRTEACGKTDGCDSGCWRIIGRDKLIKSEETGKILGFKKILKFCLKRKPIDYKRSWVMEEYRLTNNLNWKQDHVICKIRFMFEAEISFLLSKHFYTTSESVLENELLPSYGYYLSNTQEEDEFYLDAIMTSEGNEWPSYVTNNVYCLHPLELVDLQDRMFNDYGTCIFANKTCGETDKCDGGYWKILHGDKLIKSNFGKVIGFKKVFEFYETVRQIYLCDGEEVTVTWTIQEYRLSKNVKQNKVLCVIKLTYDR"
txt = st.text_area('Input sequence', DEFAULT_SEQ, height=275)

# ESMfold
def update(sequence=txt):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence)

    pdb_string = response.content.decode('utf-8')

    with open('predicted.pdb', 'w') as f:
        f.write(pdb_string)


    # Display protein structure
    st.subheader('Visualization of predicted protein structure')
    render_mol(pdb_string)



predict = st.button('Predict', on_click=update)


# if not predict:
#     st.warning('🧬 Enter your protein sequence 🧬')
