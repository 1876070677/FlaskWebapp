from User import UserDAO, User

class UserService:
    def __init__(self):
        self.userDao = UserDAO.UserDAO()

    def addUser(self, id, password, username, phone, email, address):
        user = User.User(id, password, username, phone, email, address)
        self.userDao.addUser(user)

    def checkUser(self, id):
        return self.userDao.checkUser(id)

    def login(self, id, pw):
        return self.userDao.login(id, pw)

    def updateUserInfo(self, id, password, username, phone, email, address):
        user = User.User(id, password, username, phone, email, address)
        self.userDao.updateUserInfo(user)

    def deleteUser(self, id):
        self.userDao.deleteUser(id)