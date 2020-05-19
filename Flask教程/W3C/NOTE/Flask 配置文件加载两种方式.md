# Flask 配置文件加载两种方式

#### 1 基于全局变量

```makefile
manage.py
config
- localsettings.py
- settings.py
```

**manage.py**

```python
from flask import Flask
app = Flask(__name__)

# 加载配置文件
app.config.from_object('config.settings')

@app.route('/index')
def index():
    return 'index'

if __name__ == '__main__':
    app.run()
```

**config/settings.py**

```python
import os
SECRET_KEY = os.urandom(24)
try:
    from .localsettings import *
except ImportError:
    pass
```

#### 2 基于类的方式

```makefile
manage.py
config
- settings.py
```

**manage.py**

```python
from flask import Flask
app = Flask(__name__)

# 加载配置文件
app.config.from_object('config.settings.DevSettings')

@app.route('/index')
def index():
    return 'index'

if __name__ == '__main__':
    app.run()
```

**config/settings.py**

```python
class BaseSettings(object):
    X = 123
class DevSettings(BaseSettings):
    HOST = '1.1.1.1'
class ProdSettings(BaseSettings):
    HOST = '1.1.1.2'
```
