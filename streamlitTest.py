import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


#Data Upload
st.subheader("Data Uploading")
dataUpload = st.file_uploader("Upload the file here")
df =pd.read_csv(dataUpload)
st.dataframe(df)
st.write("DataFrame format of uploaded file")
st.write(df)

st.write("Mean,Median,Max,Min in the dataframe")
st.write(df.describe())

#Select Columns and Provide Charts
st.subheader("Data Visualization")
clm = df.columns
with st.form("Data Visualization"):
    x_axis=st.selectbox("Select the x-axis",clm)
    y_axis= st.selectbox("Select the y-axis",clm)
    chart_type = st.selectbox("Select chart Type",("Bar Plot","Scatter Plot"))
    btn = st.form_submit_button("Submit")

if btn:
    ax =plt.subplot()
    if chart_type=="Bar Plot":
        plt.figure(figsize=(8,6))
        st.bar_chart(df,x=x_axis,y=y_axis)
        plt.title("BarPlot")
        plt.show()
    elif chart_type=="Scatter Plot":
        plt.figure(figsize=(8,6))
        st.scatter_chart(df,x=x_axis,y=y_axis)
        plt.title("ScatterPlot")
        plt.show()

#Filter the data as per user choice

st.subheader("Data Filtering")
filter_col = st.selectbox("Select column to filter", clm)
unique_values = df[filter_col].unique()
filter_value = st.selectbox("Select value", unique_values)
filtered_df = df[df[filter_col] == filter_value]
st.dataframe(filtered_df)


#Download the filter data
st.subheader("Download The Filtered Data")
st.download_button("Download here",filtered_df.to_csv(),"filtered_data.csv")






