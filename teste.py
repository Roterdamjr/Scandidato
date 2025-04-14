from funcoes_db_cargo import fn_exclui_cargos, fn_insere_cargo, fn_busca_cargo
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

class CargoApp:
    @staticmethod
    def main():
        root = tk.Toplevel()
        app = CargoApp(root)
        root.mainloop()

    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Cargo")

        self.style = ttk.Style()
        print("Temas disponíveis:", self.style.theme_names())
        self.style.theme_use('clam')  # Experimente outros temas aqui

        self.create_widgets()
        self.popular_campos()

    def create_widgets(self):
        # Campo Nome
        lbl_nome = ttk.Label(self.root, text="Nome:")
        lbl_nome.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.txt_nome = ttk.Entry(self.root, width=40)
        self.txt_nome.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Textarea Atividades
        lbl_atividades = ttk.Label(self.root, text="Atividades:")
        lbl_atividades.grid(row=1, column=0, padx=5, pady=5, sticky="nw")
        self.txt_atividades = scrolledtext.ScrolledText(self.root, width=40, height=5)
        self.txt_atividades.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        # Textarea Pré-requisitos
        label_pre_requisitos = ttk.Label(self.root, text="Pré-requisitos:")
        label_pre_requisitos.grid(row=2, column=0, padx=5, pady=5, sticky="nw")
        self.txt_pre_requisitos = scrolledtext.ScrolledText(self.root, width=40, height=5)
        self.txt_pre_requisitos.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        # Textarea Diferenciais
        lbl_diferenciais = ttk.Label(self.root, text="Diferenciais:")
        lbl_diferenciais.grid(row=3, column=0, padx=5, pady=5, sticky="nw")
        self.txt_diferenciais = scrolledtext.ScrolledText(self.root, width=40, height=5)
        self.txt_diferenciais.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

        btn_gravar = ttk.Button(self.root, text="Gravar", command=self.gravar_dados)
        btn_gravar.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

        # Configurar o gerenciamento de layout para redimensionamento
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)


    def popular_campos(self):
        cargo = fn_busca_cargo()
        if(cargo):
            self.txt_nome.insert(0, cargo['nome'])

            atividades_str = "\n".join(cargo['principais_atividades'])
            self.txt_atividades.insert(1.0, atividades_str)

            pre_requisitos_str= "\n".join(cargo['prerequisitos'])
            self.txt_pre_requisitos.insert(1.0, pre_requisitos_str)

            diferenciais_str=  "\n".join(cargo['diferenciais'])
            self.txt_diferenciais.insert(1.0, diferenciais_str)

    def gravar_dados(self):
        nome = self.txt_nome.get()

        atividades = self.txt_atividades.get("1.0", tk.END).strip().split("\n")
        pre_requisitos = self.txt_pre_requisitos.get("1.0", tk.END).strip().split("\n")
        diferenciais = self.txt_diferenciais.get("1.0", tk.END).strip().split("\n")

        fn_exclui_cargos()
        fn_insere_cargo(1, nome,  pre_requisitos, diferenciais, atividades)

        messagebox.showinfo("Sucesso", "Dados gravados com sucesso!")


    def limpar_campos(self):
        self.txt_nome.delete(0, tk.END)
        self.txt_atividades.delete("1.0", tk.END)
        self.txt_pre_requisitos.delete("1.0", tk.END)
        self.txt_diferenciais.delete("1.0", tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CargoApp(root)
    root.mainloop()