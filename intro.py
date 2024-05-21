import streamlit as st
from PIL import Image

st.title("¡Bienvenido!")
st.write("bienvenido a esta página interactiva. Aqúi podras ver el uso de algunos sistemas de interacción multimodal para conocer más sobre sus usos y funciones, además de las ventajas que pueden ofrecer a largo plazo")

image = Image.open('saludo.jpg')

st.image(image)

st.write("el objetivo de estas interfaces es para introducirte a como funcionan estos sistemas de varias formas y los diversos usos que pueden tener a largo plazo (en caso de que no hayas visto este tipo de sistemas antes)")
