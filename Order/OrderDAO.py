from DBConnect import DBConnect
class OrderDAO:
    def __init__(self):
        self.dbConnect = DBConnect.DBConnect()
        self.CREATE_ORDER = "insert into order_history(userid, productid, shipid, quantity, totalPrice) values(%s, %s, %s, %s, %s)"
        self.CREATE_SHIPADDRESS = "insert into ship_address(shipname, shipphone, shipemail, shipaddress) values(%s, %s, %s, %s)"
        self.LAST_INSERTED_ID = "select last_insert_id() as %s"

    def createOrder(self, userid, productid, shipid, quantity, totalPrice):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(self.CREATE_ORDER, (userid, productid, shipid, quantity, totalPrice, ))
        connection.commit()

    def createShipAddress(self, name, phone, email, address):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(self.CREATE_SHIPADDRESS, (name, phone, email, address, ))
        connection.commit()

        cursor.execute(self.LAST_INSERTED_ID, ('shipid', ))
        shipid = cursor.fetchone()['shipid']

        return shipid




