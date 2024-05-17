import streamlit as st
from PIL import Image

st.title("prueba de sistemas")

image = Image.open('Sistema.jpg')
st.image(image)

st.write("A continuación, se te presentarán unas interacciones de ejemplo con botones y texto para que puedas testear algunas de las funciones que se verán mas adelante del proceso. ¡diviertete probando todo lo que quieras!") 


texto = st.text_input('Introduce cualquier texto', 'Escribir aqui')
st.write('El texto escrito es', texto)



  st.subheader("Primera prueba")
  st.write("prueba el uso de los siguientes botones")
  resp = st.checkbox('boton #1')
  resp2 = st.checkbox('boton #2')
  if resp:
    st.write('1 presionado')
  if resp2:
    st.write('2 presionado')


  st.subheader("Segunda prueba")
  modo = st.radio("¿Cual es tu función de entrada favorita de usar en interfaces multimodales?", ('Teclado y ratón', 'Escritura', 'Voz'))
  if modo == 'Teclado y ratón':
    st.write('Elegiste teclado y ratón')
  if modo == 'Escritura':
    st.write('Elegiste escritura')
  if modo == 'Voz':
    st.write('Elegiste voz')

st.subheader("Uso de Botones")
if st.button('prueba el botón'):
  st.write('botón listo')
else:
  st.write('botón no presionado')
