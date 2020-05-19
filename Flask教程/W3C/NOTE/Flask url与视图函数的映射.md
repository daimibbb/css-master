# Flask中url与视图函数的映射

### 传递参数

传递参数的语法是： `<params>`, 路由定义了参数，那么在视图函数中， 也要定义同名的参数来进行接收, 如：

```python
# @app.route('/article/<article_id>/')
@app.route('/article/<int:article_id>/')    # 限制数据类型
def article_detail(article_id):
    return f'第 {article_id} 篇文章的详情'
```

### 指定传递的数据类型

语法： `<类型:参数名>` , 其中类型有以下几种：

1. **string**: 默认的数据类型，接受没有任何斜杠'/'的文本
2. **int**: 整型
3. **float**: 浮点类型
4. **path**: 接受路径，和 **string**类似，但是可以接受斜杠'/'
5. **uuid**: 只接受符合uuid的字符串, uuid是一个在全世界都唯一的字符串，一般可以服务业作为表的主键
6. **any**: 可以在一个`url`中指定多个路径，如下面例子：

```python
# /blog/<id>/
# /user/<id>/
@app.route('/<any(blog, user):url_path>/<int:idx>/')
def detail(url_path, idx):
    if url_path == 'blog':
        return f'博客详情： {{ {url_path}: {idx} }}'
    else:
        return f'用户详情： {{ {url_path}: {idx} }}'
```

### 接收用户传递的参数

1. 使用**path**的形式(将参数嵌入到路径中),就是上面所讲的
2. 使用查询字符串的形式(`?key=value`)来传递的, 有多个key-value，则用 `&`分隔开， 如: `?name=long&age=18`

```python
from flask import request
@app.route('/select_str/')
def select_str():
    wd = request.args.get('wd')
    return '你通过查询字符串的方式传递的参数是： %s' % wd
# http://127.0.0.1:5000/select_str/?wd=python
```
