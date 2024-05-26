from Product import ProductService
class CartService:
    def __init__(self):
        self.productService = ProductService.ProductService()

    def sessionToCartDict(self, data):
        if len(data) == 0:
            return {}
        newData = {}
        for product in data:
            newData[int(product)] = data[product]
        return newData

    def getFinalTotalPrice(self, cart):
        finalTotalPrice = 0
        for product in cart:
            finalTotalPrice += int(cart[product]['totalPrice'])

        return finalTotalPrice

    def addCart(self, sessionData, productId, quantity):
        cart = self.sessionToCartDict(sessionData)

        if productId not in cart:
            cartProduct = self.productService.getProductById(productId, quantity)
            cartProduct = cartProduct.toDict()
            cart[cartProduct['id']] = cartProduct
        else:
            cart[productId]['quantity'] += quantity
            cart[productId]['totalPrice'] += (cart[productId]['price'] * quantity)

        return cart, self.getFinalTotalPrice(cart)

    def updateQuantity(self, sessionData, productId, quantity):
        cart = self.sessionToCartDict(sessionData)

        cart[productId]['quantity'] = quantity
        cart[productId]['totalPrice'] = cart[productId]['price'] * quantity

        return cart, self.getFinalTotalPrice(cart)

    def deleteProduct(self, sessionData, productId):
        cart = self.sessionToCartDict(sessionData)

        del cart[productId]

        return cart, self.getFinalTotalPrice(cart)