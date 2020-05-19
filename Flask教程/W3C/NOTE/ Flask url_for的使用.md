# url_for的使用

与 Django 的`reverse('app_name:name') `类似，都是用来反转路由的。

### `url_for`的基本使用：

`url_for`: **url_for**的一个参数是一个视图函数的名字的字符串格式,后面的参数的参数以关键字的形式传递给`url`。 如果传递的参数在那个视图中url中定义了，那么这个参数就会以路径参数的形式给`url`。 如果传递的参数没有在`url`中定义，那么这些参数将会以查询字符串的形式放到`url`中。

```python
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    my_list_path = url_for('my_list', page=1, count=111)
    print(my_list_path) # 结果为： /list/1/?count=111
    return my_list_path

@app.route('/list/<int:page>/')
def my_list(page):
    return f'第{page}页'
```

### 为什么需要 `url_for`:

1. 将来如果修改了`URL`, 但没有修改该URL对应的函数名，就不用到处支替换URL了.
2. `url_for` 会自动的处理那些特殊的字符，不需要手动处理

```python
@app.route('')
def index():
    a = url_for('login', next='/')
    print(a)# /login/?next=%2F，会自动编码，不需要手动处理了
    return a

@app.route('/login/')
def login():
    return 'login'
```

### 使用`url_for`在模板中加载静态文件

加载静态文件使用的是`url_for`函数。第一个参数需要为`'static'`, 第二个参数需要为一个关键字参数`filename='静态文件路径'`。 如下所示：

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}">
```

路径查找，要心当前项目的`sttic`目录作为根目录

 强烈建议以后在使用url的时候，使用**url_for**来反转 url
