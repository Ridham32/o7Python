import pandas as pd
import streamlit as st
import pickle
from sklearn.metrics import accuracy_score
acc=pickle.load(open("acc.pkl","rb"))
m = pickle.load(open("model1.pkl","rb"))
st.set_page_config(page_title="Heart Disease Predictor",page_icon=":heart:")
st.title("Heart Disease Predictor")
prediction = 0

with st.form("Person's Details"):
    age = st.number_input("Age",min_value=25,max_value=100)
    sex = st.selectbox("Sex(1:Male,0:Female)",[1,0])
    cp = st.radio("cp",[0,1,2,3])
    trestbps = st.number_input("trestbps")
    chol = st.number_input("chol")
    fbs = st.radio("fbs",[0,1])
    restecg = st.radio("restecg",[0,1,2])
    thalach = st.number_input("thalach",min_value=70,max_value=220)
    exang = st.radio("exang",[0,1])
    oldpeak = st.slider("oldpeak",min_value=0.0,max_value=10.0,step= 0.1)
    slope = st.radio("slope",[0,1,2])
    ca = st.radio("ca",[0,1,2,3,4])
    thal = st.radio("thal",[0,1,2,3])
    btn = st.form_submit_button("Submit")
    df = pd.DataFrame([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

if btn:
    prediction = m.predict(df)
    st.success("submitted")
    if prediction == 1:
        st.write("Risk Of Heart Disease Detected")
        st.write(f"Model Accuracy: {acc * 100:.2f}%")
        
    elif prediction == 0:
        st.write("No Risk Of Heart Disease Detected")
        st.write(f"Model Accuracy: {acc*100:.2f}%")
    


    


