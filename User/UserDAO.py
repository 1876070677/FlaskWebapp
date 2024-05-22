from User import UserDB
from User import User

class UserDAO:
    def __init__(self):
        self.userdb = UserDB.UserDB()

    def addUser(self, user):
        self.userdb.addUser(user.id, user.pw, user.name, user.phone, user.email, user.address)

    def checkUser(self, id):
        if id in self.userdb.users:
            return True
        return False

    def checkIdPw(self, id, pw):
        if id in self.userdb.users:
            if pw == self.userdb.users[id][0]:
                return True
        return False

    def getUser(self, id):
        userInfo = self.userdb.users[id]
        user = User.User(id, userInfo[0], userInfo[1], userInfo[2], userInfo[3], userInfo[4])
        return user