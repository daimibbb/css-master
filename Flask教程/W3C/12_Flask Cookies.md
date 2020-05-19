# Flask Cookies

Cookie以文本文件的形式存储在客户端的计算机上。其目的是记住和跟踪与客户使用相关的数据，以获得更好的访问者体验和网站统计信息。

**Cookie的定义：**

1. 如果单单从数据结构的角度来说，它可以被理解成用来保存数据的一个dictionary，由一组组键值对组成。如果从作用上来说，我们知道Http协议是一种无状态的协议。什么叫无状态呢,就是本次的客户端请求不会保留上一次客户端请求的状态，简单点说就是这样会要求我们每次在浏览器中点开一个网站的链接都会输一次账户和密码。cookie就是用来解决这个问题的。
2. Cookie的主要目的是跟踪客户端浏览器。当某个浏览器访问了服务端，服务端就会向客户端浏览器写入一个或多个Cookie。当该浏览器再次访问服务端时，服务端就会知道这个浏览器曾经访问过服务端。
3. Cookie以文本文件的形式存储在客户端的计算机上。其目的是记住和跟踪与客户使用相关的数据，以获得更好的访问者体验和网站统计信息。

```python
#从客户端读取名为name的Cookie的值，并将读取结果赋给value变量
value=request.cookies.get('name')
```

**Request对象**包含Cookie的属性。它是所有cookie变量及其对应值的字典对象，客户端已传输。除此之外，cookie还存储其网站的到期时间，路径和域名。

在Flask中，对响应对象设置cookie。使用**make_response()**函数从视图函数的返回值获取响应对象。之后，使用响应对象的**set_cookie()**函数来存储cookie。

读回cookie很容易。`request.cookies`属性的**get()**方法用于读取cookie。

在以下Flask应用程序中，当您访问**'/'** URL时，会打开一个简单的表单。

```python
@app.route('/')
def index():
   return render_template('index.html')
```

**index.html**页面内容如下：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
<form action="/setcookie" method="POST">
    <h3>Enter userID</h3>
    <p><input type="text" name="nm"</p>
    <P><input type="submit" value="Login"</P>
</form>
</body>
</html>
```

表单发布到**'/ setcookie'** URL。相关联的视图函数设置Cookie名称**userID**并呈现另一个页面。

```python
@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
      user = request.form['nm']
      resp = make_response(render_template('readcookie.html'))
      resp.set_cookie('userID', user)
      return repr
```

'readcookie.html'包含指向另一个视图函数`getcookie()`的超链接，它读回并在浏览器中显示Cookie值。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h3>Cookie 'userID' is set</h3>
<a href="/getcookie">Click here t read cookie</a>
</body>
</html>
```

```python
@app.route('/getcookie')
def getcookie():
       name = request.cookies.get('userID')
       return f'<h1> Welcome {name}</h1>'
```

完整程序：

```python
from flask import Flask, render_template,request, make_response
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)

    return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return f'<h1>welcome {name}</h1>'

if __name__=="__main__":
    app.run()
```

运行应用程序，并访问**http://localhost:5000/**

![ReadCookie HTML](https://atts.w3cschool.cn/attachments/tuploads/flask/readcookie_html.jpg)

设置cookie的结果显示为这样：

![Result of Setting Cookie](https://atts.w3cschool.cn/attachments/tuploads/flask/result_of_setting_cookie.jpg)

读回cookie的输出如下所示：

![Reading Cookie Back](https://atts.w3cschool.cn/attachments/tuploads/flask/reading_cookie_back.jpg)

删除 cookie 方法

```python
@app.route('/delCookie', methods=['GET'])
def delCookie():
    response = make_response('delCookie')
    response.delete_cookie('id')
    return response
```
