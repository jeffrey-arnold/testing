import streamlit as st

st.write('hello chud')

st.header('pee pee poo poo')

result = st.slider('hello!', 1, 5)
x = st.button('click to confirm')
if x:
    st.write(f'You chose {result}!')

st.subheader('hii')
