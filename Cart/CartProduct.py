class CartProduct:
    def __init__(self, id, name, price, description, filename, categoryId, category, quantity, totalprice):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.filename = filename
        self.categoryid = categoryId
        self.category = category
        self.quantity = quantity
        self.totalprice = totalprice

    def toDict(self):
        dic = {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'filename': self.filename,
            'categoryid': self.categoryid,
            'category': self.category,
            'quantity': self.quantity,
            'totalPrice': self.totalprice
        }
        return dic