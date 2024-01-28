# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/ضيف الله/Downloads/SVC_i_model.sav', 'rb'))

def diabetes (input_data):
    #input_data = (1,85,66,29,0,26.6,0.351,30)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction == 0):
        return('The person is not diabetic')
    else:
        return('The person is diabetic')
    
    return(prediction)   
def main():
    
      # the name of the websit
    st.title('Diabetes Prediction Web App')

    Pregnancies = st.number_input('Enter the number of pregnancies: ',step=1,placeholder="Type a number...")
    Glucose = st.number_input('Enter the glucose level: ',step=1,placeholder="Type a number...")
    BloodPressure = st.number_input('Enter the blood pressure: ',step=1,placeholder="Type a number...")
    SkinThickness = st.number_input('Enter the skin thickness: ',step=1,placeholder="Type a number...")
    Insulin = st.number_input('Enter the insulin level: ',step=1,placeholder="Type a number...")
    BMI = st.number_input('Enter the BMI: ',step=1,placeholder="Type a number...")
    DiabetesPedigreeFunction = st.number_input('Enter the diabetes pedigree function: ',step=1,placeholder="Type a number...")
    Age = st.number_input('Enter the age: ',step=1,placeholder="Type a number...") 
    
    #code for pediction
    dignosis = ''
    # creating a button for perdiction
    if st.button('Diabetes test Result'):
        dignosis = diabetes([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

            

    st.success(dignosis)

if __name__ == '__main__':
    main()