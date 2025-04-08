import streamlit as st
from view_cargo import exibir_view_cargo
from view_curriculo import exibir_view_curriculo
from view_analise import exibe_view_analise
from view_ranking import exibe_view_ranking

st.sidebar.title("Menu")
opcao = st.sidebar.radio("Selecione uma tela:", ("Cargo", "Curriculo", "Analise","Ranking"))

if opcao == "Cargo":
    exibir_view_cargo()
elif opcao == "Curriculo":
    exibir_view_curriculo()
elif opcao == "Analise":
    exibe_view_analise()
elif opcao == "Ranking":
    exibe_view_ranking()