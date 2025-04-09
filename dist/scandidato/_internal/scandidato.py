import tkinter as tk
import frm_cargo,frm_curriculo,frm_analise,frm_ranking  # Supondo que frm_cargo.py tenha uma função main()

def open_cargo():
    frm_cargo.CargoApp.main() 

def open_curriculo():
    frm_curriculo.CurriculoApp.main() 

def open_analise():
    frm_analise.AnaliseApp.main() 

def open_ranking():
    frm_ranking.RankingApp.main() 

def main():
    root = tk.Tk()
    root.title("Scandidato")

    menubar = tk.Menu(root)
    cadastros_menu = tk.Menu(menubar, tearoff=0)

    cadastros_menu.add_command(label="Cargos", command = open_cargo)
    cadastros_menu.add_command(label="Curriculos", command = open_curriculo)
    cadastros_menu.add_command(label="Analises", command = open_analise)
    cadastros_menu.add_command(label="Ranking", command = open_ranking)

    menubar.add_cascade(label="Cadastros", menu=cadastros_menu)
    # ... (outros menus) ...

    root.config(menu=menubar)
    root.mainloop()

if __name__ == "__main__":
    main()