import streamlit as st
import pandas as pd
import numpy as np

###########################################################################################################
st.set_page_config(
     page_title = 'ePPS display',
     page_icon = 'clipboard',
)
st.title('PPS mock up')
###########################################################################################################

pps_data = pd.read_csv(r'data/SMS FILTERED DATA ADDED COLUMNS (1).csv', dtype = 'string',keep_default_na=False)
st.subheader('Top 3 SMS cases')
st.write(pps_data.head(3))

col1, col2 = st.columns(2)

with col1 : 
     st.write('Assessement on time')
     st.markdown(f'<p style="font-family:Arial; color:Red; font-size: 30px;">44 %</p>', unsafe_allow_html=True)
     st.write('Acknowledgement on time')
     st.markdown(f'<p style="font-family:Arial; color:Green; font-size: 30px;">89 %</p>', unsafe_allow_html=True)

with col2 : 
     st.write('Number of open SMS cases')
     st.markdown('<p style = "font-family:Arial; font-size: 40px;">34</p>', unsafe_allow_html= True)
     st.write('Number of closed SMS cases')
     st.markdown('<p style = "font-family:Arial; font-size: 40px;">1</p>', unsafe_allow_html= True)