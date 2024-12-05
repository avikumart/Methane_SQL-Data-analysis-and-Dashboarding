import pandas as pd
import numpy as np
import streamlit as st

# set up a theme
st.set_page_config(page_title="Methane Emissions Dashboard", layout="wide")

# set a caching for the the streamlit items
@st.cache_data
def load_data(path):
    data = pd.read_csv(path)
    return data

# create streamlit chart dash UI 
def emissions_sources(data):
    st.bar_chart(data, x=data["type"], y=data["count"], color="red",
                x_label="Emission sources", y_label="Count of sources")
    

# top emissions segment
def segment_of_emissions(data):
    x = data["segment"]
    y = data["ave_emissions"]
    y1 = data["total_emissions"]
    st.bar_chart(data, x=data["segment"], y=y, color="green",
                x_label="Segment of emissions", y_label="Emissions in Kt")
    st.bar_chart(data, x=data["segment"], y=y1, color="blue")

# reason for emissions
def reasons(data):
    df = data.groupby("reason").count()
    df = df.reset_index()
    st.bar_chart(df, x=df["count"], y=df["reason"], color="green",
                x_label="Count of reasons", y_label="Reasons")


# top10 emittors
def top10_emittors(data):
    df = data.drop(index=0, inplace=0)
    st.bar_chart(df, x=df["country"], y=df["total_emissions"], color="red",
                x_label="Country", y_label="Total emissions")
    
# load the data and develop the streamlit UI
df1 = load_data("Data analysis CSVs/emissions_sources.csv")
df2 = load_data("Data analysis CSVs/reasons of emissions.csv")
df3 = load_data("Data analysis CSVs/top emissions segment.csv")
df4 = load_data("Data analysis CSVs/Top10_emittors.csv")

with st.sidebar:
    st.title("Methane Emisssions Dashboard")
    st.title("Description of the dashboard")

    st.caption("""This is a demo dashboard project using PostgreSQL DB, SQL, and Python language
               to analyze and visualize Methane emissions responsible for rising temperature and climate
               change events""")

st.header("Methane Emissions Dashboard")

# put a 4 charts in column by column manner
col1, col2 = st.columns(2)

with col1:
    emissions_sources(df1)
    
with col2:
    segment_of_emissions(df2)

col3, col4 = st.columns(2)

with col3:
    reasons(df3)
    
with col4:
    top10_emittors(df4)

with st.expander("Display the dataframes"):
    st.text("Emission sources dataframe")
    st.dataframe(df1)


