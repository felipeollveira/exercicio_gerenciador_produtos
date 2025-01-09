# Sistema de Gerenciamento de Produtos - Python

Um sistema de gerenciamento de produtos em Python mantendo as informações salvas em um arquivo para garantir a persistência
Coloquei no gitignore a pasta com o arquivo para persistencia de dados, ela vai ser criada localmente na maquina do usuario

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
- **Modulos**: os e json

         os lida com operações de sistema operacional, como manipulação de arquivos e diretórios
         json é utilizado para manipular dados no formato JSON.

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
- data/: Contém o arquivo products.json, criada localmente e onde os dados dos produtos são armazenados.

## Mais Informações

Para mais informações sobre o projeto, acesse:

- **Python**: [Repositório Python Project](https://github.com/felipeollveira/exercicio_gerenciador_produtos/tree/python_project)  
- **Node.js**: [Repositório Node.js Project](https://github.com/felipeollveira/exercicio_gerenciador_produtos/tree/nodejs_project)
