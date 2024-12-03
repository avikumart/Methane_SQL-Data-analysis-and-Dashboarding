import pandas as pd
import numpy as np
import streamlit as st

# set up a theme
st.set_page_config(page_title="Methane Emissions Dashboard", layout="wide")

# set a caching for the the streamlit items
@st.cache_data
def load_data(path):
    data = pd.read_csv(path)

# create streamlit chart dash UI 