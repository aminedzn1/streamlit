import streamlit as st
import pandas as pd
import numpy as np

###########################################################################################################
st.set_page_config(
     page_title = 'Objective display',
     page_icon = 'clipboard',
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

st.page_link('home.py', label = 'Home', icon = '🏠', use_container_width=True)
st.title('2024 SMS in 1 & DOA Objectives')
###########################################################################################################

obj_data = pd.read_csv(r'data/Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv', dtype = 'string',keep_default_na=False)

###########################################################################################################


filtered = st.multiselect("Filter columns", options=list(obj_data.columns), default=['Objective','Global Status']) 
st.table(obj_data[filtered])



#st.subheader('Add comment', divider = "blue" )

#try : 
#    comments = st.session_state.comments
#except :    
#    comments = []
#comment = st.text_input("Comment")

#if st.button("Post") :
#    comments = [comment] + comments
#    st.session_state.comments = comments
#st.table(pd.DataFrame(comments, columns = ["Comments"]))