import streamlit as st
from PIL import Image


with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

print(camera_image)

img = Image.open(camera_image)

gray_image = img.convert("L")
st.image(gray_image)