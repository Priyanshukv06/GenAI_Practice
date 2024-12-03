import streamlit as st
import pandas as pd

st.title('Streamlit text input')

first_name=st.text_input('Enter your first name')
second_name=st.text_input('Enter your second name')
if first_name and second_name:
    st.write(f"Hello {first_name,second_name}")

age=st.slider('Select your age',0,100,25)
st.write('your age is ',age)


options = ['SDE','ML','AI','WEB DEV','CRYPTO']
choice=st.selectbox('Choose your favorite stream ',options)
st.write("You selected",choice)


uploaded_file=st.file_uploader("choose a csv file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
