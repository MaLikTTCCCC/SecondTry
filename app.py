import streamlit as sl
sl.write("""fucking Hell""")
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

sl.line_chart(chart_data)
