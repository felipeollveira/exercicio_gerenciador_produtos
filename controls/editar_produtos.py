
from controls.salvar_produtos import salvar_produtos

def editar_produto(produtos):
    id_produto = input("Digite o ID do produto que deseja editar: ")
    produto_encontrado = None
    
    for produto in produtos:
        if produto['id'] == id_produto:
            produto_encontrado = produto
            break

    if produto_encontrado:
        print(f"Produto encontrado: {produto_encontrado['nome']}")
        
        novo_nome = input(f"Novo nome (atual: {produto_encontrado['nome']}): ")
        if not novo_nome: 
            novo_nome = produto_encontrado['nome']

       
        nova_categoria = input(f"Nova categoria (atual: {produto_encontrado['categoria']}): ")
        if not nova_categoria:  
            nova_categoria = produto_encontrado['categoria']


        while True:
            try:
                nova_quantidade = input(f"Nova quantidade (atual: {produto_encontrado['quantidade']}): ")
                if nova_quantidade == "":  
                    nova_quantidade = produto_encontrado['quantidade']
                    break
                else:
                    nova_quantidade = int(nova_quantidade)
                    if nova_quantidade >= 0:
                        break
                    else:
                        print("A quantidade não pode ser negativa. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido para a quantidade.")

        
        while True:
            try:
                novo_preco = input(f"Novo preço (atual: {produto_encontrado['preco']}): ")
                if novo_preco == "": 
                    novo_preco = produto_encontrado['preco']
                    break
                else:
                    novo_preco = float(novo_preco)
                    if novo_preco >= 0:  
                        break
                    else:
                        print("O preço não pode ser negativo. Tente novamente.")
            except ValueError:
                print("Por favor, insira um valor válido para o preço.")


        produto_encontrado['nome'] = novo_nome
        produto_encontrado['categoria'] = nova_categoria
        produto_encontrado['quantidade'] = nova_quantidade
        produto_encontrado['preco'] = novo_preco

        salvar_produtos(produtos)  
        print("Produto editado com sucesso!")
    else:
        print("Produto não encontrado.")
