import json
import os

import os
import json

def carregar_produtos():
    if os.path.exists('produtos.json'):
        try:
            with open('produtos.json', 'r') as arquivo:
              
                conteudo = arquivo.read().strip() 
                if conteudo: 
                    return json.loads(conteudo)
                else:
                    return [] 
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON. Retornando lista vazia.")
            return []  
    else:
        return []  
