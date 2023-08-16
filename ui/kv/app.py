# -*- coding: utf-8 -*-
"""Módulo para criar e administrar a interface gráfica na versão do Kivy."""

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

kivy.require('2.2.1')

from database import BancoDeDados
from controller import InsereDados


class MessageBox(Popup):
    """
    Caixa de diálogo para exibição de mensagens.
    
    Está classe cria uma janela de diálogo para exibição de mensagens
    personalizadas.
    """

    def __init__(self, title, message, **kwargs):
        """
        Inicializador da classe MessageBox.
        
        Args:
            title (str): Título da janela.
            message (str): A mensagem que será exibida na caixa de diálogo.
            **kwargs: Argumentos adicionais que podem ser passados para o construtor
                      da classe `Popup`.
        
        Returns:
            None
        """
        # Inicializa os atributos da classe 'MessageBox'
        super(MessageBox, self).__init__(**kwargs)
        # Define o título da janela
        self.title = title
        # Define um tamanho absoluto para a caixa de diálogo
        self.size_hint = None, None
        self.size = 500, 180
        # Cria um 'BoxLayout' para acomodar os componentes da caixa de diálogo
        layout = BoxLayout(orientation="vertical", padding=(0, 20))
        # Cria e configura uma 'Label' para exibir a mensagem da caixa de diálogo
        label = Label(
            text=message,
            halign="center",
            valign="center",
            size_hint_y=None,
            height=80
        )
        # Cria e configura um botão para fechar a caixa de diálogo
        button = Button(
            text="Ok",
            size_hint=(None, None),
            size=(150, 35),
            pos_hint={'center_x': .5}
        )
        button.bind(on_release=self.dismiss)
        # Define a possibilidade de fechar a caixa de diálogo com um clique na tela
        self.bind(on_press=self.dismiss)
        # Adiciona a 'Label' e o 'Button' para o layout da caixa de diálogo
        layout.add_widget(label)
        layout.add_widget(button)

        # Define o conteúdo da caixa de diálogo
        self.content = layout


class Formulario(TextInput):
    """
    Campo de preenchimento.
    
    Esta classe representa um campo de preenchimento de texto interativo.
    Ela estende a classe `TextInput` do Kivy para fornecer funcionalidades
    adicionais relacionadas à interação com o teclado e foco.
    """

    def __init__(self, **kwargs):
        """
        Inicializador da classe Formulario.
        
        Args:
            **kwargs: Argumentos adicionais que podem ser passados para o construtor
                      da classe `TextInput`.
        
        Returns:
            None
        """
        # inicializa os atributos da classe 'TextInput'
        super(Formulario, self).__init__(**kwargs)
        # Obtém uma referência ao widget raiz do formulário
        self.root = None
        # Obtém uma referênia ao próximo formulário na cadeia de foco
        self.focus_next = None
        # Obtém uma lista de formulários na cadeia de foco (se houver)
        self.forms = None

    def _pressionou_backspace(self):
        """
        Manipula a tecla 'backspace' para remover o caractere anterior.
        
        Args:
            None
        
        Returns:
            None
        """
        # Obtém a posição atual do cursor do teclado
        cursor_pos = self.cursor[0]
        # Apaga o último caractere da string caso o cursor esteja no final
        if cursor_pos == len(self.text):
            self.text = self.text[:-1]
        # Apaga o caractere anterior á posição atual do cursor
        elif cursor_pos > 0 and cursor_pos < len(self.text):
            self.text = self.text[:cursor_pos - 1] + self.text[cursor_pos:]
        # Posiciona o cursor na posição do último caractere removido
        self.cursor = (cursor_pos - 1, 0)

    def login_pressionou_tab_enter(self, instance, keyboard, keycode, text):
        """
        Manipula os eventos de teclado para o formulário de login.

        Args:
            instance (TextInput): Instância do TextInput que chamou o método.
            keyboard (Keyboard): Instância do objeto Keyboard do Kivy.
            keycode (int): Código da tecla pressionada.
            text (str): Texto associado à tecla pressionada.
        """
        # Transfere o foco para o próximo formulário na cadeia de foco (se houver)
        if self.focus_next:
            if keyboard[1] == "enter":
                if self.text and self.focus_next.text:
                    if self.password:
                        self.root.clique_entrar(self.focus_next, self)
                    elif self.password == "*":
                        self.root.clique_entrar(self, self.focus_next)
                else:
                    self.focus_next.focus = True
        # Define o comportamento do formulário ao pressionar 'Tab'
        if keyboard[1] == "tab":
            if self.focus_next.focused:
                self.focus = True
            else:
                self.focus_next.focus = True
        # Define o comportamento do formulário ao pressionar 'Backspace'
        if keyboard[1] == "backspace":
            self._pressionou_backspace()
        # Define o comportamento do formulário ao pressionar a seta direita
        if keyboard[1] == "right":
            self.do_cursor_movement('cursor_right')
        # Define o comportamento do formulário ao pressionar a seta esquerda
        if keyboard[1] == "left":
            self.do_cursor_movement('cursor_left')

    def cadastro_pressionou_tab_enter(self, instance, keyboard, keycode, text):
        """
        Manipula os eventos de teclado para o formulário de cadastro.

        Args:
            instance (TextInput): Instância do TextInput que chamou o método.
            keyboard (Keyboard): Instância do objeto Keyboard do Kivy.
            keycode (int): Código da tecla pressionada.
            text (str): Texto associado à tecla pressionada.
        
        Returns:
            None
        """
        # Transfere o foco para o próximo formulário na cadeia de foco (se houver)
        if self.focus_next:
            if keyboard[1] == "enter":
                if all(form.text for form in self.forms):
                    self.root.clique_cadastrar(*self.forms)
                else:
                    self.focus_next.focus = True
        # Define o comportamento do formulário ao pressionar 'Tab'
        if keyboard[1] == "tab":
            if self.focus_next.focused:
                self.focus = True
            else:
                self.focus_next.focus = True
        # Define o comportamento do formulário ao pressionar 'Backspace'
        if keyboard[1] == "backspace":
            self._pressionou_backspace()

    
class TelaDeLogin(BoxLayout):
    """
    Tela de login
    
    Classe para criar e configurar o comportamento e aparência da tela
    para login de usuários.
    """
    
    def __init__(self, app, banco_de_dados):
        """
        Inicializador da tela de login
        
        Args:
            app (KvApp): Instância da classe principal da aplicação.
            banco_de_dados (BancoDeDados): Instância do banco de dados.

        Returns:
            None
        """
        # Inicializa a classe 'BoxLayout'
        super().__init__()
        # Obtém uma referência á classe principal da aplicação
        self.app = app
        # Obtém uma referência ao banco de dados
        self.banco_de_dados = banco_de_dados

    def clique_entrar(self, inp_nome_usuario_email, inp_senha):
        """
        Faz login ao clicar no botão "Entrar" com um nome de usuário ou email.
        
        Args:
            inp_nome_usuario_email (_type_):
            inp_email (_type_):
            
        Returns:
            None
        """
        # Tenta fazer login no sistema com os dados fornecidos pelo usuário
        login = self.banco_de_dados.fazer_login(
            inp_nome_usuario_email.text,
            inp_senha.text
        )
        # Exibe uma mensagem para notificar se o login foi bem-sucedido
        if login:
            # Informa que a opção 'Lembrar de mim' não está habilitada
            if self.ids.chk_lembrar_me.ids.check.active:
                self.app.show_info_message(
                    "Atenção!",
                    "Desculpe, mas a opção 'Lembrar de mim' não está habilitada!"
                )
            # Informa que o login foi bem sucedido se as credênciais forem válidas
            self.app.show_info_message("Bem-vindo!", "Usuário logado com sucesso!")
        else:
            # Informa que o usuário não é válido se as credênciais forem inválidas
            self.app.show_error_message("Erro!", "Usuário não encontrado!")
        
        # Limpa os campos de preenchimento do formulário após o procedimento
        self.app.layout_principal.limpar_campos(inp_nome_usuario_email, inp_senha)
        

class TelaDeCadastro(BoxLayout):
    """
    Tela de cadastro
    
    Classe para criar e configurar o comportamento e parência da a tela
    para cadastro de usuários.
    """
    
    def __init__(self, app, banco_de_dados, **kwargs):
        """_sumary_
        
        Args:
            app (KvApp): Instância da classe principal da aplicação.
            banco_de_dados (BancoDeDados): Instância do banco de dados.

        Returns:
            None
        """
        # Inicializa a classe 'BoxLayout'
        super(TelaDeCadastro, self).__init__(**kwargs)
        # Obtém uma referência da classe principal da aplicação
        self.app = app
        # Obtém uma referência do banco de dados
        self.banco_de_dados = banco_de_dados

    def clique_cadastrar(self, inp_nome_usuario, inp_email, inp_senha, inp_confirmar_senha):
        """
        Tenta cadastrar um usuário ao clicar no botão "Cadastrar" com um nome de usuário ou email.
        
        Args:
            inp_nome_usuario (Formulario):
            inp_email (Formulario):
            inp_senha (Formulario):
            inp_confirmsr_senha (Formulario):
        
        Returns:
            None
        """
        # Obtém referências das informações contidas nos campos de preenchimento
        nome_usuario = inp_nome_usuario.text
        email = inp_email.text
        senha = inp_senha.text
        confirmar_senha = inp_confirmar_senha.text
        focus_next = False
        
        # Emite um erro caso algum campo não tenha sido preenchido
        if not nome_usuario or not email or not senha or not confirmar_senha:
            for campo in (inp_nome_usuario, inp_email, inp_senha, inp_confirmar_senha):
                if not campo.text:
                    focus_next = campo
                    break
            self.app.show_error_message(
                "Erro!",
                "Todos os campos devem ser preenchidos!",
            )
            return
        # Emite um erro caso o teste da confirmação de senha falhe
        elif senha != confirmar_senha:
            self.app.show_error_message("Erro!", "As senhas não são iguais!")
            return
        
        # Tenta cadastrar o usuário no sistema
        try:
            InsereDados(
                self.banco_de_dados,
                nome_usuario,
                email,
                senha
            )
            # Informa que o cadastro foi bem-secedido se as informações forem válidas
            self.app.show_info_message(
                "Usuário criado!",
                f"O usuário '{nome_usuario}' foi cadastrado com sucesso!"
            )
        # Trata possíveis erros encontrados no cadastramento 
        except ValueError as erro:
            # Emite uma mensagem de erro informando o problema ocorrido
            mensagem_erro = str(erro)
            self.app.show_error_message("Erro!", mensagem_erro)
            
            # Transfere o foco para o campo de nome de usuário caso haja algum problema
            if "ter no mínimo 3 caracteres" in mensagem_erro:
                self.app.layout_principal.limpar_campos(
                    inp_nome_usuario,
                )
                inp_nome_usuario.focus = True
            elif "ter no máximo 20 caracteres" in mensagem_erro:
                self.app.layout_principal.limpar_campos(
                    inp_nome_usuario,
                )
                inp_nome_usuario.focus = True
            elif "não deve conter espaços ou caracteres especiais" in mensagem_erro:
                self.app.layout_principal.limpar_campos(
                    inp_nome_usuario,
                )
                inp_nome_usuario.focus = True
            elif "nome de usuário" in mensagem_erro and \
                "já está em uso" in mensagem_erro:
                self.app.layout_principal.limpar_campos(
                    inp_nome_usuario,
                )
                inp_nome_usuario.focus = True
            elif "ter no mínimo 6 caracteres" in mensagem_erro:
                self.app.layout_principal.limpar_campos(
                    inp_email,
                )
                inp_email.focus = True
                
            # Transfere o foco para o campo de email caso haja algum problema
            elif "ter no máximo 150 caracteres" in mensagem_erro:
                self.app.layout_principal.limpar_campos(
                    inp_email,
                )
                inp_email.focus = True
            elif "fornecido não é válido" in mensagem_erro:
                self.app.layout_principal.limpar_campos(
                    inp_email,
                )
                inp_email.focus = True
            elif "e-mail" in mensagem_erro and \
                "já está em uso" in mensagem_erro:
                self.app.layout_principal.limpar_campos(
                    inp_email,
                )
                inp_email.focus = True
                
            # Transfere o foco para o campo de senha caso haja algum problema
            elif "ter no mínimo 8 caracteres" in mensagem_erro:
                self.app.layout_principal.limpar_campos(
                    inp_senha,
                    inp_confirmar_senha,
                )
                inp_senha.focus = True
            elif "ter no máximo 64 caracteres" in mensagem_erro:
                self.app.layout_principal.limpar_campos(
                    inp_senha,
                    inp_confirmar_senha,
                )
                inp_senha.focus = True
            elif "ter no mínimo 8 caracteres" in mensagem_erro:
                self.app.layout_principal.limpar_campos(
                    inp_senha,
                    inp_confirmar_senha,
                )
                inp_senha.focus = True
            else:
                self.app.layout_principal.limpar_campos(
                    inp_nome_usuario,
                    inp_email,
                    inp_senha,
                    inp_confirmar_senha,
                )
            return
                        
        # Mostra a tela de login de usuários
        self.app.layout_principal.mostrar_tela_login()

    
class LayoutPrincipal(FloatLayout):
    """
    Layout principal da aplicação
    
    Classe para criar e configurar o layout que acomoda os componentes
    da aplicação.
    """
    
    def __init__(self, app):
        """
        Inicialização da classe LayoutPrincipal

        Args:
            app (MainApp): Uma referência á classe principal da aplicação.
            
        Returns:
            None
        """
        # Inicializa os atributos da classe FloatLayout
        super().__init__()
        # Obtém a referência á classe principal da aplicação
        self.app = app
        # Obtém uma refência ao banco de dados
        self.banco_de_dados = BancoDeDados()
        # Cria uma instância da tela de login
        self.tela_login = TelaDeLogin(self.app, self.banco_de_dados)
        # Cria uma instância da tela de cadastro
        self.tela_cadastro = TelaDeCadastro(self.app, self.banco_de_dados)
        # Exibe a tela de login
        self.mostrar_tela_login()

    def passar_foco(self, key, widget):
        """
        Transfere o foco para um widget especificado no argumento 'widget'.

        Args:
            widget (Widget): A instância de um widget do kivy.
            
        Returns:
            None
        """
        if key == ord('tab'):
            widget.focus = True
        
    def mostrar_tela_cadastro(self):
        """
        Mostra a tela de cadastro de usuários.
        
        Args:
            None
        
        Returns:
            None
        """
        # Oculta a tela de login
        self.remove_widget(self.tela_login)
        # Exibe a tela de cadastro
        self.add_widget(self.tela_cadastro)
        # Obtém uma referência das ids da tela de login
        ids = self.tela_login.ids
        # Limpa os campos de preenchimento da tela de login
        self.limpar_campos(
            ids.inp_login_nome_usuario_email,
            ids.inp_login_senha
        )
        # Transfere o foco para o campo de nome de usuário da tela de cadastro
        self.tela_cadastro.ids.inp_cadastro_nome_usuario.focus = True
            
    def mostrar_tela_login(self):
        """
        Mostra a tela de cadastro de usuários.
        
        Args:
            None
            
        Returns:
            None
        """
        # Oculta a tela de cadastro
        self.remove_widget(self.tela_cadastro)
        # Exibe a tela de login
        self.add_widget(self.tela_login)
        # Obtém uma referência das ids da tela de cadastro
        ids = self.tela_cadastro.ids
        # Limpa os campos de preenchimento da tela de cadastro
        self.limpar_campos(
            ids.inp_cadastro_nome_usuario,
            ids.inp_cadastro_email,
            ids.inp_cadastro_senha,
            ids.inp_cadastro_confirmar_senha
        )
        # Trsnsfere o foco para o campo de nome de usuário da tela de login
        self.tela_login.ids.inp_login_nome_usuario_email.focus = True
        
    def limpar_campos(self, *campos):
        """
        Limpa os campos de preenchimento de um formulário.

        Returns:
            None
        """
        for campo in campos:
            campo.text = ""
        

class MainApp(App):
    """
    Classe principal da interface do Kivy.
    """
    
    def show_error_message(self, titulo, mensagem):
        """
        Exibe um diálogo com uma mensagem de erro.
        
        Args:
            titulo (str): O título da caixa de diálogo
            mensagem (str): A mensage mda caixa de diálogo
        
        Returns:
            None
        """
        # Cria a caixa de diálogo
        popup = MessageBox(titulo, mensagem)
        # Exibe a mensagem na tela
        popup.open(animation=True)
        
    def show_info_message(self, titulo, mensagem):
        """
        Exibe um diálogo com uma mensagem informativa.
        
        Args:
            titulo (str): O título da caixa de diálogo
            mensagem (str): A mensage mda caixa de diálogo
        
        Returns:
            None
        """
        # Cria a caixa de diálogo
        popup = MessageBox(titulo, mensagem)
        # Exibe a mensagem na tela
        popup.open(animation=True)
        
    def build(self):
        """
        Construtor da aplicação Kv
        
        Args:
            None
            
        Returns:
            None
        """
        # Define o título da janela
        self.title = "Tela de Cadastro e Login de Usuários"
        # Cria uma instância do layout principal da aplicação
        self.layout_principal = LayoutPrincipal(self)
        # Retorna o widget principal da aplicação para o kivy
        return self.layout_principal
    
    
if __name__ == '__main__':
    MainApp().run()
