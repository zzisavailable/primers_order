import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder



df = pd.read_csv('primers.csv')
gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_selection(selection_mode='multiple', use_checkbox=True)
gridoptions = gd.build()

grid_table = AgGrid(df, height=800, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

st.write('To order')
selected_row = grid_table["selected_rows"]
if len(selected_row) > 0:
    st.sidebar.write(len(selected_row))
    st.sidebar.write(selected_row.columns)
    st.sidebar.dataframe(selected_row)
    st.sidebar.button(label='Download')