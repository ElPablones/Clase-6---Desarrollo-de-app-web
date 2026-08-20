import streamlit as st
from PIL import Image
st.title("Hola, mi nombre es Juan Pablo Guti Q")
image = Image.open('SpongeBob-and-Friends-vector-PNG.png')
st.image(image, caption = 'Interfaces Multimodales')
