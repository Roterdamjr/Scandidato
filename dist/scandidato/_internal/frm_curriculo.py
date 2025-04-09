from funcoes_db_curriculo import fn_insere_curriculo,fn_busca_curriculos_db,fn_exclui_curriculos_db
import tkinter as tk
from tkinter import filedialog, ttk
import os

class CurriculoApp:
    @staticmethod
    def main():
        root = tk.Toplevel()
        app = CurriculoApp(root)
        root.mainloop()

    def __init__(self, master):
        self.master = master
        master.title("Cadastro de Currículos")

        self.candidatos = []  # Lista para armazenar os nomes dos candidatos

        # Botão para fazer upload do currículo
        self.upload_button = tk.Button(master, text="Inserir Currículo", command=self.upload_curriculo)
        self.upload_button.pack(pady=10)

        self.delete_button = tk.Button(master, text="Limpar Lista", command=self.limpar_lista)
        self.delete_button.pack(pady=10)

        # Frame para a grade de candidatos
        self.grade_frame = ttk.Frame(master)
        self.grade_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Treeview para exibir os nomes dos candidatos
        self.colunas = ("Nome do Candidato",)
        self.treeview = ttk.Treeview(self.grade_frame, columns=self.colunas, show="headings")

        # Definindo os cabeçalhos das colunas
        for col in self.colunas:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=200)  # Largura inicial da coluna

        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Barra de rolagem vertical para a treeview
        self.scrollbar_y = tk.Scrollbar(self.grade_frame, orient=tk.VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=self.scrollbar_y.set)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.atualizar_lista()

    def upload_curriculo(self):
        file_path = filedialog.askopenfilename(
            title="Selecionar Arquivo de Currículo",
            filetypes=(("Arquivos PDF", "*.pdf"), ("Todos os arquivos", "*.*"))
        )

        if file_path:
            # Extrair o nome do arquivo (sem a extensão) para usar como nome do candidato
            nome_candidato = os.path.splitext(os.path.basename(file_path))[0]
            fn_insere_curriculo(nome_candidato ,file_path)
            self.atualizar_lista()

    def limpar_lista(self):
        fn_exclui_curriculos_db()
        self.atualizar_lista()

    def atualizar_lista(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        for nome in fn_busca_curriculos_db():
            self.treeview.insert("", tk.END, values=(nome,))


if __name__ == "__main__":
    root = tk.Tk()
    app = CurriculoApp(root)
    root.mainloop()