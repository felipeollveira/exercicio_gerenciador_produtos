import json


def salvar_produtos(produtos):
    with open('produtos.json', 'w') as arquivo:
        json.dump(produtos, arquivo, indent=4)
    print("Produtos salvos no arquivo 'produtos.json' com sucesso!")

