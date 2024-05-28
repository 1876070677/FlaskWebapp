class Product:
    def __init__(self, id, name, price, desc, filename, categoryId, category):
        self.id = id
        self.name = name
        self.price = price
        self.description = desc
        self.filename = filename
        self.categoryid = categoryId
        self.category = category

    def toDict(self):
        dic = {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'filename': self.filename,
            'categoryid': self.categoryid,
            'category': self.category
        }
        return dic