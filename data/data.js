const fs = require("fs");
const path = require("path");

const productsFilePath = path.join(__dirname, "/products.json");

const loadProducts = () => {
    try {
        if (!fs.existsSync(productsFilePath)) {
            fs.writeFileSync(productsFilePath, JSON.stringify([]));
            //console.log("Arquivo 'products.json' criado");
        }

        const data = fs.readFileSync(productsFilePath, "utf-8");
        return data ? JSON.parse(data) : [];
    } catch (error) {
        console.error("Erro ao carregar os produtos:", error);
        return [];
    }
};

const saveProducts = (products) => {
    try {
        fs.writeFileSync(productsFilePath, JSON.stringify(products, null, 2));
        console.log("Produtos salvos com sucesso.");
    } catch (error) {
        console.error("Erro ao salvar os produtos:", error);
    }
};

const generateId = () => Date.now().toString();

module.exports = { loadProducts, saveProducts, generateId };
