# Flask Note

### 1. 视图传递多个参数

(1) 普通传参 : 关键字参数传递

```python
return render_template('templateName.html', arg1=val1, arg2=val2,...)
```

(2) 字典传参 : 以字典的形式传递

```python
dict = {
    'key1': 'value1',
    'key2': 'value2',
    ... 
}
return render_template('templateName.html'， dict)
```

(3) 全局变量`g`传递

视图中:

```python
from flask import g

@app.route('/test')
def test():
    g.name = '张三'
    g.sex = '男'
    return render_template('test.html')
```

模板中：

```jinja2
<h2>{{g.name}}</h2>
<h2>{{g.sex}}</h2>
```

(4) 传递全部的本地变量给template，使用`**locals()`直接获取变量值

视图中:

```python
@app.route('/test')
def test():
    g.name = '张三'
    g.sex = '男'
    return render_template('test.html', **locals())
```

模板中：

```jinja2
<h2>{{name}}</h2>
<h2>{{sex}}</h2>
```

### 2. 错误页面定制

```python
# 制定捕获404和500的错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error=e, code=404)

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html', error=e, code=500)
```

指定错误页面: 只需要一个错误模板页面即可

```jinja2
{% extends 'base.html' %}
{% block title %}
{{code}}}
{% endblock %}
{% block page_content %}
<div class="alert alert-danger" role="alert">{{error}}</div>
{% endblock %}}
```

### 3. 文件上传

(1) 静态资源的加载

```jinja2
<!-- 注: static是内置的视图函数,我们通过其找到路由 -->
{{url_for('static', filename='img/demo.jpg')}}
{{url_for('static', filename='css/style.css')}}
{{url_for('static', filename='js/demo.js')}}
```

(2) 原生文件上传

模板文件

```jinja2
{% if newName %}
    <img  src="{{ url_for('static', filename=newName) }}" alt="" style="zoom: 50%;">
{% endif %}
<form action="{{url_for('upload')}}" enctype="multipart/form-data" method="POST">
    <input type="file" name="file">
    <p><input type="submit" value="submit"></p>
</form>
```

视图中:

```python
from flask import Flask, render_template, request
import os
import string
import random
app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = ['.jpg', '.jpeg', '.png', '.gif']
app.config['MAX_CONTENT_LENGTH'] = 1024*1024*60 
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'static')

@app.route('/')
def index():
   return render_template('upload.html')

def new_name(shuffix, length=16):
   myStr = string.ascii_letters + '0123456789'
   newName = ''.join(random.choice(myStr) for _ in range(length))
   return newName + shuffix

def allowed_file(shuffix):
   return shuffix.lower() in app.config['ALLOWED_EXTENSIONS'] 

@app.route('/upload', methods=['POST', 'GET'])
def upload():
   if request.method == 'POST':
      file = request.files.get('file')
      filename = file.filename
      shuffix = os.path.splitext(filename)[-1]
      if allowed_file(shuffix):
         newName = new_name(shuffix)
         newPath = os.path.join(app.config['UPLOAD_FOLDER'], newName)
         file.save(newPath)
   return render_template('upload.html', newName=newName)
if __name__ == '__main__':
   app.run(debug=True)
```

### 3. flask-uploads扩展库

```python
pip3 install flask-uploads
```

**类UploadSet** : 文件上传配置集合，包含三个参数：

*name*：文件上传配置集合的名称，默认**files**

*extensions*：上传文件类型，默认`DEFAULTS = TEXT + DOCUMENTS + IMAGES + DATA`

*default_dest*：上传文件的默认存储路径，我们可以通过`app.config[‘UPLOADS_DEFAULT_DEST’]`来指定

**方法 : configure_uploads**

应用配置好之后，调用此方法，扫描上传配置选项并保存到我们的应用中，注册上传模块。

**模板文件**

```jinja2
{% extends 'base.html' %}  #继承
{% block title %}
    首页
{% endblock %}
{% import 'bootstrap/wtf.html' as wtf %}  #导入
{% block page_content %}
    <img src="{{ url_for('static', filename=newName) }}" alt="">
    {{ wtf.quick_form(form) }}   #快速渲染
{% endblock %}block %}
```

```python
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
```

视图中:

```python
from flask import Flask, render_template, request
from flask_script import Manager
from flask_bootstrap import Bootstrap
import os
import string
import random
from flask_uploads import UploadSet, IMAGES, configure_uploads, \
   patch_request_class
# 导入库中验证的字段类
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileAllowed, FileRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'image'
app.config['MAX_CONTENT_LENGTH'] = 1024*1024*64
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(os.getcwd(), 'static')

# 实例化一个file对象  photos与PHOTOS要对应
file = UploadSet('photos', IMAGES)
# 将app的config配置注册到UploadSet实例file
configure_uploads(app, file)
# 限制上传文件的大小, size=None不采用默认size=64*1024*1024
patch_request_class(app, size=None)


bootstrap = Bootstrap(app)
manager = Manager(app)

class File(FlaskForm):
    file = FileField('文件上传', validators=[
        FileRequired(message='您还没有选择文件'),
        FileAllowed(file, message='只能上传图片')])
    submit = SubmitField('上传')

def new_name(shuffix, length=32):
   myStr = string.ascii_letters + '0123456789'
   newName = ''.join(random.choice(myStr) for _ in range(length))
   return newName + shuffix

@app.route('/upload', methods=['POST', 'POST'])
def upload():
    form = File()
    img_url = None
    if form.validate_on_submit():
        shuffix = os.path.splitext(form.file.data.filename)[-1]
        newName = new_name(shuffix=shuffix)
        file.save(newName)
        img_url = file.url(newName)
    return render_template('upload.html', newName=img_url, form=form)

if __name__ == '__main__':
    manager.run()
```

### 4. Flask g对象

Flask中的`g`对象是个很好的东西，主要用于在一个请求的过程中共享数据。可以随意给`g`对象添加属性来保存数据。下面的这个例子会使用`random`随机产生一个`0~9`的整数，并使用`g.x`保存并记录debug日志:

```python
from flask import Flask
from flask import g
import random

app = Flask(__name__)

@app.before_request
def set_on_g_object():
    x = random.randint(0, 9)
    app.logger.debug(f'before request g.x is {x}')
    g.x = x

@app.route('/')
def test():
    g.x = 1000
    return str(g.x)

@app.after_request
def get_on_g_object(response):
    app.logger.debug(f'alfer request g.x is {g.x}')
    return response
```

### 5. Flask中静态文件的处理

**`add_url_rule`的用法**

Flask中提供了`url_for`来实现创建`url`，只是生成一个`url`。如果要生成一个`css`样式的静态文件的`url`需要使用`url_for('static', filename='style.css')`来创建相应的`url`。但是如果我有一个目录`attachment`的目录存放一些文件的话是没法通过`url_for`来生成的，默认`url_for`只可以为`static`和一些`view_func`建立`url`，如果要想通过`url_for`为`attachment`来添加`url`就必须添加一个`add_url_rule`。

```python
from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def test():
    return 'url创建方式一'

def hello():
    return 'url创建方式二'
app.add_url_rule('/', 'index', hello)

@app.route('url1')
def create_url1():
    return url_for('static', filename='style.css')

app.add_url_rule('/attachment/<path:filename>', endpoint='attachment',
                 build_only=True)
@app.route('url2')
def create_url2():
    return url_for('attachment', filename='upload.txt')
```

**`send_from_directory`的用法**

`send_from_directory`主要用于下载文件：

```python
from flask import Flask
from flask import g
from flask import send_from_directory
from flask import url_for
import os

app = Flask(__name__)
dirpath = os.path.join(os.gercwd(), 'upload')

@app.route("/download/<path:filename>")
def downloader(filename):
    return send_from_directory(dirpath, filename, as_attachment=True)
```

**`static_url_path`和`static_folder`的用法**

`static_url_path`主要用于改变`url`的`path`的，静态文件放在`static`下面，所以正常情况`url`是`static/filename` ，但是可以通过`static_url_path`来改变这个`url`

`static_folder`主要是用来改变`url`的目录的，默认是`static`，可以通过这个变量来改变静态文件目录。

```python
# encoding=utf-8
from flask import Flask
from flask import g
from flask import send_from_directory
from flask import url_for
import os.path

app = Flask(__name__, static_url_path="/test")

@app.route("/")
def static_create():
    return url_for('static', filename='style.css')
```

**静态页面缓存和文件索引**

`SEND_FILE_MAX_AGE_DEFAULT `这个变量用于配置静态文件缓存的时间，Flask默认缓存时间是12hours
例如: `app.comfig['SEND_FILE_MAX_AGE_DEFAULT']=2592000` 将其缓存时间改为了30天。
Flask不能实现文件索引的功能，也就是无法列出文件名，这个需要web server(Nginx 或 Apache)来实现。

### 6. 视图高级add_url_rule

之前我们使用`@app.route`这个装饰器来把视图函数和`url`绑定

```python
@app.route('/')
def hell_world():
    return 'hello world'
```

而且我们可以通过`url_for(‘hello_world‘)`反转得到url `/`

实际上我们可以给这个装饰器再加上*endpoint*参数，给这个`url`命名

```python
@app.route('/', endpoint='index')
def hello_word():
    return 'hello world'
```

一旦我们指定了`endpoint`参数，则在使用`url_for()`反转的时候就**不能使用视图函数名了，而是要用我们定义的url名，即`endpoint`参数值**

```python
url_for('index')
```

另外一种方式绑定视图函数和url，那就是`add_url_rule`。

```python
def my_list():
    return 'my list'

app.add_url_rule(rule='/list/', endpoint='list', view_func=my_list)
```

如果要使用`url_for`反转的话，也是：`url_for('list')`，而不是`url_for('my_list')`，因为在映射这个函数与url时，设置了`endpoint='list'`。
