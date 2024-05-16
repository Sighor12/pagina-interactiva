import streamlit as st
from PIL import Image

st.title("¡Bienvenido!")
st.write("en esta página podrá ver el funcionamiento de diversos sistemas que cumplen una función similar de diversas formas, ya sea por medio de la voz, reconocimiento facial, lectura de pdf, interacción y manejo de sistemas digitales y reales juntos, entre otras cosas mas. ¡Sige explorando estos nuevos sistemas!") 

image = Image.open('sistema.jpg')

st.image(image, caption='Sistema')
