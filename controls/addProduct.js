const { loadProducts, saveProducts, generateId } = require("../data/data");

const addProduct = (rl, main) => {
    rl.question("Digite o nome do produto: ", (name) => {
        rl.question("Digite a categoria do produto: ", (category) => {
            rl.question("Digite a quantidade: ", (quantity) => {
                rl.question("Digite o preço: ", (price) => {
                    const products = loadProducts();
                    const id = generateId();

                    const newProduct = {
                        id,
                        name: name.trim(),
                        category: category.trim(),
                        quantity: parseInt(quantity, 10),
                        price: parseFloat(price),
                    };

                    if (!newProduct.name || !newProduct.category || isNaN(newProduct.quantity) || isNaN(newProduct.price) || newProduct.price <= 0 || newProduct.quantity < 0) {
                        console.log("Dados inválidos. Tente novamente.");
                        main();
                    } else {
                        products.push(newProduct);
                        saveProducts(products);
                        console.log("Produto adicionado com sucesso!");
                        main();
                    }
                });
            });
        });
    });
};

module.exports = addProduct;
