from DBConnect import DBConnect
from Order import Order, Sequence

class OrderDAO:
    def __init__(self):
        self.dbConnect = DBConnect.DBConnect()
        self.CREATE_ORDER = "insert into order_sequence(userid, orderdate, shipname, shipphone, shipemail, shipaddress, finalTotalPrice) values(%s, %s, %s, %s, %s, %s, %s)"
        self.ADD_ORDER_DETAILS = "insert into order_details(orderid, productid, quantity, totalprice) values(%s, %s, %s, %s)"
        self.LAST_INSERTED_ID = "select last_insert_id() as %s"
        self.PERMISSION_CHECK = "select * from order_sequence where id=%s and userid=%s"
        self.GET_ORDER_DETAILS = "select order_details.*, product.name, product.price from order_details, product where order_details.orderid=%s and order_details.productid=product.id"
        self.GET_SEQUENCES = "select * from order_sequence where userid=%s"

    def addOrderDetails(self, order):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(self.ADD_ORDER_DETAILS, (order.orderId, order.productId, order.quantity, order.totalPrice, ))
            connection.commit()
        except Exception as e:
            raise Exception("주문 정보 추가 실패")
        finally:
            cursor.close()
            connection.close()

    def createOrder(self, sequence):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(self.CREATE_ORDER, (sequence.id, sequence.orderdate, sequence.shipname, sequence.shipphone, sequence.shipemail, sequence.shipaddress, sequence.finalTotalPrice, ))
            connection.commit()

            cursor.execute(self.LAST_INSERTED_ID, ('sequenceid', ))
            sequenceId = cursor.fetchone()['sequenceid']
        except Exception as e:
            raise Exception("주문 생성 실패")
        finally:
            cursor.close()
            connection.close()

        return sequenceId

    def permissionCheck(self, id, sequenceId):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(self.PERMISSION_CHECK, (sequenceId, id, ))
            sequence = cursor.fetchone()
        except Exception as e:
            raise Exception("주문자 정보 권한 확인 실패")
        finally:
            cursor.close()
            connection.close()

        if sequence is None:
            return False
        return sequence

    def getOrderDetails(self, orderId):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)
        orderList = []
        try:
            cursor.execute(self.GET_ORDER_DETAILS, (orderId, ))
            order_details = cursor.fetchall()
        except Exception as e:
            raise Exception("주문 정보 상세 보기 실패")
        finally:
            cursor.close()
            connection.close()


        for order in order_details:
            orderList.append(Order.Order(order['orderid'], order['productid'], order['quantity'], order['totalprice'], order['name'], order['price']))
        return orderList

    def getSequences(self, userid):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(self.GET_SEQUENCES, (userid, ))
            sequences = cursor.fetchall()
        except Exception as e:
            raise Exception("주문 정보 보기 실패")
        finally:
            cursor.close()
            connection.close()

        sequenceList = []
        for sequence in sequences:
            sequenceList.append(Sequence.Sequence(sequence['id'], sequence['orderdate'], sequence['shipname'], sequence['shipphone'], sequence['shipemail'], sequence['shipaddress'], sequence['finaltotalprice']))

        return sequenceList