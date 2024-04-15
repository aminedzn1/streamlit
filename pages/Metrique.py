import streamlit as st 
import pandas as pd 
import numpy as np

###########################################################################################################
st.title('2024 SMS in 1 & DOA Objectives by domain / function')

try :
    obj_data = st.session_state.obj_data
except : 
    obj_data = pd.read_csv(r'data/Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv', dtype = 'string',keep_default_na=False)

obj_data.columns = ["Objective category","Source","#","Objective","KPI / Achievement criteria","Owners/ Applicability","Target date","Global Status","1","1A","1C","1G","1I","1P","1S","1T","1V","1Y","1Z","B","S","P","Q"]

###########################################################################################################

domain = st.selectbox('Fonction / Domaine', ("Global Status","1","1A","1C","1G","1I","1P","1S","1T","1V","1Y","1Z","B","S","P","Q"))

try :    
    accomplished = obj_data[domain]
except :
    accomplished = obj_data[obj_data.columns[8:]]

array_accomplished = accomplished.to_numpy().flatten()
array_accomplished = array_accomplished[array_accomplished != 'N/A']
def boolean_values(X) :
    if X == '1' :
        return(1)
    else :
        return(0)

array_accomplished = np.array(pd.Series(array_accomplished).apply(lambda x : boolean_values(x)))

###########################################################################################################

value = round(array_accomplished.mean()*100, 2)
if value < 50 : 
    with open (r'styles/metric_red.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        st.metric("Objective %", value)
elif value > 50 and value < 85 : 
    with open (r'styles/metric_amber.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        st.metric("Objective %", value)
elif value > 85 and value <= 100 : 
    with open (r'styles/metric_green.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        st.metric("Objective %", value)

###########################################################################################################
st.subheader('Add comment', divider = "red" )
 
try : 
    comments = st.session_state.comments
except :    
    comments = []
comment = st.text_input("Comment")

if st.button("Post") :
    comments.append(comment)
    st.session_state.comments = comments
st.table(pd.DataFrame(comments))