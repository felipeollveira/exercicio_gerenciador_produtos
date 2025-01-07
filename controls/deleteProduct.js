const { loadProducts, saveProducts } = require("../data/data");
const listProducts = require("./listProducts");

const deleteProduct = (rl, main) => {
    const products = loadProducts();
    if (products.length === 0) {
        console.log("\nNenhum produto cadastrado.");
        main();
        return;
    }

    listProducts();
    rl.question("Digite o ID do produto que deseja excluir: ", (id) => {
        const productIndex = products.findIndex((product) => product.id === id.trim());

        if (productIndex === -1) {
            console.log("Produto não encontrado.");
            main();
        } else {
            const productName = products[productIndex].name;
            products.splice(productIndex, 1); // Remove o produto
            saveProducts(products);
            console.log(`Produto "${productName}" excluído com sucesso!`);
            main();
        }
    });
};

module.exports = deleteProduct;
