import streamlit as st
import pandas as pd
import numpy as np

###########################################################################################################
st.title("1 & DOA SMS Dashboard")

###########################################################################################################
col1, col2, col3 = st.columns([1,2,1])

with col1: 
    st.subheader('Objectives')
    col11, col12 = st.columns(2)
    with col11 :
        st.write('Objective %')
        st.session_state.obj_acc
    with col12 :
        st.write('Filled %')
        st.session_state.obj_fil
    st.subheader('SQE Nomination')
    st.subheader('CASID')
    st.subheader('Budget')
with col2 :
    st.subheader('Risk Management on Systemic Safety Topics')
    col21, col22 = st.columns(2)

    with col21 : 
        st.write('Assessement on time')
        st.markdown(f'<p style="font-family:Arial; color:Red; font-size: 30px;">44 %</p>', unsafe_allow_html=True)
        st.write('Acknowledgement on time')
        st.markdown(f'<p style="font-family:Arial; color:Green; font-size: 30px;">89 %</p>', unsafe_allow_html=True)

    with col22 : 
        st.write('Number of open SMS cases')
        st.markdown('<p style = "font-family:Arial; font-size: 40px;">34</p>', unsafe_allow_html= True)
        st.write('Number of closed SMS cases')
        st.markdown('<p style = "font-family:Arial; font-size: 40px;">1</p>', unsafe_allow_html= True)