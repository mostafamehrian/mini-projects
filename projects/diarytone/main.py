import streamlit as st
import plotly.express as pt
from backend import analyze

st.title('Diary Tone')

st.subheader('Positivity')
data = analyze()
posdata = [] 
for value in data.values():
    posdata.append(value['pos'])
Posdatels = []
for value in data.keys():
    Posdatels.append(value)
Positfigure = pt.line(x=Posdatels,y=posdata)
st.plotly_chart(figure_or_data=Positfigure)

st.subheader('Negativity')
Negdata = [] 
for value in data.values():
    Negdata.append(value['neg'])
Negdatels = []
for value in data.keys():
    Negdatels.append(value)
Negativfigure = pt.line(x=Negdatels,y=Negdata)
st.plotly_chart(figure_or_data=Negativfigure)