'''
The Data Incubator 12-day program milestone project app
Author: Bilal Assaad [ba17]
Date: 31 December 2021
'''

# Python 3.9.7 64-bit
# 'ba-mlstn':conda env on Win10 P51s machine
# Final working .py file as of 1/1/22 11:00 PM

# Raw Package
import numpy as np
import pandas as pd

# Data Source
import yfinance as yf

# Data Visualization
import plotly.graph_objs as go

# Web App Creation
import streamlit as st

# Added ssl and unverified context to make this work in local windows machine using ba-mlstn conda env
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Market data list
market_list = ["Cryptocurrencies", "Stocks"]

# Sample crypto pairs data list
cryptoPair_list = ["BTC-USD", "ETH-USD", "BNB-USD", "SOL-USD", "DOGE-USD"]

# Comprehensive stock ticker list retrieved from wikipedia and stored as list
stockTable = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
stockTicker_df = stockTable[0]['Symbol']
stockTicker_list = stockTicker_df.sort_values().to_list()

# Start of Streamlit Web Page
st.set_page_config(layout="wide")

# Add sidebar to the app
st.sidebar.markdown("## My TDI Milestone App")
st.sidebar.markdown(
    """
    Welcome to my first app.
    This app is built using Streamlit and uses YFinance data of Cryptocurrencies and Stocks to plot historical **candlestick** price fluctuations to date.
    I hope you enjoy!
    """)

st.title('TDI 12-day Milestone Assignment (Day 10)')
st.write('Bilal Assaad [ba17] | 12/31/2021')

market = st.selectbox('Select - Market:', market_list)

if market == "Cryptocurrencies":
    ticker = st.selectbox('Select - Crypto Pair Symbol', cryptoPair_list)

if market == "Stocks":
    ticker = st.selectbox('Select - Stock Ticker Symbol', stockTicker_list)

# Retrieval of data timeframe from present to past by X time
tPeriod_list = ["1d", "1mo", "3mo", "6mo",
                "1y", "5y", "10y", "ytd", "max"]
tPeriod = st.selectbox('Select - Retrieve Past Data Timeframe', tPeriod_list)

# Select candle bar time interval
interval_list = ["30m", "1h", "1d", "1wk"]
interval = st.selectbox('Select - Candle Bar Interval', interval_list)

# Retrieve stock/crypto data using yahoo finance library
yf_data = yf.download(tickers=ticker, period=tPeriod, interval=interval)

# Declare plotting of chart/figure
fig = go.Figure()

# Show button to plot chart
if st.button('Show Chart'):
    st.write("Chart of **" + ticker + "** plotted")

    # Candlestick plot
    fig.add_trace(go.Candlestick(x=yf_data.index,
                                 open=yf_data['Open'],
                                 high=yf_data['High'],
                                 low=yf_data['Low'],
                                 close=yf_data['Close'], name='market data'))

    # Add titles
    fig.update_layout(
        title=go.layout.Title(
            text=f"Price History of {ticker} to Date <br><sup>Timeframe {tPeriod} | Candle Interval {interval}</sup>",
            xref="paper",
            x=0),
        yaxis_title="USD $",
        height=900,
        width=1500
    )

    # Show plot
    st.plotly_chart(fig)
    st.write("** TO THE MOOOOOON!!! ** 🚀🌝")
