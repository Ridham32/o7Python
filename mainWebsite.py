import streamlit as st
with st.sidebar:
    btn1 = st.button("About")
    btn2 = st.button("Form")
if btn1:
    st.header("About MyWebsite",divider="orange",anchor=False)
    with st.container():
        st.text("This is about the Website")
if btn2:
    st.header("Fill the Form")
    with st.form("Personal Details"):
        st.text("Personal Details")
        name = st.text_input("Name")
        papaName = st.text_input("Father's Name")
        mamaName = st.text_input("Mother's Name")
        contact = st.text_input("Mobile No.")
        if contact:
            if contact.isdigit():
                doB = st.date_input("DoB")
                age = st.number_input("Age")
                btn3 = st.form_submit_button("Save")
    with st.form("Educational Details"):
        st.text("Educational Details")
        college = st.text_input("College Name")
        course = st.selectbox("Course",("Select","CSE","ECE","IT","BCA","ME","CE"))
        passingYear = st.selectbox("Passing Year",("2025","2026","2027","2028"))
        cgpa = st.number_input("CGPA")
        btn4 = st.form_submit_button("Save")
    







        
