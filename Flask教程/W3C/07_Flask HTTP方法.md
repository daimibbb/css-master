# Flask HTTP方法

## Flask HTTP方法

Http协议是万维网中数据通信的基础。在该协议中定义了从指定URL检索数据的不同方法。

下表总结了不同的http方法：

| 方法       | 与描述                                                       |
| ---------- | ------------------------------------------------------------ |
| **GET**    | 以未加密的形式将数据发送到服务器。最常见的方法。             |
| **HEAD**   | 和GET方法相同，但没有响应体。                                |
| **POST**   | 用于将HTML表单数据发送到服务器。POST方法接收的数据不由服务器缓存。 |
| **PUT**    | 用上传的内容替换目标资源的所有当前表示。                     |
| **DELETE** | 删除由URL给出的目标资源的所有当前表示。                      |

默认情况下，Flask路由响应**GET**请求。但是，可以通过为**route()**装饰器提供方法参数来更改此首选项。

为了演示在URL路由中使用**POST**方法，首先让我们创建一个HTML表单，并使用**POST**方法将表单数据发送到URL。

将以下脚本另存为login.html

```html
<html>
    <body>
        <form action="http://localhost:5000/login" method="POST">
            <p>Enter Name:</p>
            <p><input type="text" name="nm"/></p>
            <p><input type="submit" name="submit"/></p>
        </form>
    </body>
</html>
```

现在在Python shell中输入以下脚本：

```python
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return f'welcome {name:s}'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

if __name__ == '__main__':
   app.run(debug = True)
```

开发服务器开始运行后，在浏览器中打开**login.html**，在文本字段中输入name，然后单击**提交**。

![Flask HTTP方法](https://atts.w3cschool.cn/attachments/tuploads/flask/post_method_example.jpg)

表单数据将POST到表单标签的action子句中的URL。

**http://localhost/login**映射到**login()**函数。由于服务器通过**POST**方法接收数据，因此通过以下步骤获得从表单数据获得的“nm”参数的值：

```python
user = request.form['nm']
```

它作为变量部分传递给**'/ success'** URL。浏览器在窗口中显示**welcome**消息。

```python
welcome mvl
```

在**login.html**中将方法参数更改为**'GET'**，然后在浏览器中再次打开它。服务器上接收的数据是通过**GET**方法获得的。通过以下的步骤获得'nm'参数的值：

```python
user = request.args.get(‘nm’)
```

这里，**args**是包含表单参数对及其对应值对的列表的字典对象。与'nm'参数对应的值将像之前一样传递到'/ success' URL。

