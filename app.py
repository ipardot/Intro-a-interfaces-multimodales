import streamlit as st
from PIL import Image

st.title ("Hola, yo soy ipardot")

st.header ("Mi comienzo con apps")
st.write ("Me gusta mucho la transmedia")
image = Image.open ('IMG_1036.jpeg')
st.image(image, caption = 'Representación mental de yo')
