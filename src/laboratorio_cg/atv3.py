
import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Atividade 3 - Padrões de Imagem")

k = st.slider("k", 1, 20, 4)
y, x = np.indices((64, 64))



def padrao(x, y, k):
    tamanho = max(1, k)
    return (((x // tamanho) + (y // tamanho)) % 2) * 255



imagem = padrao(x, y, k).astype(np.uint8)

st.image(ampliar(imagem, 4), caption="Padrão gerado")
