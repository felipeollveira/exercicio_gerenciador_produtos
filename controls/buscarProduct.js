const { loadProducts } = require("../data/data");

const searchProducts = (rl, main) => {
    rl.question("Digite o ID do produto ou parte do nome para buscar: ", (searchTerm) => {
        const products = loadProducts(); 
        const filteredProducts = products.filter(product => {
            return product.id.includes(searchTerm) || product.name.toLowerCase().includes(searchTerm.toLowerCase());
        });

        if (filteredProducts.length > 0) {
            console.log("\nProdutos encontrados:");
            filteredProducts.forEach(product => {
                console.log(`ID: ${product.id} - Nome: ${product.name}`);
            });
            main()
        } else {
            console.log("Nenhum produto encontrado com o termo informado.");
        }

        
    });
   
};

module.exports = searchProducts