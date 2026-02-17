import streamlit as st
import plotly.express as pt
import pandas as pd
import matplotlib


df = pd.read_csv('hapycountry/happy.csv')

st.title('in search for happiness')


xoption = st.selectbox('select the data for X-axis',options=('GDP','Happiness','Generosity'))

yoption = st.selectbox('select the data for Y-axis',options=('GDP','Happiness','Generosity'))

st.subheader(f"{xoption} AND {xoption}")

figure = pt.scatter(x=df[xoption.lower()],y=df[yoption.lower()],labels={'x':xoption,'y':yoption})

st.plotly_chart(figure_or_data=figure)