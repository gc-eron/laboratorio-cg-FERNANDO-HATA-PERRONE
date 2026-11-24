from pathlib import Path

import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Atividade 5 - HSV")

# Carregar a fotografia da Atividade 4
pasta_projeto = Path(__file__).resolve().parents[2]
caminho_foto = pasta_projeto / "imagens" / "foto.jpg"

foto = Image.open(caminho_foto).convert("RGB")
img = np.array(foto)

# CHECKPOINT 1 - HSV
st.header("1. HSV")

col1, col2 = st.columns(2)

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

col1.image(img, caption="Fotografia original")

so_h = hsv.copy()
so_h[:, :, 1] = 255
so_h[:, :, 2] = 255

col2.image(
    cv2.cvtColor(so_h, cv2.COLOR_HSV2RGB),
    caption="Canal H"
)

# CHECKPOINT 2 - Mudando o HSV
st.header("2. Mudando o HSV")

col1, col2 = st.columns(2)

# Saturação
fator_s = col1.slider("Saturação", 0.0, 2.0, 1.5)

s = hsv[:, :, 1].astype(float)
s = np.clip(s * fator_s, 0, 255)

hsv_s = hsv.copy()
hsv_s[:, :, 1] = s

col1.image(
    cv2.cvtColor(hsv_s, cv2.COLOR_HSV2RGB),
    caption="Saturação alterada"
)

# Brilho
fator_v = col1.slider("Brilho", 0.0, 2.0, 1.2)

v = hsv[:, :, 2].astype(float)
v = np.clip(v * fator_v, 0, 255)

hsv_v = hsv.copy()
hsv_v[:, :, 2] = v

col1.image(
    cv2.cvtColor(hsv_v, cv2.COLOR_HSV2RGB),
    caption="Brilho alterado"
)

# Rotação da matiz
giro = col2.slider("Giro (graus)", 0, 360, 120)

h = hsv[:, :, 0].astype(int)
h = (h + giro // 2) % 180

hsv_giro = hsv.copy()
hsv_giro[:, :, 0] = h

col2.image(
    cv2.cvtColor(hsv_giro, cv2.COLOR_HSV2RGB),
    caption="Matiz girada"
)