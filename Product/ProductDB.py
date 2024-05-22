class ProductDB:
    def __init__(self):
        self.products = {}

    def addProduct(self, id, name, price, description, kind, quantity):
        self.products[id] = [name, price, description, kind, quantity]

    def getProduct(self, id):
        return self.products[id]

    def removeProduct(self, id):
        del self.products[id]