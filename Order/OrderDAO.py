from DBConnnect import DBConnect
from datetime import datetime

class OrderDAO:
    def __init__(self):
        self.dbConnect = DBConnect.DBConnect()
        self.CREATE_ORDER = "insert into order_sequence(userid, orderdate, shipname, shipphone, shipemail, shipaddress, finalTotalPrice) values(%s, %s, %s, %s, %s, %s, %s)"
        self.ADD_ORDER_DETAILS = "insert into order_details(orderid, productid, quantity, totalprice) values(%s, %s, %s, %s)"
        self.LAST_INSERTED_ID = "select last_insert_id() as %s"
        self.PERMISSION_CHECK = "select * from order_sequence where id=%s and userid=%s"
        self.GET_ORDER_DETAILS = "select order_details.*, product.name, product.price from order_details, product where order_details.orderid=%s and order_details.productid=product.id"
        self.GET_SEQUENCES = "select id, orderdate, finaltotalprice from order_sequence where userid=%s"

    def addOrderDetails(self, sequenceId, productId, quantity, totalPrice):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(self.ADD_ORDER_DETAILS, (sequenceId, productId, quantity, totalPrice, ))
        connection.commit()

        cursor.close()
        connection.close()

    def createOrder(self, id, name, phone, email, address, finalTotalPrice):
        currenttime = datetime.today().strftime("%Y%m%d%H%M%S")

        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(self.CREATE_ORDER, (id, currenttime, name, phone, email, address, finalTotalPrice, ))
        connection.commit()

        cursor.execute(self.LAST_INSERTED_ID, ('sequenceid', ))
        sequenceId = cursor.fetchone()['sequenceid']

        cursor.close()
        connection.close()

        return sequenceId

    def permissionCheck(self, id, sequenceId):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(self.PERMISSION_CHECK, (sequenceId, id, ))
        sequence = cursor.fetchone()

        cursor.close()
        connection.close()

        if sequence is None:
            return False
        return sequence

    def getOrderDetails(self, orderId):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(self.GET_ORDER_DETAILS, (orderId, ))
        order_details = cursor.fetchall()

        cursor.close()
        connection.close()

        return order_details

    def getSequences(self, userid):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(self.GET_SEQUENCES, (userid, ))
        sequences = cursor.fetchall()

        cursor.close()
        connection.close()

        return sequences