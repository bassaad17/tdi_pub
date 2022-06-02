# main app.py

import streamlit as st
import app1  # intro
import app2  # topic modeling
import app3  # lda tfidf viz/display
import app4  # knowledge graphs

PAGES = {
    "PG1 | Intro": app1,
    "PG2 | Topic Modeling": app2,
    "PG3 | LDA Visualization": app3,
    "PG4 | Knowledge Graphs": app4,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to...", list(PAGES.keys()))
page = PAGES[selection]
page.app()

st.sidebar.markdown('''##### Tools used in this project:''')
st.sidebar.markdown('''
    - [Gensim](https://radimrehurek.com/gensim/)
    - [NLTK](https://www.nltk.org/)
    - [spaCy](https://spacy.io/)
    - [NetworkX](https://networkx.org/)
    - [Streamlit](https://streamlit.io/)
    - [GitHub [Under Construction]](https://github.com/bassaad17/tdi_pub)''')


st.sidebar.markdown('''
    ##### ---
    ##### Developed by:
    ##### Bilal Assaad
    ##### ---
    ##### The Data Incubator 
    ##### Data Science Fellowship
    ##### Capstone Showcase Project
    ##### Winter Cohort '22
    ##### April 24, 2022
    ##### Ver 0.0.3
    #### ---''')