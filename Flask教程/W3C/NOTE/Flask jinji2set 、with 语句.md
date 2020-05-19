# Flask jinji2set 、with 语句

### 1. set语句

在模板中，可以使用`set`语句来定义变量。示例如下：

```jinja2
<!--定义--> 
{% set username='cheng' %}
<!--使用--> 
{{ username }}
```

一旦定义了这个变量，那么在后面的代码中，都可以使用这个变量了，就跟Python中的变量定义和使用是一样的

### 2. with语句

`with`语句定义的变量，只能在`with`语句块中使用，出了这个代码块，就不能使用了，如：

```jinja2
{% with my_room='cheng' %}
    {{ my_room }}
    <!-- 里面也可以通过set语句来定义多个局部变量 -->
{% endwith %}
```

`with`语句不一定要跟一个变量，可以定义一个空的`with`语句，以后在`with`块中通过`set`定义的变量，就只能在`with`块中使用了

```jinja2
{% with %}
    {% set my_room='cheng' %}
    {{ my_room }}   <!-- 当然， my_room这个变量还是只能在with这个代码块中使用的-->
{% endwith %}
```
