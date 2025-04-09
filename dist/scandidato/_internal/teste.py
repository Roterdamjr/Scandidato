from dotenv import load_dotenv
from google import genai
from funcoes_prompt import fn_busca_resumo,  fn_busca_opiniao,fn_gerar_score,fn_gera_response
from funcoes_db_curriculo import   fn_busca_curriculo_db
from funcoes_db_cargo import fn_busca_job
import os 




load_dotenv()


curriculo = fn_busca_curriculo_db('Bart')
prompt = fn_busca_resumo(curriculo)
resumo = fn_gera_response(prompt)
print(resumo)
 
        
     




