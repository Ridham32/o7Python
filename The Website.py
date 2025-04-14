import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "home"

def go_to_page(page):
    st.session_state.page = page

if st.session_state.page == "home":
    st.title("Welcome To My Website!")
    st.header("About Website")
    st.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

    if st.button("Next"):
        go_to_page("Form")

elif st.session_state.page == "form":
    st.header("Fill the Form")
    with st.form("The Form"):
        name = st.text_input("Enter Your Name")
        age = st.slider("Enter Your age", min_value=18, max_value=100)
        dob = st.date_input("Date of Birth")
        contact = st.number_input("Enter Your Contact Details")
        mail = st.text_input("Enter Your email", placeholder="abc@gmail.com")
        branch = st.selectbox("Enter Your branch", ("ECE", "CSE", "IT", "BCA", "ME"))
        course = st.selectbox("Enter Your course", ("B.Tech", "BCA"))
        collegeName = st.text_input("Enter Your College Name")
        motherName = st.text_input("Mother's Name")
        fatherName = st.text_input("Father's Name")
        btn = st.form_submit_button("Submit")

    if btn:
            if name == "" or contact == "":
                st.error("Fill all the details in the Form")
            else:
                st.success("Form Submitted")
                if st.button("Next"):
                    go_to_page("Voice_Video")

elif st.session_state.page == "Voice_Video":
    st.header("Voice and Video")
    a = st.audio_input("Record Voice")
    if a:
        st.audio(a, loop=False)

    b = st.video("5 Sacred Offerings Lord Shiva Loves! (2).mp4")

    if st.button("Back"):
        go_to_page("form")
