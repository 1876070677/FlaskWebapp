from DBConnect import DBConnect
from Product import Product

class ProductDAO:
    def __init__(self):
        self.dbConnect = DBConnect.DBConnect()
        self.GET_CATEGORYID = "select id from category where name=%s"
        self.GET_COUNT_BY_CATEGORY = "select count(*) as count from product where categoryid=%s"
        self.GET_PRODUCTS_BY_CATEGORY = "select product.*, category.name as category from product, category where categoryid=%s and product.categoryid=category.id limit 15 offset %s"
        self.GET_COUNT = "select count(*) as count from product"
        self.GET_ALL_PRODUCTS = "select product.*, category.name as category from product, category where product.categoryid=category.id limit 15 offset %s"
        self.GET_PRODUCT = "select product.*, category.name as category from product,category where product.id=%s and product.categoryid=category.id "

    def getProductsByCategory(self, category, page):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        # 카테고리 아이디 가져오기
        cursor.execute(self.GET_CATEGORYID, (category, ))
        categoryId = cursor.fetchone()

        # 데이터 수 가져오기
        cursor.execute(self.GET_COUNT_BY_CATEGORY, (categoryId['id'], ))
        count = cursor.fetchone()['count']

        # 실제 데이터 가져오기
        cursor.execute(self.GET_PRODUCTS_BY_CATEGORY, (categoryId['id'], (page-1) * 15, ))
        products = cursor.fetchall()

        productList = []
        for product in products:
            productList.append(Product.Product(product['id'], product['name'], product['price'], product['description'], product['filename'], product['categoryid'], product['category']))

        cursor.close()
        connection.close()

        return productList, count

    def getAllProducts(self, page):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        # 데이터 수 가져오기
        cursor.execute(self.GET_COUNT)
        count = cursor.fetchone()['count']

        # 실제 데이터 가져오기
        cursor.execute(self.GET_ALL_PRODUCTS, ((page - 1) * 15,))
        products = cursor.fetchall()

        cursor.close()
        connection.close()

        productList = []
        for product in products:
            productList.append(Product.Product(product['id'], product['name'], product['price'], product['description'], product['filename'], product['categoryid'], product['category']))

        return productList, count

    def getProductById(self, id):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(self.GET_PRODUCT, (id, ))
        product = cursor.fetchone()

        cursor.close()
        connection.close()

        return Product.Product(product['id'], product['name'], product['price'], product['description'], product['filename'], product['categoryid'], product['category'])