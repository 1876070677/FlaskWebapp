from User import UserDAO, User

class UserService:
    def __init__(self):
        self.userDao = UserDAO.UserDAO()

    def addUser(self, id, password, username, phone, email, address):
        user = User.User(id, password, username, phone, email, address, 2)
        self.userDao.addUser(user)
        user = self.userDao.login(id, password)
        return user.toDict()

    def checkUser(self, id):
        return self.userDao.checkUser(id)

    def login(self, id, pw):
        user = self.userDao.login(id, pw)
        return user.toDict()

    def updateUserInfo(self, id, password, username, phone, email, address):
        user = User.User(id, password, username, phone, email, address, 2)
        self.userDao.updateUserInfo(user)
        user = self.userDao.login(id, password)
        return user.toDict()

    def deleteUser(self, id):
        self.userDao.deleteUser(id)