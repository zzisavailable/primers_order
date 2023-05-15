import streamlit as st
import pandas as pd


df = pd.read_csv('primers.csv')
st.dataframe(df)
