# 초기 설정
레포지토리에 DBConnect/DBConnect.py 파일을 생성해주세요.
```angular2html
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
            host='',
            port=9000,
            database='jiwonshop',
            user='',
            password='',
        )

    def getConnection(self):
        return self.pool.get_connection()
```
다음과 같이 작성하고, host, user, password는 개발자에게 문의해주세요.

# 실행
파이썬 인터프리터를 설정하고 requirements.txt에 적혀있는 패키지들을 설치해주세요.
+ flask
+ flask_cors
+ mysql-connector-python

main.py를 실행하고, configuration을 다음의 사진과 같이 맞춰주세요.
![img.png](img.png)

이제 실행이 됩니다.