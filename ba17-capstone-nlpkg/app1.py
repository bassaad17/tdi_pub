import streamlit as st
from PIL import Image



def app():

    st.title('Page-1 | Introduction')
    # st.write('Welcome to Page-1 Intro')
    st.markdown('---')
    
    st.markdown('### Objective')
    st.markdown('''
    The purpose of this capstone Data Science project is to showcase the ability of combining Machine Learning algorithms
    such as **Natural Language Processing (NLP)** with **Knowledge Graphs (KG)** to obtain better topic extraction, identification,
    and visual relations when conducting queries of published media content in written form.
    The aim of the application is to allow teams working in Strategy, Marketing, and Content Media managers to be able
    to swiftly understand what vast amounts of published text is referring to in order to enhance the decision-making process within your industry.
    ''')

    image_biden = Image.open('./images/biden_nlpkg_infra.png')
    st.image(image_biden, caption='Using NLP and KG to extract relationships from text media published regarding Biden\'s Infrastructure Plan')

    st.markdown('### Deliverables')
    st.markdown('''
    The work perfomed in this analysis consisted of four stages:

    1. Data Ingestion and Text Preprocessing
    2. Train Model using NLP libraries such as Gensim, NLTK, and spaCy
    3. Topic Modeling (see PG2 and PG3)
    4. Visualization Displays such as Word Frequency, and Knowledge Graphs using NetworkX (see PG4)
    ''')

    st.markdown('#### - Data Ingestion')
    st.markdown('''
    The data used in the creation of this application was scrapped from the web with news articles related the mid 2019 political
    landscape in the U.S. and interntionally. The scrapped data was saved as a CSV file and further processed and cleaned in
    preparation for the subsequent algorithms applied.
    ''')

    st.markdown('#### - Model Training')
    st.markdown('''
    In order to train the model, unstructured data obtained from various news articles were converted into structured data by utilizing
    processeses such as Tokenization, Lemmatization and Stemming of words contained in the set. Named entity recognition and subject-verb-object
    (SVO) triples relationship were established to have the ability to map the data.
    ''')

    st.markdown('#### - Topic Modeling')
    st.markdown('''
    Topic modeling is a technique in extracting hidden topics from large volumes of text. Latent Dirichlet Allocation (LDA) was
    used as an algorithmic tool in this project due to its excellent implementation with Python's Gensim package.
    Page 2 and 3 of this web application allows you to view the results of the NLP model. Page 2 classifies any of the documents used
    to train the model on. User is also able to supply 'unseen' text where the model attempts to classify it based on what it was previously
    trained on.
    ''')

    st.markdown('#### - Knowledge Graphs')
    st.markdown('''
    A knowledge graph, also known as a semantic network, represents real word entities and illustrates the relationship betwen them.
    This information is stored in a graph database and visualized as a structure made up of nodes, edges and labels. Page 4 allows you to
    identify the subject, object, and verb relationships extracted from the corpus of published media used in this application.
    ''')

    image_model = Image.open('./images/machine_modeling.png')
    st.image(image_model, caption='Overall Machine Learning Approach Taken to Process Text Media')

   