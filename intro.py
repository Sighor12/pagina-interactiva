import streamlit as st
from PIL import Image

st.title("Página Principal")
st.write("bienvenido a esta página interactiva. Aqúi podras ver el uso de algunos sistemas de interacción multimodal para conocer más sobre sus usos y funciones, además de las ventajas que pueden ofrecer a largo plazo")

image = Image.open('saludo.jpg')

st.image(image, caption='bienvenida')
