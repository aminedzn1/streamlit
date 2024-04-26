import streamlit as st
import pandas as pd
import numpy as np

###########################################################################################################
st.set_page_config(
     page_title = 'ePPS display',
     page_icon = 'clipboard',
)
st.title('1 & DOA SMS cases')
###########################################################################################################

pps_data = pd.read_csv(r'data/SMS FILTERED DATA ADDED COLUMNS (1).csv', dtype = 'string',keep_default_na=False)
speakup_data = pd.read_csv(r'data/Report database non-confidential - Employee speak-up follow-up.csv',dtype = 'string',keep_default_na=False)

speakup_data['Timestamp'] = pd.to_datetime(speakup_data['Timestamp'], dayfirst=True, format='mixed')
speakup_data['Initial employee feedback'] = pd.to_datetime(speakup_data['Initial employee feedback'], dayfirst=True, format='mixed')

speakup_data['onTime'] = (speakup_data['Initial employee feedback'] - speakup_data['Timestamp']) > pd.Timedelta(days =21)

df = speakup_data[['Domain leader (dept)',]]
