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

Y = np.array(y_evo)[~np.isnan(y_evo)]
X = np.linspace(1, len(Y), num = len(Y))

B0 = sum((Y-np.mean(Y))*(X - np.mean(X)))/sum((X-np.mean(X))**2)
B1 = np.mean(Y) - B0*np.mean(X)

X = np.linspace(1, len(x), num = len(x))

y_pro = list(B0*X+B1)

bar_1 = go.Bar(
    x=x,
    y=y_evo,
    name='Actuals evolution (k€)',
    zorder=1,
    marker=dict(color="#1035AC"),
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
    marker=dict(color="#ADD8E6"),
)
line_2 = go.Scatter(
    x=x,
    y=y_tar,
    mode="lines",
    name='Target linear evolution (k€)',
    zorder=4,
    marker=dict(color="rgb(0,230,115)"),
)
fig = go.Figure(data=[bar_1,line_1, line_2])
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
    y=['Actuals (k€)','Commitment (k€)'],
    color_discrete_sequence=px.colors.sequential.Blues_r
)
fig.add_trace(go.Scatter(
      x=x,
      y=y_1,
      mode = 'markers',
      marker=dict(symbol = "line-ew-open",color="rgb(191,128,255)",size = 30,line=dict(width=3.5, color="rgb(191,128,255)")),
      name = 'Baseline EOY (k€)'
)) 

fig.add_trace(go.Scatter(
      x=x,
      y=y_4,
      mode = 'markers',
      marker=dict(symbol = 'line-ew-open', color="rgb(0,230,115)",size = 30,line=dict(width=3.5, color="rgb(0,230,115)")),
      name = 'Linear Taget (k€)'
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