class Product:
    def __init__(self, id, name, price, desc, categoryId):
        self.id = id
        self.name = name
        self.price = price
        self.description = desc
        self.categoryid = categoryId

    def toDict(self):
        dic = {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'categoryid': self.categoryid
        }
        return dic