# controller.py
# -*- coding: utf-8 -*-
"""Módulo para administrar a relação entre as interfaces e o Banco de Dados."""

import bcrypt
import re


class LembrarUsuario:
    """
    Classe para administrar a inserção dos usuários lembrados.
    """

    def __init__(self, ui, banco_de_dados, nome_usuario_email, senha, login):
        """
        Inicializa um objeto LembrarUsuario.

        Args:
            ui (str): A interface gráfica (tk, kv, qt) para a qual o usuário está sendo relembrado.
            banco_de_dados (BancoDeDados): Instância do objeto BancoDeDados.
            nome_usuario_email (str): O nome de usuário ou email a ser relembrado.
            senha (str): A senha do usuário a ser relembrado.
            login (bool): Indica se é um processo de login (True) ou cadastro (False).
            
        Returns:
            None
        """
        self.login = login
        self.banco_de_dados = banco_de_dados
        self.nome_usuario_email = nome_usuario_email
        self.senha = senha
        
        if self.login:
            self.banco_de_dados.lembrar_usuario(ui, self.nome_usuario_email, self.senha)

class InsereDados:
    """
    Classe para administrar a inserção de dados nos campos de preenchimento.
    """

    def __init__(self, banco_de_dados, nome_usuario, email, senha):
        """
        Inicializa um objeto InsereDados.

        Args:
            banco_de_dados (BancoDeDados): Instância do objeto BancoDeDados.
            nome_usuario (str): O nome de usuário do novo usuário.
            email (str): O email do novo usuário.
            senha (str): A senha do novo usuário.
        
        Returns:
            None
        """
        self.banco_de_dados = banco_de_dados
        self.nome_usuario = nome_usuario
        self.email = email
        self.senha = senha
        
        self.senha_criptografada = self.gerar_criptografia(senha)
        
        if self.verificar_dados():
            self.banco_de_dados.cadastrar_usuario(self.nome_usuario, self.email, self.senha_criptografada)

    def verificar_dados(self):
        """
        Verifica se os dados são válidos e emite um erro caso algum deles não seja.

        Args:
            None
        
        Returns:
            bool: Retorna True se os dados forem válidos.
        Raises:
            ValueError: Erro lançado se algum dado for inválido.
        """
        try:
            self.verificar_nome_usuario(self.nome_usuario)        
            self.verificar_email(self.email)
            self.verificar_senha(self.senha)
        except ValueError as erro:
            raise erro
        
        return True
                
    def verificar_nome_usuario(self, nome_usuario):
        """
        Verifica se um nome de usuário é válido e emite um erro se não for.

        Args:
            nome_usuario (str): O nome de usuário a ser verificado.

        Raises:
            ValueError: Erro lançado se o nome de usuário for inválido.
        """
        padrao = r'^[A-Za-z0-9_]+$'
            
        if len(nome_usuario) < 3:
            raise ValueError('O nome de usuário deve ter no mínimo 3 caracteres!')
        
        elif len(nome_usuario) > 20:
            raise ValueError('O nome de usuário deve ter no máximo 20 caracteres!')
        
        elif not re.match(padrao, nome_usuario):
            raise ValueError('O nome de usuário não deve conter espaços ou caracteres especiais!')
        
        self.banco_de_dados.cursor.execute("""
            SELECT nome_usuario from usuarios WHERE(nome_usuario = ?)
        """, (nome_usuario,))
        
        usuario = self.banco_de_dados.cursor.fetchone()
        
        if usuario:
            raise ValueError(f"O nome de usuário '{nome_usuario}' já está em uso!")
        
    def verificar_email(self, email):
        """
        Verifica se um endereço de e-mail é válido e emite um erro se não for.

        Args:
            email (str): O email a ser verificado.

        Raises:
            ValueError: Erro lançado se o email for inválido.
        """
        padrao_email = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        
        if len(email) < 6:
            raise ValueError('O endereço de e-mail deve ter no mínimo 6 caracteres!')

        elif len(email) > 150:
            raise ValueError('O endereço de e-mail deve ter no máximo 150 caracteres!')
        
        elif not re.match(padrao_email, email):
            raise ValueError('O endereço de e-mail fornecido não é válido!')
        
        self.banco_de_dados.cursor.execute("""
            SELECT nome_usuario from usuarios WHERE(email = ?)
        """, (email,))
        
        usuario = self.banco_de_dados.cursor.fetchone()
        
        if usuario:
            raise ValueError(f"O endereço de e-mail '{email}' já está em uso!")
        
    def verificar_senha(self, senha):
        """
        Verifica se uma senha é válida e emite um erro se não for.

        Args:
            senha (str): A senha a ser verificada.

        Raises:
            ValueError: Erro lançado se a senha for inválida.
        """
        if len(senha) < 8:
            raise ValueError('A senha deve ter no mínimo 8 caracteres!')

        elif len(senha) > 64:
            raise ValueError('A senha deve ter no máximo 64 caracteres!')

    def gerar_criptografia(self, senha):
        """
        Gera uma senha criptografada usando técnicas de hash e salt.

        Args:
            senha (str): A senha do usuário.

        Returns:
            bytes: A senha criptografada.
        """
        salt = bcrypt.gensalt()
        senha_hasheada = bcrypt.hashpw(senha.encode(), salt)
        
        return senha_hasheada
