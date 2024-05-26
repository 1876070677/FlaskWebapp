# 초기 설정
DBConnect/DBConnect.py 파일에서 DB 설정을 해주세요.
```python
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
원격 DB를 사용하려면 다음과 같이 작성하고, host, user, password는 개발자에게 문의해주세요.

그게 아니라면 mysql을 설치하고 데이터베이스를 생성한 뒤, Database 디렉토리의 스키마를 바탕으로 테이블들을 구성해주세요. 이후, 해당 DB 정보를 사용하시면 됩니다.

# 실행
파이썬 인터프리터를 설정하고 requirements.txt에 적혀있는 패키지들을 설치해주세요.
+ flask
+ flask_cors
+ mysql-connector-python

main.py를 실행하고, configuration을 다음의 사진과 같이 맞춰주세요.
![img.png](img.png)

이제 실행이 됩니다.

# ERD
![img.png](Diagram/ERD.jpg)

# Class 다이어그램
![img.png](Diagram/ClassDiagram.jpg)