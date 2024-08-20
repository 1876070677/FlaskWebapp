from DBConnect import DBConnect
from User import User

class UserDAO:
    def __init__(self):
        self.dbConnect = DBConnect.DBConnect()
        self.ADD_USER = "insert into user(id, password, name, phone, email, address, roleid) values(%s, %s, %s, %s, %s, %s, %s)"
        self.CHECK_USER = "select * from user where id = %s"
        self.GET_USER = "select user.*, role.name as role from user, role where user.id=%s and user.roleid=role.id"
        self.UPDATE_USER = "update user set password=%s, name=%s, phone=%s, email=%s, address=%s where id=%s"
        self.DELETE_USER = "delete from user where id=%s"

    def addUser(self, user):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(self.ADD_USER, (user.id, user.password, user.name, user.phone, user.email, user.address, user.role, ))
            connection.commit()
        except Exception as e:
            raise Exception("회원 가입 실패")
        finally:
            cursor.close()
            connection.close()

    def checkUser(self, id):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(self.CHECK_USER, (id,))
            row = cursor.fetchone()
        except Exception as e:
            raise Exception("중복 확인 실패")
        finally:
            cursor.close()
            connection.close()

        if row is None:
            return False
        return True

    def login(self, id, pw):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(self.GET_USER, (id,))
            user = cursor.fetchone()
        except Exception as e:
            raise Exception("로그인 에러")
        finally:
            cursor.close()
            connection.close()

        if user is None:
            return False
        elif id == user['id'] and pw == user['password']:
            userData = User.User(user['id'], user['password'], user['name'], user['phone'], user['email'], user['address'], user['role'])
            return userData

    def updateUserInfo(self, user):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(self.UPDATE_USER, (user.password, user.name, user.phone, user.email, user.address, user.id, ))
            connection.commit()
        except Exception as e:
            raise Exception("사용자 정보 업데이트 실패")
        finally:
            cursor.close()
            connection.close()

    def deleteUser(self, id):
        connection = self.dbConnect.getConnection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(self.DELETE_USER, (id,))
            connection.commit()
        except Exception as e:
            raise Exception("회원 탈퇴 실패")
        finally:
            cursor.close()
            connection.close()
