class User:
    def __init__(self, id, password, name, phone, email, address):
        self.id = id
        self.password = password
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.role = ''

    def setRole(self, role):
        self.role = role