class Sequence:
    def __init__(self, id, orderdate, name, phone, email, address, finalTotalPrice):
        self.id = id
        self.orderdate = orderdate
        self.shipname = name
        self.shipphone = phone
        self.shipemail = email
        self.shipaddress = address
        self.finalTotalPrice = finalTotalPrice

    def toDict(self):
        dic = {
            'id': self.id,
            'orderdate': self.orderdate,
            'shipname': self.shipname,
            'shipphone': self.shipphone,
            'shipemail': self.shipemail,
            'shipaddress': self.shipaddress,
            'finaltotalprice': self.finalTotalPrice
        }
        return dic