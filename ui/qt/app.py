# -*- coding: utf-8 -*-
"""Módulo para criar e administrar a interface gráfica na versão do PySide6."""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit, QCompleter

from ui.qt.screens import Ui_MainWindow
from database import BancoDeDados
from controller import InsereDados, LembrarUsuario
from constants import *


def obter_nomes_usuarios(usuarios):
    """
    Obtém uma lista com os nomes dos usuários relembrados.

    Args:
        usuarios (list): Uma lista com os dados dos usuários relembrados.
    
    Returns:
        nomes (list): Uma lista com os nomes dos usuários recebidos.
    """
    nomes= []
    for usuario in usuarios:
            nomes.append(usuario[1])
    
    return nomes


def autocompletar(root, opcoes, campo, comando):
    """
    Define as configurações da ferramenta de autocompletar (usuários relembrados)
    
    Args:
        root: (QWidget): O Widget pai do campo de texto.
        opcoes (list): Uma lista de opcoes para ser sugerida.
        campo (QLineEdit): O campo onde o recurso de autocompletar será integrado.
        comando (function): Um comando que será chamado em uma opção selecionada.
    
    Returns:
        None
    """
    completar = QCompleter(opcoes, root)
    completar.activated.connect(comando)
    campo.setCompleter(completar)
            
                
class QtApp(QMainWindow):
    
    def __init__(self):
        # Inicializa a superclasse 'QMainWindow'
        super().__init__()
        # Cria uma instância do Banco de Dados
        self.banco_de_dados = BancoDeDados()
        # Carrega e configura a interface gráfica
        self.carregar_ui()
        
    def carregar_ui(self):
        """
        Carrega e configura a interface gráfica.
        
        Args:
            None
            
        Returns:
            None
        """
        # Carrega o arquivo .py da interface gráfica
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Inicializa as definições gerais da tela de login
        self.configurar_tela_login()
        # Inicializa as definições gerais da tela de cadastro
        self.configurar_tela_cadastro()
        
    def configurar_tela_login(self):
        """
        Definições gerais da tela de login.
        
        Args:
            None
            
        Returns:
            None
        """
        # Passa o foco para o próximo campo se 'Enter' for pressionado no campo de nome de usuário
        self.ui.le_login_nome_usuario_email.returnPressed.connect(self.passar_foco)
        # Tenta fazer login se o foco estiver no campo de senha e 'Enter' for pressionado
        self.ui.le_login_senha.returnPressed.connect(self.clique_entrar)
        
        # Restaura cores padrão dos campos se digitar com um usuário relembrado selecionado
        self.ui.le_login_nome_usuario_email.textEdited.connect(self.restaurar_cor_padrao)
        self.ui.le_login_senha.textEdited.connect(self.restaurar_cor_padrao)
        
        # Obtém a lista com os dados dos usuários relembrados da tela 'qt'
        self.lista_usuarios_relembrados = self.banco_de_dados.obter_usuarios_relembrados("qt")
        # Obtém uma lista com os nomes dos usuários relembrados
        lista_nomes = obter_nomes_usuarios(self.lista_usuarios_relembrados)
        
        # Adiciona o recurso de autocompletar o campo de nome de usuário
        autocompletar(
            # Referênca a tela de login
            self,
            # Lista com os nomes dos usuários relembrados
            lista_nomes,
            # O campo de nome de usuário receberá o recurso de autocompletar
            self.ui.le_login_nome_usuario_email,
            # Ações que ocorrerão quando um nome da lista for selecionado 
            self.usuario_relembrado_selecionado
        )
        
        # Tenta fazer login quando clicar em 'Entrar'
        self.ui.btn_entrar.clicked.connect(self.clique_entrar)
        # Ir para a tela de cadastro quando clicar em 'Você ainda não tem uma conta?'
        self.ui.cl_criar_conta.clicked.connect(self.mostrar_tela_cadastro)
        
    def configurar_tela_cadastro(self):
        """
        Definições gerais da tela de cadastro.
        
        Args:
            None
            
        Returns:
            None
        """
        # Passa o foco para o próximo campo se 'Enter' for pressionado no campo de nome de usuário
        self.ui.le_cadastro_nome_usuario.returnPressed.connect(self.passar_foco)
        # Passa o foco para o próximo campo se 'Enter' for pressionado no campo de email
        self.ui.le_cadastro_email.returnPressed.connect(self.passar_foco)
        # Passa o foco para o próximo campo se 'Enter' for pressionado no campo de senha
        self.ui.le_cadastro_senha.returnPressed.connect(self.passar_foco)
        # Passa o foco para o próximo campo se 'Enter' for pressionado no campo de confirmação de senha
        self.ui.le_cadastro_confirmar_senha.returnPressed.connect(self.clique_cadastrar)
        # Tenta cadastrar os dados do usuário se clicar no botão 'Cadastrar'
        self.ui.btn_cadastrar.clicked.connect(self.clique_cadastrar)
        # Ir para a tela de login se clicar no link de comando 'Você já tem uma conta?'
        self.ui.cl_fazer_login.clicked.connect(self.mostrar_tela_login)
                
    def passar_foco(self):
        """
        Passa o foco para o próximo campo de preenchimento quando a tecla 'Enter' for digitada.
        
        Args:
            None
        
        Returns:
            None
        """
        # Encontre o widget que está com o foco atualmente
        current_widget = self.focusWidget()

        # Encontre o próximo widget na ordem de tabulação
        next_widget = current_widget.nextInFocusChain()

        # Verifique se o próximo widget é um QLineEdit
        while next_widget and not isinstance(next_widget, QLineEdit):
            next_widget = next_widget.nextInFocusChain()

        # Se houver um próximo QLineEdit, passe o foco para ele
        if next_widget:
            next_widget.setFocus()

    def definir_cor_personalizada(self):
        """
        Define uma cor personalizada para os campos de preenchimento do formulário.
            
        Returns:
            None
        """
        campos = (
            self.ui.le_login_nome_usuario_email,
            self.ui.le_login_senha
        )
        for campo in campos:
            campo.setStyleSheet(
                f"background-color: {C_LIGHTYELLOW}"    
            )
    
    def restaurar_cor_padrao(self):
        """
        Restaura a cor padrão dos campos de preenchimento do formulário.
            
        Returns:
            None
        """
        campos = (
            self.ui.le_login_nome_usuario_email,
            self.ui.le_login_senha
        )
        for campo in campos:
            campo.setStyleSheet(
                f"background-color: {C_WHITE}"    
            )
        
    def limpar_campos(self, *campos):
        """
        Limpa os campos de preenchimento do formulário.
        
        Args:
            campos (list): Os campos que terão suas informações apagados.
        Returns:
            None
        """
        for campo in campos:
            campo.setText("")
    
    def usuario_relembrado_selecionado(self, nome_usuario):
        """
        Completa automaticamente os dados do usuário relembrado selecionado da lista suspensa.
        
        Args:
            nome_usuario (str): Nome do usuário que foi selecionado no recurso de autocompletar.
        Returns:
            None
        """
        for usuario in self.lista_usuarios_relembrados:
            if usuario[1] == nome_usuario:
                senha = usuario[3]
                self.ui.le_login_nome_usuario_email.setText(nome_usuario)
                self.ui.le_login_senha.setText(senha.decode())
                # Altera a cor de fundo dos campos preenchidos pelo recurso autocompletar
                self.definir_cor_personalizada()

    def clique_entrar(self):
        """
        Faz login ao clicar no botão "Entrar" com um nome de usuário ou email.

        Args:
            None

        Returns:
            None
        """
        # Obtém as informações dos campos de login
        nome_usuario_email = self.ui.le_login_nome_usuario_email.text()
        senha = self.ui.le_login_senha.text()
        
        # Tenta logar no sistema se os dados forem válidos
        login = self.banco_de_dados.fazer_login(nome_usuario_email, senha)
        
        # Exibe uma menssagem de erro se os campos não forem preenchidos
        if nome_usuario_email == "" or senha == "":
            QMessageBox.critical(self, "Erro!", "Todos os campos devem ser preenchidos!")
            # Passa o foco para o primeiro campo sem preenchimento encontrado
            for campo in (self.ui.le_login_nome_usuario_email, self.ui.le_login_senha):
                if campo.text() == "":
                    campo.setFocus()
                    break
        # Exibe uma mensagem de erro se os dados não forem válidos
        elif not login:
            QMessageBox.critical(self, "Erro!", "Usuário não encontrado!")
            self.ui.le_login_nome_usuario_email.setFocus()
            self.limpar_campos(
                self.ui.le_login_nome_usuario_email,
                self.ui.le_login_senha
            )
        # Exibe uma mensagem de sucesso caso o usuário seja logado com sucesso
        else:
            QMessageBox.information(self, "Bem-vindo!", "Login lealizado com sucesso!")
            self.limpar_campos(
                self.ui.le_login_nome_usuario_email,
                self.ui.le_login_senha
            )
            # Cadastra o usuário na tabela de usuários lembrados se os dados forem válidos
            if self.ui.chk_lembrar_me.isChecked():
                criptografia = self.banco_de_dados.obter_senha_criptografada(
                    nome_usuario_email,
                    senha
                )
                lembrar = LembrarUsuario(
                    "qt",
                    self.banco_de_dados,
                    nome_usuario_email,
                    criptografia,
                    login
                )
                if lembrar:
                    QMessageBox.information(
                        self,
                        "Lembrar de mim!",
                        "Suas credenciais serão lembradas da próxima vez!"
                    )

                self.limpar_campos(
                    self.ui.le_login_nome_usuario_email,
                    self.ui.le_login_senha
                )
                self.ui.le_login_nome_usuario_email.setFocus()
        
        self.restaurar_cor_padrao()
    
    def clique_cadastrar(self):
        """
        Tenta cadastrar um usuário ao clicar no botão "Cadastrar".

        Args:
            None

        Returns:
            None
        """
        # Obtém as informações dos campos de cadastro
        nome_usuario = self.ui.le_cadastro_nome_usuario.text()
        email = self.ui.le_cadastro_email.text()
        senha = self.ui.le_cadastro_senha.text()
        confirmar_senha = self.ui.le_cadastro_confirmar_senha.text()
        
        # Realiza a validação dos dados antes do cadastro
        if not nome_usuario or not email or not senha or not confirmar_senha:
            QMessageBox.critical(self, "Erro!", "Todos os campos devem ser preenchidos!")
            if not nome_usuario:
                self.ui.le_cadastro_nome_usuario.setFocus()
            elif not email:
                self.ui.le_cadastro_email.setFocus()
            elif not senha:
                self.ui.le_cadastro_senha.setFocus()
            elif not confirmar_senha:
                self.ui.le_cadastro_confirmar_senha.setFocus()
            return
        
        # Verifica a confirmação de senha antes do cadastro
        if senha != confirmar_senha:
            QMessageBox.critical(self, "Erro!", "As senhas digitadas não são iguais!")
            self.limpar_campos(
                self.ui.le_cadastro_senha,
                self.ui.le_cadastro_confirmar_senha
            )
            self.ui.le_cadastro_senha.setFocus()
            return
        
        try:
            # Cadastro do usuário no sistema
            InsereDados(
                self.banco_de_dados,
                nome_usuario,
                email,
                senha
            )
            QMessageBox.information(
                self,
                "Cadastro realizado!",
                f"O usuário '{nome_usuario}' foi cadastrado com sucesso!"
            )
            # Limpa os campos de entrada após o cadastro bem-sucedido
            self.limpar_campos(
                self.ui.le_cadastro_nome_usuario,
                self.ui.le_cadastro_email,
                self.ui.le_cadastro_senha,
                self.ui.le_cadastro_confirmar_senha
            )
            
        except ValueError as erro:
            # Tratamento de outros erros específicos (se houver)
            mensagem_erro = str(erro)
            
            # Exibir mensagem de erro genérico caso não seja um erro específico tratado acima
            QMessageBox.critical(
                self,
                "Erro!",
                mensagem_erro
            )
            
            # Número mínimo de caracteres para o nome de usuário
            if "ter no mínimo 3 caracteres" in mensagem_erro:
                self.limpar_campos(
                    self.ui.le_cadastro_nome_usuario
                )
                self.ui.le_cadastro_nome_usuario.setFocus()
            
            # Número máximo de caracteres para o nome de usuário
            elif "ter no máximo 20 caracteres" in mensagem_erro:
                self.limpar_campos(
                    self.ui.le_cadastro_nome_usuario
                )
                self.ui.le_cadastro_nome_usuario.setFocus()
            
            # Especificação de caracteres para o nome de usuário
            elif "não deve conter espaços ou caracteres especiais" in mensagem_erro:
                self.limpar_campos(
                    self.ui.le_cadastro_nome_usuario
                )
                self.ui.le_cadastro_nome_usuario.setFocus()
            
            # Nome de usuário já foi utilizado
            elif "nome de usuário" in mensagem_erro and \
                "já está em uso" in mensagem_erro:
                self.limpar_campos(
                    self.ui.le_cadastro_nome_usuario
                )
                self.ui.le_cadastro_nome_usuario.setFocus()
            
            # Número mínimo de caracteres para o email
            elif "ter no mínimo 6 caracteres" in mensagem_erro:
                self.limpar_campos(
                    self.ui.le_cadastro_email
                )
                self.ui.le_cadastro_email.setFocus()
            
            # Número máximo de caracteres para o email
            elif "ter no máximo 150 caracteres" in mensagem_erro:
                self.limpar_campos(
                    self.ui.le_cadastro_email,
                )
                self.ui.le_cadastro_email.setFocus()
            
            # Número máximo de caracteres para o email
            elif "fornecido não é válido" in mensagem_erro:
                self.limpar_campos(
                    self.ui.le_cadastro_email,
                )
                self.ui.le_cadastro_email.setFocus()
            
            elif "e-mail" in mensagem_erro and \
                "já está em uso" in mensagem_erro:
                self.limpar_campos(
                    self.ui.le_cadastro_email,
                )
                self.ui.le_cadastro_email.setFocus()
            
            # Número mínimo de caracteres para a senha
            elif "ter no mínimo 8 caracteres" in mensagem_erro:
                self.limpar_campos(
                    self.ui.le_cadastro_senha,
                    self.ui.le_cadastro_confirmar_senha,
                )
                self.ui.le_cadastro_senha.setFocus()
            
            # Número máximo de caracteres para a senha
            elif "ter no mínimo 64 caracteres" in mensagem_erro:
                self.limpar_campos(
                    self.ui.le_cadastro_senha,
                    self.ui.le_cadastro_confirmar_senha,
                )
                self.ui.le_cadastro_senha.setFocus()
            
            # Erros desconhecidos
            else:
                self.limpar_campos(
                    self.ui.le_cadastro_nome_usuario,
                    self.ui.le_cadastro_email,
                    self.ui.le_cadastro_senha,
                    self.ui.le_cadastro_confirmar_senha,
                )
                self.ui.le_cadastro_nome_usuario.setFocus()
            return
        
        # Mostra a tela de login de usuários caso o cadastramento seja bem-sucedido
        self.mostrar_tela_login()

    def mostrar_tela_cadastro(self):
        """
        Ação a ser executada quando o link de comando 'Você não tem uma conta?' for clicado

        Args:
            None
        """
        self.ui.stk_telas.setCurrentWidget(self.ui.pg_tela_cadastro)
        self.limpar_campos(
            self.ui.le_login_nome_usuario_email,
            self.ui.le_login_senha
        )
        self.restaurar_cor_padrao()
        
    def mostrar_tela_login(self):
        """
        Ação a ser executada quando o link de comando 'Você já tem uma conta?' for clicado 
        
        Args:
            None
        """
        self.ui.stk_telas.setCurrentWidget(self.ui.pg_tela_login)
        self.limpar_campos(
            self.ui.le_cadastro_nome_usuario,
            self.ui.le_cadastro_email,
            self.ui.le_cadastro_senha,
            self.ui.le_cadastro_confirmar_senha
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QtApp()
    window.show()
    sys.exit(app.exec())
