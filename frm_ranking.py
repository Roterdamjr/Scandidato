import tkinter as tk
from tkinter import ttk
from funcoes_db_analise import fn_busca_nomes_analisados_db,fn_busca_nota_final,fn_busca_nomes_analisados_db
from funcoes_widget import configurar_botao


class RankingApp:
    
    @staticmethod
    def main():
        root = tk.Toplevel()
        app = RankingApp(root)
        root.mainloop()

    def __init__(self, master):
        self.master = master
        master.title("Análise de Currículos")
        self.master.config(bg='gray70')  # Cor de fundo da janela
        self.master.geometry("700x500") 

        self.style = ttk.Style()
        self.style.theme_use('clam')  # Isso permite customizar fundo e texto
        
    def create_widgets(self):
        self.exibir_ranking()

        lista = fn_busca_nomes_analisados_db()
        self.analises = [c for c in lista]
        self.combo = ttk.Combobox(self.master, values=self.analises, state="readonly")
        self.combo.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.combo.set(self.analises[0] if self.analises else "") # Define o primeiro como padrão


    def exibir_ranking(self):
        nomes_analisados = fn_busca_nomes_analisados_db()

        self.data = []
        for nome in nomes_analisados:
            nota_final = fn_busca_nota_final(nome)
            self.data.append({"Nome": nome, "Nota Final": nota_final})

        # Criação da Treeview para exibir os dados
        self.tree = ttk.Treeview(self.master, columns=("Nome", "Nota Final"), show="headings")

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

if __name__ == "__main__":
    root = tk.Tk()
    app = RankingApp(root)
    root.mainloop()