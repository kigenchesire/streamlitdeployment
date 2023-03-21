import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import numpy as np
st.set_page_config(layout="wide")
st.title("DataFrame Visualization")
df = pd.read_csv('water_potability.csv')

min_value = 1
max_value = len(df)
#age = st.slider('How old are you?', 0, max_value, 25)
values = st.slider(
     'Select a range of values',
     0, len(df), ( 0, len(df)))
value = np.asarray((values))
st.write('Range between:',value[0], value[1])
df2 = df.iloc[value[0]:value[1]]
st.dataframe(df2)