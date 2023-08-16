# -*- coding: utf-8 -*-
"""Módulo para criação da interface gráfica do Cadastro de Usuários com o framework Tkinter."""

import tkinter as tk

from tkinter import messagebox

from ui.tk.tk_utils import TkCustomWidget, TkCustomForm, get_entry
from controller import InsereDados


class TelaDeCadastro(tk.Frame):
    """
    Classe que representa a tela de cadastro de usuários.

    Attributes:
        ...
    """

    def __init__(self, *args, **kwargs):
        """
        Inicializa a tela de cadastro.

        Args:
            *args: Argumentos posicionais para tk.Frame.
            **kwargs: Argumentos nomeados para tk.Frame.

        Returns:
            None
        """
        
        super().__init__(*args, **kwargs)

        # Instância do Banco de Dados
        self.banco_de_dados = self.master.banco_de_dados
        
        # Título da Tela de Cadastro
        TkCustomWidget.criar_titulo(self, "Criar usuário")

        # Cria e configura os formulários
        self.frm_campos = tk.Frame(self, pady=30)
        self.frm_campos.pack()

        campos = ["Nome de usuário:", "E-mail:", "Senha:*", "Confirmar senha:*"]
        TkCustomForm(self.frm_campos, campos, tk.TOP)

        # Cria e configura o botão 'Entrar'
        TkCustomWidget.criar_botao(self, "Cadastrar")
        
        # Obtém as instâncias dos formulários
        ent_nome_usuario = get_entry(
            self.frm_campos,
            'frm_nome_de_usuario', 
            'ent_nome_de_usuario',
        )
        ent_email = get_entry(
            self.frm_campos,
            'frm_email',
            'ent_email'
        )
        ent_senha = get_entry(
            self.frm_campos,
            'frm_senha',
            'ent_senha'
        )
        ent_confirmar_senha = get_entry(
            self.frm_campos,
            'frm_confirmar_senha',
            'ent_confirmar_senha'
        )
        
        # Adiciona as interações de teclado aos formulários
        ent_nome_usuario.bind(
            '<KeyPress-Return>',
            lambda e: ent_email.focus_force()
        )
        ent_email.bind(
            '<KeyPress-Return>',
            lambda e: ent_senha.focus_force()
        )
        ent_senha.bind(
            '<KeyPress-Return>',
            lambda e: ent_confirmar_senha.focus_force()
        )
        ent_confirmar_senha.bind(
            '<KeyPress-Return>',
            lambda e: self.clique_cadastrar(ent_nome_usuario,
                                     ent_email,
                                     ent_senha,
                                     ent_confirmar_senha)
        )

        btn_cadastrar = self.children['frm_cadastrar'].children['btn_cadastrar']
        
        btn_cadastrar.configure(
            command=lambda: self.clique_cadastrar(ent_nome_usuario,
                                                  ent_email,
                                                  ent_senha,ent_confirmar_senha)
        )

        # Cria e configura o link para fazer login
        texto = "Você já tem uma conta?"
        TkCustomWidget.criar_link(self, texto, lambda e: self.master.mostrar_tela_login())

    def clique_cadastrar(self, ent_nome_usuario, ent_email, ent_senha, ent_confirmar_senha):
        """
        Cadastra um novo usuário no Banco de Dados.

        Args:
            nome_usuario (str): O nome de usuário para cadastro.
            email (str): O email para cadastro.
            senha (str): A senha para cadastro.
            confirmar_senha (str): A confirmação da senha para cadastro.

        Returns:
            None
        """
        
        nome_usuario = ent_nome_usuario.get()
        email = ent_email.get()
        senha = ent_senha.get()
        confirmar_senha = ent_confirmar_senha.get()
        
        # Realiza a validação dos dados antes do cadastro
        if not nome_usuario or not email or not senha or not confirmar_senha:
            messagebox.showerror("Erro!", "Todos os campos devem ser preenchidos!")
            if not nome_usuario:
                ent_nome_usuario.focus_force()
            elif not email:
                ent_email.focus_force()
            elif not senha:
                ent_senha.focus_force()
            elif not confirmar_senha:
                ent_confirmar_senha.focus_force()
            return
        
        elif senha != confirmar_senha:
            messagebox.showerror("Erro!", "As senhas digitadas não são iguais!")
            ent_senha.delete(0, tk.END)
            ent_confirmar_senha.delete(0, tk.END)
            ent_senha.focus_force()
            return
        
        try:
            # Cadastro do usuário no sistema
            InsereDados(self.banco_de_dados, nome_usuario, email, senha)
            messagebox.showinfo(
                "Cadastro realizado!",
                f"O usuário '{nome_usuario}' foi cadastrado com sucesso!"
            )
            
            # Limpa os campos de entrada após o cadastro bem-sucedido
            ent_nome_usuario.delete(0, tk.END)
            ent_email.delete(0, tk.END)
            ent_senha.delete(0, tk.END)
            ent_confirmar_senha.delete(0, tk.END)
            
        except ValueError as erro:
            # Tratamento de outros erros específicos (se houver)
            mensagem_erro = str(erro)
            messagebox.showerror("Erro!", mensagem_erro)
            
            if "ter no mínimo 3 caracteres" in mensagem_erro:
                ent_nome_usuario.delete(0, tk.END)
                ent_nome_usuario.focus_force()
            elif "ter no máximo 20 caracteres" in mensagem_erro:
                ent_nome_usuario.delete(0, tk.END)
                ent_nome_usuario.focus_force()
            elif "não deve conter espaços ou caracteres especiais" in mensagem_erro:
                ent_nome_usuario.delete(0, tk.END)
                ent_nome_usuario.focus_force()
            elif "nome de usuário" in mensagem_erro and \
                "já está em uso" in mensagem_erro:
                ent_nome_usuario.delete(0, tk.END)
                ent_nome_usuario.focus_force()
            elif "ter no mínimo 6 caracteres" in mensagem_erro:
                ent_email.delete(0, tk.END)
                ent_email.focus_force()
            elif "ter no máximo 150 caracteres" in mensagem_erro:
                ent_email.delete(0, tk.END)
                ent_email.focus_force()
            elif "fornecido não é válido" in mensagem_erro:
                ent_email.delete(0, tk.END)
                ent_email.focus_force()
            elif "e-mail" in mensagem_erro and \
                "já está em uso" in mensagem_erro:
                ent_email.delete(0, tk.END)
                ent_email.focus_force()
            elif "ter no mínimo 8 caracteres" in mensagem_erro:
                ent_senha.delete(0, tk.END)
                ent_confirmar_senha.delete(0, tk.END)
                ent_senha.focus_force()
            elif "ter no máximo 64 caracteres" in mensagem_erro:
                ent_senha.delete(0, tk.END)
                ent_confirmar_senha.delete(0, tk.END)
                ent_senha.focus_force()
            elif "ter no mínimo 8 caracteres" in mensagem_erro:
                ent_senha.delete(0, tk.END)
                ent_confirmar_senha.delete(0, tk.END)
                ent_senha.focus_force()
            else:
                ent_nome_usuario.delete(0, tk.END)
                ent_email.delete(0, tk.END)
                ent_senha.delete(0, tk.END)
                ent_confirmar_senha.delete(0, tk.END)
            return
                        
        # Mostra a tela de login de usuários
        self.master.mostrar_tela_login()
