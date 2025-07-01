
import streamlit as st
import pandas as pd

# Load the data
@st.cache_data
def load_data():
    return pd.read_csv("ARR_Customer_Level_Changes.csv")

df = load_data()

st.title("ARR Waterfall Drill-Down")

# Sidebar filters
month = st.selectbox("Select Month", sorted(df["Month"].unique()))
change_type = st.selectbox("Select ARR Change Type", ["New", "Expansion", "Contraction", "Lost"])

# Filtered data
filtered_df = df[(df["Month"] == month) & (df["Change Type"] == change_type)]

st.metric(label=f"{change_type} ARR in {month}", value=f"${filtered_df['ARR Change'].sum():,.0f}")
st.dataframe(filtered_df.sort_values("ARR Change", ascending=False), use_container_width=True)
