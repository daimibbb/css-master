# Flask 静态文件处理

Web应用中大多会提供静态文件服务以便给用户更好的访问体验。

**静态文件主要包含CSS样式文件，js脚本，图片和字体等。**

Flask也支持静态文件访问的，默认情况下只需在项目根目录下，创建名为`static`的目录，在应用中使用`‘/static`'开头的路径就可以访问了。但是为了获得更好的处理能力，推荐使用`Nginx`或者其他服务器管理静态文件。

不要直接在模板中写死静态文件路径，应该使用`url_for`生成路径。

```python
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates', 
            static_folder='statics', static_url_path='/static')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>首页</h1> 
    <!-- 建议 -->
    <img src="{{ url_for('static',filename='mm.jpg')}}" />
</body>
</html>
```

在视图中的Flask类中的参数作用：

- `template_folder` 是存放页面的文件夹，默认是templates

- `static_folder` 是静态文件夹的名字

- `static_url_path` 是静态文件的路径，跟前端页面中的url路径一致

在前端页面中`url_for('static', filename='1.jpg') `

- `url_for`中的第一个参数"`static`"是一个默认值，**这个值不允许改动**，当你的Flask类中的参数`static_url_path`名字改变之后，它会将`url_for`中的"`static`"替换成"`static_url_path`"的路径值；所以以后在做前端的时候就推荐写"`url_for`"这种方法，如果以后的静态文件地址有改变就不需要在前端页面重新写了； 

- 后边的"`filename`"是文件名
