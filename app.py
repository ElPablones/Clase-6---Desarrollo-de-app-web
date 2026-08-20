import streamlit as st
from PIL import Image
st.title("Hola, mi nombre es Juan Pablo GQ")
image = Image.open('BobEsponja.png')
st.image(image, caption = 'Interfaces Multimodales')
texto = st.text_input('escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)


st.subheader("Ahora usemos dos columnas")
col1, col2 = st.columns(2)
with col1:
  st.sbheader("Esta es la primera columna")
  st.write("las interfaces multimodales mejoran la experiencia del usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('Correcto!')
with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que movilidad es la principal en tu interfaz", ('visual', 'auditiva', 'táctil'))
  if modo == 'visual':
    st.write('la vista es fundamental para tu intefaz')
  if modo == 'auditiva':
    st.write('la audición es fundamental para tu interfaz')
  if modo == 'táctil':
    st.write('el tacto es fundamental para tu interfaz')
