from funcoes_db_curriculo import fn_insere_curriculo,fn_busca_curriculos_db,fn_exclui_curriculos_db
import tkinter as tk
from tkinter import filedialog, ttk
import os
from funcoes_widget import configurar_botao

class CurriculoApp:
    @staticmethod
    def main():
        master = tk.Toplevel()
        app = CurriculoApp(master)
        master.mainloop()

    def __init__(self, master):
        self.master = master
        master.title("Cadastro de Currículos")
        self.master.config(bg='gray70')  # Cor de fundo da janela
        self.master.geometry("700x500") 

        self.style = ttk.Style()
        self.style.theme_use('clam')  # Isso permite customizar fundo e texto
        configurar_botao(self)

        self.create_widgets()

    def create_widgets(self):
        self.candidatos = []  # Lista para armazenar os nomes dos candidatos

    ############################### BOTOES ########################
        botoes_frame = tk.Frame(self.master, bg=self.master['bg'])
        botoes_frame.pack(pady=10)

        upload_button = ttk.Button(
            botoes_frame,
            text="Inserir Currículo",
            command=self.upload_curriculo,
            style="BotaoPersonalizado.TButton"
        )
        upload_button.pack(side=tk.LEFT, padx=5)

        delete_button = ttk.Button(
            botoes_frame,
            text="Limpar Lista",
            command=self.limpar_lista,
            style="BotaoPersonalizado.TButton"
        )
        delete_button.pack(side=tk.LEFT, padx=5)

        ############################### GRADE ########################
        grade_frame = ttk.Frame(self.master)
        grade_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.colunas = ("Currículos",)
        self.treeview = ttk.Treeview(grade_frame, columns=self.colunas, show="headings")

        for col in self.colunas:
            self.treeview.heading(col, text=col)
            self.treeview.column(col, width=200)  # Largura inicial da coluna

        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Barra de rolagem vertical para a treeview
        self.scrollbar_y = tk.Scrollbar(grade_frame, orient=tk.VERTICAL, command=self.treeview.yview)
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
    master = tk.Tk()
    app = CurriculoApp(master)
    master.mainloop()