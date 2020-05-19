# Flask Session操作

### session：

`session`的基本概念：`session`和`cookie`的作用有点类似，都是为了存储用户相关的信息。不同的是，`cookie`是存储在本地浏览器，`session`是一个思路、一个概念、一个服务器存储授权信息的解决方案，不同的服务器，不同的框架，不同的语言有不同的实现。虽然实现不一样，但是他们的目的都是服务器为了方便存储数据的。`session`的出现，是为了解决`cookie`存储数据不安全的问题的。

`session`与`cookie`的结合使用：

* `session`存储在服务器端：服务器端可以采用`mysql`、`redis`、`memcached`等来存储`session`信息。原理是，客户端发送验证信息过来（比如用户名和密码），服务器验证成功后，把用户的相关信息存储到`session`中，然后随机生成一个唯一的*session_id*，再把这个*session_id*存储`cookie`中返回给浏览器。浏览器以后再请求我们服务器的时候，就会把这个*session_id*自动的发送给服务器，服务器再从`cookie`中提取*session_id*，然后从服务器的`session`容器中找到这个用户的相关信息。这样就可以达到安全识别用户的需求了。
* `session`存储到客户端：原理是，客户端发送验证信息过来（比如用户名和密码）。服务器把相关的验证信息进行一个非常严格和安全的加密方式进行加密，然后再把这个加密后的信息存储到`cookie`，返回给浏览器。以后浏览器再请求服务器的时候，就会自动的把`cookie`发送给服务器，服务器拿到`cookie`后，就从`cookie`找到加密的那个`session`信息，然后也可以实现安全识别用户的需求了。

### flask操作session：

设置session：通过`flask.session`就可以操作session了。操作`session`就跟操作字典是一样的。

```python
session['username']='zhiliao'。
```

获取session：也是类似字典，`session.get(key)`。

删除session中的值：也是类似字典。可以有三种方式删除session中的值。

* `session.pop(key)`。
* `del session[key]`。
* `session.clear()`：删除session中所有的值。

设置session的有效期：如果没有设置session的有效期。那么默认就是浏览器关闭后过期。如果设置`session.permanent=True`，那么就会默认在31天后过期。如果不想在31天后过期，那么可以设置`app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hour=2)`在两个小时后过期。

```python
from flask import Flask, session
from datetime import timedelta
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)

@app.route('/')
def hello_world():
    session['username'] = 'saber'
    # session permanent持久化，session将保存31天.
    session.permanent = True
    return 'Hello World'

@app.route('/get_session/')
def get_session():
    username = session.get('username')
    return username or 'no session set'

@app.route('/delete_session/')
def delete_session():
    # clear session 'username'
    session.pop('username')
    # clear all session.
    session.clear()
    return 'delete success.'

if __name__ == '__main__':
    app.run()
```


