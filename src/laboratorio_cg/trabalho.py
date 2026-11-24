
import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

# TEMA 1 - SATURAÇÃO
st.header("1. Saturação")

fator = st.slider("Saturação", 0.0, 2.0, 1.3)
s = hsv[:, :, 1].astype(float)
s = s * fator
s = np.clip(s, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 1] = s
saturada = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)

col1, col2 = st.columns(2)
col1.image(img, caption="Original")
col2.image(saturada, caption="Saturação alterada")


# TEMA 2 - BRILHO
st.header("2. Brilho")

fator = st.slider("Brilho", 0.0, 2.0, 0.8)
v = hsv[:, :, 2].astype(float)
v = v * fator
v = np.clip(v, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 2] = v
brilho = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)

col1, col2 = st.columns(2)
col1.image(img, caption="Original")
col2.image(brilho, caption="Brilho alterado")


# TEMA 3 - MATIZ GIRADA
st.header("3. Matiz girada")

giro = st.slider("Giro (graus)", 0, 360, 90)
h = hsv[:, :, 0].astype(int)
h = h + giro // 2
h = h % 180
hsv2 = hsv.copy()
hsv2[:, :, 0] = h
girada = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)

col1, col2 = st.columns(2)
col1.image(img, caption="Original")
col2.image(girada, caption="Matiz girada")


# TEMA 8 - NEGATIVO
st.header("8. Negativo")

negativo = 255 - img

col1, col2 = st.columns(2)
col1.image(img, caption="Original")
col2.image(negativo, caption="Negativo")


# TEMA 11 - ESPELHAMENTO
st.header("11. Espelhamento")

horizontal = img[:, ::-1]
vertical = img[::-1, :]

col1, col2 = st.columns(2)
col1.image(horizontal, caption="Espelhamento horizontal")
col2.image(vertical, caption="Espelhamento vertical")
