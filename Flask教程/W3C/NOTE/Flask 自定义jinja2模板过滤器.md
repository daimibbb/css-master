# 自定义jinja2模板过滤器

### 自定义过滤器

自定义的过滤器如果和内置的过滤器重名，会覆盖内置的过滤器。

过滤器本质上就是一个函数。如果在模板中调用这个过滤器。那么就会将这个变量的值作为第一个参数传递给过滤器这个函数，然后函数的返回值会作为这个过滤器的返回值。

**通过add_template_filter(过滤器函数名， 模板中使用的过滤器名字)**

```python
def filer_double_sort(li):
    return li[::2]
app.add_template_filter(filer_double_sort, 'li2')
```

**通过装饰器： @app.template_filter('过滤器名称')**

```python
# 可以设置这个， 模板修改了，也自动加载
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.template_filter('cut')
def cut(value):
    value = value.replace('hello', '')
    return value
```

```python
# 在模板中使用
{{ 'hello world hello world replace hello replace value world'|cut }}</p>
# 结果为：
hello：world world replace replace value world
```
