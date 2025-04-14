import streamlit as st

st.title("Welcome To My Website2!")
st.header("About Website")
st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
btn1=st.button("Next")

if btn1:
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
    btn2 = st.button("Next")              

if btn2:
    st.header("Voice and Video")
    a = st.audio_input("Record Voice")
    if a:
        st.audio(a,loop=False)
    b = st.video("5 Sacred Offerings Lord Shiva Loves! (2).mp4")
