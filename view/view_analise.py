import streamlit as st
import asyncio
from dotenv import load_dotenv
from google import genai
from funcoes_prompt import fn_busca_resumo, fn_busca_curriculo_db, fn_busca_job,fn_busca_opiniao,fn_gerar_score
from funcoes_db import fn_inserir_analise_db,fn_exclui_analises_db,  fn_busca_curriculos_db,fn_exclui_analise_db, fn_busca_nomes_analisados_db
from funcoes_db import fn_busca_nota_final
import os 

def fn_gera_response(prompt):
    client = genai.Client(api_key=os.getenv("API_KEY"))
    response_text = ""
    try:
        response = client.models.generate_content_stream(
            model="gemini-2.0-flash",
            contents=[prompt]
        )
        for chunk in response:
            response_text += chunk.text
        return response_text
    except Exception as e:
        st.error(f"Erro ao gerar resposta da IA: {e}")
        return None


def exibe_view_analise():
    st.title("Análise de Currículos")

    load_dotenv()


    st.header("Análises Realizadas")

    analises = fn_busca_nomes_analisados_db()
    if analises:
        for analise in analises:
            st.write(analise)
    else:
        st.write("Nenhuma analise realizada ainda.")

    if st.button("Excluir"):
        fn_exclui_analises_db()
        st.success("Análises excluídas com sucesso!")

    
    nome_candidato = st.selectbox("Selecione um Candidato:", [""] + fn_busca_curriculos_db())

    if st.button("Analisar"):
        fn_exclui_analise_db(nome_candidato)

        st.write(f"Analisando candidato: **{nome_candidato}**")
        curriculo = fn_busca_curriculo_db(nome_candidato)


        with st.status("Gerando resumo..."):
            prompt = fn_busca_resumo(curriculo)
            resumo = fn_gera_response(prompt)
            if resumo:  
                st.write("Resumo:", resumo)

        with st.status("Gerando opinião..."):
            prompt = fn_busca_opiniao(curriculo, fn_busca_job())
            opiniao = fn_gera_response(prompt)
            if opiniao:  
                st.write("Opiniao:", opiniao)

        with st.status("Calculando nota..."):
            prompt = fn_gerar_score(curriculo, fn_busca_job())

            nota = fn_gera_response(prompt)
            if nota:  
                st.write("Nota:", nota)
        
        fn_inserir_analise_db(nome_candidato, resumo,opiniao,nota)

        st.write('Pronto!')


