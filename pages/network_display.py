import streamlit as st
import pandas as pd
import numpy as np

###########################################################################################################
st.set_page_config(
     page_title = 'SMS Network contact list',
     page_icon = 'clipboard',
)
st.title('SMS Network contact list')

network_data = pd.read_csv(r"data/Network Contact list - SMS contact.csv")

filtered = st.multiselect("Filter columns", options = list(network_data.columns), default = ["Name", "Siglum", "Trained"])

st.write(network_data[filtered])

###########################################################################################################

st.session_state.network_data = network_data