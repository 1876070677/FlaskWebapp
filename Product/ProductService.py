from Product import ProductDAO

class ProductService:
    def __init__(self):
        self.productDao = ProductDAO.ProductDAO()

    def getProductsByCategory(self, category, page):
        return self.productDao.getProductsByCategory(category, page)

    def getAllProducts(self, page):
        return self.productDao.getAllProducts(page)

    def getProductById(self, id, quantity):
        product = self.productDao.getProductById(id)
        product['quantity'] = quantity
        product['totalPrice'] = int(product['price']) * quantity
        return product
