import streamlit as st 
import pandas as pd 
import numpy as np
from streamlit_extras.stylable_container import stylable_container 
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
     page_title = 'SQE Measure',
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
st.title('2024 SMS in 1 & DOA SQE by domain / function')

sqe_data = pd.read_csv(r'data/SQE Follow-up - Sheet1.csv', dtype = 'string',keep_default_na=False)
###########################################################################################################

def boolean_values(X) :
    if X == 'Y' :
        return(1)
    else : 
        return(0)
def date_alert (X) :
    inAMonth = pd.Timestamp.today() + pd.DateOffset(months=1)
    if inAMonth > X and  pd.Timestamp.today() < X  :
        return(1)
    elif pd.Timestamp.today() > X :
        return(2)
    else : 
        return(0)

sqe_data['activeBool'] =sqe_data['SQE Active?'].apply(lambda x : boolean_values(x))
sqe_data['End of validity'] = pd.to_datetime(sqe_data['End of validity'],dayfirst = True, format = 'mixed')
sqe_data['dateAlert'] = sqe_data['End of validity'].apply(date_alert)
sqe_data['color'] = ''
for i in sqe_data.index :
    if sqe_data.loc[i,'dateAlert'] == 2 :
        sqe_data.loc[i, 'SQE Active?'] = 'N'
        sqe_data.loc[i, 'activeBool'] = 0

for i in sqe_data.index :
    if sqe_data.loc[i,'SQE Active?'] == 'Y' and sqe_data.loc[i, 'dateAlert'] == 0 :
        sqe_data.loc[i,'color'] = 'Green'
    elif sqe_data.loc[i,'SQE Active?'] == 'Y' and sqe_data.loc[i, 'dateAlert'] == 1 :
        sqe_data.loc[i,'color'] = 'rgb(230, 184, 0)'
    else :
        sqe_data.loc[i,'color'] = 'Red'
############################################################################################################

sqe_count_domain = sqe_data[['Domain/Function', 'activeBool']].groupby(['Domain/Function']).sum()
sqe_count_domain['color'] = ''
for func in sqe_count_domain.index :
    vColor = list(sqe_data.loc[sqe_data['Domain/Function'] == func]['color'])
    if 'Green' in vColor :
        sqe_count_domain.loc[func,'color'] = 'Green'
    elif 'rgb(230,184,0)' in vColor :
        sqe_count_domain.loc[func,'color'] = 'rgb(230,184,0)'
    else : 
        sqe_count_domain.loc[func,'color'] = 'Red'

container_style = """
{
    background-color: #051650;
    border: 1px solid #ffffff;
    border-radius : 10px;
    padding-left:30px;
}
  
}
"""
sqe_count_domain = sqe_count_domain.rename(columns = {'activeBool' : 'Active SQEs'})

fig = px.bar(sqe_count_domain, y = 'Active SQEs')
st.plotly_chart(fig, use_container_width=True   )
###########################################################################################################
with stylable_container(key = 'Details_button', css_styles="""button{
                            background-color:#051650;
                            border: 1px solid #ffffff;
    }""")    :
        details_obj = st.button('Details', key = "DETAILSOBJETS")
if details_obj : 
        switch_page('sqe display')