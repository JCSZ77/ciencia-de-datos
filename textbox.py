import streamlit as st

myname = st.text_input('Teclea tu nombre: ')

if (myname):
    print(f"Tu nombre es: {myname}")

