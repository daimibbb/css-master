- [Flask-SQLAlchemy Documentation (2.x)](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

```python
pip install Flask-SQLAlchemy
```

一旦创建`db`对象，这个对象就包含 `sqlalchemy `和` sqlalchemy.orm` 中的所有方法参数：

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
```

为了创建初始数据库，只需要从交互式 Python shell 中导入 `db `对象并且调用 `SQLAlchemy.create_all() `方法来创建表和数据库:

```python
from yourapplication import db
db.create_all()
```

数据库已经生成。现在来创建一些用户:

```python
from yourapplication import User
admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')
```

But they are not yet in the database, so let’s make sure they are:

```python
db.session.add(admin)
db.session.add(guest)
db.session.commit()
```

Accessing the data in database is easy as a pie:

```python
User.query.all()
Out[27]: [<User 1>, <User 2>]
User.query.filter_by(username='admin').first()
Out[28]: <User 1>
```





```markdown
DBMS         URI
Mysql        mysql://username:password@host/databasename
Sqlite       sqlite:///absolute/path/to/foo.db
Sqlite       sqlite:/// or sqlite:///:memory
```

#### 1. 设置内置配置参数`SQLALCHEMY_DATABASE_URI`

```python
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', '')
db = SQLAlchemy(app)
```

#### 2. 在`.env`中保存数据库连接的隐私数据

```python
DATABASE_URL = mysql+pymysql://root:123456@localhost:3306/forum?charset=utf8
```

### SQLAlchemy连接数据库

```python
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:123456@localhost:3306/forum?charset=utf8",
                        echo=True)
```

- *echo*设置为`True`表示开启生成所有的SQLAlchemy日志记录；

- `create_engine()`并没有建立与DBAPI的连接；

- 可以直接向数据库发出SQL。

```python
connection = engine.connect()
result = connection.execute("select username from users")
for row in result:
    print("username:", row['username'])
connection.close()  
```
