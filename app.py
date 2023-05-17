import datetime
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
selected_row = pd.DataFrame(grid_table["selected_rows"])#.drop("_selectedRowNodeInfo")
st.sidebar.write(selected_row.columns)

if len(selected_row) > 0:

    st.sidebar.dataframe(selected_row)
    
    to_be_downloaded = selected_row.copy()
    to_be_downloaded['scale'] = '25nm'
    to_be_downloaded['Purification'] = 'STD'
    csv = to_be_downloaded.to_csv(f'idt_order_{datetime.date.today()}.csv', index=False)
    
    st.download_button(label="Download", data=csv, file_name=f'idt_order_{datetime.date.today()}.csv', mime='text/csv')
