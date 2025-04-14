import streamlit as st

st.title("Voice and Video")
a = st.audio_input("Record Voice")
if a:
    st.audio(a,loop=False)
    
b = st.video("5 Sacred Offerings Lord Shiva Loves! (2).mp4")