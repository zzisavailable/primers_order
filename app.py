import datetime
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder


def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')


df = pd.read_csv('primers.csv')
st.title('Primers')
gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_selection(selection_mode='multiple', use_checkbox=True)
gridoptions = gd.build()

grid_table = AgGrid(df, height=1200, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

st.sidebar.header('Order list')
selected_row = pd.DataFrame(grid_table["selected_rows"])

if len(selected_row) > 0:
    selected_row = selected_row.drop("_selectedRowNodeInfo", axis=1)

    st.sidebar.dataframe(selected_row)
    
    to_be_downloaded = selected_row.copy()
    to_be_downloaded['scale'] = '25nm'
    to_be_downloaded['Purification'] = 'STD'
    csv = convert_df(to_be_downloaded)
    
    st.sidebar.download_button(label="Download", data=csv, file_name='idt_order_{dt}.csv'.format(dt=datetime.date.today()), mime='text/csv')
