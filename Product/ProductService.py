from Product import ProductDAO

class ProductService:
    def __init__(self):
        self.productDao = ProductDAO.ProductDAO()

    def getProductsByCategory(self, category, page):
        if category == 'all':
            products, count = self.productDao.getAllProducts(page)
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
            products, count = self.productDao.getProductsByCategory(category, page)
            end = count // 15 + 1
            if page - 5 < 1:
                pageFirst = 1
            else:
                pageFirst = page - 5

            if page + 5 > end:
                pageEnd = end
            else:
                pageEnd = page + 5
        return products, pageFirst, pageEnd, end

    def getProductById(self, id, quantity):
        product = self.productDao.getProductById(id)
        product['quantity'] = quantity
        product['totalPrice'] = int(product['price']) * quantity
        return product
