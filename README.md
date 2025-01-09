# Sistema de Gerenciamento de Produtos - NodeJS

Um sistema de gerenciamento de produtos em NodeJS mantendo as informações salvas em um arquivo para garantir a persistência

---

## Funcionalidades

- **Listar produtos**: Mostra todos os produtos cadastrados no sistema
- **Buscar produtos**: Permite buscar produtos por ID ou parte do nome.
- **Adicionar produto**: Adiciona novos produtos ao sistema.
- **Atualizar produto**: Atualiza as informações de um produto existente.
- **Excluir produto**: Remove um produto do sistema.
- **Persistência de Dados**: Os produtos são armazenados em um arquivo `products.json`.

---

## Requisitos

- **Node.js**: Versão 14.x ou superior.
- **Módulos**: 
  - **`fs`**: O módulo **`fs`** (File System) permite realizar operações de leitura e escrita em arquivos no sistema de arquivos.
  - **`path`**: O módulo **`path`** fornece utilitários para lidar com caminhos de arquivos e diretórios. Por exemplo, utilizo o path em data.js para informar o caminho do arquivo json onde sera armazenado os produtos

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
   git checkout nodejs_project

3. Executar:
   ```bash
   node index.js 
   ou 
   npm run start

## Estrutura do Projeto

- app.js: Modulo com as funcoes primarias como o menu e selecao das opcoes
- index.js: Arquivo principal que inicia o sistema.
- controls/: Contém os módulos responsáveis pelas operações (adicionar, buscar, atualizar, excluir e listar produtos).
- data/: Contém o arquivo products.json, onde os dados dos produtos são armazenados
- data.js: um modulo para tratar o dados que serao inseridos e retornados do arquivo json

## Mais Informações

Para mais informações sobre o projeto, acesse:

- **Python**: [Repositório Python Project](https://github.com/felipeollveira/exercicio_gerenciador_produtos/tree/python_project)  
- **Node.js**: [Repositório Node.js Project](https://github.com/felipeollveira/exercicio_gerenciador_produtos/tree/nodejs_project)
