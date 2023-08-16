# -*- coding: utf-8 -*-
"""Módulo para criar e administrar as regras de negócio do Banco de Dados."""

import bcrypt
import sqlite3


class BancoDeDados:
    """
    Classe para criar e administrar o Banco de Dados.
    """

    def __init__(self):
        """
        Inicializa a conexão com o Banco de Dados e cria a tabela de usuários.
        
        Args:
            None
        
        Returns:
            None
        """
        
        self.conexao = sqlite3.connect('usuarios.db')
        self.cursor = self.conexao.cursor()

        self.criar_tabela()
        
    def criar_tabela(self):
        """
        Cria a tabela de usuários se ela não existir.

        Args:
            None

        Returns:
            None
        """
        
        # Cria tabela de usuários se ela não existir
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_usuario VARCHAR(20) NOT NULL UNIQUE,
            email VARCHAR(150) NOT NULL UNIQUE,
            senha VARCHAR(64) NOT NULL
        )
        """)
        
        # Cria a tabela de usuários relembrados da aplicação Tk se ela não existir
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tk_usuarios_relembrados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
        )
        """)
        
        # Cria a tabela de usuários relembrados da aplicação Qt se ela não existir
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS qt_usuarios_relembrados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
        )                   
        """)
        
        # Cria a tabela de usuários relembrados da aplicação Kv se ela não existir
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS kv_usuarios_relembrados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            FOREIGN KEY (id_usuario) REFERENCES usuarios (id)
        )                   
        """)
        
        # Encerra a conexão com o Banco de Dados
        self.conexao.commit()
        
    def cadastrar_usuario(self, nome_usuario, email, senha):
        """
        Cadastra um novo usuário no Banco de Dados.

        Args:
            nome_usuario (str): O nome de usuário do novo usuário.
            email (str): O email do novo usuário.
            senha (str): A senha do novo usuário.

        Returns:
            None
        """
        
        self.cursor.execute("""
            INSERT INTO usuarios (nome_usuario, email, senha)
            VALUES (?, ?, ?)
        """, (nome_usuario, email, senha))

        self.conexao.commit()
    
    def verificar_criptografia(self, senha_inserida, senha_criptografada):
        """
        Verifica se a senha inserida pelo usuário é igual a senha criptografada no sistema.
        
        Args:
            senha_inserida (str): A senha inserida pelo usuário.
            senha_criptografada (str): A senha criptografada no banco de dados.
        
        Returns:
            bool: True se as senhas forem equivalentes ou False, caso contrário.
        """
        return bcrypt.checkpw(senha_inserida.encode(), senha_criptografada)
    
    def obter_senha_criptografada(self, nome_usuario_email, senha):
        """
        Retorna a senha criptografada do usuário solicitado.

        Args:
            nome_usuario_email (str): O nome de usuário ou email do usuário.
            senha (str): A senha do usuário.

        Returns:
            str: A senha criptografada do usuário ou False, caso o usuário não seja encontrado.
        """
        
        self.cursor.execute("""
            SELECT senha FROM usuarios WHERE (nome_usuario = ? OR email = ?)
        """, (nome_usuario_email, nome_usuario_email))

        criptografia = self.cursor.fetchone()[0]
        
        if bcrypt.checkpw(senha.encode(), criptografia):        
            return criptografia
        
    def fazer_login(self, nome_usuario_email, senha):
        """
        Realiza o login de um usuário no sistema.

        Args:
            nome_usuario_email (str): O nome de usuário ou email do usuário.
            senha (str): A senha do usuário.

        Returns:
            bool: True se o login for bem-sucedido, False caso contrário.
        """
        
        self.cursor.execute("""
            SELECT * FROM usuarios WHERE (nome_usuario = ? OR email = ?)
        """, (nome_usuario_email, nome_usuario_email))
        
        usuario = self.cursor.fetchone()
        
        if usuario:
            criptografia = usuario[3]
            teste = self.verificar_criptografia(senha, criptografia)
            
            if teste or senha.encode() == criptografia:
                return True
            
            return False
        else:
            return False
    
    def checar_id_usuario_relembrado(self, ui, id_usuario):
        """
        Procura por uma id de usuário cadastrada na lista de usuários relembrados.

        Args:
            id_usuario (_type_): A id de usuário a ser procurada.
        
        Returns:
            list / bool: Uma lista com os dados do usuário ou False.
        """
        self.cursor.execute(f"""
            SELECT * FROM {ui}_usuarios_relembrados WHERE id_usuario = ?
        """, (id_usuario,))
            
        return self.cursor.fetchone()
    
    def checar_nome_usuario_email_relembrado(self, ui, nome_usuario_email):
        """
        Procura por um nome de usuário ou e-mail cadastrada na lista de usuários relembrados.

        Args:
            nome_usuario_email (_type_): O nome ou e-mail do usuário a ser procurada.
        
        Returns:
            list / bool: Uma lista com os dados do usuário ou False.
        """
        self.cursor.execute(f"""
            SELECT * 
            FROM usuarios AS u
            JOIN {ui}_usuarios_relembrados AS ur ON u.id = ur.id_usuario
            WHERE u.nome_usuario = ? OR u.email = ?
        """, (nome_usuario_email, nome_usuario_email))
        
        return self.cursor.fetchone()
        
    def lembrar_usuario(self, ui, nome_usuario_email, senha):
        """
        Cadastra o usuário na tabela de usuários lembrados.

        Args:
            nome_usuario_email (str): O nome de usuário ou email a ser relembrado.
            senha (str): A senha do usuário a ser relembrado.
        
        Returns:
            None
        """
        # Verifica se o usuário está cadastrado no sistema
        self.cursor.execute("""
            SELECT * FROM usuarios WHERE (nome_usuario = ? OR email = ?) AND senha = ?
        """, (nome_usuario_email, nome_usuario_email, senha))

        # Armazena as credênciais do usuário se ele for válido
        usuario_cadastrado = self.cursor.fetchone()
        
        # Cadastra o usuário na lista de usuários lembrados se ele ainda não estiver cadastrado
        if usuario_cadastrado:
            # Obtém a id de usuário do usuário que foi verificado
            id_usuario = usuario_cadastrado[0]
            # Verifica se o usuário já está na lista de usuários lembrados
            usuario_na_lista = self.checar_id_usuario_relembrado(ui, id_usuario)
            
            # Cadastra o usuário caso ele ainda não esteja na lista de usuáios lembrados
            if not usuario_na_lista:
                self.cursor.execute(f"""
                    INSERT INTO {ui}_usuarios_relembrados (id_usuario) VALUES(?)
                """, (id_usuario,))
            
            self.conexao.commit()
    
    def obter_usuarios_relembrados(self, ui):
        """
        Obtém uma lista com os dados de todos os usuários relembrados.

        Args:
            ui (str): A interface gráfica (tk, kv, qt) para a qual os usuários foram relembrados.

        Returns:
            list: Uma lista de tuplas contendo os dados dos usuários relembrados.
        """
        self.cursor.execute(f"""
            SELECT id_usuario, nome_usuario, email, senha FROM usuarios AS u
            JOIN {ui}_usuarios_relembrados AS ur ON u.id = ur.id_usuario
        """)
        
        lista_usuarios_relembrados = self.cursor.fetchall()
        
        return lista_usuarios_relembrados
        
    def fechar_conexao(self):
        """
        Fecha a conexão com o Banco de Dados.

        Args:
            None

        Returns:
            None
        """
        
        self.conexao.close()
