import tkinter as tk
from tkinter import ttk
from funcoes_db_analise import fn_busca_nomes_analisados_db,fn_busca_nota_final
class ResultadosAnaliseApp:
    def __init__(self, master):
        self.master = master
        master.title("Resultados da Análise")



        nomes_analisados = fn_busca_nomes_analisados_db()

        self.data = []
        for nome in nomes_analisados:
            nota_final = fn_busca_nota_final(nome)
            self.data.append({"Nome": nome, "Nota Final": nota_final})

        # Criação da Treeview para exibir os dados
        self.tree = ttk.Treeview(master, columns=("Nome", "Nota Final"), show="headings")

        # Define os cabeçalhos das colunas
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Nota Final", text="Nota Final")

        # Insere os dados na Treeview
        for item in self.data:
            self.tree.insert("", tk.END, values=(item["Nome"], item["Nota Final"]))

        # Configura o redimensionamento das colunas
        self.tree.column("Nome", width=150)
        self.tree.column("Nota Final", width=100, anchor="center")

        # Adiciona a Treeview à janela
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Adiciona um botão "Fechar"
        self.botao_fechar = tk.Button(master, text="Fechar", command=master.destroy)
        self.botao_fechar.pack(pady=10)

if __name__ == '__main__':
    root = tk.Tk()
    app = ResultadosAnaliseApp(root)
    root.mainloop()