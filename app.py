import streamlit as st
st.write("""fucking Hell""")
import numpy as np
import pandas as pd
import yfinance as yf




#st.map(map_data)

msft=yf.Ticker('msft')
aapl=yf.Ticker('aapl')
meta=yf.Ticker('meta')
amzn=yf.Ticker('amzn')
nflx=yf.Ticker('nflx')

Rate=msft.actions

line=st.line_chart(Rate)
