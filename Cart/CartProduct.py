class CartProduct:
    def __init__(self, id, name, price, description, categoryId, quantity, totalprice):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.categoryid = categoryId
        self.quantity = quantity
        self.totalprice = totalprice

    def toDict(self):
        dic = {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'categoryid': self.categoryid,
            'quantity': self.quantity,
            'totalPrice': self.totalprice
        }
        return dic