from Order import OrderDAO

class OrderService:
    def __init__(self):
        self.orderDao = OrderDAO.OrderDAO()

    def createOrder(self, id, name, phone, email, address, cart, finalTotalPrice):
        sequenceId = self.orderDao.createOrder(id, name, phone, email, address, finalTotalPrice)
        for product in cart:
            self.orderDao.addOrderDetails(sequenceId, cart[product]['id'], cart[product]['quantity'], cart[product]['totalPrice'])

        return sequenceId

    def permissionCheck(self, id, sequenceId):
        return self.orderDao.permissionCheck(id, sequenceId)

    def getOrderDetails(self, orderId):
        return self.orderDao.getOrderDetails(orderId)

    def getSequences(self, userid):
        sequences = self.orderDao.getSequences(userid)

        if sequences is None:
            return []
        return sequences