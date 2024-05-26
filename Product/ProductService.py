from Product import ProductDAO
from Cart import CartProduct

class ProductService:
    def __init__(self):
        self.productDao = ProductDAO.ProductDAO()

    def getProductsByCategory(self, category, page):
        if category == 'all':
            productList, count = self.productDao.getAllProducts(page)
            end = count // 15 + 1
            if page - 5 < 1:
                pageFirst = 1
            else:
                pageFirst = page - 5

            if page + 5 > end:
                pageEnd = end
            else:
                pageEnd = page + 5
        else:
            productList, count = self.productDao.getProductsByCategory(category, page)
            end = count // 15 + 1
            if page - 5 < 1:
                pageFirst = 1
            else:
                pageFirst = page - 5

            if page + 5 > end:
                pageEnd = end
            else:
                pageEnd = page + 5
        products = []
        for product in productList:
            productDic = product.toDict()
            products.append(productDic)
        return products, pageFirst, pageEnd, end

    def getProductById(self, id, quantity):
        product = self.productDao.getProductById(id)
        cartProduct = CartProduct.CartProduct(product.id, product.name, product.price, product.description, product.categoryid, quantity, int(product.price) * quantity)
        return cartProduct
