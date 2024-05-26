class User:
    def __init__(self, id, password, name, phone, email, address, role):
        self.id = id
        self.password = password
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.role = role

    def toDict(self):
        dic = {
            'id': self.id,
            'password': self.password,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'role': self.role
        }
        return dic