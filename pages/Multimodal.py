import streamlit as st
from PIL import Image

st.title("¿Qué es una interfaz multimodal?")
st.write("Las interfaces multimodales son sistemas de interacción múltiple que le permiten al usuario introducir algún tipo de información al sistema por medio de varios tipos de modos de entrada diferentes, ya sea por medio del ratón y teclado, habla, escritura manual, gestos, entre muchos otros tipos de entrada diferentes")

image = Image.open('interfaz.jpg')

st.image(image)
