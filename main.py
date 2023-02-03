import streamlit as st
import yfinance as yf
st.write("""
# Simple stock Price app 
Shown are the stock closing price and volume of Google 
""")
# define thi ticker symbol
tickerSymbol = "GOOGL"
# app data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')
# Open High Low Close Volume Dividends Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
