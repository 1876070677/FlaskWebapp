from DBConnnect import DBConnect
from User import User

class UserDAO:
    def __init__(self):
        self.dbConnect = DBConnect.DBConnect()
        self.ADD_USER = "insert into user(id, password, name, phone, email, address, roleid) values(%s, %s, %s, %s, %s, %s, 2)"
        self.CHECK_USER = "select * from user where id = %s"
        self.GET_USER = "select user.*, role.name as role from user, role where user.id=%s and user.roleid=role.id"
        self.UPDATE_USER = "update user set password=%s, name=%s, phone=%s, email=%s, address=%s where id=%s"
        self.DELETE_USER = "delete from user where id=%s"

    def addUser(self, user):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(self.ADD_USER, (user.id, user.password, user.name, user.phone, user.email, user.address,))
        connection.commit()
        cursor.close()
        connection.close()

    def checkUser(self, id):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(self.CHECK_USER, (id,))
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        if row is None:
            return False
        return True

    def login(self, id, pw):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(self.GET_USER, (id,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        if id == user['id'] and pw == user['password']:
            return user
        return False

    def updateUserInfo(self, user):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(self.UPDATE_USER, (user.password, user.name, user.phone, user.email, user.address, user.id, ))
        connection.commit()
        cursor.close()
        connection.close()

    def deleteUser(self, id):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(self.DELETE_USER, (id,))
        connection.commit()
        cursor.close()
        connection.close()
