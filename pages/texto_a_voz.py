import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image

st.title("Texto a voz")

try:
  os.mkdir("temp")
except:
  pass

  st.write("Pasemos ahora una frase cualquiera de texto a voz. Escribe abajo en el espacio en blanco que quieras que se convierta en una salida de audio en español.")
