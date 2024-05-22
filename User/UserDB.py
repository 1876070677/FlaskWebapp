class UserDB:
    def __init__(self):
        self.users = {}

    def addUser(self, id, pw, name, phone, email, address):
        self.users[id] = [pw, name, phone, email, address]

    def getUser(self, id):
        return self.users[id]

    def editUser(self, id, pw, name, phone, email, address):
        self.users[id] = [pw, name, phone, email, address]

    def removeUser(self, id):
        del self.users[id]