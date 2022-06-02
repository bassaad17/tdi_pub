import streamlit as st
import streamlit.components.v1 as components

# local paths to data, images, models, etc.
# localpath = 'C:\\coding\\python\\tdi_dsf\\cpstn\\strmlit\\v03\\'
pyLDAvis_lda_tfidf_display_html = './models/pyLDAvis_lda_tfidf_display.html'

def app():

    st.title('Page-3 | LDA Visualization')
    # st.write('Welcome to Page-3 Viz of LDA TF-IDF Topic Modeling')
    st.markdown('---')

    st.markdown('''
    Once the visualization is generated, it displays the number of topics, in this case five (5), in which the LDA
    algorithm was programmed to be trained on. The left side of the plot displays the global topic views and their perceived
    relationships between each other (i.e. proximity). The bar charts on the right display the Top 30 most important
    words that make up a given topic.
    ''')

    st.markdown('---')

    if st.button('Generate pyLDAvis'):
        
        # HtmlFile = open(localpath + pyLDAvis_lda_tfidf_display_html, 'r', encoding='utf-8')
        HtmlFile = open(pyLDAvis_lda_tfidf_display_html, 'r', encoding='utf-8')
        source_code = HtmlFile.read()
        print(source_code)
        components.html(source_code, width=1200, height=800)
