
import streamlit as st
import runpy
from pathlib import Path

st.set_page_config(page_title="Computação Gráfica")

pagina = st.sidebar.radio(
    "Escolha uma atividade:",
    ["Início", "Atividade 1", "Atividade 2", "Atividade 3"]
)

pasta = Path(__file__).parent / "src" / "laboratorio_cg"

if pagina == "Início":
    st.title("Laboratório de Computação Gráfica")
    st.write("Selecione uma atividade no menu lateral.")

elif pagina == "Atividade 1":
    runpy.run_path(str(pasta / "atv1.py"))

elif pagina == "Atividade 2":
    runpy.run_path(str(pasta / "atv2.py"))

elif pagina == "Atividade 3":
    runpy.run_path(str(pasta / "atv3.py"))
