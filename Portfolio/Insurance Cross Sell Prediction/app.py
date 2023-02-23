# https://pythonspot.com/flask-web-app-with-python/

import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image


pickle_in = open("loan.pkl","rb")
classifier = pickle.load(pickle_in)


def predict(Age,AP,Vintage,Gender, DL,PI,VA1, VA2,VD):
	prediction=classifier.predict([[Age,AP,Vintage,Gender, DL,PI,VA1, VA2,VD]])	
	return prediction

def main():
	st.title("Health Insurance Cross sell Prediction")
	html_temp = """
	<div style="background-color: tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit Classification ML App </h2>
	</div>
        """
	
	st.markdown(html_temp, unsafe_allow_html=True)
	Age = st.number_input("Age")
	AP = st.number_input("Annual Premium")
	Vintage = st.number_input("Vintage")
	Gender = st.number_input("Gender(1-Male)")
	DL = st.number_input("Driving Licence")
	PI = st.number_input("Previously Insured")
	VA1 = st.number_input("Vehicle Age less than 1 year")
	VA2 = st.number_input("Vehicle Age greater than 1 year")
	VD = st.number_input("Vehicle Damage")

	result=""
	if st.button("Predict"):
		result=predict(Age,AP,Vintage,Gender, DL,PI,VA1, VA2,VD)
	st.success('The output is {}'.format(result))
	#if st.button("Interpret Results"):
	st.text("0 stands for the customer would not be interested in a vehicle loan")
	st.text("1 stands for the customer wil be interested in a vehicle loan")

if __name__ =='__main__':
	main()
