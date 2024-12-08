import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache
def load_data():
    return pd.read_csv('../data/raw/benin-malanville.csv')

st.title("Dataset Dashboard")

st.sidebar.header("Filters")
date_range = st.sidebar.date_input("Select Date Range", [])

data = load_data()
if st.sidebar.checkbox("Show raw data"):
    st.write(data.head())

st.header("Solar Irradiance Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=data, x='Timestamp', y='GHI', label='GHI', ax=ax)
sns.lineplot(data=data, x='Timestamp', y='DNI', label='DNI', ax=ax)
sns.lineplot(data=data, x='Timestamp', y='DHI', label='DHI', ax=ax)
ax.set_title("GHI, DNI, DHI Trends")
ax.set_ylabel("Irradiance (W/m²)")
st.pyplot(fig)

