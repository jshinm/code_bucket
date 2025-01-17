import numpy as np
import pandas as pd
import streamlit as st
import time

st.title('test project')

st_text = st.text('hello world')
time.sleep(1)
st_text.text('good bye')

st.subheader('subheading')
st.write(['data1', 'data2'])

values = np.random.rand(1,10)
st.bar_chart(values)

st.subheader('buttons')
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
st.write(df)

st.spinner(text='In progress...') #Temporarily displays a message while executing a block of code


st.subheader('progressive texts')

text_demo = """It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    """

field = ''
ta = st.empty()

button = st.button('start') #adds button; here the button is placed below the text_area

if button:
    for i in text_demo.split(' '):
        time.sleep(0.3)
        field += i + ' '
        ta.text_area('Text Field', field)