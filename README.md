# Sistema de Gerenciamento de Produtos - Python

Um sistema de gerenciamento de produtos em Python mantendo as informações salvas em um arquivo para garantir a persistência

---

## Funcionalidades

- **Listar produtos**: Mostra todos os produtos cadastrados no sistema.
- **Buscar produtos**: Permite buscar produtos por ID ou parte do nome.
- **Adicionar produto**: Adiciona novos produtos ao sistema.
- **Atualizar produto**: Atualiza as informações de um produto existente.
- **Excluir produto**: Remove um produto do sistema.
- **Persistência de Dados**: Os produtos são armazenados em um arquivo `products.json`.

---

## Requisitos

- **Python**: Versão 3.8+

---

## Instalação e Execução

1. Clone este repositório:
   ```bash
   git clone https://github.com/felipeollveira/exercicio_gerenciador_produtos/
   
2. Acesse a pasta do projeto:
   ```bash
   cd exercicio_gerenciador_produtos
   
3. Selecione a branch:
   ```bash
   git checkout python_project

3. Executar:
   ```bash
   py main.py

## Estrutura do Projeto

- menu.py: Modulo do menu 
- main.py: Arquivo principal que inicia o sistema e exibe o menu.
- controls/: Contém os módulos responsáveis pelas operações (adicionar, buscar, atualizar, excluir e listar produtos).
- data/: Contém o arquivo products.json, onde os dados dos produtos são armazenados.