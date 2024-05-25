import streamlit as st
st.write("""fucking Hell""")
import numpy as np
import pandas as pd
import yfinance as yf




#st.map(map_data)

msft = yf.download("msft", start="2020-01-01", end="2021-01-01")
aapl=yf.download("aapl", start="2020-01-01", end="2021-01-01")
meta=yf.download("meta", start="2020-01-01", end="2021-01-01")
amzn=yf.download("amzn", start="2020-01-01", end="2021-01-01")
nflx=yf.download("nflx", start="2020-01-01", end="2021-01-01")



#line=st.line_chart(Rate[0:1])
#msft['Close'].plot()
st.pyplot(aapl.plot.barh(stacked=True).figure)

