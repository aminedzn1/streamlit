import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.stylable_container import stylable_container 
from streamlit_extras.switch_page_button import switch_page
###########################################################################################################

st.set_page_config(
     page_title = '1 & DOA SMS CoCkPiT',
     page_icon = 'barchart',
     layout = 'wide',
#     initial_sidebar_state = 'collapsed'
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
    background-color: #051650;
    border: 1px solid #ffffff;
    border-radius : 10px;
    padding-left:30px;
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
        try :
            st.markdown(st.session_state.obj_acc, unsafe_allow_html= True)
        except :
            with open('data/obj_acc.txt') as f :
                st.session_state.obj_acc = f.read()
                st.markdown(st.session_state.obj_acc, unsafe_allow_html= True)
    with col12 :
        st.write('Filled')
        try : 
            st.markdown(st.session_state.obj_fil, unsafe_allow_html= True)
        except : 
            with open('data/obj_fil.txt') as f :
                st.session_state.obj_fil = f.read()
                st.markdown(st.session_state.obj_fil, unsafe_allow_html= True)

    with stylable_container(key = 'Details_button', css_styles="""button{
                            background-color:#051650;
                            border: 1px solid #ffffff;
    }""")    :
        details_obj = st.button('Details', key = "DETAILSOBJETS")
    if details_obj : 
        switch_page('objectives metriques')
    
###########################################################################################################    

    st.subheader('SQE Nomination')
    with stylable_container(key = 'metric_container',
                            css_styles = container_style, ) :
        sqe = st.container()
    sqe.write('Domain / Function with SQE')
    try :    
        sqe.markdown(st.session_state.sqe_kpi, unsafe_allow_html=True)
    except :
        with open('data/sqe_kpi.txt') as f :
            st.session_state.sqe_kpi = f.read()
        sqe.markdown(st.session_state.sqe_kpi, unsafe_allow_html=True)
    with stylable_container(key = 'Details_button', css_styles="""button{
                            background-color:#051650;
                            border: 1px solid #ffffff;
    }""")    :
        details_sqe = st.button('Details', key = 'DETAILSSQE')
    
    if details_sqe : 
        switch_page('sqe metrique')

###########################################################################################################    

    st.subheader('CASID')

with col2 :
    st.subheader('Risk Management on Systemic Safety Topics')
    with stylable_container(key = 'metric_container',
                            css_styles = container_style, ) : 
        col21, col22 = st.columns(2)
    with col21 : 
        st.markdown('Assessement on time')
        st.markdown(f'<p style="font-family:Arial; color:Red; font-size: 30px;">44 %</p>', unsafe_allow_html=True)
        st.write('Acknowledgement on time')
        st.markdown(f'<p style="font-family:Arial; color:Green; font-size: 30px;">89 %</p>', unsafe_allow_html=True)

    with col22 : 
        st.write('Number of open SMS cases')
        st.markdown('<p style = "font-family:Arial; font-size: 30px;">34</p>', unsafe_allow_html= True)
        st.write('Sources of SMS cases')
    ###########################################################################################################    

    st.subheader('Budget')
    try:
        st.plotly_chart(st.session_state.budg_fig, use_container_width=True)
    except:
        st.write(":/")
    with stylable_container(key = 'Details_button', css_styles="""button{
                            background-color:#051650;
                            border: 1px solid #ffffff;
    }""")    :
        details_budg = st.button('Details', key = 'DETAILSBUDGET')
    
    if details_budg : 
        switch_page('budget display')
with col3 :
    st.subheader('Assurance')
    st.subheader('Promotion')