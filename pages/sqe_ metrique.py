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
    st.session_state.sqe_data = sqe_data

#sqe_data.columns = ["Domain/Function","SQE Holder","Date of signature","End of validity","Part of active network?","SQE Active?"]

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

sqe_number = sum(np.array(sqe_count_domain['activeBool']) > 0)
domain_number = len(sqe_count_domain['activeBool'])

value = f"{sqe_number}/{domain_number}"

if 'Red' in list(sqe_count_domain['color']) :
    st.session_state.sqe_kpi = f'<p style="font-family:Arial; color:Red; font-size: 30px;">{value}</p>'
elif 'rgb(230, 184, 0)' in list(sqe_count_domain['color'])  :
    st.session_state.sqe_kpi = f'<p style="font-family:Arial; color:rgb(230, 184, 0); font-size: 30px;">{value}</p>'
else : 
    st.session_state.sqe_kpi = f'<p style="font-family:Arial; color:Green; font-size: 30px;">{value}</p>'
with open('data/sqe_kpi.txt', 'w') as f:
    f.write(st.session_state.sqe_kpi)

#if sqe_number <= 5 :
#    st.write("Domain/Function with SQE") 
#    st.markdown(f'<p style="font-family:Arial; color:Red; font-size: 30px;">{value}</p>', unsafe_allow_html=True)

#elif sqe_number > 5 and sqe_number <  domain_number :
#    st.write("Domain/Function with SQE") 
#    st.markdown(f'<p style="font-family:Arial; color:rgb(230, 184, 0); font-size: 30px;">{value}</p>', unsafe_allow_html=True)

#elif sqe_number == domain_number :
#    st.write("Domain/Function with SQE")
#    st.markdown(f'<p style="font-family:Arial; color:Green; font-size: 30px;">{value}</p>', unsafe_allow_html=True)
###########################################################################################################

#st.subheader('Add comment', divider = "red" )

#try : 
#    comments = st.session_state.comments
#except :    
#    comments = []
#comment = st.text_input("Comment")

#if st.button("Post") :
#    comments = [comment] + comments
#    st.session_state.comments = comments
#st.table(pd.DataFrame(comments, columns = ["Comments"]))

domain = st.selectbox('Fonction / Domaine', ("1","1A","1C","1G","1I","1P","1S","1T","1V","1Y","1Z","B","S","P","Q"))

st.write(f"Number of SQE for {domain}") 
st.markdown(f'<p style="font-family:Arial; color:{sqe_count_domain.loc[domain,"color"]}; font-size: 30px;">{sqe_count_domain.loc[domain,"activeBool"]}</p>', unsafe_allow_html=True)

###########################################################################################################