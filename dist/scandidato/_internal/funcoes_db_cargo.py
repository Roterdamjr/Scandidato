from tinydb import TinyDB, Query
import os
import sys


# Caminho da pasta onde o .exe está (mesmo em modo sem --onefile)




def fn_quebra_linhas(titulo, lista):
    texto = ""
    for item in lista:
        texto += item + '\n'
    return titulo + '\n' + texto + '\n\n'
    
def fn_busca_job():

    db = TinyDB("cargos.json") 
    dados = db.storage.read()

    if dados:
        dados = db.all()  # Pega todos os registros corretamente
        for vaga in dados:
            nome_vaga = vaga.get("nome", "Nome não encontrado")

            prerequisitos = vaga.get("prerequisitos", [])
            prerequisitos = [p.strip("',") for p in prerequisitos]

            diferenciais = vaga.get("diferenciais", [])
            diferenciais = [p.strip("',") for p in diferenciais]

            principais_atividades = vaga.get("principais_atividades", [])
            principais_atividades = [p.strip("',") for p in principais_atividades]

    else:
        print("Nenhuma vaga encontrada no banco de dados.")

    return fn_quebra_linhas('prerequisitos', prerequisitos) + fn_quebra_linhas('diferenciais',diferenciais) + fn_quebra_linhas('principais_atividades',principais_atividades)


def fn_busca_cargo():
    #db = TinyDB('cargos.json')

    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(sys.argv[0])))
    db_path = os.path.join(base_path, "cargos.json")
    db = TinyDB(db_path)
    print("caminho:" , db_path)
    Analise = Query()
    resultado = db.all()
    if resultado:
        return resultado[0]  # Retorna o primeiro resultado encontrado
    return None

def fn_insere_cargo( id, nome, prerequisitos, diferenciais, atividades):
    db = TinyDB('cargos.json')
    cargo = {
      'id': id,
      'nome': nome,
      'prerequisitos': prerequisitos,
      'diferenciais': diferenciais,
      'principais_atividades': atividades  # Corrigido o nome do campo
    }
    db.insert(cargo)

def fn_exclui_cargos():
    db = TinyDB('cargos.json')
    db.truncate()

def fn_consulta_cargos():

  db = TinyDB('cargos.json')
  Cargo = Query()
  resultados = db.search(Cargo.id.exists())  # Busca por qualquer cargo com um ID
  return resultados