import streamlit as st
import plotly.express as pt
import sqlite3



connection = sqlite3.connect('tempwebscraping/tempdata.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM temp")
rows = cursor.fetchall()
temps = [row[0] for row in rows]
date = [row[1] for row in rows]


figure = pt.line(x=date,y=temps)
st.plotly_chart(figure_or_data=figure)
