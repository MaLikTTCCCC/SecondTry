import streamlit as st
st.write("""fucking Hell""")
import numpy as np
import pandas as pd
import yfinance as yf


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

#st.map(map_data)

msft=yf.Tickers('msft')
aapl=yf.Tickers('aapl')
meta=yf.Tickers('meta')
amzn=yf.Tickers('amzn')
nflx=yf.Tickers('nflx')

Rate=msft.actions

line=st.line_chart(Rate)
