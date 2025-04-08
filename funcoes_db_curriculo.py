from tinydb import TinyDB, Query
import fitz


def fn_busca_candidatos_db():
    db = TinyDB('curriculos.json')
    return [item["nome"] for item in db.all()]
    
def fn_insere_curriculo(nome_candidato, caminho_pdf):

    db = TinyDB('curriculos.json')
    
    text = ""
    with fitz.open(caminho_pdf) as doc:
        for page in doc:
            text += page.get_text()
    
    db.insert({'nome': nome_candidato,  'content': text})
 
def fn_busca_curriculo_db(nome_candidato):
    db = TinyDB('curriculos.json')
    QueryDB = Query()
    resultado = db.search(QueryDB.nome == nome_candidato)

    if resultado:
        return resultado[0]['content']
    else:
        return "    " 

def fn_busca_curriculos_db():
  db = TinyDB('curriculos.json')
  return [item['nome'] for item in db.all() if 'nome' in item]


def fn_busca_conteudo_curriculo(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()

    return text
    
def fn_exclui_curriculos_db():
    db = TinyDB('curriculos.json')
    db.truncate()


def fn_exclui_curriculo_db(nome_procurado):
    db = TinyDB('curriculos.json')
    Candidato = Query()
    resultados = db.search(Candidato.nome == nome_procurado)

    if resultados:
        db.remove(Candidato.nome == nome_procurado)
        db.close()
        return True
    else:
        db.close()
        return False