import streamlit as st 
import pandas as pd 
import numpy as np

st.set_page_config(
     page_title = 'Objectives Measure',
     page_icon = 'bar_chart'
)

###########################################################################################################
st.title('2024 SMS in 1 & DOA Objectives by domain / function')

try :
    obj_data = st.session_state.obj_data
except : 
    obj_data = pd.read_csv(r'data/Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv', dtype = 'string',keep_default_na=False)

obj_data.columns = ["Objective category","Source","#","Objective","KPI / Achievement criteria","Owners/ Applicability","Target date","Global Status","1","1A","1C","1G","1I","1P","1S","1T","1V","1Y","1Z","B","S","P","Q"]

###########################################################################################################

domain = st.selectbox('Fonction / Domaine', ("All","Global Status","1","1A","1C","1G","1I","1P","1S","1T","1V","1Y","1Z","B","S","P","Q"))

try :    
    accomplished = obj_data[domain]
except :
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
###########################################################################################################
col1, col2 = st.columns(2)
with col1 :
        value = round(array_accomplished.mean()*100, 2)
        if value < 50 :
            st.write("Objectives accomplished") 
            st.markdown(f'<p style="font-family:Arial; color:Red; font-size: 30px;">{value} %</p>', unsafe_allow_html=True)
            st.session_state.obj_acc = f'<p style="font-family:Arial; color:Red; font-size: 30px;">{value} %</p>'
        elif value > 50 and value < 85 :
            st.write("Objectives accomplished") 
            st.markdown(f'<p style="font-family:Arial; color:rgb(230, 184, 0); font-size: 30px;">{value} %</p>', unsafe_allow_html=True)
            st.session_state.obj_acc = f'<p style="font-family:Arial; color:rgb(230, 184, 0); font-size: 30px;">{value} %</p>'
        elif value > 85 and value <= 100 :
            st.write("Objectives accomplished")
            st.markdown(f'<p style="font-family:Arial; color:Green; font-size: 30px;">{value} %</p>', unsafe_allow_html=True)
            st.session_state.obj_acc = f'<p style="font-family:Arial; color:Green; font-size: 30px;">{value} %</p>'

with col2 :
    value = round(array_filled.mean()*100, 2)
    if value < 50 :
        st.write("Objectives filled") 
        st.markdown(f'<p style="font-family:Arial; color:Red; font-size: 30px;">{value} %</p>', unsafe_allow_html=True)
        st.session_state.obj_fil = f'<p style="font-family:Arial; color:Red; font-size: 30px;">{value} %</p>'
    elif value > 50 and value < 85 :
        st.write("Objectives filled") 
        st.markdown(f'<p style="font-family:Arial; color:rgb(230, 184, 0); font-size: 30px;">{value} %</p>', unsafe_allow_html=True)
        st.session_state.obj_fil = f'<p style="font-family:Arial; color:rgb(230, 184, 0); font-size: 30px;">{value}  %</p>'
    elif value > 85 and value <= 100 :
        st.write("Objectives filled")
        st.markdown(f'<p style="font-family:Arial; color:Green; font-size: 30px;">{value} %</p>', unsafe_allow_html=True)
        st.session_state.obj_fil = f'<p style="font-family:Arial; color:Green; font-size: 30px;">{value} %</p>'


###########################################################################################################
st.subheader('Add comment', divider = "red" )

try : 
    comments = st.session_state.comments
except :    
    comments = []
comment = st.text_input("Comment")

if st.button("Post") :
    comments = [comment] + comments
    st.session_state.comments = comments
st.table(pd.DataFrame(comments, columns = ["Comments"]))