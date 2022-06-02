import streamlit as st

import numpy as np
import pandas as pd
import pickle

import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from gensim import corpora, models
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
np.random.seed(1234) # set seed number to avoid random variation between consecutive runs
import nltk


# local paths to data, images, models, etc.
# localpath = 'C:\\coding\\python\\tdi_dsf\\cpstn\\strmlit\\v03\\'
q_df_5K_content_selection_csv = './data/df_q_5K_content_selection.csv'
lda_tfidf_model_pkl = './models/lda_tfidf_model.pkl'
preprocessed_docs_pkl = './models/preprocessed_docs.pkl'


# preprocess selected signal content data using nltk
stemmer = SnowballStemmer('english')

def lemmatize_stemming(text):
    # lemmatize and stem a text
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        # remove stopword tokens and tokens of length smaller than 3
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 2:
            # lemmatize and stem tokens
            result.append(lemmatize_stemming(token))
    return result

def app():

    st.title('Page-2 | Topic Modeling')
    # st.write('Welcome to Page-2 TM')
    st.markdown('---')
    
    st.write('**Sample Published Content**')

    # load dataframe df_5K_cont_sel from binary pickle file saved in data directory
    columns = ['signal num', 'content', 'regioncountry', 'audiences', 'title', 'sentiment', 'image', 'topics',
               'aisummary', 'likes', 'sitename', 'url', 'authorname', '@version', '@timestamp', 'id', 'language',
               'comments', 'type', 'publisheddate', 'organization', 'reposts', 'eocs', 'retrieveddate', 'verticals',
               'dislikes', 'content_str_len', 'content_raw_words_count', 'publisheddate_notz']

    # load csv data into dataframe object
    # df_5K_cont_sel = pd.read_csv(localpath + q_df_5K_content_selection_csv, usecols=columns,
    #                              encoding='UTF-8', low_memory=False)

    df_5K_cont_sel = pd.read_csv(q_df_5K_content_selection_csv, usecols=columns,
                                 encoding='UTF-8', low_memory=False)

    # select content column from dataframe
    content = df_5K_cont_sel['content']

    # allow user to select signal number
    number = st.number_input(
        "Enter sample signal number [1 - 4,985]:", 1, 4985, 1, 1)
    sample = content[df_5K_cont_sel.index[number-1]]

    # allow user to display up to 750 characters of signal selected from above
    st.write(
        'Displaying below first 750 characters of text from above selected signal number')
    st.write('\n')
    if len(sample) > 750:
        st.write(str(sample[:750]) + ' [...remaining text not displayed]')
    else:
        st.write(str(sample))
    st.write('\n')

    # load the preprocessed_docs model pickle object
    # preprocessed_docs = pickle.load(open(localpath + preprocessed_docs_pkl, "rb"))
    preprocessed_docs = pickle.load(open(preprocessed_docs_pkl, "rb"))
    
    dictionary = gensim.corpora.Dictionary(preprocessed_docs)
    dictionary.filter_extremes(no_below=10, no_above=0.5, keep_n=100000)
    
    
    st.subheader('LDA TF-IDF | TM Output for Sample Text:')

    if st.button('Run TM on Sample Text'):

        # create dictionary and bag of words for sample text
        txt = dictionary.doc2bow(preprocess(sample))
        
        # load the lda tfidf model pickle object
        # lda_tfidf_model = pickle.load(open(localpath + lda_tfidf_model_pkl, "rb"))
        lda_tfidf_model = pickle.load(open(lda_tfidf_model_pkl, "rb"))
        
        st.write('---')
        # Classify sample document using LDA TF-IDF model
        for index, score in sorted(lda_tfidf_model[txt], reverse=True):
            score_string = '- Score: {}'.format(score)
            topic_string = '- Topic: {}'.format(
                lda_tfidf_model.print_topic(index, 7))
            st.write(score_string)
            st.write(topic_string)
            st.write('---')
            # end of TM sample text
    
    st.markdown('---')

    st.write('**Unseen Content**')
    
    unseen_document = st.text_area(
        'Type an unseen text by NLP model:', placeholder='Enter text here', height=80)

    st.subheader('LDA TF-IDF | TM Output for Unseen Text:')

    if st.button('Run TM on Unseen Text'):

        # create dictionary and bag of words for unseen text
        bow_vector = dictionary.doc2bow(preprocess(unseen_document))

        # load the lda tfidf model pickle object
        # lda_tfidf_model = pickle.load(open(localpath + lda_tfidf_model_pkl, "rb"))
        lda_tfidf_model = pickle.load(open(lda_tfidf_model_pkl, "rb"))

        st.write('---')
        # Classify sample document using LDA TF-IDF model
        for index, score in sorted(lda_tfidf_model[bow_vector], key=lambda tup: tup[1], reverse=True):
            score_string = '- Score: {}'.format(score)
            topic_string = '- Topic: {}'.format(
                lda_tfidf_model.print_topic(index, 7))
            st.write(score_string)
            st.write(topic_string)
            st.write('---')
            # end of TM unseen text``