import paho.mqtt.client as paho
import time
import json
import streamlit as st
import cv2
import numpy as np
#from PIL import Image
from PIL import Image as Image, ImageOps as ImagOps
from keras.models import load_model

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

        


broker="broker.mqttdashboard.com"
port=1883
client1= paho.Client("Luis")
client1.on_message = on_message
client1.on_publish = on_publish
client1.connect(broker,port)

model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

st.title("Sistema MQTT")
st.write("este sistema está conectado con una página externa llamada Wokwi, la cual consiste en un simulador de sistemas embebidos físicos y su funcionamiento por medio de códigos. Este sistema funciona de forma que debes aparecer tu en la imagen y que debe quedar vacio el espacio detras tuyo. Debajo estará el link para ingresar al sistema de la página. ¡pruebalo como se ve!")

st.write("página wokwi: [link](https://wokwi.com/projects/396783658426730497)")

img_file_buffer = st.camera_input("Toma una Foto")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
   #To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    newsize = (224, 224)
    img = img.resize(newsize)
    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Normalize the image
    normalized_image_array = (img_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(prediction)
    if prediction[0][0]>0.5:
      st.header('Joven')
      client1.publish("EWAW","{'gesto': 'Persona'}",qos=0, retain=False)
      time.sleep(0.2)
    if prediction[0][1]>0.5:
      st.header('Vacio')
      client1.publish("EWAW","{'gesto': 'Nada'}",qos=0, retain=False)
      time.sleep(0.2)  
