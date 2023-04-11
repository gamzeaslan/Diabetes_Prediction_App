#!/usr/bin/env python
# coding: utf-8

# In[4]:
"""
url=http://localhost:8501/
"""


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
        return 'Diyabet hastası değilsiniz'
    else:
        return 'Diyabet hastasısınız'

def main():
    st.title("Diyabet Hastalığı Tahmini")


    Pregnancies = st.text_input("Hamilelik Sayısı")
    Glucose = st.text_input("Glucose Değeri")
    BloodPressure = st.text_input("Kan Basıncı Değeri")
    Insulin = st.text_input("Insulin Değeri")
    BMI = st.text_input("BMI Değeri")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Değeri")
    Age = st.text_input("Yaş")

    diagnosis = ""
    if st.button("Diyabet Tahmin Sonucu"):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure,Insulin, BMI, DiabetesPedigreeFunction, Age])

    st.success(diagnosis)


if __name__ == '__main__':
    main() 


# In[ ]:




