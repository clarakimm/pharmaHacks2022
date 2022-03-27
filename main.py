import array
import streamlit as st
import numpy as np

#create page dropdown


page = st.selectbox("", ["welcome", "Patient Data input", "Prediction"])

#page = "Prediction"

if page == "welcome":
    st.write("Welcome to")
    title = '<p style="text-align: center; font-size:60px;">project_name</p>'
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
    

hgb = 0
ca = 0
b2m = 0
creat =0
alb =0
a_glob =0
b_glob =0
y_glob =0
prorate = 0
ost_les =0
ldh = 0   

if page == "Patient Data input":
    col1, col2 = st.columns(2)
    #Collect patient data & convert inputs into strings
    with col1:
        hgb = st.text_input("Hemoglobin level", value = "0", placeholder='0', key=0)
        ca = float(st.text_input("Calcium test",  value = "0", placeholder='0', key=1))
        b2m = float(st.text_input("β-2 Microglobulin test", value = "0", placeholder='0', key=2))
        creat = float(st.text_input("Creatinine level", value = "0", placeholder='0', key=3))
        alb = float(st.text_input("Albumin", value = "0", placeholder='0', key=4))
    with col2:
        a_glob = float(st.text_input("α_globulin", value = "0", placeholder='0', key=5))
        b_glob = float(st.text_input("β_globulin", value = "0", placeholder='0', key=6))
        y_glob = float(st.text_input("γ_globulin", value = "0", placeholder='0', key=7))
        prorate = float(st.text_input("Proteins rate", value = "0", placeholder='0', key=8))
        ost_les = float(st.text_input("Osteolytic lesions", value = "0", placeholder='0', key=9))
        ldh = float(st.text_input("Lactate dehydrogenase", value = "0", placeholder='0', key=10))

#store user data into an array
userdata = np.array([[hgb, ca, b2m, alb, a_glob, b_glob, y_glob, ost_les, ldh], [0,0,0,0,0,0,0,0,0]], np.int32)

#prediction function
#def predictor (arr):



if page == "Prediction":
    with st.container():

        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("50%")
            st.write("Similarity to _____ (type of Mulpitle Myeloma)")

        with col2:
            import matplotlib.pyplot as plt

            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            labels = 'yes', 'no'
            sizes = [50,50]
            #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            st.pyplot(fig1)

        with col3:
            # You can call any Streamlit command, including custom components:
            st.bar_chart(np.random.randn(50, 3))

        with st.container():
            st.write("Next Steps")
            st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
