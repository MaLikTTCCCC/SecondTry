import streamlit as sl
sl.write("""fucking Hell""")
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     [1,2,4],
     columns=['a', 'b', 'c'])

sl.line_chart(chart_data)
