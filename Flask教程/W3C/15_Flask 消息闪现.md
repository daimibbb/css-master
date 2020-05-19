# Flask 消息闪现

一个好的基于GUI的应用程序会向用户提供有关交互的反馈。例如，桌面应用程序使用对话框或消息框，JavaScript使用警报用于类似目的。

在Flask Web应用程序中生成这样的信息性消息很容易。Flask框架的闪现系统可以在一个视图中创建消息，并在名为**next**的视图函数中呈现它。

Flask模块包含**flash()**方法。它将消息传递给下一个请求，该请求通常是一个模板。

```python
flash(message, category)
```

其中，

- *message*参数是要闪现的实际消息。
- *category*参数是可选的。它可以是“`error`”，“`info`”或“`warning`”。

为了从会话中删除消息，模板调用`get_flashed_messages()`。

```python
get_flashed_messages(with_categories, category_filter)
```

两个参数都是可选的。如果接收到的消息具有类别，则第一个参数是元组。第二个参数仅用于显示特定消息。

以下闪现在模板中接收消息。

```jinja2
{% with messages = get_flashed_messages() %}
   {% if messages %}
      {% for message in messages %}
         {{ message }}
      {% endfor %}
   {% endif %}
{% endwith %}
```

让我们看一个简单的例子，演示Flask中的闪现机制。在以下代码中，**'/'** URL显示登录页面的链接，没有消息闪现。

```python
@app.route('/')
def index():
    return render_template('index.html')
```

该链接会将用户引导到**'/ login'** URL，该URL显示登录表单。提交时，**login()**视图函数验证用户名和密码，并相应闪现**'success'**消息或创建**'error'**变量。

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
           request.form['password'] != 'admin':
           error = 'Invalid username or password. Please try again!'
       else:
           flash('You were successfully logged in')
           return redirect(url_for('index'))
    return render_template('login.html', error=error)
```

如果出现**错误**，则会重新显示登录模板，并显示错误消息。

**login.html**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
<h1>Login</h1>
{% if error %}
<p><b>Error: </b>{{ error }}</p>
{% endif %}
<form action="" method="POST">
    <dl>
        <dt>Username: </dt>
        <dd><input type="text" name="username" value="{{ request.form.uesrname }}"></dd>
        <dt>Password:</dt>
        <dd><input type="password" name="password"></dd>
    </dl>
    <p><input type="submit" value="Login" /></p>
</form>
</body>
</html>
```

另一方面，如果登录成功，则会在索引模板上刷新成功消息。

**index.html**

```html
<html>
<head>
  <title>index</title>
</head>
<body>
 {% with messages = get_flashed_messages() %}
    {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}
 {% endwith %}
 <h1>Flask Message Flashing Example</h1>
 <p>Do you want to <a href="{{ url_for('login') }}">
 <b>log in ?</b>   </a></p>
</body>
</html>
```

下面给出了Flask消息闪现示例的完整代码：

**flash.py**

```python
from flask import Flask, redirect, render_template, url_for, \
   request, flash, get_flashed_messages
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
   error = None
   if request.method == 'POST':
      if request.form['username'] != 'admin' or \
         request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
      else:
          flash('You were successfully logged in')
          return redirect(url_for('index'))
   return render_template('login.html', error=error)
if __name__ == '__main__':
    app.run(debug=True)
```

执行上述代码后，您将看到如下所示的界面。

![Flask Message Flashing Example](https://atts.w3cschool.cn/attachments/tuploads/flask/flask_message_flashing_example.jpg)

当您点击链接，您将被定向到登录页面。

输入用户名和密码。

![Login Page](https://atts.w3cschool.cn/attachments/tuploads/flask/login_page.jpg)

点击**登录**。将显示一条消息“您已成功登录”。

![Successfully Logged in Page](https://atts.w3cschool.cn/attachments/tuploads/flask/successfully_logged_in_page.jpg)