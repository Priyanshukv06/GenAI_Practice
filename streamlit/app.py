import streamlit as st
import pandas as pd
import numpy as np

##Title of application
st.title('Hello Priyanshu')


##Display simple text
st.write("My age is 20.")

##Create a dataframe
df=pd.DataFrame(
    {
        'first column':[1,2,3,4],
        'second column':[10,20,40,70]
    }
)

##Display the dataframe
st.write("Here is the required dataframe")
st.write(df)

##create a linechart
chart_data=pd.DataFrame(
    np.random.randn(10,4),columns=['a','b','c','d']
)
st.line_chart(chart_data)

