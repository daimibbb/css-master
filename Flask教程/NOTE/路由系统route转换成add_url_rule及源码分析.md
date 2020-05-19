# 路由系统route转换成add_url_rule及源码分析

这节我们不用`@app.route`来写路由，而是通过`add_url_rule`

传统写法  （`<int:nid>`传递`int`类型参数，`endpoint`是取别名）

```python
@app.route('/detail/<int:nid>',methods=['GET'],endpoint='detail')
```

默认转换器

```python
DEFAULT_CONVERTERS = {
    'default':          UnicodeConverter,
    'string':           UnicodeConverter,
    'any':              AnyConverter,
    'path':             PathConverter,
    'int':              IntegerConverter,
    'float':            FloatConverter,
    'uuid':             UUIDConverter,
}
```

**路由系统本质（源码分析）**

从`@app.route`的`route`入手

源码app.py （从下面的源码可以看出`route`本质就是`add_url_rule`，这里的`self`就是实例化对象，也就是之前的`app`）

```python
def route(self, rule, **options)：
        def decorator(f):
            endpoint = options.pop("endpoint", None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator
```

然后跳转到`add_url_rule`中

```python
    @setupmethod
    def add_url_rule(
        self,
        rule,  #视图函数路由
        endpoint=None,   #取别名（非必填）
        view_func=None,  #这个就是上一个跳转过来的f,就是视图函数名（必填）
        provide_automatic_options=None,
        **options
    ):
   
        if endpoint is None:  #如果endpoint(别名)没填，就进入_endpoint_from_view_func看看
            endpoint = _endpoint_from_view_func(view_func)
        options["endpoint"] = endpoint
        methods = options.pop("methods", None)

        if methods is None:
            methods = getattr(view_func, "methods", None) or ("GET",)
        if isinstance(methods, string_types):
            raise TypeError(
                "Allowed methods have to be iterables of strings, "
                'for example: @app.route(..., methods=["POST"])'
            )
        methods = set(item.upper() for item in methods)

        # Methods that should always be added
        required_methods = set(getattr(view_func, "required_methods", ()))

        if provide_automatic_options is None:
            provide_automatic_options = getattr(
                view_func, "provide_automatic_options", None
            )

        if provide_automatic_options is None:
            if "OPTIONS" not in methods:
                provide_automatic_options = True
                required_methods.add("OPTIONS")
            else:
                provide_automatic_options = False

        # Add the required methods now.
        methods |= required_methods

        rule = self.url_rule_class(rule, methods=methods, **options)
        rule.provide_automatic_options = provide_automatic_options

        self.url_map.add(rule)
        if view_func is not None:
            old_func = self.view_functions.get(endpoint)
            if old_func is not None and old_func != view_func:
                raise AssertionError(
                    "View function mapping is overwriting an "
                    "existing endpoint function: %s" % endpoint
                )
            self.view_functions[endpoint] = view_func
```

进入`_endpoint_from_view_func()`看看是怎么取别名的

```python
assert view_func is not None, "expected view func if endpoint is not provided."
return view_func.__name__
```

第一句话是永远不是执行的，看第二句，取名就是视图函数名，这里就是`login`

**取别名使用方法（`url_for`）： 访问`login`路径,返回`123`**

```python
from flask import Flask,url_for
app  =Flask(__name__)
app.debug = True

def index():
    return '123'
app.add_url_rule('/index', view_func=index, endpoint='sb', \
    methods  =['POST', 'GET'])

def login():
    return url_for("sb")
app.add_url_rule('/login', view_func=index, methods=['POST', 'GET'])

if __name__ == '__main__': 
　　app.run()
```

**`add_url_rule`参数总结：**

- *rule*: 必填参数，就是跳转路由。

- *endpoint*:  非必填参数，如果不填就是视图函数名。如果设置了*endpoint*，就在视图函数中通过`url_for`使用，不能设置重复，用于反向生成URL，即： `url_for`('名称')

- *view_func*: 也就是请求该路由时，相应的视图函数名称

- *methods*:设置请求方式，默认是`get`请求，如：`['GET','POST']`

**`add_url_rule`额外参数：**

```python
# 默认值, 当URL中无参数，函数需要参数时，使用defaults={'k': 'v'}
defaults=None,

# 对URL最后的 / 符号是否严格要求，False是非严格模式，True严格模式，默认是严格模式
strict_slashes = None
'''
@app.route('/index', strict_slashes=False)
# 访问 http://www.xx.com/index/ 或 http://www.xx.com/index 均可
@app.route('/index', strict_slashes=True)
# 仅访问 http://www.xx.com/index
'''

#重定向到指定地址
redirect_to = None, 
'''
@app.route('/index/<int:nid>', redirect_to='/home/<nid>')
 '''
```
