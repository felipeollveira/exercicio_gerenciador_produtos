def buscar_produto(produtos):
    busca = input("Digite o ID completo ou parte do nome do produto: ")

    produtos_encontrados = [] 
    for produto in produtos:
       
        if produto['id'].lower().startswith(busca.lower()) or produto['nome'].lower().startswith(busca.lower()):
            produtos_encontrados.append(produto)

    if produtos_encontrados:
        print("\n--- Produtos Encontrados ---")
        for produto in produtos_encontrados:
            print(f"ID: {produto['id']}")
            print(f"Nome: {produto['nome']}")
            print(f"Categoria: {produto['categoria']}")
            print(f"Quantidade em Estoque: {produto['quantidade']}")
            print(f"Preço: R${produto['preco']:.2f}")
            print('-' * 30)  
    else:
        print("Nenhum produto encontrado. Verifique o ID ou tente uma parte do nome.")
