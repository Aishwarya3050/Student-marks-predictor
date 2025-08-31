import streamlit as st
import pickle
import warnings
warnings.filterwarnings('ignore')


st.title("Student Marks Predictor")
sh=st.number_input("Enter Study Hours")
btn=st.button("Predict")


if btn:
    if sh<=12:
        model=pickle.load(open("smp.pkl","rb"))
        res=model.predict([[sh]])[0][0].round(2)
        st.success(f"Predicted Marks : {res}")
    else:
        st.warning("Invalid Input")