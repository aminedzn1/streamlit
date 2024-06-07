import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
     page_title = 'DOA Concern upload file',
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

st.title('DOA Concern follow-up file upload')
file = st.file_uploader('Upload .csv file')
if file is not None :
    df = pd.read_csv(file)

    df['Opening Date'] = pd.to_datetime(df['Opening Date'], dayfirst= True)
    df = df.loc[df['Opening Date'] >= pd.to_datetime('22/05/2023')]
    df2 = df[[
        'Opening Date',
        'Title',
        'T0\n (message sent to the DAN and the SMS Officer )',
        'T1 \n(Date of\nSystemic Safety Impact \nStatus Confirmation)',
        'Systemic Safety Impact\n\nYes / No', 
        'SMS Officer',
        'e-PPS Ref.\n(SMS or not SMS)',
        'T2 \n(Date of\nSystemic Safety Topic\nClosure)',
        'T0\n (message sent to the DAN and the SMS Officer ).1',
        'T1 \n(Date of\nSystemic Safety Impact \nStatus Confirmation).1',
        'Systemic Safety Impact\n\nYes / No.1',
        'SMS Officer.1',
        'e-PPS Ref.\n(SMS or not SMS).1',
        'T2 \n(Date of\nSystemic Safety Topic\nClosure).1'
        ]]

    cols2 = []
    for col in df2.columns :
        if col[len(col)-2] == '.' :
            cols2.append(col)

    for i in df2.index : 
        if type(df2.loc[i,'SMS Officer.1']) == float :
            df2.loc[i,'Systemic Safety Impact\n\nYes / No.1'] = 'N/A'
        else :
            if df2.loc[i,'Systemic Safety Impact\n\nYes / No.1'] != 'Yes' and df2.loc[i,'Systemic Safety Impact\n\nYes / No.1'] != 'No':
                df2.loc[i,'Systemic Safety Impact\n\nYes / No.1'] = 'Under review'

    for i in df2.index : 
        if df2.loc[i,'Systemic Safety Impact\n\nYes / No'] != 'Yes' and df2.loc[i,'Systemic Safety Impact\n\nYes / No'] != 'No':
                df2.loc[i,'Systemic Safety Impact\n\nYes / No'] = 'Under review'

    #st.bar_chart(df2['Systemic Safety Impact\n\nYes / No.1'].value_counts())
    #st.bar_chart(df2['Systemic Safety Impact\n\nYes / No'].value_counts())
    dfinal = df2[['Title', 'Systemic Safety Impact\n\nYes / No','SMS Officer','Systemic Safety Impact\n\nYes / No.1', 'SMS Officer.1']]
    st.write(dfinal.head())

