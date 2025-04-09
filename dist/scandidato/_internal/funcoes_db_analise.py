from tinydb import TinyDB, Query
import re
 
def fn_inserir_analise_db(nome, resumo,opiniao,nota,):
    db = TinyDB('analises.json')
    analise = {
      'nome': nome,
      'resumo': resumo,
      'opiniao': opiniao,
      'nota': nota 
    }
    db.insert(analise)
    
def fn_busca_nomes_analisados_db():
    db = TinyDB('analises.json')
    return [item["nome"] for item in db.all()]

def fn_busca_analise_por_nome(nome):
    """Busca os dados de análise de um nome específico no banco de dados."""
    db = TinyDB('analises.json')
    Analise = Query()
    resultado = db.search(Analise.nome == nome)
    if resultado:
        return resultado[0]  # Retorna o primeiro resultado encontrado
    return None 

def fn_exclui_analises_db():
    db = TinyDB('analises.json')
    db.truncate()

def fn_exclui_analise_db(nome_procurado):
    db = TinyDB('analises.json')
    Analise = Query()
    resultados = db.search(Analise.nome == nome_procurado)

def fn_busca_nota_final(nome):
    db = TinyDB('analises.json')
    Analise = Query()
    result_raw = db.search(Analise.nome == nome)

    if not result_raw:
        print(f"Nenhuma análise encontrada para {nome}.")
        return None  # Or some other appropriate value to indicate no result

    texto = str(result_raw[0])

    chave = 'Nota final do candidato'
    try:
        indice = texto.index(chave)
        texto = texto[indice + len(chave):].strip()
    except ValueError:
        print(f"A string '{chave}' não foi encontrada no texto.")

    padrao = r':\s*(\d+\.?\d*)'
    resultado = re.search(padrao, texto)

    if resultado:
        nota_final = resultado.group(1)
        #print(nota_final)
    else:
        print("Nenhuma nota encontrada no texto.")

    return nota_final