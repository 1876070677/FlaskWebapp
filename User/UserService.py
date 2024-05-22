from User import UserDAO

class UserService:
    def __init__(self):
        self.userDao = UserDAO.UserDAO()

    def addUser(self, user):
        self.userDao.addUser(user)

    def checkUser(self, id):
        return self.userDao.checkUser(id)

    def checkIdPw(self, id, pw):
        return self.userDao.checkIdPw(id, pw)

    def getUser(self, id):
        return self.userDao.getUser(id)