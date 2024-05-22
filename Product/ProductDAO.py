from Product import ProductDB
from Product import Product

class ProductDAO:
    def __init__(self):
        self.productdb = ProductDB.ProductDB()

    def addProduct(self, product):
        self.productdb.products[product.productId] = [product.name, product.price, product.description, product.kind, product.quantity]

    def getProductsOfKind(self, kind):
        products = []
        for product in self.productdb.products:
            if self.productdb.products[product][3] == kind:
                products.append(Product.Product(product, self.productdb.products[product][0], self.productdb.products[product][1], self.productdb.products[product][2], self.productdb.products[product][3], self.productdb.products[product][4]))

        return products

