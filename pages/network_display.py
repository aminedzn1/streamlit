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

filtered = st.multiselect("Filter columns", ["Name","E-mail","Phone number","Role","Domain","Siglum","Technical perimeter","ATA","Sites","Nomination status","Nomination letter Reference","Trained","Role 2"])

st.write(network_data[filtered])