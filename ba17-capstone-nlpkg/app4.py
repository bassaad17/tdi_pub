import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# local paths to data, images, models, etc.
# localpath = 'C:\\coding\\python\\tdi_dsf\\cpstn\\strmlit\\v03\\'
relations_df_csv = './models/relations_df.csv'
kg_df_5K_csv = './models/kg_df_5K.csv'

# load model csv data into dataframe object
# relations_df = pd.read_csv(localpath + relations_df_csv)
# kg_df_5K = pd.read_csv(localpath + kg_df_5K_csv)
relations_df = pd.read_csv(relations_df_csv)
kg_df_5K = pd.read_csv(kg_df_5K_csv)

def plot_knowgraph(graph):
    fig = plt.figure(figsize=(7,7))
    pos = nx.spring_layout(graph, k=0.5)  # k regulates the distance between nodes
    nx.draw(graph, with_labels=True, node_color='skyblue', node_size=800, edge_cmap=plt.cm.Blues, pos=pos)
    st.pyplot(fig)

def app():

    st.title('Page-4 | Knowledge Graphs')
    # st.write('Welcome to Page-4 KG')
    st.markdown('---')

    st.markdown('''
    Given a source (i.e. subject) and its relation (i.e. verb/edge) with an user specified depth, a KG figure is constructed below that visualizes
    the multilevel nature of relationships words form based on the written content used in this model.
    ''')

    st.markdown('---')

    col1, col2, col3 = st.columns(3)

    with col1:

        values = st.slider('Select a range of subject values', 1, 100, (1, 20))
        col1_min = values[0]
        col1_max = values[1]

        st.header(f'Top {col1_min} - {col1_max} Subjects\n(Source)')

        # plot of top subject frequencies
        fig, myaxis = plt.subplots()
        kg_df_5K.source.value_counts()[col1_min-1:col1_max].sort_values().plot.barh(ax=myaxis, figsize=(4,6), grid=True)
        st.pyplot(fig)

    with col2:

        values = st.slider('Select a range of object values', 1, 100, (1, 20))
        col2_min = values[0]
        col2_max = values[1]

        st.header(f'Top {col2_min} - {col2_max} Objects\n(Targets)')

        # plot of top object/target frequencies
        fig, myaxis = plt.subplots()
        kg_df_5K.target.value_counts()[col2_min-1:col2_max].sort_values().plot.barh(ax=myaxis, figsize=(4,6), grid=True)
        st.pyplot(fig)

    with col3:

        values = st.slider('Select a range of verb values', 1, 300, (170, 190))
        col3_min = values[0]
        col3_max = values[1]

        st.header(f'Top {col3_min} - {col3_max} Verbs\n(Edge/Relations)')

        # plot of verb/edge/relation frequencies
        fig, myaxis = plt.subplots()
        kg_df_5K.edge.value_counts()[col3_min-1:col3_max].sort_values().plot.barh(ax=myaxis, figsize=(4,6), grid=True)
        st.pyplot(fig)


    col1, col2 = st.columns(2)
    
    # enter subject/source of interest for kg creation
    with col1:
        txt_subject = st.text_input('Enter subject/source text:', placeholder='[candidates]')

    # enter verb/edge/relations of interest for kg creation
    with col2:
        txt_verb = st.text_input('Enter verb/edge/relations text:', placeholder='meet')

    kg_depth_sel = st.select_slider('Select KG Depth:', options=['1', '2', '3', '4'])

    if st.button('Generate KGvis'):

        # create a directed graph from a kg_df_5K dataframe
        G = nx.from_pandas_edgelist(kg_df_5K, "source", "target", edge_attr=True, create_using=nx.MultiDiGraph())
        selected_nodes = [n for (n, v, e) in G.edges(data=True) if (e['edge'] in [txt_verb])]
        SG = G.subgraph(selected_nodes)

        nx_SG_depth = nx.dfs_tree(SG, source=txt_subject, depth_limit=int(kg_depth_sel))
        
        plot_knowgraph(nx_SG_depth)