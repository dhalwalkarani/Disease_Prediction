# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Disease Registry Prediction System',
                          
                          ['Diabetes Prediction',
                           'Cancer Prediction',
                           'Mental Health Prediction'],
                          icons=['activity','Alexa','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Gender = st.text_input('Gender (M / F)')
        
    with col2:
        Age = st.text_input('Age (Year)')
    
    with col3:
        Urea = st.text_input('Urea Level (mmol/L)')
    
    with col1:
        Cr = st.text_input('Creatine Level (mmol/L)')
    
    with col2:
        HbA1c = st.text_input('HbA1c Level (%)')
    
    with col3:
        Chol = st.text_input('Cholesterol Level (mmol/L)')
    
    with col1:
        TG = st.text_input('triGlyceride Level  (mmol/L)')
    
    with col2:
        HDL = st.text_input('HDL Level (mmol/L)')
        
    with col3:
        LDL = st.text_input('LDL Level (mmol/L)')

    with col1:
        VLDL = st.text_input('VLDL Level (mmol/L)')
    
    with col2:
        BMI = st.text_input('BMI Level')
        
    
    
    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[float(Age),float(Urea),float(Cr),float(HbA1c),float(Chol),float(TG),float(HDL),float(LDL),float(VLDL),float(BMI)]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)

 