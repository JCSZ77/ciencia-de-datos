import pandas as pd
import streamlit as st
names_link = 'https://github.com/JCSZ77/ciencia-de-datos/blob/main/movies.csv'
names_data = pd.read_csv(name_link)

#Create the title for the web app
st.title("Streamlit y pandas")

st.dataframe(names_data)