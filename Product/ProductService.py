from Product import ProductDAO

class ProductService:
    def __init__(self):
        self.productDao = ProductDAO.ProductDAO()

    def addProduct(self, product):
        self.productDao.addProduct(product)

    def getProductsByKind(self, kind):
        return self.productDao.getProductsByKind(kind)

    def getAllProducts(self):
        return self.productDao.getAllProducts()

    def getProductById(self, id):
        return self.productDao.getProductById(id)