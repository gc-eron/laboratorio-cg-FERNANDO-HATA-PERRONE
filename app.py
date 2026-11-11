
import streamlit as st
import importlib

st.set_page_config(
    page_title="Laboratório de Computação Gráfica",
    layout="centered"
)

pagina = st.sidebar.radio(
    "Escolha uma atividade:",
    [
        "Início",
        "Atividade 1",
        "Atividade 2",
        "Atividade 3",
        "Atividade 4"
    ]
)

if pagina == "Início":
    st.title("Laboratório de Computação Gráfica")
    st.write("Selecione uma atividade no menu lateral.")

elif pagina == "Atividade 1":
    from src.laboratorio_cg import atv1
    importlib.reload(atv1)

elif pagina == "Atividade 2":
    from src.laboratorio_cg import atv2
    importlib.reload(atv2)

elif pagina == "Atividade 3":
    from src.laboratorio_cg import atv3
    importlib.reload(atv3)

elif pagina == "Atividade 4":
    from src.laboratorio_cg import atv4
    importlib.reload(atv4)
