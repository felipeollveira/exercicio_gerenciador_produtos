import json
import os

def salvar_produtos(produtos):
    try:
        caminho_arquivo = './data/products.json'
        
        os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
        
        with open(caminho_arquivo, 'w') as arquivo:
            json.dump(produtos, arquivo, indent=4)
    except Exception as e:
        print("erro no salvamento...")
