const { loadProducts } = require("../data/data");

const listProducts = () => {
    const products = loadProducts();
    if (products.length === 0) {
        console.log("\nNenhum produto cadastrado.");
    } else {
        console.log("\n=== Lista de Produtos ===");
        products.forEach((product, index) => {
            console.log(
                `${index + 1}. [ID: ${product.id}] Nome: ${product.name}, Categoria: ${product.category}, Quantidade: ${product.quantity}, Preço: R$ ${product.price.toFixed(2)}`
            );
        });
    }
};

module.exports = listProducts;
