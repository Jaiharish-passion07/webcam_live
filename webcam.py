import cv2
import streamlit as st

st.title("webcam")
run=st.checkbox("run")
frame_window=st.image([])
cam=cv2.VideoCapture(0)
while run:
    ret,frame=cam.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame_window.image(frame)

else:
    st.write("stopped")