const readline = require("readline");
const listProducts = require("./controls/listProducts");
const addProduct = require("./controls/addProduct");
const updateProduct = require("./controls/updateProduct");
const deleteProduct = require("./controls/deleteProduct");
const searchProducts = require("./controls/buscarProduct");

// Menu de opcoes
const showMenu = () => {
    console.log("\n=== Sistema de Gerenciamento de Produtos ===");
    console.log("1. Listar produtos");
    console.log("2. Buscar produto por ID ou nome");
    console.log("3. Adicionar produto");
    console.log("4. Atualizar produto");
    console.log("5. Excluir produto");
    console.log("6. Sair");
};

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const main = () => {
    showMenu();
    rl.question("Escolha uma opção: ", (option) => {
        switch (option) {
            case "1":
                listProducts(rl, main);
                break;
            case "2":
                searchProducts(rl, main);
                break;
            case "3":
                addProduct(rl, main);
                break;
            case "4":
                updateProduct(rl, main);
                break;
            case "5":
                deleteProduct(rl, main);
                break;
            case "6":
                console.log("Saindo do sistema...");
                rl.close(); 
                break;
            default:
                console.log("Opção inválida. Tente novamente.");
                main(); 
                break;
        }
    });
};



module.exports = {
    main,
    rl
};
