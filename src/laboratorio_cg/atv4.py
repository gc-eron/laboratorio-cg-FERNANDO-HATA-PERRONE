
from pathlib import Path

import streamlit as st
import numpy as np
from PIL import Image

st.title("Atividade 4 - Cor e canais")

# Localizar a fotografia
pasta_projeto = Path(__file__).resolve().parents[2]
caminho_foto = pasta_projeto / "imagens" / "foto.jpg"

if not caminho_foto.exists():
    st.error("Fotografia não encontrada na pasta imagens.")
    st.stop()

foto = Image.open(caminho_foto).convert("RGB")
imagem = np.array(foto)

altura, largura, canais = imagem.shape

# SEÇÃO 1 - LEITURA DA FOTOGRAFIA
st.header("1. Leitura da fotografia")

col1, col2 = st.columns(2)

with col1:
    st.image(imagem, caption="Fotografia original",
             width=350)

with col2:
    st.write(f"Dimensões: {largura} x {altura} pixels")
    st.write(f"Número de canais: {canais}")

    if altura > 100 and largura > 100:
        pixel = imagem[100, 100]
        st.write(
            f"Pixel (100, 100) - RGB: {pixel.tolist()}"
        )

# SEÇÃO 2 - CANAIS RGB
st.header("2. Canais RGB")

col1, col2 = st.columns(2)

canal_r = imagem[:, :, 0]
canal_g = imagem[:, :, 1]
canal_b = imagem[:, :, 2]

with col1:
    st.subheader("Canais em tons de cinza")
    st.image(canal_r, caption="Canal R",
             clamp=True, width=300)
    st.image(canal_g, caption="Canal G",
             clamp=True, width=300)
    st.image(canal_b, caption="Canal B",
             clamp=True, width=300)

with col2:
    st.subheader("Canais em cores")

    somente_r = np.zeros_like(imagem)
    somente_r[:, :, 0] = canal_r

    somente_g = np.zeros_like(imagem)
    somente_g[:, :, 1] = canal_g

    somente_b = np.zeros_like(imagem)
    somente_b[:, :, 2] = canal_b

    st.image(somente_r, caption="Somente vermelho",
             width=300)
    st.image(somente_g, caption="Somente verde",
             width=300)
    st.image(somente_b, caption="Somente azul",
             width=300)

# SEÇÃO 3 - CUBO RGB E BGR
st.header("3. Cubo RGB e BGR")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Cores do cubo RGB")

    cores = {
        "Amarelo": (255, 255, 0),
        "Vermelho": (255, 0, 0),
        "Verde": (0, 255, 0),
        "Azul": (0, 0, 255)
    }

    for nome, rgb in cores.items():
        quadrado = np.zeros((80, 80, 3),
                            dtype=np.uint8)
        quadrado[:, :] = rgb
        st.image(quadrado, caption=nome, width=120)

with col2:
    st.subheader("Fotografia interpretada como BGR")
    st.image(imagem, channels="BGR",
             caption="Ordem BGR", width=300)

# SEÇÃO 4 - TONS DE CINZA
st.header("4. Conversão para tons de cinza")

col1, col2 = st.columns(2)

# Média simples dos três canais
cinza_media = np.mean(imagem, axis=2).astype(np.uint8)

# Média ponderada dos canais RGB
cinza_ponderada = (
    0.299 * canal_r +
    0.587 * canal_g +
    0.114 * canal_b
).astype(np.uint8)

with col1:
    st.subheader("Média simples")
    st.image(cinza_media,
             caption="Cinza pela média simples",
             clamp=True, width=300)

with col2:
    st.subheader("Média ponderada")
    st.image(cinza_ponderada,
             caption="Cinza pela média ponderada",
             clamp=True, width=300)
