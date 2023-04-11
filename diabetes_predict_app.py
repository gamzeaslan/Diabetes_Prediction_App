#!/usr/bin/env python
# coding: utf-8

# In[4]:




# In[5]:


import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open("C:/Users/Gamze/diabetes_predict/diabetes_predict_model.sav","rb"))



def diabetes_prediction(input_data):
    input_data_as_narray = np.asarray(input_data)
    input_data_reshape = input_data_as_narray.reshape(1, -1)
    prediction = loaded_model[0].predict(input_data_reshape)
    print(prediction)


    if (prediction[0] == 0) :
        return 'You are not diabetic 😊'
    else:
        return 'You are diabetic.It is recommended that you see a doctor to be sure of this situation.'

def main():
    st.title("Diabetes Disease Prediction")


    Pregnancies = st.text_input("Number of Pregnancy")
    Glucose = st.text_input("Glucose Value")
    BloodPressure = st.text_input("Blood Pressure Value")
    Insulin = st.text_input("Insulin Value")
    BMI = st.text_input("BMI Value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    Age = st.text_input("Age")

    diagnosis = ""
    if st.button("Diabetes Prediction Result"):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure,Insulin, BMI, DiabetesPedigreeFunction, Age])

    st.success(diagnosis)


if __name__ == '__main__':
    main() 


# In[ ]:




