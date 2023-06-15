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

st.markdown('''# 🏯 Pagodas''')
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
    switch_page("Protein_Structure")
