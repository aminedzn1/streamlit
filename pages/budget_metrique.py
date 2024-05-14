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
st.title('1 & DOA SMS Budget')

###########################################################################################################

data_budg = pd.read_csv(r'data/sms_budget_yoy.csv')
st.subheader('Global budget status')
x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_act = list(data_budg['Actuals (k€)'])
y_com = list(data_budg['Commitment (k€)'])
y_evo = list(data_budg['Actuals evolution (k€)'])
y_tar = list(data_budg['Target linear evolution (k€)'])

Y = np.array(y_evo)
X = np.linspace(1, len(Y), num = len(Y))

B0 = sum((Y-np.mean(Y))*(X - np.mean(X)))/np.var(X)
B1 = np.mean(Y) - B0*np.mean(X)
st.write(y_pro)
y_pro = list(B0*X+B1)

bar_1 = go.Bar(
    x=x,
    y=y_evo,
    name='Actuals evolution (k€)',
    zorder=1,
    marker=dict(color="blue"),
)
#bar_2 = go.Bar(
#    x=x,
#    y=y_com,
#    name='Commitment (k€)',
#    zorder=2,
#    marker=dict(color="green"),
#)

line_1 = go.Scatter(
    x=x,
    y=y_pro,
    mode="lines+markers",
    name='Projected trendline (k€)',
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
fig = go.Figure(data=[bar_1,line_1])
st.plotly_chart(fig, use_container_width=True)


###########################################################################################################
st.subheader('Budget status per domain')
data = pd.read_csv(r'data/sms_budget_f.csv')
x = list(data['Domain/Function'])
y_1 = list(data['Baseline (k€)'])
y_2 = list(data['Actuals (k€)'])
y_3 = list(data['Commitment (k€)'])
y_4 = list(data['Target linear (k€)'])

fig = px.bar(
    data_frame=data[['Domain/Function','Actuals (k€)','Commitment (k€)']],
    x='Domain/Function',
    y=['Actuals (k€)','Commitment (k€)']
)
fig.add_trace(go.Scatter(
      x=x,
      y=y_1,
      mode = 'markers',
      marker=dict(symbol = "arrow-bar-down",color="red",size = 20,line=dict(width=2, color="#e6e6e6")),
      name = 'Baseline (k€)'
)) 

fig.add_trace(go.Scatter(
      x=x,
      y=y_4,
      mode = 'markers',
      marker=dict(symbol = 'arrow-bar-up', color="green",size = 20,line=dict(width=2, color="#e6e6e6")),
      name = 'Target (k€)'
)) 

st.plotly_chart(fig, use_container_width=True)
###########################################################################################################
with stylable_container(key = 'Details_button', css_styles="""button{
                            background-color:#051650;
                            border: 1px solid #ffffff;
    }""")    :
        details_budg = st.button('Details')
        if details_budg :
            switch_page('budget display')
###################################################