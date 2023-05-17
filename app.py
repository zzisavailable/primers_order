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

grid_table = AgGrid(df, height=800, gridOptions=gridoptions,
                    update_mode=GridUpdateMode.SELECTION_CHANGED)

    
st.sidebar.header('Order list')

new_name = st.text_input(label='Name: ')
new_seq = st.text_input(label='Sequence: ')
if st.button('Add'):
    if new_name == '' or new_seq == '':
        st.info('Please enter the name and sequence first.')
    else:
        new_item = {'Name': new_name, 'Sequence': new_seq}
        df.loc[len(df)] = new_item
        with open('primers.csv', 'w', encoding='utf-8') as f:
            f.write(f'\n{new_name}, {new_seq}')

selected_row = pd.DataFrame(grid_table["selected_rows"])

if len(selected_row) > 0:
    selected_row = selected_row.drop("_selectedRowNodeInfo", axis=1)

    st.sidebar.dataframe(selected_row)
    
    to_be_downloaded = selected_row.copy()
    to_be_downloaded['scale'] = '25nm'
    to_be_downloaded['Purification'] = 'STD'
    csv = convert_df(to_be_downloaded)
    
    st.sidebar.download_button(label="Download", data=csv, file_name='idt_order_{dt}.csv'.format(dt=datetime.date.today()), mime='text/csv')
