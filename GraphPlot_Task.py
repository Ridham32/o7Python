import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="PlotLy Graph",page_icon=":bar_chart:",layout="centered")

df = pd.read_csv("covid.csv")
st.subheader("DataSet:- Covid.csv")
st.write(df)
#1. Bar Graph
st.subheader("Bar Plot")
fig1=px.bar(df,x="Continent",y="TotalDeaths")
st.plotly_chart(fig1)

#2. Scatter Plot
st.subheader("Scatter Plot")
fig2=px.scatter(df,x="TotalCases",y="Serious,Critical")
st.plotly_chart(fig2)

#3. 
st.header("Pie Chart")
fig3 = px.pie(df,names="Continent",values="TotalRecovered",)
st.plotly_chart(fig3)

#4 Box Plot
st.header("Box Plot")
fig4=px.box(df,x="Country/Region",y="TotalDeaths")
st.plotly_chart(fig4)

#5 Histogram
st.header("Histogram")
fig5 = px.histogram(df,x="Country/Region",y="TotalRecovered")
st.plotly_chart(fig5)

#6 Line Graph
st.header("Line Graph")
fig6 = px.line(df,x="TotalCases",y="TotalDeaths")
st.plotly_chart(fig6)

#7 Violin Graph
st.header("Violin Graph")
fig7 =px.violin(df,x="Continent",y="TotalTests")
st.plotly_chart(fig7)

#8 choropleth
st.header("choropleth Graph")
fig8= px.choropleth(df,locations="iso_alpha",locationmode="ISO-3",hover_name="Country/Region",color="TotalCases",color_continuous_scale="Reds",title="TotalDeath by Country/Region")
st.plotly_chart(fig8)







