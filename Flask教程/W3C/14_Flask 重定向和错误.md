# Flask 重定向和错误

Flask类有一个`redirect()`函数。调用时，它返回一个响应对象，并将用户重定向到具有指定状态代码的另一个目标位置。

`redirect()`函数的原型如下：

```javascript
Flask.redirect(location, statuscode, response)
```

在上述函数中：

- *location*参数是应该重定向响应的URL。

- *statuscode*发送到浏览器标头，默认为`302`。

- *response*参数用于实例化响应。

以下状态代码已标准化：

- `HTTP_300_MULTIPLE_CHOICES`
- `HTTP_301_MOVED_PERMANENTLY`
- `HTTP_302_FOUND`
- `HTTP_303_SEE_OTHER`
- `HTTP_304_NOT_MODIFIED`
- `HTTP_305_USE_PROXY`
- `HTTP_306_RESERVED`
- `HTTP_307_TEMPORARY_REDIRECT`

默认状态代码为`302`，表示'found'。

在以下示例中，`redirect()`函数用于在登录尝试失败时再次显示登录页面。

```python
from flask import Flask, redirect, url_for, render_template, request
# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
   if request.method=='POST' and request.form['username']=='admin' :
       return redirect(url_for('success'))
   return redirect(url_for('index'))

@app.route('/success')
def success():
   return 'logged in successfully'
	
if __name__ == '__main__':
   app.run(debug=True)
```

**login.html**

```html
<form action="http://localhost:5000/login" method="POST">
    <p><input type="text" name="username"</p>
    <p><input type="submit" value="Login"</p>
</form>
```

**Code**参数采用以下值之一：

- **400** - 用于错误请求

- **401** - 用于未身份验证的

- **403** - Forbidden

- **404** - 未不到

- **406** - 表示不接受

- **415** - 用于不支持的媒体类型

- **429** - 请求过多

让我们对上述代码中的login()函数稍作更改。如果要显示'Unauthurized'页面，请将其替换为调用abort(401)，而不是重新显示登录页面。

```python
from flask import Flask, redirect, url_for, render_template, request, abort
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
   if request.method == 'POST':
      if request.form['username'] == 'admin' :
         return redirect(url_for('success'))
      else:
         abort(401)
   else:
      return redirect(url_for('index'))

@app.route('/success')
def success():
   return 'logged in successfully'

if __name__ == '__main__':
   app.run(debug=True)
```


