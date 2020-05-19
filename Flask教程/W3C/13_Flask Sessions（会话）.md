# Flask Sessions（会话）

与Cookie不同，**Session（会话）**数据存储在服务器上。会话是客户端登录到服务器并注销服务器的时间间隔。需要在该会话中保存的数据会存储在服务器上的临时目录中。

为每个客户端的会话分配**会话ID**。会话数据存储在cookie的顶部，服务器以加密方式对其进行签名。对于此加密，Flask应用程序需要一个定义的**SECRET_KEY**。

Session对象也是一个字典对象，包含会话变量和关联值的键值对。

例如，要设置一个**'username'**会话变量，请使用以下语句：

```python
Session[‘username’] = ’admin’
```

要释放会话变量，请使用**pop()**方法。

```python
session.pop('username', None)
```

以下代码是Flask中的会话工作的简单演示。URL **'/'**只是提示用户登录，因为未设置会话变量**'username'**。

```python
@app.route('/')
def index():
   username = ''
   if 'username' in session:
      username = session['username']
   return render_template('index.html', username=username)
```

**index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    {% if username %}
    <p>Logged in as {{ username }}</p>
    <p><a href="/logout">click here to log out</a></p>
    {% else %}
    <p>You are not logged in</p>
    <p><a href="/login">click here to log in</a></p>
    {% endif %}
</body>
</html>
```

当用户浏览到“`/login`”时，`login()`视图函数时，因为它是通过GET方法调用的，所以将打开一个登录表单。

表单发送回**'/login'**，现在会话变量已设置。应用程序重定向到**'/'**。此时会话变量**'username'**被找到。

```python
@app.route('/login', methods=['POST', 'GET'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return render_template('login.html')
```

**login.html**

```html
<form action="" method="POST">
    <p><input type="text" name="username"</p>
    <p><input type="submit" value="Login"</p>
</form>
```

应用程序还包含一个**logout()**视图函数，它会弹出**'username'**会话变量。因此，**'/'** URL再次显示开始页面。

```python
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))
```

运行应用程序并访问主页。（确保设置应用程序的**secret_key**）

```python
from flask import Flask, render_template, request, redirect, url_for, session
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
```

完整代码：

```python
from flask import Flask, render_template, request, redirect, url_for, session
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
   username = ''
   if 'username' in session:
      username = session['username']
   return render_template('index.html', username=username)

@app.route('/login', methods=['POST', 'GET'])
def login():
   if request.method == 'POST':
      session['username'] = request.form['username']
      return redirect(url_for('index'))
   return render_template('login.html')

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)

```

输出将显示如下。点击**“点击此处登录”**链接。

![Login Page Using Session](https://atts.w3cschool.cn/attachments/tuploads/flask/login_page_using_session.jpg)

链接将被定向到另一个屏幕。键入“admin”。

![Another Login Screen](https://atts.w3cschool.cn/attachments/tuploads/flask/another_login_screen.jpg)

屏幕将显示消息**“以管理员身份登录”**。

![Logged in as admin](https://atts.w3cschool.cn/attachments/tuploads/flask/logged_in_as_admin.jpg)


