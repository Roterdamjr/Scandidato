
from funcoes_db import fn_busca_nomes_analisados_db,fn_busca_analise_por_nome,fn_busca_nota_final
import streamlit as st
import pandas as pd
import plotly.express as px

def exibe_view_ranking():
    st.title("Ranking")

    nomes_analisados = fn_busca_nomes_analisados_db()

    data = []
    for nome in nomes_analisados:
        nota_final = fn_busca_nota_final(nome)
        data.append({"Nome": nome, "Nota Final": nota_final})

    df = pd.DataFrame(data).sort_values(by="Nota Final", ascending=False)

    # Criar o gráfico de barras com Plotly Express (uma interface de alto nível para Plotly)
    fig = px.bar(df, x="Nome", y="Nota Final",
                title="Ranking de Nomes por Nota Final",
                labels={"Nota Final": "Nota Final", "Nome": "Nome"})
    fig.update_layout(xaxis_tickangle=-45, xaxis_title="Nome", yaxis_title="Nota Final")

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)




    nome_selecionado = st.selectbox("Selecione um nome analisado:", nomes_analisados)

    if nome_selecionado:
        st.subheader(f"Informações de: {nome_selecionado}")

        dados_analise = fn_busca_analise_por_nome(nome_selecionado)

        if dados_analise:
            resumo = dados_analise.get("resumo", "Resumo não disponível.")
            st.text_area("Resumo", resumo, height=200)

            # Textarea para a opinião
            opiniao_inicial = dados_analise.get("opiniao", "")
            opiniao = st.text_area("Sua opinião sobre:", opiniao_inicial, height=200)

            # Textarea para a nota
            nota_inicial = dados_analise.get("nota", "")
            nota = st.text_area("Sua nota:", nota_inicial, height=200)

        else:
            st.warning(f"Nenhum dado de análise encontrado para o nome: {nome_selecionado}")