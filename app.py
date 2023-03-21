# create a streamlit app that will take input for the model in te hackathon.ipynb file
# and display the output

import streamlit as st
import pandas as pd
import numpy as np
import pickle

#load the model from the pickle file
#model = pickle.load(open('model1.pkl','rb'))
pickle_in = open('classifierfinal.pkl', 'rb') 
classifier = pickle.load(pickle_in)


# create a function that will take the inputs from the user
def prediction(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity,
               phtype,phtubdiv, phcon,solidsph,
                            solidshardness, solidsconductivity,carbonsulfate,carbonchloromines,carbonesTrihalomethanes):
    
    # Making predictions 
    prediction = classifier.predict( [[ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity,
                                       phtype,phtubdiv, phcon,solidsph,
                            solidshardness, solidsconductivity,carbonsulfate,carbonchloromines,carbonesTrihalomethanes]])

    # set prediction whole number integer
    #prediction = int(prediction)
    if prediction == 0:
        pred = 'Safe to drink'
    elif prediction == 1:
        pred = 'Not safe to drink'
    else:
       pred = 'an error occured during prediction'
    return pred


# main function
#'ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity',
       #'Organic_carbon', 'Trihalomethanes', 'Turbidity',
def main():
    st.title('''WATER POTABILITY PREDICTION''')
    Ph = st.number_input('PH')
    Hardness = st.number_input('Hardness')
    Solids = st.number_input('Solids')
    Chloramines = st.number_input('Chloramines')
    Sulfate = st.number_input('Sulfate')
    Conductivity = st.number_input('Conductivity')
    Organic_carbon = st.number_input('Organic_carbon ')
    Trihalomethanes = st.number_input('Trihalomethanes')
    Turbidity = st.number_input('Turbidity')
    phtype = int(Ph/4)
    phtubdiv = abs(Ph - Turbidity)
    phcon = Ph/(Conductivity+0.0001)
    solidshardness = Solids/(Hardness+0.0001)
    solidsph = Ph/(Solids+0.00001)
    solidsconductivity = Solids/(Conductivity+0.00001)
    carbonsulfate = Organic_carbon/(Sulfate+0.00001)
    carbonchloromines = Organic_carbon/(Chloramines+0.00001)
    carbonesTrihalomethanes = Organic_carbon/(Trihalomethanes+0.00001)

    if st.button("Predict"): 
        result = prediction(Ph,Hardness,Solids, Sulfate,Chloramines,Conductivity,Organic_carbon,Trihalomethanes,Turbidity, phtype,phtubdiv, phcon,solidsph,
                            solidshardness, solidsconductivity,carbonsulfate,carbonchloromines,carbonesTrihalomethanes) 
        st.success('The water potability is  {}'.format(result))
       
        

if __name__ == '__main__':
    main()
from pyngrok import ngrok
 
public_url = ngrok.connect('8501')
public_url