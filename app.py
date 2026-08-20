import streamlit as st
from PIL import Image

st.title ("Hola, yo soy ipardot")

st.header ("Mi comienzo con apps")
st.write ("Me gusta mucho la transmedia")
image = Image.open ('IMG_1036.jpeg')
st.image(image, caption = 'Representación mental de yo')

texto = st.text_input('Dime con quien andas', 'Aquí')
st.write('El texto escrito es', texto)

st.subheader ("Ahora usemos 2 Columnas")
col1, col2 = st. columns(2)
with col1:
  st.subheader!("£sta es la primera columna")
  st.write("las interfaces multimodales mejoran la experiencia de usuario") 
  resp = st. checkbox('Estoy de acuerdo')
  if resp: 
    st.irite("Correcto!")
    
with col2: 
  st.subheader("Esta es la segunda columna") 
  modo = st.radio("Que Modalidad es la principal en tu interfaz", ('Visual', 'auditiva', 'Táctil')) 
  if modo == "Visual':
     st.write('La vista es fundamental para tu interfaz') 
  if modo == 'auditiva':
     st.write('La audición es fundamental para tu interfaz') 
  if modo == 'Tácti'
     st.write('El tacto es fundamental para tu interfaz')


