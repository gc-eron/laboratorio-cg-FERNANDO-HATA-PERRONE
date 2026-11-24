
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


# TEMA 4 - TONS DE CINZA
st.header("4. Tons de cinza")

r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)

soma = r + g + b
media = (soma / 3).astype(np.uint8)

peso_r = st.slider("Peso do vermelho", 0.0, 1.0, 0.30)
peso_g = st.slider("Peso do verde", 0.0, 1.0, 0.59)
peso_b = st.slider("Peso do azul", 0.0, 1.0, 0.11)

total = peso_r + peso_g + peso_b

if total == 0:
    total = 1

ponderada = peso_r * r + peso_g * g + peso_b * b
ponderada = (ponderada / total).astype(np.uint8)

col1, col2 = st.columns(2)
col1.image(media, caption="Média simples")
col2.image(ponderada, caption="Média ponderada")


# TEMA 10 - NEGATIVO NUMA REGIÃO
st.header("10. Negativo numa região")

altura, largura = img.shape[0], img.shape[1]

t = st.slider("Tamanho do quadrado", 10, largura // 2, largura // 3)
y = st.slider("Posição vertical", 0, altura - t, altura // 4)
x = st.slider("Posição horizontal", 0, largura - t, largura // 4)

nova = img.copy()
regiao = nova[y:y + t, x:x + t]
negativo = 255 - regiao
nova[y:y + t, x:x + t] = negativo

col1, col2 = st.columns(2)
col1.image(img, caption="Original")
col2.image(nova, caption="Negativo na região")


# TEMA 11 - ESPELHAMENTO
st.header("11. Espelhamento")

horizontal = img[:, ::-1]
vertical = img[::-1, :]

col1, col2 = st.columns(2)
col1.image(horizontal, caption="Espelhamento horizontal")
col2.image(vertical, caption="Espelhamento vertical")


# TEMA 16 - GRANULADO
st.header("16. Granulado")

intensidade = st.slider("Intensidade do granulado", 0, 100, 40)

ruido = np.random.randint(
    -intensidade, intensidade + 1, img.shape, dtype=np.int16
)

resultado = img.astype(np.int16) + ruido
resultado = np.clip(resultado, 0, 255)
granulada = resultado.astype(np.uint8)

col1, col2 = st.columns(2)
col1.image(img, caption="Original")
col2.image(granulada, caption="Imagem granulada")
