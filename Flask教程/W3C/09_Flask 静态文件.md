# Flask 静态文件

Web应用程序通常需要静态文件，例如**javascript**文件或支持网页显示的**CSS**文件。通常，配置Web服务器并为您提供这些服务，但在开发过程中，这些文件是从您的包或模块旁边的**static**文件夹中提供，它将在应用程序的**/static**中提供。

**静态文件主要包含CSS样式文件，js脚本，图片和字体等。**

Flask也支持静态文件访问的，默认情况下只需在项目根目录下，创建名为`static`的目录，在应用中使用‘`/static`'开头的路径就可以访问了。但是为了获得更好的处理能力，推荐使用Nginx或者其他服务器管理静态文件。

不要直接在模板中写死静态文件路径，应该使用`url_for`生成路径。

例如：

```javascript
url_for('static',filename='style.css')
```

生成的路径就是‘`/static/style.css`'。当然我们也可以定制静态文件的真是目录：

```python
app = Flask(__name__ , static_folder='/tmp')
```

那么访问‘`http://localhost:9000/static/style.css`',

也就是访问`/tmp/style.css`这个文件了。

在下面的示例中，在**index.html**中的HTML按钮的**OnClick**事件上调用**hello.js**中定义的**javascript**函数，该函数在Flask应用程序的**“/”**URL上呈现。

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)
```

**templates/index.html**的HTML脚本如下所示：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <script src="{{url_for('static', filename='hello.js')}}"></script>
</head>
<body>
    <input type="button" onclick="sayHello()" value="Say Hello"/>
</body>
</html>
```

**static/hello.js**包含**sayHello()**函数。

```javascript
function sayHello() {
   alert("Hello World")
}
```







