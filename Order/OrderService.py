from Order import OrderDAO

class OrderService:
    def __init__(self):
        self.orderDao = OrderDAO.OrderDAO()

    def createOrder(self, id, name, phone, email, address, cart):
        shipid = self.orderDao.createShipAddress(name, phone, email, address)
        for product in cart:
            self.orderDao.createOrder(id, cart[product]['id'], shipid, cart[product]['quantity'], cart[product]['totalPrice'])