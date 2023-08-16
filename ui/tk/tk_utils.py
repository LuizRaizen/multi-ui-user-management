# -*- coding: utf-8 -*-

"""Módulo para automatizar a criação de widgets personalizados do Tkinter."""

import os
import sys
import tkinter as tk
from tkinter import ttk

from utils import get_hex_from_rgb, to_snake_case


def get_entry(master, frame_name, form_name):
    """ 
    Obtém um widget a partir dos nomes de seus frames pai e próprio, respectivamente.

    Args:
        master (tk.Tk or tk.Frame): O container onde o widget está localizado.
        nome_frame (str): O nome do frame que contém o widget.
        nome_formulario (str): O nome do widget a ser obtido.

    Returns:
        tk.Entry: O widget de entrada obtido.
    """
    
    return master.children[frame_name].children[form_name]


def clear_entries(frame):
    """
    Limpa todos os formulários dentro de um frame específico
    """
    
    for frm in frame.children.values():
        for id, ent in frm.children.items():
            if "ent_" in id:
                ent.delete(0, tk.END)
                    
                    
class TkCustomWidget:    
    """Classe para criação de widgets personalizados do Tkinter."""

    @staticmethod
    def criar_titulo(master, texto):
        """
        Cria um título personalizado na tela.

        Args:
            master (tk.Tk or tk.Frame): O container onde o título será exibido.
            texto (str): O texto do título.

        Returns:
            None
        """
        
        id = to_snake_case(texto)
        container = tk.Frame(master, name="frm_"+id, border=1, pady=20)
        container.pack()
        titulo = tk.Label(container, text=texto, font="Roboto 16 bold")
        titulo.pack(side=tk.TOP)

    @staticmethod
    def criar_link(master, texto, funcao):
        """
        Cria um link interativo na tela.

        Args:
            master (tk.Tk or tk.Frame): O container onde o link será exibido.
            texto (str): O texto do link.
            funcao (callable): A função a ser executada ao clicar no link.

        Returns:
            None
        """
        
        frm_link = tk.Frame(master, pady=20)
        frm_link.pack(side=tk.BOTTOM)
        link_create_account = tk.Label(
            frm_link,
            text=texto,
            font="Roboto 10 underline",
            fg=get_hex_from_rgb(0, 60, 255),
        )
        link_create_account.bind("<Button-1>", funcao)
        link_create_account.pack()

    @staticmethod
    def criar_botao(master, texto):
        """
        Cria um botão personalizado na tela.

        Args:
            master (tk.Tk or tk.Frame): O container onde o botão será exibido.
            texto (str): O texto do botão.

        Returns:
            None
        """
        
        id = to_snake_case(texto)
        cor_ativo = get_hex_from_rgb(50, 200, 50)
        cor_normal = get_hex_from_rgb(0, 180, 0)
        frm_botao = tk.Frame(master, name='frm_'+id, pady=20)
        frm_botao.pack()
        botao = tk.Button(
            frm_botao,
            name='btn_'+id,
            text=texto,
            font="Helvetica 16",
            foreground="#FFF",
            activeforeground="#FFF",
            background=cor_normal,
            activebackground=cor_ativo,
            padx=20,
            pady=5,
        )
        botao.pack(side=tk.BOTTOM)

class TkCustomForm:
    """Classe para criação de rótulos e campos de entrada (formulários)."""

    def __init__(self, master, formularios, lado):
        """
        Inicializa o formulário.

        Args:
            master (tk.Tk or tk.Frame): O container onde o formulário será exibido.
            campos (list): Uma lista com os nomes dos campos do formulário.
            lado (str): O lado de exibição do formulário ('left' ou 'right').

        Returns:
            None
        """
        
        self.master = master
        self.formularios = []
        self.listas = []
        
        for formulario in formularios:
            if type(formulario) in (tuple, list) and 'list' in formulario:
                self.listas.append(formulario)
            else:
                self.formularios.append(formulario)
            
            self.lado = lado
        
        if self.listas:
            self.criar_listas()
        if self.formularios:
            self.criar_formularios()
        
    def criar_formularios(self):
        """
        Cria os rótulos e campos de entrada do formulário.

        Args:
            None

        Returns:
            None
        """
        
        esconder_senha = False
        
        for formulario in self.formularios:
            if "*" in formulario:
                formulario = formulario.replace("*", "")
                esconder_senha = True
                          
            id = to_snake_case(formulario)
            
            container = tk.Frame(self.master, name="frm_" + id, width=20)
            container.pack(side=self.lado, ipady=5)
            
            rotulo = tk.Label(container, name="lbl_" + id, text=formulario, anchor=tk.W)
            rotulo.pack(side=tk.TOP, fill=tk.X)
            ttk.Combobox()
            entrada = tk.Entry(container, name="ent_" + id, width=30)
            if esconder_senha:
                entrada.configure(show="*")    
            entrada.pack(side=tk.TOP, ipadx=2, ipady=2)
            
    def criar_listas(self):
        """
        Cria os rótulos e campos de entrada da lista.

        Args:
            None

        Returns:
            None
        """
        
        esconder_senha = False
        
        for formulario in self.listas:
            formulario = formulario[0]
            if "*" in formulario:
                formulario = formulario.replace("*", "")
                esconder_senha = True
            
            id = to_snake_case(formulario)
            
            container = tk.Frame(self.master, name="frm_" + id, width=20)
            container.pack(side=self.lado, ipady=5)
            rotulo = tk.Label(container, name="lbl_" + id, text=formulario, anchor=tk.W)
            rotulo.pack(side=tk.TOP, fill=tk.X)
            
            entrada = ttk.Combobox(container, name="ent_" + id, width=29)
            if esconder_senha:
                entrada.configure(show="*")    
            entrada.pack(side=tk.TOP, ipadx=2, ipady=2)
