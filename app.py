

import streamlit as st
import pandas as pd

# 创建一个示例DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'Age': [25, 30, 35]})

# 添加额外的列
df['Action'] = ""

# 显示DataFrame和按钮
for index, row in df.iterrows():
    # 添加按钮到每一行
    button_clicked = st.button("Action", key=index)
    if button_clicked:
        # 在按钮点击时执行的操作
        st.write("Button clicked for row:", index)

# 显示DataFrame
st.table(df)

