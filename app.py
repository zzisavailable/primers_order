import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


df = pd.read_csv('primers.csv')
AgGrid(df)

to_order_df = pd.DataFrame(columns=df.co)

name_list = df.iloc[:, 0].tolist()
selected_name = st.sidebar.selectbox('Select a primer name:', options=name_list)

selected_row = df.loc[df['Name'] == selected_name]

st.write(selected_row)
to_order_df.loc[len(to_order_df)] = {'Name': 'test'}

st.write(to_order_df)

