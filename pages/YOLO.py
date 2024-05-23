import cv2
import yolov5
import streamlit as st
import numpy as np
import pandas as pd
from ultralytics import YOLO
from PIL import Image

model = yolov5.load('yolov5s.pt')

model.conf = 0.25  
model.iou = 0.45  
model.agnostic = False  
model.multi_label = False  
model.max_det = 1000  

st.title("Sistema YOLO")
st.subheader("identificación de objetos en fotos o imágenes")
image = Image.open('YOLO uso.jpg')
st.image(image)


with st.sidebar:
            st.subheader('Parámetros de Configuración')
            model.iou= st.slider('Seleccione el IoU',0.0, 1.0)
            st.write('IOU:', model.iou)

with st.sidebar:
            model.conf = st.slider('Seleccione el Confidence',0.0, 1.0)
            st.write('Conf:', model.conf)

st.write("la siguiente interfaz es relacionada a YOLO (You Only Look Once), consiste en un sistema que puede detectar objetos dentro de una foto en tiempo real que utiliza una única red neuronal para dicha tarea. ¡Activa tu camara y ve por ti mismo como funciona!")
picture = st.camera_input("Capturar foto",label_visibility='visible' )

if picture:
    #st.image(picture)

    bytes_data = picture.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
  
    # perform inference
    results = model(cv2_img)

    # parse results
    predictions = results.pred[0]
    boxes = predictions[:, :4] 
    scores = predictions[:, 4]
    categories = predictions[:, 5]

    col1, col2 = st.columns(2)

    with col1:
        # show detection bounding boxes on image
        results.render()
        # show image with detections 
        st.image(cv2_img, channels = 'BGR')

    with col2:      

        # get label names
        label_names = model.names
        # count categories
        category_count = {}
        for category in categories:
            if category in category_count:
                category_count[category] += 1
            else:
                category_count[category] = 1        

        data = []        
        # print category counts and labels
        for category, count in category_count.items():
            label = label_names[int(category)]            
            data.append({"Categoría":label,"Cantidad":count})
        data2 =pd.DataFrame(data)
        
        # agrupar los datos por la columna "categoria" y sumar las cantidades
        df_sum = data2.groupby('Categoría')['Cantidad'].sum().reset_index() 
        df_sum
        
