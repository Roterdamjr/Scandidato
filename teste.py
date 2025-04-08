import os
import sys

def fn_busca_cargo():
    #db = TinyDB('cargos.json')

    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(sys.argv[0])))
    db_path = os.path.join(base_path, "cargos.json")
    return db_path

print(fn_busca_cargo())
    