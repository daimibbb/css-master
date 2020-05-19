# Flask 变量规则

## Flask 变量规则

通过向规则参数添加变量部分，可以动态构建URL。此变量部分标记为`<variable-name>`。它作为关键字参数传递给与规则相关联的函数。

在以下示例中，`route()`装饰器的规则参数包含附加到URL '`/hello`'的。因此，如果在浏览器中输入http://localhost:5000/hello/w3cschool作为URL，则'`w3cschool`'将作为参数提供给`hello()`函数。

```python
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return f'Hello {name}'

if __name__ == '__main__':
   app.run(debug = True)
```

将上述脚本保存为**hello.py**并从Python shell运行它。接下来，打开浏览器并输入URL：

```html
http:// localhost:5000/hello/w3cschool
```

以下输出将显示在浏览器中:

```out
Hello w3cschool!
```

除了默认字符串变量部分之外，还可以使用以下转换器构建规则：

| 转换器    | 描述                     |
| --------- | ------------------------ |
| **int**   | 接受整数                 |
| **float** | 对于浮点值               |
| **path ** | 接受用作目录分隔符的斜杠 |

在下面的代码中，使用了所有这些构造函数：

```python
from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return f'Blog Number {postID:d}'

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return f'Revision Nu,ber {revNo:.2f}'
if __name__ == '__main__':
    app.run(debug=True)
```

从Python Shell运行上面的代码。访问浏览器中的URL **http://localhost:5000/blog/11**。

给定的数字用作**show_blog()**函数的参数。浏览器显示以下输出：

```out
Blog Number 11
```

在浏览器中输入此URL - **http://localhost:5000/rev/1.1**

**revision()**函数将浮点数作为参数。以下结果显示在浏览器窗口中：

```
Revision Number 1.10
```

Flask的URL规则基于**Werkzeug**的路由模块。这确保形成的URL是唯一的，并且基于Apache规定的先例。

考虑以下脚本中定义的规则：

```python
from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

if __name__ == '__main__':
   app.run()
```

这两个规则看起来类似，但在第二个规则中，使用斜杠**（/）**。因此，它成为一个规范的URL。因此，使用 **/python** 或 **/python/**返回相同的输出。但是，如果是第一个规则，**/flask/ URL**会产生“404 Not Found”页面。