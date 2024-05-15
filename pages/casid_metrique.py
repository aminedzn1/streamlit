import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.stylable_container import stylable_container 
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
     page_title = 'CASID Status (FAKE DATA)',
     page_icon = 'bar_chart',
     layout = 'wide',
     initial_sidebar_state = 'collapsed'
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

###########################################################################################################

st.page_link('home.py', label = 'Home', icon = '🏠', use_container_width=True)
st.title('1 CASID Status (FAKE DATA)')
###########################################################################################################

COC = ['1A', '1C','1P', '1Y']
ontime = [3,2,2,5]
risk = [0,0,0,1]
late = [0,1,2,0]
done = [1,1,2,2]
###########################################################################################################
bar_1 = go.Bar(
    x=COC,
    y=ontime,
    name='CASID on time',
    zorder=1,
    marker=dict(color="rgb(0,230,115)"),
)
bar_2= go.Bar(
    x=COC,
    y=risk,
    name='CASID at risk',
    zorder=2,
    marker=dict(color="rgb(255, 166,77 )"),
)
bar_3= go.Bar(
    x=COC,
    y=late,
    name='CASID late',
    zorder=3,
    marker=dict(color="rgb(255,102,102)"),
)
bar_4= go.Bar(
    x=COC,
    y=late,
    name='CASID on follow up',
    zorder=4,
    marker=dict(color="#ADD8E6"),
)
col1, col2, = st.columns(2)
with col1 : 
    fig = go.Figure(data=bar_1)
    fig.update_traces(width=1)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("<p style ='text-align: center; font-family: Arial; font-size: 40px;'>CASID On Time</p>", unsafe_allow_html=True)
    
    fig = go.Figure(data=bar_2)
    fig.update_traces(width=1)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("<p style ='text-align: center; font-family: Arial; font-size: 40px;'>CASID At Risk</p>", unsafe_allow_html=True)

with col2 : 
    fig = go.Figure(data=bar_3)
    fig.update_traces(width=1)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("<p style ='text-align: center; font-family: Arial; font-size: 40px;'>CASID Late</p>", unsafe_allow_html=True)

    fig = go.Figure(data=bar_4)
    fig.update_traces(width=1)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("<p style ='text-align: center; font-family: Arial; font-size: 40px;'>CASID On Follow Up</p>", unsafe_allow_html=True)
