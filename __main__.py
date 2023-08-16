#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Módulo principal que inicia a demonstração de Cadastro e Login de Usuários.
Permite ao usuário escolher com qual interface gráfica iniciar.
"""

import os


print("Bem-vindo à demo de 'Cadastro e Login de Usuários' (Digite: tk=Tkinter, kv=Kivy, qt=PySide6)")
print("E-mail do autor: luizrdererita@gmail.com\n-")

while True:
    # Solicita que o usuário escolha a interface que o programa deverá abrir
    entrada = input("Com qual interface você deseja iniciar?\n>>> ")

    if entrada == 'tk':
        # Carrega o script da interface Tkinter
        with open(os.path.join("ui", "tk", "app.py")) as file:
            tk_script = file.read()

        # Executa o script da interface Tkinter
        exec(tk_script)

    elif entrada == 'kv':
        # Carrega o script da interface Kivy
        with open(os.path.join("ui", "kv", "app.py")) as file:
            kv_script = file.read()

        # Executa o script da interface Kivy
        exec(kv_script)

    elif entrada == 'qt':
        # Carrega o script da interface PySide6
        with open(os.path.join("ui", "qt", "app.py")) as file:
            qt_script = file.read()

        # Executa o script da interface PySide6
        exec(qt_script)

    elif entrada == 'exit':
        # Encerra o loop ao digitar 'exit'
        break

    else:
        # Emite um erro se o usuário digitar um comando inválido
        print("ERRO! Entrada inválida! Por favor, escolha uma UI ('tk', 'qt', 'kv') ou digite 'exit' para sair.")
        continue
    
    # Exibe uma mensagem de finalização após encerrar o programa
    print("Finalizando aplicação...")
    break
