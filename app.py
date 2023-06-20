import datetime
import smtplib
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')


def send_email(message):
    # 配置发件人邮箱和SMTP服务器
    sender_email = "chang_lab@outlook.com"
    sender_password = "Abc12345678"
    smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587

    # 配置收件人邮箱和邮件内容
    recipient_email = "qdong8@wisc.edu"
    subject = "Primers order"
    message = message

    # 创建邮件对象
    email = MIMEMultipart()
    email["From"] = sender_email
    email["To"] = recipient_email
    email["Subject"] = subject

    # 添加邮件内容
    email.attach(MIMEText(message, "plain"))

    # 连接SMTP服务器并发送邮件
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, email.as_string())

    # 显示成功发送邮件的消息
    st.success("Email sent successfully!")

st.set_page_config(page_title="Primers order")
df = pd.read_csv('primers.csv')
st.title('Primers')
gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_selection(selection_mode='multiple', use_checkbox=True)
gridoptions = gd.build()

grid_table = AgGrid(df, gridOptions=gridoptions,
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
    if st.button("Send Email"):
        send_email(csv)