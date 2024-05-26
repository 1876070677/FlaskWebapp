from DBConnnect import DBConnect

class ProductDAO:
    def __init__(self):
        self.dbConnect = DBConnect.DBConnect()
        self.GET_CATEGORYID = "select id from category where name=%s"
        self.GET_COUNT_BY_CATEGORY = "select count(*) as count from product where categoryid=%s"
        self.GET_PRODUCTS_BY_CATEGORY = "select * from product where categoryid=%s limit 15 offset %s"
        self.GET_COUNT = "select count(*) as count from product"
        self.GET_ALL_PRODUCTS = "select * from product limit 15 offset %s"
        self.GET_PRODUCT = "select * from product where id=%s"

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
        cursor.execute(self.GET_PRODUCTS_BY_CATEGORY, (categoryId['id'], (page-1) * 10, ))
        products = cursor.fetchall()

        cursor.close()
        connection.close()

        return products, count

    def getAllProducts(self, page):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        # 데이터 수 가져오기
        cursor.execute(self.GET_COUNT)
        count = cursor.fetchone()['count']

        # 실제 데이터 가져오기
        cursor.execute(self.GET_ALL_PRODUCTS, ((page - 1) * 10,))
        products = cursor.fetchall()

        cursor.close()
        connection.close()

        return products, count

    def getProductById(self, id):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(self.GET_PRODUCT, (id, ))
        product = cursor.fetchone()

        cursor.close()
        connection.close()

        return product