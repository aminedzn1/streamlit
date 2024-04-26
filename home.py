import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.stylable_container import stylable_container 
from streamlit_extras.switch_page_button import switch_page
###########################################################################################################

st.set_page_config(
     page_title = '1 & DOA SMS CoCkPiT',
     page_icon = 'barchart',
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

st.title("1 & DOA SMS Dashboard")
container_style = """
{
    background-color: #051650;
    border: 1px solid #ffffff;
   
    padding-left:30px;
    padding-bottom:30px;
}
  
}
"""
#################################################################################################################################
#OBJECTIFS
obj_data = pd.read_csv(r'data/Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv', dtype = 'string',keep_default_na=False)
global_status = obj_data['Global Status']

array_accomplished = global_status.to_numpy().flatten()
array_filled = global_status.to_numpy().flatten()

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


value = round(array_accomplished.mean()*100 / array_filled.mean(), 2) 
if value < 50 :
    st.session_state.obj_acc = f'<p style="font-family:Arial; color:Red; font-size: 30px;">{value} %</p>'

elif value > 50 and value < 85 :
    st.session_state.obj_acc = f'<p style="font-family:Arial; color:rgb(230, 184, 0); font-size: 30px;">{value} %</p>'

elif value > 85 and value <= 100 :
    st.session_state.obj_acc = f'<p style="font-family:Arial; color:Green; font-size: 30px;">{value} %</p>'


value = round(array_filled.mean()*100, 2)
if value < 50 :
    st.session_state.obj_fil = f'<p style="font-family:Arial; color:Red; font-size: 30px;">{value} %</p>'

elif value > 50 and value < 85 :
    st.session_state.obj_fil = f'<p style="font-family:Arial; color:rgb(230, 184, 0); font-size: 30px;">{value}  %</p>'

elif value > 85 and value <= 100 :
    st.session_state.obj_fil = f'<p style="font-family:Arial; color:Green; font-size: 30px;">{value} %</p>'
###########################################################################################################
###########################################################################################################
#BUDGET
data_budg = pd.read_csv(r'data/sms_budget_yoy.csv')

x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_act = list(data_budg['Actuals (k€)'])
y_com = list(data_budg['Commitment (k€)'])
y_evo = list(data_budg['Actuals evolution (k€)'])
y_tar = list(data_budg['Target linear evolution (k€)'])

month = np.argmax(y_evo) - 1
delta = y_tar[month] - y_evo[month]
tol = .05*y_tar[month]

if delta < -tol :
    text = f"""
<p style ="font-family:Arial; font-size:30px; color: White;">{y_evo[month]} k€ \n</p>
<p style ="font-family:Arial; font-size:20px; color: rgb(230, 184, 0);">Overspend of {delta} k€</p>
"""
elif delta > tol :
    text = f"""
<p style ="font-family:Arial; font-size:30px; color: White;">{y_evo[month]} k€ \n</p>
<p style ="font-family:Arial; font-size:20px; color: Red;">Underspend of {delta} k€</p>
"""
else :
    if delta > 0 :
        text = f"""
    <p style ="font-family:Arial; font-size:30px; color: White;">{y_evo[month]} k€ \n</p>
    <p style ="font-family:Arial; font-size:20px; color: Green;">Underspend of {delta} k€</p>
    """
    else :
        text = f"""
    <p style ="font-family:Arial; font-size:30px; color: White;">{y_evo[month]} k€ \n</p>
    <p style ="font-family:Arial; font-size:20px; color: Green;">Overspend of {delta} k€</p>
    """

st.session_state.budg_metr = text

###########################################################################################################
###########################################################################################################
#SQE
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

sqe_number = sum(np.array(sqe_count_domain['activeBool']) > 0)
domain_number = len(sqe_count_domain['activeBool'])

value = f"{sqe_number}/{domain_number}"

if 'Red' in list(sqe_count_domain['color']) :
    st.session_state.sqe_kpi = f'<p style="font-family:Arial; color:Red; font-size: 30px;">{value}</p>'
elif 'rgb(230, 184, 0)' in list(sqe_count_domain['color'])  :
    st.session_state.sqe_kpi = f'<p style="font-family:Arial; color:rgb(230, 184, 0); font-size: 30px;">{value}</p>'
else : 
    st.session_state.sqe_kpi = f'<p style="font-family:Arial; color:Green; font-size: 30px;">{value}</p>'
###########################################################################################################
###########################################################################################################
#PROMO
promo = pd.read_csv(r'data/Engineering SMS Promotion Follow-up - Safety Briefing, Training, Hub.csv')
promo['Date'] = pd.to_datetime(promo['Date'], dayfirst=True,format='mixed')
troismois = pd.Timestamp.today() - pd.DateOffset(months = 3)
promo = promo.loc[promo['Date']>troismois]

value  = len(list(promo['Date']))
text =f"<p style = 'font-family:Arial; font-size:30px; color:White;'>{value}</p>"
st.session_state.promo = text
###########################################################################################################
###########################################################################################################
#TRAINED
network_data = pd.read_csv(r'data/Network Contact list - SMS contact.csv')
value = round(np.mean(network_data['Trained'] == 'Yes')*100, 2)
text = f"<p style = 'font-family:Arial; font-size: 30px;'>{value} %</p>"
st.session_state.trained = text
###########################################################################################################
###########################################################################################################
#DAHSBOARD

col1, col2, col3 = st.columns([1,2,1])

with col1:
    st.subheader('Objectives')
    with stylable_container(key = 'metric_container',
                            css_styles = container_style, ) :
        objectives = st.container()
    col11, col12 = objectives.columns(2)
    with col11 :
        st.write('Accomplished')
        st.markdown(st.session_state.obj_acc, unsafe_allow_html= True)

    with col12 :
        st.write('Filled')
        st.markdown(st.session_state.obj_fil, unsafe_allow_html= True)

    with stylable_container(key = 'Details_button', css_styles="""button{
                            background-color:#051650;
                            border: 1px solid #ffffff;
    }""")    :
        details_obj = st.button('Details', key = "DETAILSOBJETS")
    if details_obj : 
        switch_page('objectives metriques')
    
###########################################################################################################    

    st.subheader('SQE Nomination')
    with stylable_container(key = 'metric_container',
                            css_styles = container_style, ) :
        sqe = st.container()
    sqe.write('Domain / Function with SQE')
    try :    
        sqe.markdown(st.session_state.sqe_kpi, unsafe_allow_html=True)
    except :
        with open('data/sqe_kpi.txt') as f :
            st.session_state.sqe_kpi = f.read()
        sqe.markdown(st.session_state.sqe_kpi, unsafe_allow_html=True)
    with stylable_container(key = 'Details_button', css_styles="""button{
                            background-color:#051650;
                            border: 1px solid #ffffff;
    }""")    :
        details_sqe = st.button('Details', key = 'DETAILSSQE')
    
    if details_sqe : 
        switch_page('sqe metrique')
    ###########################################################################################################    

    st.subheader('Budget')
    with stylable_container(key = 'metric_container',
                            css_styles = container_style, ) : 
        budg = st.container()
    budg.write("Actuals")
    budg.markdown(st.session_state.budg_metr, unsafe_allow_html=True)

    with stylable_container(key = 'Details_button', css_styles="""button{
                            background-color:#051650;
                            border: 1px solid #ffffff;
    }""")    :
        details_budg = st.button('Details', key = 'DETAILSBUDGET')
    
    if details_budg : 
        switch_page('budget metrique')
###########################################################################################################    

    st.subheader('CASID')

with col2 :
    st.subheader('Risk Management on Systemic Safety Topics')
    with stylable_container(key = 'metric_container',
                            css_styles = container_style, ) : 
        col21, col22 = st.columns(2)
    with col21 : 
        st.markdown('Assessement on time')
        st.markdown(f'<p style="font-family:Arial; color:Red; font-size: 30px;">44 %</p>', unsafe_allow_html=True)
        st.write('Acknowledgement on time')
        st.markdown(f'<p style="font-family:Arial; color:Green; font-size: 30px;">89 %</p>', unsafe_allow_html=True)

    with col22 : 
        st.write('Number of open SMS cases')
        st.markdown('<p style = "font-family:Arial; font-size: 30px;">34</p>', unsafe_allow_html= True)
        st.write('Sources of SMS cases')
        st.markdown(pd.DataFrame(np.array([['OCCURENCE', 2],['SARI', 10],['TEST', 4],['OTHERS', 3]]), columns = ['Source', 'Number']).style.hide(axis="index").to_html(), unsafe_allow_html=True)

with col3 :
    st.subheader('Assurance')
    st.subheader('Promotion')
    with stylable_container(key = 'metric_container',
                            css_styles = container_style, ) : 
        promo = st.container()
    promo.write("Number of promotions in the last 3 months")
    promo.markdown(st.session_state.promo, unsafe_allow_html=True)

    with stylable_container(key = 'Details_button', css_styles="""button{
                            background-color:#051650;
                            border: 1px solid #ffffff;
    }""")    :
        details_promo = st.button('Details', key = 'DETAILSPROMO')
    if details_promo :
        switch_page('promotion display')
    with stylable_container(key = 'metric_container',
                            css_styles = container_style, ) : 
        training = st.container()
    training.write("Trained safety reps")
    training.markdown(st.session_state.trained, unsafe_allow_html=True)

    with stylable_container(key = 'Details_button', css_styles="""button{
                            background-color:#051650;
                            border: 1px solid #ffffff;
    }""")    :
        details_training = st.button('Details', key = 'DETAILSTRAINING')
    if details_training :
        switch_page('network metrique')