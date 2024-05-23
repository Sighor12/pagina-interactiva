import streamlit as st
from PIL import Image

st.title("gracias por participar")
st.subheader("nos vemos pronto")
image = Image.open('Despedida.jpg')
st.image(image)

st.write("muchas gracias por navegar por medio de estas interfaces, espero que hayas aprendido sobre el uso y funcionamiento de algunas interfaces multimodales que fueron diseñadas aquí. ¡Animate a descubrir más interfaces y sistemas con varias funciones y metodos de entrada! Nos vemos :D")
