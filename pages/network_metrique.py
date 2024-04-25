import streamlit as st 
import pandas as pd 
import numpy as np
from streamlit_extras.stylable_container import stylable_container 
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
     page_title = 'Network Measure',
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

###########################################################################################################
st.title('Percentage of trained safety representatives per domain / function')

network_data = pd.read_csv(r'data/Network Contact list - SMS contact.csv')

network_data['trainedBool'] = (network_data['Trained'] == 'Yes')

plot_tr = network_data[['Domain', 'trainedBool']].groupby(['Domain']).mean()
plot_tr['trainedBool'] = plot_tr['trainedBool'].apply(lambda x : round(x*100, 2))
plot_tr = plot_tr.rename(columns = {'trainedBool' : 'Percent trained'})

import plotly.express as px
fig = px.bar(plot_tr)

st.plotly_chart(fig)

###########################################################################################################
with stylable_container(key = 'Details_button', css_styles="""button{
                            background-color:#051650;
                            border: 1px solid #ffffff;
    }""")    :
        details_train = st.button('Details')
        if details_train :
            switch_page('network display')
###################################################