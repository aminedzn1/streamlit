import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.stylable_container import stylable_container 
from streamlit_extras.switch_page_button import switch_page
import plotly.express as px 
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

st.title("1 (& DOA ?) SMS Cockpit")
container_style = """
{   
    z-index : 0;
    background-color: #171717;
    border: 1px solid #373737;
    border-radius : 10px;
    padding-left:40px;
    padding-bottom:40px;
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
    st.session_state.obj_acc = f'<p style="font-weight: 900; font-family:system-ui; color:rgb(255,102,102); font-size: 40px;">{value} %</p>'

elif value > 50 and value < 85 :
    st.session_state.obj_acc = f'<p style="font-weight: 900; font-family:system-ui; color:rgb(255,166,77); font-size: 40px;">{value} %</p>'

elif value > 85 and value <= 100 :
    st.session_state.obj_acc = f'<p style="font-weight: 900; font-family:system-ui; color:rgb(0,230,115); font-size: 40px;">{value} %</p>'


value = round(array_filled.mean()*100, 2)
if value < 50 :
    st.session_state.obj_fil = f'<p style="font-weight: 900; font-family:system-ui; color:rgb(255,102,102); font-size: 40px;">{value} %</p>'

elif value > 50 and value < 85 :
    st.session_state.obj_fil = f'<p style="font-weight: 900; font-family:system-ui; color:rgb(255,166,77); font-size: 40px;">{value}  %</p>'

elif value > 85 and value <= 100 :
    st.session_state.obj_fil = f'<p style="font-weight: 900; font-family:system-ui; color:rgb(0,230,115); font-size: 40px;">{value} %</p>'
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
<p style ="font-weight: 900; font-family:system-ui; font-size:40px; color: White;">{y_evo[month]} k€ \n</p>
<p style ="font-weight: 900; font-family:system-ui; font-size:20px; color: rgb(255,166,77);">Overspend of {delta} k€</p>
"""
elif delta > tol :
    text = f"""
<p style ="font-weight: 900; font-family:system-ui; font-size:40px; color: White;">{y_evo[month]} k€ \n</p>
<p style ="font-weight: 900; font-family:system-ui; font-size:20px; color: rgb(255,102,102);">Underspend of {delta} k€</p>
"""
else :
    if delta > 0 :
        text = f"""
    <p style ="font-weight: 900; font-family:system-ui; font-size:40px; color: White;">{y_evo[month]} k€ \n</p>
    <p style ="font-weight: 900; font-family:system-ui; font-size:20px; color: rgb(0,230,115);">Underspend of {delta} k€</p>
    """
    else :
        text = f"""
    <p style ="font-weight: 900; font-family:system-ui; font-size:40px; color: White;">{y_evo[month]} k€ \n</p>
    <p style ="font-weight: 900; font-family:system-ui; font-size:20px; color: rgb(0,230,115);">Overspend of {delta} k€</p>
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
        sqe_data.loc[i,'color'] = 'rgb(0,230,115)'
    elif sqe_data.loc[i,'SQE Active?'] == 'Y' and sqe_data.loc[i, 'dateAlert'] == 1 :
        sqe_data.loc[i,'color'] = 'rgb(255,166,77)'
    else :
        sqe_data.loc[i,'color'] = 'rgb(255,102,102)'
############################################################################################################

sqe_count_domain = sqe_data[['Domain/Function', 'activeBool']].groupby(['Domain/Function']).sum()
sqe_count_domain['color'] = ''
for func in sqe_count_domain.index :
    vColor = list(sqe_data.loc[sqe_data['Domain/Function'] == func]['color'])
    if 'rgb(0,230,115)' in vColor :
        sqe_count_domain.loc[func,'color'] = 'rgb(0,230,115)'
    elif 'rgb(230,184,0)' in vColor :
        sqe_count_domain.loc[func,'color'] = 'rgb(230,184,0)'
    else : 
        sqe_count_domain.loc[func,'color'] = 'rgb(255,102,102)'

sqe_number = sum(np.array(sqe_count_domain['activeBool']) > 0)
domain_number = len(sqe_count_domain['activeBool'])

value = f"{sqe_number}/{domain_number}"

if 'rgb(255,102,102)' in list(sqe_count_domain['color']) :
    st.session_state.sqe_kpi = f'<p style="font-weight: 900; font-family:system-ui; color:rgb(255,102,102); font-size: 40px;">{value}</p>'
elif 'rgb(255,166,77)' in list(sqe_count_domain['color'])  :
    st.session_state.sqe_kpi = f'<p style="font-weight: 900; font-family:system-ui; color:rgb(255,166,77); font-size: 40px;">{value}</p>'
else : 
    st.session_state.sqe_kpi = f'<p style="font-weight: 900; font-family:system-ui; color:rgb(0,230,115); font-size: 40px;">{value}</p>'
###########################################################################################################
###########################################################################################################
#PROMO
promo = pd.read_csv(r'data/Engineering SMS Promotion Follow-up - Safety Briefing, Training, Hub.csv')
promo['Date'] = pd.to_datetime(promo['Date'], dayfirst=True,format='mixed')
troismois = pd.Timestamp.today() - pd.DateOffset(months = 3)
promo = promo.loc[promo['Date']>troismois]

value  = len(list(promo['Date']))
text =f"<p style = 'font-weight: 900; font-family:system-ui; font-size:40px; color:White;'>{value}</p>"
st.session_state.promo = text
###########################################################################################################
###########################################################################################################
#TRAINED
network_data = pd.read_csv(r'data/Network Contact list - SMS contact.csv')
value = round(np.mean(network_data['Trained'] == 'Yes')*100, 2)
text = f"<p style = 'font-weight: 900; font-family:system-ui;color:rgb(255,166,77);font-size: 40px;'>{value} %</p>"
st.session_state.trained = text
###########################################################################################################
###########################################################################################################
#DAHSBOARD
button_style = """button{
                            background-color:#171717;
                            opacity: 0;
                            padding-top: 40%; 
                            position: absolute;
                            top: 0;
                            left: 0;
                            z-index : 1;
                            margin : 0;
                            float: none;
                            border: 1px solid white;
    }"""
st.session_state.button_style = button_style
col1, col2, col3 = st.columns([1,2,1])

with col1:
    totobj = st.container()
    with totobj :
        st.subheader('Objectives')
        with stylable_container(key = 'Details_button', css_styles= button_style)    :
            details_obj = st.button('Details', use_container_width= True, key = "DETAILSOBJETS")
        if details_obj : 
            switch_page('objectives metriques')
        
        with stylable_container(key = 'metric_container',
                                css_styles = container_style, ) :
            objectives = st.container()
    #    col11, col12 = objectives.columns(2)
    #    with col11 :
    #        st.write('Accomplished')
    #        st.markdown(st.session_state.obj_acc, unsafe_allow_html= True)

    #    with col12 :
    #        st.write('Filled')
    #        st.markdown(st.session_state.obj_fil, unsafe_allow_html= True)
        objectives.markdown('<p style = "font-size : 40px;">TBD<p>', unsafe_allow_html=True)

    
###########################################################################################################    
    totsqe = st.container()
    with totsqe :
        st.subheader('SQE')
        with stylable_container(key = 'Details_button', css_styles= button_style)    :
            details_sqe = st.button('Details', key = 'DETAILSSQE', use_container_width= True)
        
        with stylable_container(key = 'metric_container',
                                css_styles = container_style, ) :
            sqe = st.container()
        sqe.markdown('<p style = "font-weight: bold; font-size: 20px;">Domain / Function with Active SQE</p>', unsafe_allow_html=True)
        try :    
            sqe.markdown(st.session_state.sqe_kpi, unsafe_allow_html=True)
        except :
            with open('data/sqe_kpi.txt') as f :
                st.session_state.sqe_kpi = f.read()
            sqe.markdown(st.session_state.sqe_kpi, unsafe_allow_html=True)

        if details_sqe : 
            switch_page('sqe metrique')
    ###########################################################################################################    

    st.subheader('Budget')    
    with stylable_container(key = 'Details_button', css_styles=button_style)    :
        details_budg = st.button('Details', key = 'DETAILSBUDGET', use_container_width=True)
    
    with stylable_container(key = 'metric_container',
                            css_styles = container_style, ) : 
        budg = st.container()
    budg.markdown("<p style = 'font-weight: bold; font-size: 20px;'>Actuals</p>", unsafe_allow_html=True)
    budg.markdown(st.session_state.budg_metr, unsafe_allow_html=True)


    if details_budg : 
        switch_page('budget metrique')
###########################################################################################################    

    st.subheader('CASID')
    with stylable_container(key = 'Details_button', css_styles=button_style)    :
        details_budg = st.button('Details', key = 'DETAILSCASID', use_container_width=True)
    
    with stylable_container(key = 'metric_container',
                            css_styles = container_style, ) : 
        cas1, cas2, cas3 = st.columns(3)
    cas1.markdown("<p style = 'font-weight: bold; font-size: 20px;'>On Time</p>", unsafe_allow_html=True)
    cas1.markdown('<p style = "font-weight: 900; font-family: system-ui; color: rgb(0,230,115); font-size: 40px;">12</p>', unsafe_allow_html=True)
    cas2.markdown("<p style = 'font-weight: bold; font-size: 20px;'>At Risk</p>", unsafe_allow_html=True)
    cas2.markdown('<p style = "font-weight: 900; font-family: system-ui; color: rgb(255,166,77); font-size: 40px;">1</p>', unsafe_allow_html=True)
    cas3.markdown("<p style = 'font-weight: bold; font-size: 20px;'>Late</p>", unsafe_allow_html=True)
    cas3.markdown('<p style = "font-weight: 900; font-family: system-ui; color: rgb(255,102,102); font-size: 40px;">3</p>', unsafe_allow_html=True)


    if details_budg : 
        switch_page('casid metrique')
###########################################################################################################    

with col2 :
    st.subheader('Risk Management on Systemic Safety Topics')
    with stylable_container(key = 'metric_container',
                            css_styles = container_style, ) : 
        col21, col22 = st.columns(2)
    with col21 : 
        st.markdown("<p style = 'font-weight: bold; font-size: 20px;'>Assessement On Time</p>", unsafe_allow_html=True)
        st.markdown(f'<p style="font-weight: 900; font-family:system-ui; color:rgb(255,102,102); font-size: 40px;">44 %</p>', unsafe_allow_html=True)
        st.markdown("<p style = 'font-weight: bold; font-size: 20px;'>Acknowledgement On Time</p>", unsafe_allow_html=True)
        st.markdown(f'<p style="font-weight: 900; font-family:system-ui; color:rgb(0,230,115); font-size: 40px;">89 %</p>', unsafe_allow_html=True)

    with col22 : 
        st.markdown("<p style = 'font-weight: bold; font-size: 20px;'>Number Of SMS Cases</p>", unsafe_allow_html=True)
        st.markdown('<p style = "font-weight: 900; font-family:system-ui; font-size: 40px;">34</p>', unsafe_allow_html= True)
        st.markdown("<p style = 'font-weight: bold; font-size: 20px;'>Sources Of SMS Cases</p>", unsafe_allow_html=True)
        fig = px.pie(pd.DataFrame(np.array([['OCCURENCE', 2],['SARI', 10],['TEST', 4],['OTHERS', 3]]), columns = ['Source', 'Number']), values= 'Number', names='Source',hole = .6,color_discrete_sequence=px.colors.sequential.Blues_r)
        fig.update_layout(height = 100, margin=dict(l=0,r=0,b=0,t=0,pad=0),plot_bgcolor = 'rgba(0, 0, 0, 0)',paper_bgcolor= 'rgba(0, 0, 0, 0)')
        fig.update_traces(textinfo='value')
        st.plotly_chart(fig, use_container_width=True)
    st.subheader('Assurance')
    with stylable_container(key = 'metric_container',
                            css_styles = container_style, ) : 
        col21b, col22b = st.columns(2)
    with col21b : 
        st.markdown("<p style = 'font-weight: bold; font-size: 20px;'>Deployment</p>", unsafe_allow_html=True)
        st.markdown(f'<p style="font-weight: 900; font-family:system-ui; color:white; font-size: 40px;">44 %</p>', unsafe_allow_html=True)
        st.markdown("<p style = 'font-weight: bold; font-size: 20px;'>DOA Score Card</p>", unsafe_allow_html=True)
        st.markdown(f'<p style="font-weight: 900; font-family:system-ui; color:rgb(0,230,115); font-size: 50px;">⬤</p>', unsafe_allow_html=True)
    with col22b :
        st.markdown("<p style = 'font-weight: bold; font-size: 20px;'>Number of EASA Findings On Time</p>", unsafe_allow_html=True)
        st.markdown(f'<p style="font-weight: 900; font-family:system-ui; color:rgb(0,230,115); font-size: 40px;">1/1</p>', unsafe_allow_html=True)
        st.markdown('Number of Internal findings on time')
        st.markdown(f'<p style="font-weight: 900; font-family:system-ui; color:rgb(255,166,77); font-size: 40px;">2/3</p>', unsafe_allow_html=True)
with col3 :
    st.subheader('Promotion')

    with stylable_container(key = 'Details_button', css_styles=button_style)    :
        details_promo = st.button('Details', key = 'DETAILSPROMO', use_container_width=True)
    
    with stylable_container(key = 'metric_container',
                            css_styles = container_style, ) : 
        promo = st.container()
    promo.markdown(f'<p style="font-weight: bold; font-family:system-ui; font-size: 20px;">Number Of Promotions In The Last Three Months</p>', unsafe_allow_html=True)
    promo.markdown(st.session_state.promo, unsafe_allow_html=True)


    if details_promo :
        switch_page('promotion display')
    with stylable_container(key = 'Details_button', css_styles=button_style)    :
        details_training = st.button('Details', key = 'DETAILSTRAINING', use_container_width=True)
    with stylable_container(key = 'metric_container',
                            css_styles = container_style, ) : 
        training = st.container()
    training.markdown(f'<p style="font-weight: bold; font-family:system-ui; font-size: 20px;">Trained Safety Reps</p>', unsafe_allow_html=True)
    training.markdown(st.session_state.trained, unsafe_allow_html=True)


    if details_training :
        switch_page('network metrique')