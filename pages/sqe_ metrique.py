import streamlit as st 
import pandas as pd 
import numpy as np

st.set_page_config(
     page_title = 'SQE Measure',
     page_icon = 'bar_chart'
)

###########################################################################################################
st.title('2024 SMS in 1 & DOA SQE by domain / function')

try :
    sqe_data = st.session_state.sqe_data
except : 
    sqe_data = pd.read_csv(r'data/SQE Follow-up - Sheet1.csv', dtype = 'string',keep_default_na=False)

sqe_data.columns = ["Domain/Function","SQE Holder","Date of signature","End of validity","Part of active network?","SQE Active?"]

###########################################################################################################

domain = st.selectbox('Fonction / Domaine', ("All","1","1A","1C","1G","1I","1P","1S","1T","1V","1Y","1Z","B","S","P","Q"))
if domain == "All" :
    pass
else :
    sqe_data = sqe_data.loc[sqe_data["Domain/Function"] == domain]
###########################################################################################################
def boolean_values(X) :
    if X == 'Y' :
        return(1)
    else : 
        return(0)

sqe_data['activeBool'] =sqe_data['SQE Active?'].apply(lambda x : boolean_values(x))


sqe_count_domain = sqe_data[['Domain/Function', 'activeBool']].groupby(['Domain/Function']).sum()
sqe_number = sum(np.array(sqe_count_domain['activeBool']) > 0)
domain_number = len(sqe_count_domain['activeBool'])
value = f"{sqe_number}/{domain_number}"

if sqe_number <= 5 :
    st.write("Objective %") 
    st.markdown(f'<p style="font-family:Verdana; color:Red; font-size: 30px;">{value}</p>', unsafe_allow_html=True)

elif sqe_number > 5 and sqe_number <  domain_number :
    st.write("Domain/Function with SQE") 
    st.markdown(f'<p style="font-family:Arial; color:rgb(230, 184, 0); font-size: 30px;">{value}</p>', unsafe_allow_html=True)

elif sqe_number == domain_number :
    st.write("Domain/Function with SQE")
    st.markdown(f'<p style="font-family:Arial; color:Green; font-size: 30px;">{value}</p>', unsafe_allow_html=True)
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