
import streamlit as st
import numpy as np

st.title("Atividade 2 - Bandeira da França")

st.write("Bandeira criada utilizando matrizes NumPy.")

largura = 300
altura = 200

# Cria uma imagem RGB
img = np.zeros((altura, largura, 3), dtype=np.uint8)

# Faixa azul
img[:, 0:100] = [0, 35, 149]

# Faixa branca
img[:, 100:200] = [255, 255, 255]

# Faixa vermelha
img[:, 200:300] = [237, 41, 57]

# Exibe a bandeira
st.image(img, caption="Bandeira da França", width=450)
