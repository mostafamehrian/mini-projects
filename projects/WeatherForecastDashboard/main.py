import streamlit as st
import plotly.express as pt
import pandas as pd
import matplotlib
from backend import getdata


df = pd.read_json('WeatherForecastDashboard/city.list.json.gz')


st.title('Weather Forecast Dashboard')

place = st.selectbox('select the place',options=df['name'].squeeze())

days = st.slider('days',min_value=1,max_value=5)

option = st.selectbox('select the data',options=('Temperture','Sky'))

st.subheader(f"{option} for the next {days} days in {place} ")

if option == 'Temperture':
    lsdays , lstemps = getdata(place=place,days=days,kind=option)
    figure = pt.line(x=lsdays,y=lstemps)
    st.plotly_chart(figure_or_data=figure)
elif option == 'Sky':
    lswethere , weatherdesclist = getdata(place=place,days=days,kind=option)
    imgpath = [f'WeatherForecastDashboard/images/{condition}.png' \
               for condition in lswethere] 
    st.image(imgpath,width=100,caption=weatherdesclist)