import os
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from PIL import Image
import time
import glob

from gtts import gTTS
from googletrans import Translator

st.title("Voz a texto y traductor")
st.subheader("sistema para introducir texto por medio de voz y traducirlo")

image = Image.open('voz a texto y traductor.jpg')

st.image(image)

st.write("en esta sección podrás interactuar con el sistema de voz al decir algún tipo de frase que quieras pasar a texto. Además, si buscas saber su significado en otro idioma, puedes decidir que tipo de salida tendrá de los distintos idiomas cargados en el sistema. Pruebalo!")
