# Flask Cookie操作

### 什么是cookie：

在网站中，`http`请求是无状态的。也就是说即使第一次和服务器连接后并且登录成功后，第二次请求服务器依然不能知道当前请求是哪个用户。  
`cookie`的出现就是为了解决这个问题，第一次登录后服务器返回一些数据（`cookie`）给浏览器，然后浏览器保存在本地，  
当该用户发送第二次请求的时候，就会自动的把上次请求存储的`cookie`数据自动的携带给服务器，服务器通过浏览器携带的数据就能判断当前用户是哪个了。  
`cookie`存储的数据量有限，不同的浏览器有不同的存储大小，但一般不超过`4`KB。因此使用`cookie`只能存储一些小量的数据。  

1. `cookie`有有效期：服务器可以设置`cookie`的有效期，以后浏览器会自动的清除过期的`cookie`。  
2. `cookie`有域名的概念：只有访问同一个域名，才会把之前相同域名返回的`cookie`携带给服务器。也就是说，访问谷歌的时候，不会把百度的`cookie`发送给谷歌。

### flask操作cookie：

设置`cookie`：设置`cookie`是应该在`Response`的对象上设置。`flask.Response`对象有一个`set_cookie`方法，可以通过这个方法来设置`cookie`信息。  
在Chrome浏览器中查看cookie的方式： 

* 右键->检查->Network->重新加载页面->找到请求，然后查看Response Headers中的cookie  
* 点击Application，然后找到相应的域名，再展开查看cookie。  
* 在Chrome的设置界面->高级设置->内容设置->所有cookie->找到当前域名下的cookie。  

删除`cookie`：通过`Response.delete_cookie`，指定`cookie`的*key*，就可以删除`cookie`了。

### Flask 设置/删除 cookie

```python
from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def hello_world():
    resp = Response("saber's home")
    resp.set_cookie('username', 'saber')
    return resp

@app.route('/del')
def delete_cookie():
    resp = Response("saber's home 2")
    resp.delete_cookie('username')
    return resp

if __name__ == '__main__':
    app.run(debug=True)
```

###### 设置cookie的有效期：

* *max_age*：以秒为单位，距离现在多少秒后cookie会过期。  
* *expires*：为datetime类型。这个时间需要设置为格林尼治时间，也就是要距离北京少8个小时的时间。  
* 如果*max_age*和*expires*都设置了，那么这时候以*max_age为*标准。  
* *max_age*不支持IE8以下的浏览器。*expires*虽然在新版的HTTP协议中是被废弃了，但是到目前为止，所有的浏览器都还是能够支持，所以如果想要兼容IE8以下的浏览器，那么应该使用*expires*，否则可以使用*max_age*。  
* 默认的过期时间：如果没有显示的指定过期时间，那么这个cookie将会在浏览器关闭后过期。

```python
from flask import Flask, Response
from datetime import datetime, timedelta
app = Flask(__name__)

@app.route('/')
def hello_world():
    resp = Response("saber's home")
    # setCookie method 1.
    resp.set_cookie('username', 'saber', max_age=60)
    # setCookie method 2.
    resp.set_cookie('username', 'saber', expires=datetime(2020, 12, 12))
    # setCookie method 3.
    expires = datetime.now() + timedelta(days=30, hours=16)
    resp.set_cookie('username', 'saber', expires=expires)

    return resp

if __name__ == '__main__':
    app.run(debug=True)
```

#### 设置cookie有效域名

cookie默认是只能在主域名下使用。如果想要在子域名下使用，那么应该给`set_cookie`传递一个`domain='.hy.com'`，这样其他子域名才能访问到这个cookie信息。

```python
from flask import Flask, Response
from cmsviews import bp
app = Flask(__name__)
app.register_blueprint(bp)
app.config['SERVER_NAME'] = 'hy.com:5000'

@app.route('/')
def hello_world():
    resp = Response("saber's home")
    resp.set_cookie('username', 'saber', domain='.hy.com')

    return resp

if __name__ == '__main__':
    app.run(debug=True)
```
