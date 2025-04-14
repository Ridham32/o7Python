import streamlit as st
from streamlit_option_menu import option_menu
import db1
import pandas as pd
from streamlit_lottie import st_lottie
import requests
import base64
##### Lottie Animation #####
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
lottie_url = "https://lottie.host/f2740528-f42d-4748-9948-0b12c2b5688c/wpP9eWIYNS.json"
lottie_json = load_lottie_url(lottie_url)

col1,col2 = st.columns([1,10])
#### form formation ####

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Register","Login","All Data","Update","Delete"],
        icons =["clipboard","key","list-task","pencil","trash"],
        )
def get_base64(image_file):
    with open(image_file, "rb") as file:
        return base64.b64encode(file.read()).decode()
def set_background(image_path):
    base64_str = get_base64(image_path)
    css = f"""
    <style>
    .stApp {{
    background-image: url("data:image/png;base64,{base64_str}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    }}
    """
    st.markdown(css, unsafe_allow_html=True)


set_background("bkgfake.JPG")

###### CREATE ######

############SignUp###############
if selected == "Register":
    with st.form("SignUp Form"):
        with col1:
            st_lottie(lottie_json,speed=1,width=70,height=80,key="lottie",)
        with col2:
            st.header("Sign Up")
        name = st.text_input("Enter Name")
        email = st.text_input("Enter Email")
        password = st.text_input("Password",type="password")
        gender = st.selectbox("Gender",("Male","Female"))
        age = st.slider("Age",max_value=18,min_value=100)
        btn = st.form_submit_button("Submit")

    if btn:
        if name=="" or email=="" or password=="" or gender=="" or age=="" :
            st.error("Please fill the form")
        else:
            data = (name,email,password,gender,age)
            db1.reg(data)

##########LogIn##########
elif selected =="Login":
    st.title("LogIn Form")
    with st.form("LogIn Form"):
        email = st.text_input("Enter Your Email")
        password = st.text_input("Enter the Password",type='password')
        btn = st.form_submit_button("LogIn")
    if btn:
        if email=="" or password=="":
            st.error('Please fill all the credentials')
        else:
            data=(email,password)
            res = db1.login(data)
            if res:
                st.success("Welcome Back")
            else:
                st.error("Invalid Credentials")

##### READ #####
elif selected == "All Data":
    res= db1.all_data()
    df=pd.DataFrame(res,columns=["id","name","email","password","gender","age"])
    st.dataframe(df)

##### UPDATE #####

elif selected=="Update":
    a = st.number_input("Enter Id")
    res=db1.readone(a)
    if res:
        with st.form("EditFrom"):
            name = st.text_input("Name",value=res[1])
            email = st.text_input("Email",value=res[2])
            password = st.text_input("Password",type="password",value=res[3])
            gender = st.selectbox("Gender",["Male","Female"],index=["Male","Female"].index(res[4]))
            age = st.slider("Age",value=res[5])

            btn = st.form_submit_button("Save Changes")
        if btn:
            if name=="" or email=="" or password=="" or gender=="" or age=="":
                st.error("Please fill all the details")
            else:
                data =(name,email,password,gender,age,a)
                result = db1.update(data)
                if result:
                    st.success("Data Updated :white_check_mark:")
                else:
                    st.error("Error")


#### DELETE ####

elif selected =="Delete":
    id = st.number_input("Enter id")
    btn = st.button("Delete")
    if btn:
        delet = db1.delete(id)
        print(delet)
        if delet:
            st.success("Deleted Sucessfully")
        else:
            st.error("Error")



