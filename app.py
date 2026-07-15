import streamlit as st

import pickle

with open('iris_model.pkl','rb') as file:
   model= pickle.load(file)

st.title('iris classification app')
st.write("used for iris classification")

sl= st.number_input(label="Enter sepal Length")
sw= st.number_input(label="Enter sepal width")
pl= st.number_input(label="Enter petal Length")
pw= st.number_input(label="Enter petal width")

if st.button("predict"):
   result=classifier.predict([[sl,sw,pl,pw]])
   st.success(result[0])