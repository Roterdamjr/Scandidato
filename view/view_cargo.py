import streamlit as st
from funcoes_db import fn_exclui_cargos,fn_insere_cargo
from funcoes_prompt import fn_busca_cargo


def exibir_view_cargo():
    
    st.title("Cadastro de Cargo")

    cargo = fn_busca_cargo()


    nome = st.text_input("Nome do cargo", value =cargo['nome'], placeholder="Digite o nome do cargo")
    atividades_texto = st.text_area("Atividades", value="\n".join(cargo.get("principais_atividades", [])), height=150)
    atividades = [linha.strip() for linha in atividades_texto.splitlines() if linha.strip()]

    prerequisitos_texto = st.text_area("Pré-requisitos", value="\n".join(cargo.get("prerequisitos", [])),height=150)
    prerequisitos = [linha.strip() for linha in prerequisitos_texto.splitlines() if linha.strip()]

    diferenciais_texto = st.text_area("Diferenciais", value="\n".join(cargo.get("diferenciais", [])),height=150)
    diferenciais = [linha.strip() for linha in diferenciais_texto.splitlines() if linha.strip()]

    # Botão de cadastro
    if st.button("Cadastrar"):
        if nome and atividades and prerequisitos and diferenciais:
            fn_exclui_cargos()

            fn_insere_cargo(1, nome,  prerequisitos, diferenciais, atividades)
            st.success(f"✅Cargo  cadastrado com sucesso!")
        else:
            st.error("❌ Preencha todos os campos antes de cadastrar.")
