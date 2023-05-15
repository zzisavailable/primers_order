import streamlit as st
import pandas as pd
# from st_aggrid import AgGrid


df = pd.read_csv('primers.csv')
st.dataframe(df)

to_order_df = pd.DataFrame(columns=df.columns)

name_list = df.iloc[:, 0].tolist()
selected_name = st.sidebar.selectbox(name_list)

selected_row = df.loc[df['Name'] == selected_name]
to_order_df.append(selected_row)

st.write(to_order_df)

