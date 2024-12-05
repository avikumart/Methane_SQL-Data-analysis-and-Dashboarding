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
    st.text("Methane emission sources")
    st.bar_chart(data, x="type", y="count", color="#fc2c03",
                x_label="Emission sources", y_label="Count of sources")
    
# emissions by region
def region_by_emissions(data):
    df = data.groupby("region")["emissions"].mean().reset_index()
    st.text("Emissions by regions of the world")
    st.area_chart(df, x="region", y="emissions",
                color="#d9ce38")
    

# top emissions segment
def segment_of_emissions(data):
    x = "segment"
    y = "ave_emissions"
    y1 = "total_emisssions"
    st.text("Average emissions by segment")
    st.bar_chart(data, x="segment", y=y, color="#45fc03",
                x_label="Segment of emissions", y_label="Average emissions")
    st.text("Total emissions by segment")
    st.bar_chart(data, x="segment", y=y1, color="#039dfc")

# reason for emissions
def reasons(data):
    df = data.groupby("reason")["emissions"].mean().reset_index()
    st.text("Methane emissions by reasons")
    st.bar_chart(df, x="reason", y="emissions" , color="#45fc03",
                x_label="Reasons of emissions", y_label="Average emissions")


# top10 emittors
def top10_emittors(data):
    st.text("Total emissions by country")
    st.bar_chart(data, x="country", y="total_emissions", color="#fc2c03",
                x_label="Country", y_label="Total emissions")
    
# load the data and develop the streamlit UI
df1 = load_data("Data analysis CSVs/emissions_sources.csv")
df2 = load_data("Data analysis CSVs/methan_new.csv")
df3 = load_data("Data analysis CSVs/top emissions segment.csv")
df4 = load_data("Data analysis CSVs/Top10_emittors.csv")

st.logo(image="Images/streamlit-mark-color.png")

with st.sidebar:
    st.title("Methane Emisssions Dashboard")
    st.subheader("Description of the dashboard")

    st.caption("""This is a demo dashboard project is developed using PostgreSQL DB, SQL, and Python language
            to analyze and visualize Methane emissions responsible for rising temperature and climate
            change events""")

st.header("Methane Emissions Dashboard")

# put a 4 charts in column by column manner
col1, col2 = st.columns(2)

with col1:
    emissions_sources(df1)
    region_by_emissions(df2)
    
with col2:
    segment_of_emissions(df3)

col3, col4 = st.columns(2)

with col3:
    reasons(df2)
    
with col4:
    top10_emittors(df4)

with st.expander("Display the dataframes"):
    st.text("Emission sources dataframe")
    st.dataframe(df1)

    st.text("Top emisssions segment")
    st.dataframe(df3)

    st.text("Top10 emittors")
    st.dataframe(df4)

    st.text("Editable emissions dataframe")
    st.data_editor(df2)


