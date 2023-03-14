# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 18:18:46 2023

@author: Sarah Ahmed
"""

import numpy as np
import pickle
import streamlit as st

model = pickle.load(open('cancerdiseaseprediction.sav', 'rb'))


#prediction function

def cancer_prediction(data_input):
    

#converting input to numpy array easier for reshaping
 
    input_numpy= np.asarray(data_input)

#reshaping array helps make prediction for one value not all the 251 values
#tells ML model that prediction is for one 

    reshape_input = input_numpy.reshape(1,-1)

    predictionsystem =model.predict(reshape_input)
    print(predictionsystem)

    if (predictionsystem[0] == 0):
      return 'CONGRATULATIONS! you do not have cancer'
    else:
      return 'unfortunately you have cancer , it is advised you book an appointment with an oncologist in the app immediately for fast treatment'
  
    
  
def main():
    

    st.title('welcome to MediHelp cancer Prediction')
    
    Age = st.text_input('enter your age')
    Gender = st.text_input(' enter your gender , Male = 1 , Female = 2')
    GeneticRisk = st.text_input('enter your level of genetic risk 1 to 7 , 7 being the highest genetic risk ')
    chronicLungDisease = st.text_input('enter your level of chronic lung disease 1 to 7 , 7 being highest chronic lung disease')
    Obesity = st.text_input('enter your your level of obesity 1 to 7 , 7 being highest obesity')
    PassiveSmoker = st.text_input('enter your level of passive smoking from 1 to 8 , 8 being highest passive smoking')
    ChestPain = st.text_input('enter your level of chest pain 1 to 9 , 9 being the highest chest pain')
    CoughingofBlood =st.text_input('enter your level of coughing blood 1 to 9 , 9 being the highest of coughing blood')
    Fatigue = st.text_input('enter your level of fatigue 1 to 9 , 9 being the highest fatigue')
    WeightLoss = st.text_input('enter your level of weightloss 1 to 8 , 8 being the highest weight loss')
    DryCough= st.text_input('enter your dry coughing value 1 to 7 , 7 being the highest dry coughing value')



    diagnosebyML = ''
    
    # prediction button
    
    if st.button('cancer prediction Test Result'):
           diagnosebyML = cancer_prediction([  Age, Gender, GeneticRisk, chronicLungDisease,Obesity , PassiveSmoker, ChestPain, CoughingofBlood , Fatigue, WeightLoss, DryCough ])
           
           
    st.success(diagnosebyML)
       
    
    
if __name__ == '__main__':
    main()