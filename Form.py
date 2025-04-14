import streamlit as st

st.title("Fill the From")

st.header("Fill the Form")
with st.form("The Form"):
        name = st.text_input("Enter Your Name")
        age = st.slider("Enter Your age",min_value=18,max_value=100)
        doB = st.date_input("Date of Birth")
        contact = st.number_input("Enter Your Contact Details")
        mail = st.text_input("Enter Your email",placeholder="abc@gmail.com")
        branch = st.selectbox("Enter Your branch",("Ece","Cse","IT","BCA","ME"))
        course = st.selectbox("Enter Your course",("Btech","BCA"))
        collegeName = st.text_input("Enter Your College Name")
        motherName = st.text_input("Mother's Name")
        fatherName = st.text_input("Father's Name")
        btn = st.form_submit_button("Submit")
        if btn:
            if name=="" or age=="" or contact=="":
                st.error("Fill all the details in the Form")
                st.stop()
            else:
                st.write("Name:",name)
                st.write("Age:",age)
                st.write("Contact:",contact)
                st.write("Email:",mail)
                st.write("DoB",doB)
                st.write("Branch",branch)
                st.write("Course",course)
                st.write("College Name",collegeName)
                st.write("Mother's Name",motherName)
                st.write("Father's Name",fatherName)
                st.success("Form Submitted") 
                st.page_link("pages/voice_video.py",label="Go to Voice and Video Page")
