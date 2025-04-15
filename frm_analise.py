
from funcoes_db_curriculo import fn_busca_curriculo_db,fn_busca_curriculos_db
from funcoes_db_analise import fn_exclui_analise_db,fn_inserir_analise_db, fn_exclui_analises_db,fn_busca_nomes_analisados_db
from funcoes_db_cargo import fn_busca_job
from funcoes_prompt import fn_busca_opiniao,fn_busca_resumo, fn_gerar_score,fn_gera_response
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
import os
from google import genai
from dotenv import load_dotenv
from funcoes_widget import configurar_botao


class AnaliseApp:

    @staticmethod
    def main():
        root = tk.Toplevel()
        app = AnaliseApp(root)
        root.mainloop()

    def __init__(self, master):
        self.master = master
        master.title("Análise de Currículos")
        self.master.config(bg='gray70')  # Cor de fundo da janela
        self.master.geometry("700x500") 

        self.style = ttk.Style()
        self.style.theme_use('clam')  # Isso permite customizar fundo e texto

        configurar_botao(self)
        self.create_widgets()
        self.atualizar_lista_analises()

    def create_widgets(self):
        curriculos = fn_busca_curriculos_db()
        self.nomes_curriculos = [c for c in curriculos]

        # Combo Box para selecionar o currículo
        self.combo_curriculos = ttk.Combobox(self.master, values=self.nomes_curriculos, state="readonly")
        self.combo_curriculos.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.combo_curriculos.set(self.nomes_curriculos[0] if self.nomes_curriculos else "") # Define o primeiro como padrão

        botao_analisar = ttk.Button(self.master, text="Analisar", command=self.analisar_curriculo, style="BotaoPersonalizado.TButton")
        botao_analisar.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        # Text Areas
        self.label_resumo = tk.Label(self.master, text="Resumo:", bg=self.master['bg'])
        self.label_resumo.grid(row=1, column=0, padx=10, pady=5, sticky="nw")
        self.text_resumo = tk.Text(self.master, height=4, width=80)
        self.text_resumo.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")

        self.label_opiniao = tk.Label(self.master, text="Opinião:", bg=self.master['bg'])
        self.label_opiniao.grid(row=2, column=0, padx=10, pady=5, sticky="nw")
        self.text_opiniao = tk.Text(self.master, height=4, width=80)
        self.text_opiniao.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")
        
        self.label_nota = tk.Label(self.master, text="Nota:", bg=self.master['bg'])
        self.label_nota.grid(row=3, column=0, padx=10, pady=5, sticky="nw")
        self.text_nota = tk.Text(self.master, height=4, width=80) 
        self.text_nota.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="nsew") # Alterei columnspan e sticky

        # Frame inferior para título, botão e lista de análises
        self.frame_inferior = tk.Frame(self.master, bg='gray80')
        self.frame_inferior.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Sub-frame para o título e o botão
        self.frame_topo_inferior = tk.Frame(self.frame_inferior, bg='gray80')
        self.frame_topo_inferior.pack(fill="x", padx=5, pady=(5, 8))

        self.label_analises = tk.Label(self.frame_topo_inferior, text="Análises realizadas", bg='gray80', font=("Arial", 10, "bold"))
        self.label_analises.pack(side="left", padx=(5, 10))

        self.botao_limpar = ttk.Button(self.frame_topo_inferior, text="Limpar Análises", command=self.limpar_analises, style="BotaoPersonalizado.TButton")
        self.botao_limpar.pack(side="right", padx=(10, 5))

        # Lista de análises realizadas
        self.lista_analises = tk.Listbox(self.frame_inferior, height=5, bg="#f0f0f0")
        self.lista_analises.pack(fill="both", expand=True, padx=5, pady=(0, 5))

        # Configurar o gerenciamento de redimensionamento das linhas e colunas
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_rowconfigure(3, weight=1)
        self.master.grid_rowconfigure(4, weight=1)  # permite que o frame inferior também cresça

    def analisar_curriculo(self):
        load_dotenv()

        nome_selecionado = self.combo_curriculos.get()
        
        curriculo = fn_busca_curriculo_db(nome_selecionado)
        prompt = fn_busca_resumo(curriculo)
        resumo = fn_gera_response(prompt)
        self.text_resumo.delete("1.0", tk.END)
        self.text_resumo.insert(tk.END, resumo)

        prompt = fn_busca_opiniao(curriculo, fn_busca_job())
        opiniao = fn_gera_response(prompt)
        self.text_opiniao.delete("1.0", tk.END)
        self.text_opiniao.insert(tk.END, opiniao)

        prompt = fn_gerar_score(curriculo, fn_busca_job())
        nota = fn_gera_response(prompt)
        self.text_nota.delete("1.0", tk.END)
        self.text_nota.insert(tk.END, nota)     

        fn_exclui_analise_db(nome_selecionado)
        fn_inserir_analise_db(nome_selecionado, resumo,opiniao,nota)   
        self.atualizar_lista_analises()

    def limpar_analises(self):
        fn_exclui_analises_db()
        self.atualizar_lista_analises()

    def atualizar_lista_analises(self):
        self.lista_analises.delete(0, tk.END)

        curriculos = fn_busca_nomes_analisados_db()

        for curriculo in curriculos:
            self.lista_analises.insert(tk.END, curriculo)


    
if __name__ == "__main__":
    root = tk.Tk()
    app = AnaliseApp(root)
    root.mainloop()
