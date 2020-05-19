# Flask flash消息闪现

### flash介绍

好的应用和用户界面的重点是回馈。如果用户没有得到足够的反馈，他们可能最终会对您的应用产生不好的评价。
Flask 提供了一个非常简单的方法来使用闪现系统向**用户反馈信息**。
闪现系统使得在一个请求结束的时候记录一个信息，然后在且仅仅在下一个请求中访问这个数据。这通常配合一个布局模板实现

以上内容来自Flask官方文档，对flash的说明[http://docs.jinkan.org/docs](https://links.jianshu.com/go?to=http%3A%2F%2Fdocs.jinkan.org%2Fdocs%2Fflask%2Fpatterns%2Fflashing.html)

这几句话你只需记住两点即可：

- 一个请求结束时记录
- **仅仅**在下一个请求中访问

### 关于介绍的误解

flash介绍中说了，在一个请求结束时记录flash，然后仅仅在下一个请求中访问。此处的**下一个请求**，不是任意的请求，而是**下一次获取flash内容的请求。**
来看一个例子:

```python
from flask import Flask, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = 'not guess'

@app.route('/')
def index():
    flash("add flash -- hello Flask")
    return "<h3> Add Flash </h3>"

@app.route('/hello')
def hello():
    return "<h3> Hello World </h3>"

@app.route('/read')
def read():
    return "<h3> %s </h3>" % get_flashed_messages()

if __name__ == '__main__':
    app.run(port=5001)
```

```python
http://127.0.0.1:5000/read
# 返回一个列表
# ['add flash -- hello Flask']
```

这段代码我就不使用html模板渲染的，只是通过这个例子让大家先对flash有一个初步的认识。实现效果如下：

![img](https://upload-images.jianshu.io/upload_images/5847426-1b25f67ae069057d.gif?imageMogr2/auto-orient/strip|imageView2/2/w/838/format/webp)

首次访问`http://127.0.0.1:5001`，我们添加了flash，之后的下一个请求，我们去访问了一个hello的uri，此时我们简单返回了helloworld，那么此时的flash是否还存在？接下来我们去访问了read的uri，读取到了flash的内容，然后再次访问read去读取flash的时候已经为空了...

所以，不要被flash官网中说的**仅仅在下一次请求**给误解了，应该是**仅仅在下一次获取flash的请求**中获取。再次访问时清空，那么flash的实现方式是什么呢？其实很简单...

### flash实现原理

flash的实现原理，其实就是简单的在浏览器中添加`session`与删除`session`这么简单，具体如何操作的呢？

**flash 方法:**

```python
def flash(message, category='message'):
    flashes = session.get('_flashes', [])
    flashes.append((category, message))
    session['_flashes'] = flashes
    message_flashed.send(current_app._get_current_object(),
                         message=message, category=category)
```

**get_flashed_messages 方法：**

```python
def get_flashed_messages(with_categories=False, category_filter=[]):
    flashes = _request_ctx_stack.top.flashes
    if flashes is None:
        _request_ctx_stack.top.flashes = flashes = session.pop('_flashes') \
            if '_flashes' in session else []
    if category_filter:
        flashes = list(filter(lambda f: f[0] in category_filter, flashes))
    if not with_categories:
        return [x[1] for x in flashes]
    return flashes
```

其他的内容你都可以忽略，只要关注两点即可:

```python
flashes = session.get('_flashes', []); flashes.append((category, message))
session.pop('_flashes')
```

这么看是不一目了然，`flash`的时候给`session`中塞入一个_flashes的list，然后开始append，get_flashed_messages的时候把session中的_flashes pop出来，即达到了最终的请求结束前设置，仅供下一次获取flash时使用...
那么既然看了源码，大家肯定注意到一个*category*的参数，这个是用来干嘛的？

### category参数操作

flash消息既然是用于消息闪现，必然有好消息、坏消息与默认消息，系统默认的`category='message'`，那么如果我们将*category*设置为其他类型呢？

比如`flash('用户名或密码错误...', category='error')`，

那么我们在模板中针对flash可以做些什么事情？

#### 分类展示

```python
get_flashed_messages(with_categories=True)
```

`with_categories=true`代表我们启用消息分类，之后针对消息类型，可以进行相关的过滤操作

```jinja2
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    <ul class=flashes>
    {% for category, message in messages %}
      <li class="{{ category }}">{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
```

### 过滤消息

```python
get_flashed_messages(category_filter=["error"]
```



```jinja2
{% with errors = get_flashed_messages(category_filter=["error"]) %}
{% if errors %}
<div class="alert-message block-message error">
  <a class="close" href="#">×</a>
  <ul>
    {% for msg in errors %}
    <li>{{ msg }}</li>
    {% endfor -%}
  </ul>
</div>
{% endif %}
{% endwith %}
```

这个就比较简单了，为*message*添加一个过滤器，在日常中，我们完全可以重写自己的方法...

### 综合例子

介绍了这么多，我们来设计一个案例，简单的用户登录界面，如果用户输入的用户名密码错误，则显示错误消息，如果用户登录成功则跳转页面，并欢迎一下小盆友。因为登录和跳转页面都需要使用到flash，则创建一个base.html的模板

```jinja2
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
{% block info %}
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    <ul class=flashes>
    {% for category, message in messages %}
        {% if category == 'error' %}
            <li style="color:red">{{ message }}</li>
        {% else %}
            <li style="color:green">{{ message }}</li>
        {% endif %}
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
{% endblock %}
</body>
</html>
```

之后分别在登录和欢迎页面引入该模板...
**login.html:**

```xml
{% extends "base.html" %}
{% block info %}
<h2>欢迎登陆系统</h2>
<form action="" method="POST">
    <dl>
        <dt>用户名：</dt>
        <dd><input type="text" name="username" value="{{request.form.username}}"></dd>
        <dt>密码：</dt>
        <dd><input type="password"></dd>
    </dl>
    <p><input type="submit" value="Login"</p>
</form>
{% endblock %}
```

**index.html**

```jinja2
{% extends "base.html" %}
{% block info %}
<h2>恭喜 {{ user }} ,您已登陆！</h2>
{% endblock %}
```

然后创建**app.py**进行调度：

```python
from flask import Flask, flash, get_flashed_messages, \
    request, url_for, render_template
app = Flask(__name__)
app.secret_key = 'not guess'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            flash('用户名或密码错误...', category='error')
            flash('上点心再输入一次...', category='error')
        else:
            flash('登陆成功', category='info')
            return render_template('index.html', user=request.form['username'])
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
```

实现效果如下：

![img](https://upload-images.jianshu.io/upload_images/5847426-b0559559f076de96.gif?imageMogr2/auto-orient/strip|imageView2/2/w/580/format/webp)

我们在base.html中针对不同类型的消息进行了颜色的过滤，为了让大家了解flash其实是一个列表，所以添加了两条错误信息。
希望这个实例能让大家对flash有进一步的了解。

### flash如何闪现？

为了可以让flash真的如何闪现之名，我们应该让flash消息，出现跳刀闪烁消失的效果，如何来做？简单的使用**jQuery**即可！只需两行代码
**base.html:**

```xml
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
{% block info %}
<div class="flash">
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    <ul class=flashes>
    {% for category, message in messages %}
        {% if category =='error'%}
            <li style="color:red">{{ message }}</li>
        {% else %}
            <li style="color:green">{{ message }}</li>
        {% endif %}
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
{% endblock %}
</div>
<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
<script>$(".flash").fadeOut(3000);</script>
</body>
</html>
```

我们通过jQuery自带的**fadeOut**动画效果，即可达到我们的闪现的效果：

![img](https://upload-images.jianshu.io/upload_images/5847426-505ede454d2508d6.gif?imageMogr2/auto-orient/strip|imageView2/2/w/580/format/webp)

这才符合flash的之名啊....