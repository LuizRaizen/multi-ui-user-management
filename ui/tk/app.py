# -*- coding: utf-8 -*-
"""Módulo para criar e administrar a interface gráfica na versão do Tkinter."""

import tkinter as tk

from database import BancoDeDados
from ui.tk.tk_utils import get_entry, clear_entries
from ui.tk.login import TelaDeLogin
from ui.tk.register import TelaDeCadastro


class TkApp(tk.Tk):
    """
    Classe principal da aplicação.

    Attributes:
        tela_login (TelaDeLogin): A instância da tela de login.
        tela_cadastro (TelaDeCadastro): A instância da tela de cadastro.
        banco_de_dados (BancoDeDados): A instância do banco de dados.
    """

    def __init__(self, *args, **kwargs):
        """
        Inicializa a aplicação.

        Args:
            *args: Argumentos posicionais para tk.Tk.
            **kwargs: Argumentos nomeados para tk.Tk.

        Returns:
            None
        """
        
        super().__init__(*args, **kwargs)

        # Configurações da janela da aplicação
        self.title("Tela de Cadastro e Login de Usuários")
        self.resizable(width=False, height=False)
        self.geometry("500x600")

        # Cria e configura o Banco de Dados
        self.banco_de_dados = BancoDeDados()
        self.banco_de_dados.criar_tabela()
        
        # Cria as telas da aplicação e exibe a Tela de Login
        self.tela_login = TelaDeLogin(self)
        self.tela_cadastro = TelaDeCadastro(self)
        self.mostrar_tela_login()
        
    def mostrar_tela_login(self):
        """
        Exibe a tela de login.

        Args:
            None

        Returns:
            None
        """
        
        # Limpa os formulários antes de trocar de tela
        clear_entries(self.tela_cadastro.frm_campos)
        
        self.tela_cadastro.pack_forget()
        self.tela_login.configure(relief=tk.SOLID, border=1)
        self.tela_login.pack(
            expand=True,
            fill=tk.BOTH,
            anchor=tk.CENTER,
            padx=20,
            pady=20
        )
        
        ent_nome_usuario = get_entry(
            self.tela_login.frm_campos,
            'frm_nome_de_usuario_email', 
            'ent_nome_de_usuario_email',
        )
        
        ent_nome_usuario.focus_force()
        
    def mostrar_tela_cadastro(self):
        """
        Exibe a tela de cadastro.

        Args:
            None

        Returns:
            None
        """
        
        # Limpa os formulários antes de trocar de tela
        clear_entries(self.tela_login.frm_campos)
        
        self.tela_login.pack_forget()
        self.tela_cadastro.configure(relief=tk.SOLID, border=1)
        self.tela_cadastro.pack(
            expand=True,
            fill=tk.BOTH,
            anchor=tk.CENTER,
            padx=20,
            pady=20
        )
        
        # Redefine a confuguração padrão dos formulários da tela de login antes de mudar de tela
        self.tela_login.combo_estilo.configure(
            "TCombobox",
            fieldbackground="white"
        )
        ent_senha = get_entry(
            self.tela_login.frm_campos,
            'frm_senha',
            'ent_senha'
        )
        ent_senha.configure(background="white")
        
        # Coloca o foco no campo do nome de usuário
        ent_nome_usuario = get_entry(
            self.tela_cadastro.frm_campos,
            'frm_nome_de_usuario', 
            'ent_nome_de_usuario',
        )
        ent_nome_usuario.focus_force()
                

if __name__ == "__main__":
    TkApp().mainloop()
