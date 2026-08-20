import streamlit as st
from PIL import Image
st.title("Hola, mi nombre es Juan Pablo GQ")
image = Image.open('BobEsponja.png')
st.image(image, caption = 'Interfaces Multimodales')
