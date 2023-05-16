import streamlit as st
import pandas as pd

# create a dataframe
df = pd.DataFrame({
    "Name": ["John", "Jane", "Mike", "Sarah"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
})

# add checkboxes and buttons to the dataframe
# df["Select"] = [st.checkbox("", False, key=i) for i in range(len(df))]
df["Button"] = [st.button("Edit", key=i) for i in range(len(df))]

# display the dataframe with checkboxes and buttons
st.dataframe(df)