from controls.salvar_produtos import salvar_produtos


import uuid

def adicionar_produto(produtos):
    print("\n--- Adicionar Novo Produto ---")
    
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria do produto: ")
    
    while True:
        try:
            quantidade = int(input("Digite a quantidade em estoque: "))
            if quantidade >= 0:
                break
            else:
                print("A quantidade não pode ser negativa. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido para a quantidade.")
    
  
    while True:
        try:
            preco = float(input("Digite o preço do produto: R$"))
            if preco >= 0:
                break
            else:
                print("O preço não pode ser negativo. Tente novamente.")
        except ValueError:
            print("Por favor, insira um valor válido para o preço.")

    id_produto = str(uuid.uuid4())
    
    novo_produto = {
        "id": id_produto,
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco
    }
    
    produtos.append(novo_produto)  
    salvar_produtos(produtos)  
    print(f"Produto '{novo_produto['nome']}' adicionado com sucesso!")


