const { loadProducts } = require("../data/data");

const listProducts = (rl, main) => {
    const products = loadProducts(); 

    rl.question("Deseja filtrar por categoria? (Digite uma categoria ou pressione Enter para não filtrar): ", (category) => {
        let filteredProducts = products;
        if (category) {
            filteredProducts = products.filter(product => product.category.toLowerCase().includes(category.toLowerCase()));
        }

     
        rl.question("Deseja ordenar os produtos? (Digite 'nome', 'quantidade' ou 'preco', ou pressione Enter para não ordenar): ", (orderOption) => {
            if (orderOption) {
                switch (orderOption.toLowerCase()) {
                    case "nome":
                        filteredProducts.sort((a, b) => a.name.localeCompare(b.name));
                        break;
                    case "quantidade":
                        filteredProducts.sort((a, b) => a.quantity - b.quantity);
                        break;
                    case "preco":
                        filteredProducts.sort((a, b) => a.price - b.price);
                        break;
                    default:
                        console.log("Opção de ordenação inválida.");
                        break;
                }
            }

          
            if (filteredProducts.length > 0) {
                console.log("\nProdutos encontrados:");
                filteredProducts.forEach(product => {
                    console.log(`ID: ${product.id} - Nome: ${product.name} - Categoria: ${product.category} - Quantidade: ${product.quantity} - Preço: R$ ${product.price.toFixed(2)}`);
                });
            } else {
                console.log("Nenhum produto encontrado com os critérios informados.");
            }

            
            main()
        });
    });
};

module.exports = listProducts;
