import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
plt.style.use('default')
st.title('Streamlit Analytics Demo')


first_file = st.file_uploader('Select the stock data file (IBM weekly default provided)')
if first_file is not None:
   df1 = pd.read_csv(first_file,index_col='Date',parse_dates=True)
else:
    df1 = pd.read_csv('/Users/diegoveras/StreamlitAnalyticsDemo/DefaultValues/weekly_IBM.csv')

fig1 = px.line(df1, x = 'timestamp', y = 'open', title='Weekly Stock Data')
fig2 = px.line(df1, x = 'timestamp', y = 'high', title='Weekly Stock Data')
fig3 = px.line(df1, x = 'timestamp', y = 'low', title='Weekly Stock Data')
fig4 = px.line(df1, x = 'timestamp', y = 'close', title='Weekly Stock Data')
fig5 = px.line(df1, x = 'timestamp', y = 'volume', title='Weekly Stock Data')


st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)
st.plotly_chart(fig4, use_container_width=True)
st.plotly_chart(fig5, use_container_width=True)