import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
     page_title = 'Network list',
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
st.title('SMS Network contact list')

###########################################################################################################


network_data = pd.read_csv(r"data/Network Contact list - SMS contact.csv")

filtered = st.multiselect("Filter columns", options = list(network_data.columns), default = ["Name", "Siglum", "Trained"])

st.dataframe(network_data[filtered], use_container_width=True)

###########################################################################################################
