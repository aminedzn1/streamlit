import streamlit as st
import pandas as pd
import numpy as np

###########################################################################################################
st.set_page_config(
     page_title = 'Promotion display',
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
st.title('1 & DOA SMS Promotion Follow-up in the last 3 months')

promo = pd.read_csv(r'data/Engineering SMS Promotion Follow-up - Safety Briefing, Training, Hub.csv')
promo['Date'] = pd.to_datetime(promo['Date'], dayfirst=True,format='mixed')
troismois = pd.Timestamp.today() - pd.DateOffset(months = 3)
promo = promo.loc[promo['Date']>troismois]

filt = st.multiselect("Filter columns",options=promo.columns, default =['Promotion Type','Date'] )
st.table(promo[filt])

value  = len(list(promo['Date']))
text =f"<p style = 'font-family:Arial; font-size:30px; color:White;'>{value}</p>"
st.session_state.promo = text
