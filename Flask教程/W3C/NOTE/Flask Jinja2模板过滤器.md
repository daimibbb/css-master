# Jinja2模板过滤器

### 常用过滤器

1. `default`： 有则使用传的，没则使用默认值  。

使用方式： `{{ value|default('默认值') }}`, 如果value这个key不存在，则会使用default过滤器提供的默认值。如果你想使用类似于`python`中判断一个值是否为False (例如：None, 空字符串，空列表，空字典等), 那么就必须要传递另外一个参数`{{ value|default('默认值', boolean=True) }}`, 可以使用`or`来替代`default('默认值', boolean=True)`。

```python
{{name|default('test')}}
{{name|default('test', boolean=True)}}
{{name or 'test'}}
```

2. `abs(value)`: 返回一个数值的绝对值。如: `-1|abs`

3. 关于转义:
   
   `safe`过滤器: 可以关闭一个字符串的自动转义, 禁用转义  
   `escape`过滤器: 对某一个字符串进行转义  
   `autoescape`标签: 可以对他里面的代码块关闭或开启自动转义

```python
{% autoescape off/on %}
    ...代码块
{% endautoescape %}
```

4. `first`: 返回一个序列的第一个元素. 如：` names|first`

5. `last`: 返回最后一个值。 如： `names|last`.

6. `format`: 格式化字符串

```python
{{ '我的名字是: %s'|format(username) }}
```

7. `length`: 返回一个序列类型的长度, 如： `names|length`

8. `join`: 将一个序列，用指定的参数拼接成字符串

```python
# 后台：
@app.route('/')
def index():
    context = {
        'username': 'cheng',
        'age': 18,
        'country': '',
        'names': ['ceng', 'yan', 'cheng', 'long', 'dong', 'zhu']
    }
    return render_template('index.html', **context)


# 前台
{{ names|join('/') }}

# 结果：
ceng/yan/cheng/long/dong/zhu
```

9. `int`: 将值转换为 int 类型，`float`: 将值转换为 float 类型

10. `lower`: 将字符串转换为小写

11. `upper`: 将字符串转换为大写

12. `string`: 将变量转换为字符串

13. `replace`: 替换字符串

```python
# 将字符串中所有的 hello 替换成 hi
{{ 'hello world aaa bbb hello'|replace('hello', 'hi') }}
```

14. `truncate`: 截取指定长度的字符串

```python
{{ article|truncate(length=8) }}
```

15. `striptags`: 删除字符串中所有的HTML标签，如果出现多个空格，将替换成一个空格

16. `trle`: 截取字符串前面和后面的空白字符

17. `wordcount`: 计算一个长字符串中单词的个数

```python
{{ article|wordcount }}
```

18. `title`: 把值中的第个单词的首页字母变成大写

19. `capitalize`： 把变量值的首字母转成大写，其余字母转小写

```python
{{ 'capitalize Hello HHHH aAAA'|capitalize }}
# 结果为：
Capitalize hello hhhh aaaa
```

20. `trim`： 把值的首尾空格去掉

21. `reverse`: 字符串的反转

```python
{{'hello world'|reverse}}
# 结果为：
dlrow olleh
```

### 列表操作

- `first`: 取第一个元素
- `last`: 取最后一个元素
- `length`: 获取列表的长度
- `sum`: 列表求和
- `sort`: 列表排序

```python
{{ [1, 2, 3, 4, 5]|first }}
{{ [1, 2, 3, 4, 5]|last }}
{{ [1, 2, 3, 4, 5]|length }}
{{ [1, 2, 3, 4, 5]|sum }}
{{ [8, 1, 6, 4, 5]|sort }}
```


