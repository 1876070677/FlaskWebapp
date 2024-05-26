from Order import OrderDAO, Sequence, Order
from datetime import datetime

class OrderService:
    def __init__(self):
        self.orderDao = OrderDAO.OrderDAO()

    def createOrder(self, id, name, phone, email, address, cart, finalTotalPrice):
        sequence = Sequence.Sequence(id, datetime.today().strftime("%Y%m%d%H%M%S"), name, phone, email, address, finalTotalPrice)
        sequenceId = self.orderDao.createOrder(sequence)
        for product in cart:
            order = Order.Order(sequenceId, cart[product]['id'], cart[product]['quantity'], cart[product]['totalPrice'], cart[product]['name'], cart[product]['price'])
            self.orderDao.addOrderDetails(order)

        return sequenceId

    def permissionCheck(self, id, sequenceId):
        return self.orderDao.permissionCheck(id, sequenceId)

    def getOrderDetails(self, orderId):
        orders = self.orderDao.getOrderDetails(orderId)
        orderList = []
        for order in orders:
            orderList.append(order.toDict())
        return orderList

    def getSequences(self, userid):
        sequences = self.orderDao.getSequences(userid)

        if len(sequences) == 0:
            return []

        sequenceList = []
        for sequence in sequences:
            sequenceList.append(sequence.toDict())
        return sequenceList