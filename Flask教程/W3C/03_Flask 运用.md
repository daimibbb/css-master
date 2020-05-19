# Flask 应用

为了测试 **Flask** 安装，请在编辑器中将以下代码输入 **Hello.py：**

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World’

if __name__ == '__main__':
   app.run()
```

必须在项目中导入Flask模块。 Flask类的一个对象是我们的**WSGI**应用程序。

Flask构造函数使用**当前模块（__name __）**的名称作为参数。

Flask类的**route()**函数是一个装饰器，它告诉应用程序哪个URL应该调用相关的函数。

```python
app.route(rule, options)
```

- **rule** 参数表示与该函数的URL绑定。
- **options** 是要转发给基础Rule对象的参数列表。

在上面的示例中，'`/` ' URL与**hello_world()**函数绑定。因此，当在浏览器中打开web服务器的主页时，将呈现该函数的输出。

最后，Flask类的**run()**方法在本地开发服务器上运行应用程序。

```python
app.run(host, port, debug, options)
```

所有参数都是可选的

| 参数        | 描述                                                         |
| ----------- | ------------------------------------------------------------ |
| **host**    | 要监听的主机名。 默认为127.0.0.1（localhost）。设置为“0.0.0.0”以使服务器在外部可用 |
| **port**    | 默认值为5000                                                 |
| **debug**   | 默认为false。 如果设置为true，则提供调试信息                 |
| **options** | 要转发到底层的Werkzeug服务器。                               |

上面给出的**Python**脚本是从Python shell执行的。

```shell
$python Hello.py
```

Python shell中的消息通知您：

```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

在浏览器中打开上述URL**（localhost：5000）**。将显示**“Hello World”**消息。

## 调试模式

通过调用**run()**方法启动**Flask**应用程序。但是，当应用程序正在开发中时，应该为代码中的每个更改手动重新启动它。为避免这种不便，请启用**调试支持**。如果代码更改，服务器将自行重新加载。它还将提供一个有用的调试器来跟踪应用程序中的错误（如果有的话）。

在运行或将调试参数传递给**run()**方法之前，通过将**application**对象的**debug**属性设置为**True**来启用**Debug模式**。

```python
app.debug = True
app.run()
```

```python
app.run(debug = True)
```

