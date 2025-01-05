
from controls.salvar_produtos import salvar_produtos

def remover_produto(produtos):

    id_produto = input("Digite o ID do produto que deseja remover: ")
    produto_removido = None
    
    
    for produto in produtos:
        if produto['id'] == id_produto:
            produto_removido = produto
            break

    if produto_removido:
      
        confirmacao = input(f"Tem certeza que deseja remover o produto '{produto_removido['nome']}'? (y/n): ").strip().lower()
        
        if confirmacao == 'y':
            produtos.remove(produto_removido) 
            salvar_produtos(produtos)  
            print(f"Produto '{produto_removido['nome']}' removido com sucesso!")
        elif confirmacao == 'n':
            print("Remoção cancelada.")
        else:
            print("Opção inválida. Remoção cancelada.")
    else:
        print(f"Produto com ID {id_produto} não encontrado.")


