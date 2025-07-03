
import streamlit as st
import pandas as pd

# Load the data
@st.cache_data
def load_data():
    return pd.read_csv("ARR_Customer_Level_Changes.csv")

df = load_data()

st.title("ARR Waterfall Overview with Drill-Down")

# --- ARR Pivot Table ---
st.subheader("ARR Change Summary (Pivot Table)")

pivot_df = df.pivot_table(index='Change Type', columns='Month', values='ARR Change', aggfunc='sum', fill_value=0)
pivot_df = pivot_df.applymap(lambda x: f"${x:,.0f}")
st.dataframe(pivot_df, use_container_width=True)

# --- Drill-Down Section ---
st.subheader("Drill Down to Customer-Level Detail")

col1, col2 = st.columns(2)
with col1:
    selected_month = st.selectbox("Select Month", sorted(df["Month"].unique()))
with col2:
    selected_type = st.selectbox("Select ARR Change Type", df["Change Type"].unique())

filtered_df = df[(df["Month"] == selected_month) & (df["Change Type"] == selected_type)]

st.write(f"### {selected_type} ARR Detail – {selected_month}")
st.metric(label=f"Total {selected_type} ARR", value=f"${filtered_df['ARR Change'].sum():,.0f}")
st.dataframe(filtered_df.sort_values("ARR Change", ascending=False), use_container_width=True)
