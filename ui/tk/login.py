# -*- coding: utf-8 -*-

"""Módulo para criação da interface gráfica Login de Usuários no framework Tkinter."""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from ui.tk.tk_utils import TkCustomWidget, TkCustomForm, get_entry
from controller import LembrarUsuario

from utils import get_hex_from_rgb


class TelaDeLogin(tk.Frame):
    """
    Classe que representa a tela de login de usuários.

    Attributes:
        frm_campos (tk.Frame): O frame que contém os campos de entrada.
        chk_lembrar (tk.Checkbutton): O checkbutton para a opção 'Lembrar de mim'.
        btn_entrar (tk.Button): O botão para realizar o login.
        frm_link (tk.Frame): O frame que contém o link para criar uma nova conta.
        link_create_account (tk.Label): O label que representa o link para criar uma nova conta.
    """

    def __init__(self, master, **kwargs):
        """
        Inicializa a tela de login.

        Args:
            *args: Argumentos posicionais para tk.Frame.
            **kwargs: Argumentos nomeados para tk.Frame.

        Returns:
            None
        """
        super().__init__(master, **kwargs)

        # Título da Tela de Login
        TkCustomWidget.criar_titulo(self, "Fazer login")
        
        # Criação e configurações dos formulários
        self.frm_campos = tk.Frame(self, name='frm_campos', pady=30)
        self.frm_campos.pack()

        campos = [("Nome de usuário / E-mail:", 'list'), "Senha:"]
        TkCustomForm(self.frm_campos, campos, tk.TOP)
        
        # Obtém a instância do banco de dados
        self.banco_de_dados = self.master.banco_de_dados
        
        # Obtém os formulários criados
        # Obtém a instância do formulário para nome de usuário ou e-mail
        ent_nome_usuario_email = get_entry(
            self.frm_campos,
            'frm_nome_de_usuario_email',
            'ent_nome_de_usuario_email',
        )
        self.mostrar_lista_usuarios_relembrados(ent_nome_usuario_email)
        
        # Obtém e configura a instância do formulário para a senha
        ent_senha = get_entry(
            self.frm_campos,
            'frm_senha',
            'ent_senha'
        )
        ent_senha.configure(show="*")
        
        # Definir alguns binds para ajudar na experiência do usuário
        # Cria um estilo personalizado para o campo de nome de usuário
        self.combo_estilo = ttk.Style()
        self.combo_estilo.theme_create(
            "combo_estilo",
            parent="alt",
            settings={
                "TCombobox": {
                    "configure": {
                        "selectforeground": "black",
                        "selectbackground": "lightgray"
                    }
                }
            }
        )
        self.combo_estilo.theme_use("combo_estilo")
        ent_nome_usuario_email.bind(
            '<KeyPress>',
            self.desativar_cor_fundo
        )
        
        # Exibir os dados de um usuário relembrado caso algum for selecionado da lista
        ent_nome_usuario_email.bind(
            '<<ComboboxSelected>>',
            lambda e: self.obter_usuario_relembrado(
                ent_nome_usuario_email,
                ent_senha)
        )
        # Desativar cor de fundo especial dos formulários quando o usuário digitar
        ent_nome_usuario_email.bind(
            '<KeyPress>',
            self.desativar_cor_fundo
        )
        # Passar o foco para o formulário de senha ao pressionar 'Enter';
        ent_nome_usuario_email.bind(
            '<KeyPress-Return>',
            lambda e: ent_senha.focus_force()
        )
        
        # Desativar cor de fundo especial dos formulários quando o usuário digitar
        ent_senha.bind(
            '<KeyPress>',
            self.desativar_cor_fundo
        )
        # Fazer Login ao pressionar 'Enter' com o foco no formulário de senha
        ent_senha.bind(
            '<KeyPress-Return>',
            lambda e: self.clique_entrar(ent_nome_usuario_email, ent_senha)
        )
        
        # Variável para guardar o valor do Checkbutton 'Lembrar de mim'
        self.lembrar = tk.BooleanVar(self)
        self.lembrar.set(True)
        
        # Criação e configurações da opção "Lembrar de mim"
        self.chk_lembrar = tk.Checkbutton(
            self.frm_campos,
            text="Lembrar de mim",
            variable=self.lembrar,
            onvalue=True,
            offvalue=False,
            anchor=tk.W
        )
        
        self.chk_lembrar.pack(side=tk.TOP, fill=tk.X)

        # Criação e configurações do botão 'Entrar'
        TkCustomWidget.criar_botao(self, "Entrar")  
        
        btn_entrar = self.children['frm_entrar'].children['btn_entrar']
        btn_entrar.configure(
            command=lambda: self.clique_entrar(ent_nome_usuario_email, ent_senha)
        )

        # Criação e configurações do link para criar um novo usuário
        texto = "Você ainda não tem uma conta?"
        TkCustomWidget.criar_link(self, texto, lambda e: self.master.mostrar_tela_cadastro())

    def desativar_cor_fundo(self, event):
        """
        Desativa a cor de fundo especial dos formulários.

        Args:
            event (_type_): _description_
        """
        self.combo_estilo.configure("TCombobox", fieldbackground="white")
        ent_senha = get_entry(self.frm_campos, 'frm_senha', 'ent_senha')
        ent_senha.configure(background='white')
        
    def mostrar_lista_usuarios_relembrados(self, formulario):
        """
        Exibe uma lista de usuários relembrados no formulário para nome de usuário.
        """
        banco_de_dados = self.master.banco_de_dados
        lista_usuarios_relembrados = banco_de_dados.obter_usuarios_relembrados("tk")
        nomes_relembrados = []
        
        for usuario in lista_usuarios_relembrados:
            nome_usuario = usuario[1]
            email = usuario[2]
            
            if formulario.get() in nome_usuario or formulario.get() in email:
                nomes_relembrados.append(nome_usuario)
                
        formulario.configure(values=nomes_relembrados)
            
    def obter_usuario_relembrado(self, ent_nome_usuario, ent_senha):
        """
        Obtém os dados de login de um usuário relembrado.
        
        Args:
            nome_usuario (_type_): _description_
        """
        banco_de_dados = self.master.banco_de_dados
        lista_usuarios_relembrados = banco_de_dados.obter_usuarios_relembrados("tk")
        nome_usuario = ent_nome_usuario.get()
        
        for usuario in lista_usuarios_relembrados:
            nome_usuario_relembrado = usuario[1]
            senha = usuario[3]
            
            if nome_usuario_relembrado == nome_usuario:
                ent_nome_usuario.delete(0, tk.END)
                ent_nome_usuario.insert(0, nome_usuario_relembrado)
                ent_senha.delete(0, tk.END)
                ent_senha.insert(0, senha)
        
        # Altera a cor de fundo da caixa de texto para senha 
        cor_fundo_destaque = get_hex_from_rgb(255, 255, 100)
        self.combo_estilo.configure("TCombobox", fieldbackground=cor_fundo_destaque)
        ent_senha.configure(background=cor_fundo_destaque)
        
    def clique_entrar(self, ent_nome_usuario, ent_senha):
        """
        Faz login ao clicar no botão "Entrar" com um nome de usuário ou email.

        Args:
            nome_usuario_email (str): O nome de usuário ou email para login.
            senha (str): A senha para login.

        Returns:
            None
        """
        txt_nome_usuario_email = ent_nome_usuario.get()
        txt_senha = ent_senha.get()
        
        banco_de_dados = self.master.banco_de_dados
        login = banco_de_dados.fazer_login(txt_nome_usuario_email, txt_senha)
        
        # O usuário faz login no sistema se os dados forem válidos
        if txt_nome_usuario_email == "" or txt_senha == "":
            messagebox.showerror("Erro!", "Todos os campos devem ser preenchidos!")
            for campo in (ent_nome_usuario, ent_senha):
                if campo.get() == "":
                    campo.focus_force()
                    return
        elif not login:
            messagebox.showerror("Erro!", "Usuário não encontrado!")
            self.combo_estilo.configure("TCombobox", fieldbackground="white")      
            ent_nome_usuario.delete(0,tk.END)
            ent_nome_usuario.focus_force()
            ent_senha.configure(background="white")
            ent_senha.delete(0,tk.END)
            ent_nome_usuario.focus_force()
        else:
            messagebox.showinfo("Bem-vindo!", "Login realizado com sucesso!")
            # Cadastra o usuário na tabela de usuários lembrados se os dados forem válidos
            if self.lembrar.get() == True:
                txt_criptografia = self.banco_de_dados.obter_senha_criptografada(
                    txt_nome_usuario_email,
                    txt_senha
                )
                lembrar = LembrarUsuario(
                    "tk",
                    banco_de_dados,
                    txt_nome_usuario_email,
                    txt_criptografia,
                    login
                )
                if lembrar:
                    messagebox.showwarning(
                        "Lembrar de mim!",
                        "Suas credenciais serão lembradas da próxima vez!"
                    )
        
            self.combo_estilo.configure("TCombobox", fieldbackground="white")            
            ent_nome_usuario.delete(0,tk.END)
            ent_nome_usuario.focus_force()
            ent_senha.configure(background="white")
            ent_senha.delete(0,tk.END)
        