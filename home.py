import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.stylable_container import stylable_container
###########################################################################################################

st.set_page_config(
     page_title = '1 & DOA SMS Dashboard',
     page_icon = 'barchart',
     layout = 'wide'#,
     #initial_sidebar_state = 'collapsed'
)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

st.title("1 & DOA SMS Dashboard")
container_style = """
{
    background-color: rgb(0,0,66);
    border-left : 10px solid rgb(0, 0, 66);
    border-radius : 10px;
}
  
}
"""
###########################################################################################################
col1, col2, col3 = st.columns([1,2,1])

with col1:
    st.subheader('Objectives')
    with stylable_container(key = 'metric_container',
                            css_styles = container_style, ) :
        objectives = st.container()
    col11, col12 = objectives.columns(2)
    with col11 :
        st.write('Accomplished')
        st.markdown(st.session_state.obj_acc, unsafe_allow_html= True)
    with col12 :
        st.write('Filled')
        st.markdown(st.session_state.obj_fil, unsafe_allow_html= True)
    objectives.page_link("pages/objectives_metriques.py", label = 'Details', icon='🔎', use_container_width=True)
    st.subheader('SQE Nomination')
    st.subheader('CASID')
    st.subheader('Budget')
with col2 :
    st.subheader('Risk Management on Systemic Safety Topics')
    with stylable_container(key = 'metric_container2',
                            css_styles = container_style, )
        col21, col22 = st.columns(2)
    with col21 : 
        st.write('Assessement on time')
        st.markdown(f'<p style="font-family:Arial; color:Red; font-size: 30px;">44 %</p>', unsafe_allow_html=True)
        st.write('Acknowledgement on time')
        st.markdown(f'<p style="font-family:Arial; color:Green; font-size: 30px;">89 %</p>', unsafe_allow_html=True)

    with col22 : 
        st.write('Number of open SMS cases')
        st.markdown('<p style = "font-family:Arial; font-size: 40px;">34</p>', unsafe_allow_html= True)
    st.write('Sources of SMS cases')
with col3 :
    st.subheader('Assurance')
    st.subheader('Promotion')