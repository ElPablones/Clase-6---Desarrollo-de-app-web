import streamlit as st
from PIL import Image
st.title("Hola, mi nombre es Juan Pablo GQ")
image = Image.open('BobEsponja.png')
st.image(image, caption = 'Interfaces Multimodales')
texto = st.text_input('escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)
