
def listar_produtos(produtos):
    if produtos:
        
        print("\nLista de Produtos:")
        print("Escolha uma opção para filtrar ou ordenar os produtos:")
        print("1. Filtrar por categoria")
        print("2. Ordenar por nome")
        print("3. Ordenar por quantidade")
        print("4. Ordenar por preço")
        print("5. Mostrar todos os produtos sem filtro ou ordenação")
        
        opcao = input("\nDigite o número da opção desejada: ")

        if opcao == '1':
            categoria_filtro = input("Digite a categoria para filtrar: ").strip()
            produtos = [produto for produto in produtos if categoria_filtro.lower() in produto['categoria'].lower()]
        
        # Ordenar por nome
        elif opcao == '2':
            produtos = sorted(produtos, key=lambda p: p['nome'].lower())
        
        elif opcao == '3':
            produtos = sorted(produtos, key=lambda p: p['quantidade'])
        
        elif opcao == '4':
            produtos = sorted(produtos, key=lambda p: p['preco'])
        
        elif opcao == '5':
            pass  

        else:
            print("Opção inválida. Exibindo todos os produtos.")

        
        for produto in produtos:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}, Categoria: {produto['categoria']}, Quantidade: {produto['quantidade']}, Preço: R${produto['preco']:.2f}")
    
    else:
        print("Nenhum produto disponível.")
