import array
import streamlit as st
import numpy as np
import backend
from PIL import Image

image = Image.open('logo.png')

st.image(image)


#necessary functions
def myeloma_type (numb):
    """function that takes output from ML model & provides the corresponding multiple myeloma stage"""
    if (numb[0] ==0):
        return "No recognizable signs of multiple myeloma"
    if (numb[0]==1):
        return "Stage 1 multiple myeloma"
    if (numb[0] ==2):
        return "Stage 2 multiple myeloma"
    if (numb[0] ==3):
        return "Stage 3 multiple myeloma"
    else:
        return "ERROR"

#prediction function
def predictor (arr):
    return backend.model.predict(arr)


#front-end components
#create page dropdown
page = st.selectbox("", ["welcome", "Fill Patient Data input"])


#welcome page
if page == "welcome":
    st.write("Welcome to")
    title = '<p style="text-align: center; font-size:60px;">MyeHealth</p>'
    st.markdown(title, unsafe_allow_html=True)
    st.title(" ")
    subtext = '<p style="text-align: center; font-size:15px;">harnessing the power of machine learning to aid in the diagnosis of multiple myeloma</p>'
    st.markdown(subtext, unsafe_allow_html=True)
    #st.write("harnessing the power of machine learning to aid in the diagnosis of multiple myeloma")
    #testing = st.button("\enter2")
    #if st.button("Enter2"):
        #page = "Patient Data input"
       #st.write("yuhp")

    col1, col2, col3 , col4, col5, col6, col7 = st.columns(7)

    with col1: pass
    with col2: pass
    with col3: pass
    with col4: 
        center_button = st.button('Enter')
    with col5:pass
    with col6:pass
    with col7:pass
    
    title2 = '<p style="text-align: center; font-size:15px;">DISCLAIMER:</p>'
    st.markdown(title2, unsafe_allow_html=True)
    subtext2 = '<p style="text-align: center; font-size:15px;">This application should only be used to supplement diagnosis decision making. It cannot and should not be used for official diagnosis purposes</p>'
    st.markdown(subtext2, unsafe_allow_html=True)
    
#initialize input variables first
hgb = 0
ca = 0
b2m = 0
alb =0
a_glob =0
b_glob =0
y_glob =0
ost_les = 0
ldh = 0  

#Patient Data input page
if page == "Fill Patient Data input":
    col1, col2 = st.columns(2)
    #Collect patient data & convert inputs into strings
    with col1:
        hgb = float(st.text_input("Hemoglobin level(g/dL)", value = "0", placeholder='0', key=0))
        ca = float(st.text_input("Calcium test(mg/L)",  value = "0", placeholder='0', key=1))
        b2m = float(st.text_input("β-2 Microglobulin test(mg/L)", value = "0", placeholder='0', key=2))
        #creat = float(st.text_input("Creatinine level", value = "0", placeholder='0', key=3))
        alb = float(st.text_input("Albumin(g/L)", value = "0", placeholder='0', key=4))
        a_glob = float(st.text_input("α_globulin(g/L)", value = "0", placeholder='0', key=5))

    with col2:
        b_glob = float(st.text_input("β_globulin(g/L)", value = "0", placeholder='0', key=6))
        y_glob = float(st.text_input("γ_globulin(g/L)", value = "0", placeholder='0', key=7))
        #prorate = float(st.text_input("Proteins rate", value = "0", placeholder='0', key=8))
        ost_les = float(st.text_input("Osteolytic lesions(0 for false, 1 for true)", value = "0", placeholder='0', key=9))
        ldh = float(st.text_input("Lactate dehydrogenase(U/L)", value = "0", placeholder='0', key=10))

        userData = np.array([[hgb, ca, b2m, alb, a_glob, b_glob, y_glob, ost_les, ldh], [0,0,0,0,0,0,0,0,0]], np.int32)
        button = st.button("Calculate")
        if(button):
            st.write("Patient likely has")
            st.header(myeloma_type(predictor(userData)))
        
    
    with st.container():

        col1, col2 = st.columns(2)


        with col1:
            st.write("This machine learning model is")
            percent = 100 * backend.score
            format_float = "{:.2f}".format(percent)
            st.header(format_float)
            st.header("\% accurate")
           
            
            

        with col2:
            st.write("Next Steps")
            st.write("Further diagnosis tests or begin treatment options right away depending on disease severity.")



        



