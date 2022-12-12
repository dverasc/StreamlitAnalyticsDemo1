import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import requests
from pandas import json_normalize
import json
plt.style.use('default')
st.title('Streamlit Interactive Analytics Demo')


symbol = st.text_input('Please enter the ticker symbol for the data you want to analyze', 'IBM')


# here we are using the api to grab the most likley symbols that a user is trying to search for
url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=' + symbol + '&apikey=LDGYT7FTCVVICA6X'
r = requests.get(url)
SEARCHdata = r.json()['bestMatches']

# use this native widget to show response data for user to make informed choice
st.json(SEARCHdata)

optionscount = len(SEARCHdata)


# create list of all the options and show them as choices in the radio widget
names = []
for record in SEARCHdata:
    opt = record['1. symbol']
#     print(opt)
    names.append(opt)

symbol1 = st.radio(
    "Which ticker symbol from the list would you like to use",
    (names))

# print(data)


# use the chosen symbol to call a different api for the actual data
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=' + symbol1 + '&apikey=LDGYT7FTCVVICA6X'
r = requests.get(url)
# data = r.json()

data = r.json()['Weekly Time Series']
df = pd.DataFrame(data)
# data
# df = json_normalize(data)

# little bit of data cleansing from response json and dataframe
df = df.transpose()
df.reset_index(inplace=True)
cols = df.columns.drop('index')
df[cols] = df[cols].apply(pd.to_numeric)


option = st.selectbox(
    'What data are you interested in',
    ('1. open', '2. high', '3. low', '4. close','5. volume'))


# plot the chosen data for the chosen company
fig1 = px.line(df, x = 'index', y = option, title='Weekly Stock Data')
st.plotly_chart(fig1, use_container_width=True)
