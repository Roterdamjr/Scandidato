from funcoes_db_curriculo import fn_busca_curriculo_db,fn_busca_curriculos_db
from funcoes_db_analise import fn_exclui_analise_db
from funcoes_prompt import fn_busca_opiniao,fn_busca_resumo, fn_gerar_score
from google import genai
import os

def resumo():
    nome_selecionado ="Bart Rabelo - Curriculum Vitae (EN)"

    curriculo = fn_busca_curriculo_db(nome_selecionado)
    prompt = fn_busca_resumo(curriculo)
    resumo = fn_gera_response(prompt)

def fn_gera_response(prompt):
        client = genai.Client(api_key=os.getenv("API_KEY"))
        response_text = ""
        try:
            print("Analisando")
            response = client.models.generate_content_stream(
                model="gemini-2.0-flash",
                contents=[prompt]
            )
            for chunk in response:
                response_text += chunk.text
            return response_text
        except Exception as e:
            print("Erro")
            return None


resumo()
    