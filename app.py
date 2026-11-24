
from pathlib import Path
import runpy
import streamlit as st

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
        "Atividade 4",
        "Atividade 5",
        "Trabalho"
    ]
)

pasta = Path(__file__).resolve().parent / "src" / "laboratorio_cg"

if pagina == "Início":
    st.title("Laboratório de Computação Gráfica")
    st.write("Selecione uma atividade no menu lateral.")

elif pagina == "Atividade 1":
    runpy.run_path(str(pasta / "atv1.py"))

elif pagina == "Atividade 2":
    runpy.run_path(str(pasta / "atv2.py"))

elif pagina == "Atividade 3":
    runpy.run_path(str(pasta / "atv3.py"))

elif pagina == "Atividade 4":
    runpy.run_path(str(pasta / "atv4.py"))

elif pagina == "Atividade 5":
    runpy.run_path(str(pasta / "atv5.py"))

elif pagina == "Trabalho":
    runpy.run_path(str(pasta / "trabalho.py"))
