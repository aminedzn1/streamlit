import streamlit as st 
import pandas as pd 
import numpy as np
from streamlit_extras.stylable_container import stylable_container 
from streamlit_extras.switch_page_button import switch_page

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
st.title('2024 SMS in 1 & DOA Objectives by domain / function')
###########################################################################################################
obj_data = pd.read_csv(r'data/Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv', dtype = 'string',keep_default_na=False)

accomplished = obj_data[obj_data.columns[8:]]

array_accomplished = accomplished.to_numpy().flatten()
array_filled = accomplished.to_numpy().flatten()

array_accomplished = array_accomplished[array_accomplished != 'N/A']
array_filled = array_filled[array_filled !='N/A']

def filled_values(X) : 
    if X == "1" or X == "0" :
        return (1)
    else : 
        return (0)
    
def boolean_values(X) :
    if X == '1' :
        return(1)
    else :
        return(0)

array_accomplished = np.array(pd.Series(array_accomplished).apply(lambda x : boolean_values(x)))
array_filled = np.array(pd.Series(array_filled).apply(lambda x : filled_values(x)))

import plotly.express as px

plot_objectives = pd.DataFrame(np.random.randn(len(accomplished.columns), 2),columns=['Accomplished', 'Filled'])
plot_objectives.index = accomplished.columns
for function in plot_objectives.index :
    plot_objectives.loc[function, 'Accomplished'] = accomplished[function].apply(boolean_values).mean()*100
    plot_objectives.loc[function, 'Filled'] = accomplished[function].apply(filled_values).mean()*100
    plot_objectives.loc[function, 'Accomplished'] = plot_objectives.loc[function, 'Accomplished'] * 100 / plot_objectives.loc[function, 'Filled']

fig = px.bar(plot_objectives, barmode= 'group')

st.plotly_chart(fig, use_container_width=True)



###########################################################################################################
with stylable_container(key = 'Details_button', css_styles="""button{
                            background-color:#051650;
                            border: 1px solid #ffffff;
    }""")    :
        details_obj = st.button('Details')
        if details_obj :
            switch_page('objectives display')
###########################################################################################################



