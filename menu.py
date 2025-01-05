from controls import adicionar_produto, remover_produto, listar_produtos,editar_produto,buscar_produto, carregar_produtos

produtos = carregar_produtos()



def menu():
    while True:
       
        print("\033c", end="")

        print("--- Gerenciador de Produtos ---")
        print("Escolha uma opção:")
        print("1. Listar Produtos")
        print("2. Adicionar Produto")
        print("3. Editar Produto" )
        print("4. Remover Produto")
        print("5. Buscar Produto")
        print("6. Sair")

        # Entrada do usuário
        opcao = input("\nEscolha uma opção (1-6): ")


        if opcao == '1':
            listar_produtos(produtos)
        elif opcao == '2':
            adicionar_produto(produtos) 
        elif opcao == '3':
            editar_produto(produtos) 
        elif opcao == '4':
            remover_produto(produtos)  
        elif opcao == '5':
            buscar_produto(produtos) 
        elif opcao == '6':
            print("\nSaindo... Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
        
    
        input("\nPressione Enter para continuar...")
