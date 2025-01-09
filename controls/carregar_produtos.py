import json
import os

def carregar_produtos():
    caminho_arquivo = './data/products.json'
    

    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                conteudo = arquivo.read().strip()  
                if conteudo: 
                    return json.loads(conteudo)  
                else:
                    return []  
        except json.JSONDecodeError:
            print("Tente novamente... Há algum erro no armazenamento")
            return []  # Retorna lista vazia em caso de erro de decodificação
    else:
        return [] 