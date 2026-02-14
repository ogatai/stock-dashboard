import streamlit as st
import pandas as pd

df = pd.read_csv("data/portfolio.csv")

st.title("ポートフォリオダッシュボード")
st.dataframe(df)

st.bar_chart(df.set_index("銘柄")["評価額"])
