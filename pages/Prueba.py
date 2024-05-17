import streamlit as st
from PIL import Image

st.title("prueba de sistemas")
st.write("A continuación, se te presentarán unas interacciones de ejemplo con botones y texto para que puedas testear algunas de las funciones que se verán mas adelante del proceso. ¡diviertete probando todo lo que quieras!") 

image = Image.open('Sistema.jpg')

st.image(image)
