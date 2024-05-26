class Order:
    def __init__(self, sequenceId, productId, quantity, totalPrice, name, price):
        self.orderId = sequenceId
        self.productId = productId
        self.quantity = quantity
        self.totalPrice = totalPrice
        self.name = name
        self.price = price

    def toDict(self):
        dic = {
            'orderid': self.orderId,
            'productid': self.productId,
            'quantity': self.quantity,
            'totalprice': self.totalPrice,
            'name': self.name,
            'price': self.price
        }
        return dic
