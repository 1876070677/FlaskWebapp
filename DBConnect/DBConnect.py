from mysql.connector import pooling
import mysql.connector
class DBConnect():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBConnect, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.pool = pooling.MySQLConnectionPool(
            pool_name='db_pool',
            pool_size=10,
            pool_reset_session=True,
            host='shbox.kr',
            port=9000,
            database='jiwonshop',
            user='root',
            password='root',
        )

    def getConnection(self):
        return self.pool.get_connection()