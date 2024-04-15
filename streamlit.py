import streamlit as st
import pandas as pd
import numpy as np

###########################################################################################################
st.set_page_config(
     page_title = 'Home page',
     page_icon = '',
)
st.title('2024 SMS in 1 & DOA Objectives')
###########################################################################################################

try :
    obj_data = st.session_state.obj_data
except : 
    obj_data = pd.read_csv(r'data/Objectives 2024 - 1 & DOA - 2024 objective status EOY.csv', dtype = 'string',keep_default_na=False)

###########################################################################################################


obj_data.columns = ["Objective category","Source","#","Objective","KPI / Achievement criteria","Owners/ Applicability","Target date","Global Status","1","1A","1C","1G","1I","1P","1S","1T","1V","1Y","1Z","B","S","P","Q"]
filtered = st.multiselect("Filter columns", options=list(obj_data.columns), default=['Objective','Global Status']) 
st.write(obj_data[filtered])


###########################################################################################################
from datetime import datetime
import altair as alt
import socket

import google_auth_httplib2
import httplib2
import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import HttpRequest

socket.setdefaulttimeout(15 * 60)

SCOPE = "https://www.googleapis.com/auth/spreadsheets"
SPREADSHEET_ID = "1rkMVLvh3JrBq_tbi4Ho0qjCDAP3vYdNuWOEjYpkJLNU"
SHEET_NAME = "Database"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"


@st.experimental_singleton()
def connect():
    # Create a connection object.
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[SCOPE],
    )

    # Create a new Http() object for every request
    def build_request(http, *args, **kwargs):
        new_http = google_auth_httplib2.AuthorizedHttp(
            credentials, http=httplib2.Http()
        )
        return HttpRequest(new_http, *args, **kwargs)

    authorized_http = google_auth_httplib2.AuthorizedHttp(
        credentials, http=httplib2.Http()
    )
    service = build(
        "sheets",
        "v4",
        requestBuilder=build_request,
        http=authorized_http,
    )
    gsheet_connector = service.spreadsheets()
    return gsheet_connector


def collect(gsheet_connector) -> pd.DataFrame:
    values = (
        gsheet_connector.values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!A:C",
        )
        .execute()
    )

    df = pd.DataFrame(values["values"])
    df.columns = df.iloc[0]
    df = df[1:]
    return df


def insert(gsheet_connector, row) -> None:
    values = (
        gsheet_connector.values()
        .append(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{SHEET_NAME}!A:C",
            body=dict(values=row),
            valueInputOption="USER_ENTERED",
        )
        .execute()
    )


def get_chart(data):
    hover = alt.selection_single(
        fields=["date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="Evolution of stock prices")
        .mark_line()
        .encode(
            x="date",
            y="price",
            color="symbol",
            strokeDash="symbol",
        )
    )

    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)

    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x="date",
            y="price",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("date", title="Date"),
                alt.Tooltip("price", title="Price (USD)"),
            ],
        )
        .add_selection(hover)
    )

    return (lines + points + tooltips).interactive()

SCOPE = "https://www.googleapis.com/auth/spreadsheets"
SPREADSHEET_ID = "1rkMVLvh3JrBq_tbi4Ho0qjCDAP3vYdNuWOEjYpkJLNU"
SHEET_NAME = "Database"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"
COMMENT_TEMPLATE_MD = """{} - {}
> {}"""

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

conn = connect()
comments = collect(conn)

with st.expander("💬 Open comments"):

    # Show comments

    st.write("**Comments:**")

    for index, entry in enumerate(comments.itertuples()):
        st.markdown(COMMENT_TEMPLATE_MD.format(entry.name, entry.date, entry.comment))

        is_last = index == len(comments) - 1
        is_new = "just_posted" in st.session_state and is_last
        if is_new:
            st.success("☝️ Your comment was successfully posted.")

    space(2)

    # Insert comment

    st.write("**Add your own comment:**")
    form = st.form("comment")
    name = form.text_input("Name")
    comment = form.text_area("Comment")
    submit = form.form_submit_button("Add comment")

    if submit:
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        insert(conn, [[name, comment, date]])
        if "just_posted" not in st.session_state:
            st.session_state["just_posted"] = True
        st.experimental_rerun()