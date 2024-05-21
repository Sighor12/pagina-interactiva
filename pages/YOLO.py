import cv2
import yolov5
import streamlit as st
import numpy as np
import pandas as pd
from ultralytics import YOLO

model = yolov5.load('yolov5s.pt')

model.conf = 0.25  
model.iou = 0.45  
model.agnostic = False  
model.multi_label = False  
model.max_det = 1000

st.title("Sistema YOLO")
