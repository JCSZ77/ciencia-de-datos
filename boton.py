import streamlit as st

myname = st.text_input('Introducir nombre :')
if st.button('Búsqueda'):
    st.write(f"Nombre de búsqueda : {myname}")

st.write("by Juan")