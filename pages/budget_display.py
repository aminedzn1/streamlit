import streamlit as st 
import pandas as pd 
import numpy as np
from streamlit_extras.stylable_container import stylable_container 
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
     page_title = 'Objectives Measure',
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
#try :
#    data_budg = st.session_state.data_budg
#except :
data_budg = pd.read_csv(r'data/sms_budget_yoy.csv')

x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_act = list(data_budg['Actuals (k€)'])
y_com = list(data_budg['Commitment (k€)'])
y_evo = list(data_budg['Actuals evolution (k€)'])
y_tar = list(data_budg['Target linear evolution (k€)'])


bar_1 = go.Bar(
    x=x,
    y=y_act,
    name='Actuals (k€)',
    zorder=1,
    marker=dict(color="blue"),
)
bar_2 = go.Bar(
    x=x,
    y=y_com,
    name='Commitment (k€)',
    zorder=2,
    marker=dict(color="green"),
)
line_1 = go.Scatter(
    x=x,
    y=y_evo,
    mode="lines+markers",
    name='Actuals evolution (k€)',
    zorder=3,
    marker=dict(color="blue"),
)
line_2 = go.Scatter(
    x=x,
    y=y_tar,
    mode="lines",
    name='Target linear evolution (k€)',
    zorder=4,
    marker=dict(color="red"),
)
fig = go.Figure(data=[bar_1,bar_2,line_1,line_2])
st.plotly_chart(fig, use_container_width=True)

fig.update_layout(legend=dict(x=0, y=1))  
st.session_state.budg_fig = fig

month = np.argmax(y_evo) - 1
delta = y_tar[month] - y_evo[month]
tol = .05*y_tar[month]

if delta > tol :
    text = f"""
<p style ="font-family:Arial; font-size:30px; color: White;">{y_evo[month]} k€ \n</p>
<p style ="font-family:Arial; font-size:10px; color: rgb(230, 184, 0);">+{delta}</p>
"""
elif delta < - tol :
    text = f"""
<p style ="font-family:Arial; font-size:30px; color: White;">{y_evo[month]} k€ \n</p>
<p style ="font-family:Arial; font-size:20px; color: Red;">{delta}</p>
"""
else :
    text = f"""
<p style ="font-family:Arial; font-size:30px; color: White;">{y_evo[month]} k€ \n</p>
<p style ="font-family:Arial; font-size:10px; color: Green;">{delta}</p>
"""

st.session_state.budg_metr = text