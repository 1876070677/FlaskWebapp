from Product import ProductDAO

class ProductService:
    def __init__(self):
        self.productDao = ProductDAO.ProductDAO()

    def addProduct(self, product):
        self.productDao.addProduct(product)

    def getProductsOfKind(self, kind):
        return self.productDao.getProductsOfKind(kind)