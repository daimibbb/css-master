# Flask URL构建

**url_for()**函数对于动态构建特定函数的URL非常有用。该函数接受函数的名称作为第一个参数，以及一个或多个关键字参数，每个参数对应于URL的变量部分。

以下脚本演示了如何使用**url_for()**函数：

```python
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return f'Hello {guest:s} as Guest'

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest' ,guest=name))

if __name__ == '__main__':
   app.run(debug = True)
```

上述脚本有一个函数**user(name)**，它接受来自URL的参数的值。

**User()**函数检查接收的参数是否与**'admin'**匹配。如果匹配，则使用**url_for()**将应用程序重定向到**hello_admin()**函数，否则重定向到将接收的参数作为guest参数传递给它的**hello_guest()**函数。

保存上面的代码并从Python shell运行。

打开浏览器并输入URL - **[http://localhost:5000/user/admin](http://localhost:5000/user/admin)**

浏览器中的应用程序响应是：

```
Hello Admin
```

在浏览器中输入以下URL - **[http://localhost:5000/user/mvl](http://localhost:5000/user/mvl)**

应用程序响应现在更改为：

```
Hello mvl as Guest
```