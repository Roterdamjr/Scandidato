from funcoes_db_curriculo import fn_busca_curriculo_db,fn_busca_curriculos_db
from funcoes_db_analise import fn_exclui_analise_db
from funcoes_prompt import fn_busca_opiniao,fn_busca_resumo, fn_gerar_score
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import json
import os

class TelaAnaliseCurriculo:

    def __init__(self, master):
        self.master = master
        master.title("Análise de Currículos")

        curriculos = fn_busca_curriculos_db()
        self.nomes_curriculos = [c for c in curriculos]

        # Combo Box para selecionar o currículo
        self.label_selecionar = tk.Label(master, text="Selecionar Currículo:")
        self.label_selecionar.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.combo_curriculos = ttk.Combobox(master, values=self.nomes_curriculos, state="readonly")
        self.combo_curriculos.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.combo_curriculos.set(self.nomes_curriculos[0] if self.nomes_curriculos else "") # Define o primeiro como padrão

        # Botão "Analisar"
        self.botao_analisar = tk.Button(master, text="Analisar", command=self.analisar_curriculo)
        self.botao_analisar.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        # Text Areas
        self.label_resumo = tk.Label(master, text="Resumo:")
        self.label_resumo.grid(row=1, column=0, padx=10, pady=5, sticky="nw")
        self.text_resumo = tk.Text(master, height=5, width=50)
        self.text_resumo.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")

        self.label_opiniao = tk.Label(master, text="Opinião:")
        self.label_opiniao.grid(row=2, column=0, padx=10, pady=5, sticky="nw")
        self.text_opiniao = tk.Text(master, height=5, width=50)
        self.text_opiniao.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="nsew")

        self.label_nota = tk.Label(master, text="Nota:")
        self.label_nota.grid(row=3, column=0, padx=10, pady=5, sticky="nw")
        self.text_nota = tk.Text(master, height=5, width=10)
        self.text_nota.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Configurar o gerenciamento de redimensionamento das linhas e colunas
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)
        master.grid_rowconfigure(1, weight=1)
        master.grid_rowconfigure(2, weight=1)

    def analisar_curriculo(self):
        
        nome_selecionado = self.combo_curriculos.get()
        fn_exclui_analise_db(nome_selecionado)

        curriculo = fn_busca_curriculo_db(nome_selecionado)
        prompt = fn_busca_resumo(curriculo)
        resumo = fn_gera_response(prompt)

        if curriculo:
            conteudo = curriculo.get("content", "")
            # Aqui você colocaria sua lógica de análise do currículo
            # Para este exemplo, vamos apenas preencher os campos com informações básicas

            # Simulação de análise
            resumo_simulado = f"Resumo do currículo de {nome_selecionado}..."
            opiniao_simulada = "Parece um candidato interessante..."
            nota_simulada = "7.5"

            self.text_resumo.delete("1.0", tk.END)
            self.text_resumo.insert(tk.END, resumo_simulado)

            self.text_opiniao.delete("1.0", tk.END)
            self.text_opiniao.insert(tk.END, opiniao_simulada)

            self.text_nota.delete("1.0", tk.END)
            self.text_nota.insert(tk.END, nota_simulada)
        else:
            self.text_resumo.delete("1.0", tk.END)
            self.text_resumo.insert(tk.END, "Currículo não encontrado.")
            self.text_opiniao.delete("1.0", tk.END)
            self.text_opiniao.insert(tk.END, "")
            self.text_nota.delete("1.0", tk.END)
            self.text_nota.insert(tk.END, "")

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaAnaliseCurriculo(root)
    root.mainloop()