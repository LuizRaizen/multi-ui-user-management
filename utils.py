# -*- coding: UTF-8 -*-
"""Módulo com algumas funções Utilitárias para automações de processos."""

import re
import unicodedata


def get_hex_from_rgb(r, g, b):
	""" Obtém um código hexadecimal á partir de uma sequência RGB """
	
	return '#%02x%02x%02x' %(r, g, b)
	

def remove_special_characters(string):
    # Remove todos os caracteres especiais que não são letras ou números
    
    string = re.sub(r'^[a-záàâãéèêíïóôõöúçñ ]+$/i', ' ', string)
    string = re.sub(r'[!:/;-]', '', string)
    
    return string
    

def to_snake_case(string):
    # Remove caracteres especiais
    string = remove_special_characters(string)

    # Remove acentos
    string = unicodedata.normalize("NFD", string)
    string = string.encode("ascii", "ignore")
    string = string.decode("utf-8")

    # Converte para letras minúsculas e remove espaços em branco
    string = string.lower().strip()

    # Substitui espaços em branco por underscores
    string = re.sub(r'\s+', '_', string)

    return string

