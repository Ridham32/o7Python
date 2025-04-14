import streamlit as st
import pandas as pd

st.title("Hello!,Welcome")

with st.sidebar:
    st.write("Hello to My website 1")
name = st.text_input("Enter Your Name")
age = st.number_input(label="Enter Your Age",max_value=70,min_value=18)
number = st.number_input(label="Enter Your Contact Details",min_value=1000000000,max_value=9999999999)
email = st.text_input("Enter Your Email")
pic = st.camera_input("Click Your Photo")
btn = st.button("Submit")
if btn:
    if name=="" or age=="" or number=="":
        print("Fill all the details in the Form")
        st.stop()
    else:
        st.write("Name:",name)
        st.write("Age:",age)
        st.write("Contect:",number)
        st.write("Email:",email)
        st.image(pic)
st.caption("This is Caption")
df = pd.DataFrame({"Name":[name],"Age":[age]})
st.table(df)
st.dialog("Are u a student")
st.checkbox("Yes")
st.checkbox("No")

