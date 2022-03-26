import streamlit as st
import numpy as np

#create page dropdown
page = st.sidebar.selectbox("pages", ["welcome", "Patient Data input", "Prediction"])

if page == "welcome":
    st.write("Welcome to")
    title = '<p style="font-family:Courier; color:Blue; font-size:20px;">Welcome to</p>'
    st.markdown(title, unsafe_allow_html=True)
    st.title("project_name")
    
   

elif page == "Patient Data input":
    st.title("yuhh")
        
elif page == "Prediction":
    st.title("yuhh againnn")