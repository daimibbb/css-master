# Flask路由和配置文件

**路由**

1\. 直接返回字符串（`return `后面加字符串）

```python
@app.route('/')
    return 'OK'
```

2\. 返回html页面，渲染页面（`render_template`）

```python
@app.route('/')
def index():
    name_dict = {'name': 'jason-gdx'}
    return reder_template('index.html', name_dict=name_dict)
```

**注意：**` render_template()`会去flask根目录下的`templates`里面寻找文件，所以给的参数路径时相对路径。

3\. 跳转页面（`redirect`）

```python
@app.route('/')
def index():
    return redirect('/login')
```

4\. 返回json数据(`jsonify`)

```python
@app.route('/')
def index():
    name_dict = [{'name': "jason-gdx"}, {'name': "tank-sb"}]
    return  jsonify(name_dict)
```

**flask配置文件的4种方式**

第一种，这种方式只能配置两种（`debug`, `secret_key`）

```python
app.debug = True
app.secret_key = "123123"
```

第二种，以字典的形式

```python
app.config['DEBUG'] = True
```

第三种，以文件的形式

```python
app.config.from_pyfile("settings.py")
```

**settings.py**

```python
class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
```

第四种以类的形式(推荐)

```python
app.config.from_object('settings.DevelopmentConfig')
```

flask中的配置文件是一个`flask.config.Config`对象（继承字典），默认配置为：

```python
{
    'DEBUG':                                get_debug_flag(default=False),  是否开启Debug模式
    'TESTING':                              False,                          是否开启测试模式
    'PROPAGATE_EXCEPTIONS':                 None,                          
    'PRESERVE_CONTEXT_ON_EXCEPTION':        None,
    'SECRET_KEY':                           None,
    'PERMANENT_SESSION_LIFETIME':           timedelta(days=31),
    'USE_X_SENDFILE':                       False,
    'LOGGER_NAME':                          None,
    'LOGGER_HANDLER_POLICY':               'always',
    'SERVER_NAME':                          None,
    'APPLICATION_ROOT':                     None,
    'SESSION_COOKIE_NAME':                  'session',
    'SESSION_COOKIE_DOMAIN':                None,
    'SESSION_COOKIE_PATH':                  None,
    'SESSION_COOKIE_HTTPONLY':              True,
    'SESSION_COOKIE_SECURE':                False,
    'SESSION_REFRESH_EACH_REQUEST':         True,
    'MAX_CONTENT_LENGTH':                   None,
    'SEND_FILE_MAX_AGE_DEFAULT':            timedelta(hours=12),
    'TRAP_BAD_REQUEST_ERRORS':              False,
    'TRAP_HTTP_EXCEPTIONS':                 False,
    'EXPLAIN_TEMPLATE_LOADING':             False,
    'PREFERRED_URL_SCHEME':                 'http',
    'JSON_AS_ASCII':                        True,
    'JSON_SORT_KEYS':                       True,
    'JSONIFY_PRETTYPRINT_REGULAR':          True,
    'JSONIFY_MIMETYPE':                     'application/json',
    'TEMPLATES_AUTO_RELOAD':                None,
    }
```
