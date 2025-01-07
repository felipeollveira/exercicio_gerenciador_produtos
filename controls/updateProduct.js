const { loadProducts, saveProducts } = require("../data/data");
const listProducts = require("./listProducts");

const updateProduct = (rl, main) => {
    const products = loadProducts();
    if (products.length === 0) {
        console.log("\nNenhum produto cadastrado.");
        main();
        return;
    }

    listProducts();
    rl.question("Digite o ID do produto que deseja atualizar: ", (id) => {
        const productIndex = products.findIndex((product) => product.id === id.trim());

        if (productIndex === -1) {
            console.log("Produto não encontrado.");
            main();
        } else {
            const product = products[productIndex];
            console.log("\nDeixe em branco para manter o valor atual.");
            rl.question(`Novo nome (${product.name}): `, (name) => {
                rl.question(`Nova categoria (${product.category}): `, (category) => {
                    rl.question(`Nova quantidade (${product.quantity}): `, (quantity) => {
                        rl.question(`Novo preço (${product.price}): `, (price) => {
                            product.name = name.trim() || product.name;
                            product.category = category.trim() || product.category;
                            product.quantity = isNaN(parseInt(quantity, 10)) ? product.quantity : parseInt(quantity, 10);
                            product.price = isNaN(parseFloat(price)) ? product.price : parseFloat(price);

                            saveProducts(products);
                            console.log("Produto atualizado com sucesso!");
                            main();
                        });
                    });
                });
            });
        }
    });
};

module.exports = updateProduct;
