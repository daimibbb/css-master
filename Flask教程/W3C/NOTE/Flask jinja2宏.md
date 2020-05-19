# Flask jinja2宏

类似于python中的函数，宏的作用就是在模板中重复利用代码，避免代码冗余。  
Jinja2支持宏，还可以导入宏，需要在多处重复使用的模板代码片段可以写入单独的文件，再包含在所有模板中，以避免重复。

### 宏的定义和使用

**不带参数宏的定义和使用**

```html
<!-- 定义, 相当于定义一个函数一样 -->
{% macro input() %}
    <input type="text" name="username" value="">
{% endmacro %}
<!-- 使用, 相当于调用一个函数一样 -->
{{ input() }}
```

**带参数宏的定义和使用 (与函数是一样的，可以有必须参数和默认参数)**

```html
<!-- 定义 -->
{% macro input2(name, value='', type='text, size=30') %}
    <input type="{{type}}" name="{{name}} value={{value}} size={{size}}">
{% endmacro %}
<!-- 使用 -->
{{ input2() }}   <!--name不指定， 则name="", 即也是空-->
<!-- 或者 -->
{{ input2('username') }}
<!-- 或者 -->
{{ input2('username', value='cheng', type='password', size=50) }}
```

### 导入宏和使用导入的宏 (import)

在真实的开发中，会将一些常用的宏单独放在一个文件中，在需要使用的时候，再从这个文件中进行导入。 `import`语句的语法跟`python`的`import`类似，可以直接`import ... as ...`, 也可以`from ... import ...`或者`from ... import ... as ...`

1. **import '宏文件的路径' as xxx [with context]** # with context 导入的时候，把当前模板文件中的所有上下文变量也传递到宏文件中，这样宏文件就可以使用这些变量了

2. **from '宏文件的路径' import 宏的名字 [as xxx]**

3. 如果想要在导入宏的时候，就把当前模板中一些上下文变量传给宏所在的模板，那么就应该在导入宏的时候使用`with contex`. 如：
   
   ```python
   import 'macro.html' as func with context
   form 'macor.html' import input with context
   ```
   
   **注意：** 宏文件路径，不要以相对路径去寻找，都要以`templates`作为绝对路径去寻找

假设有一个macro.html的模板文件，在里面定义的宏如下：

```html
<!-- macro.html -->
{% macro input(name, value='', type='text') %}
    <input type="{{type}}" value="{{value}}" name="{{name}}">
{% endmacro %}
```

导入macro.html中的宏和使用其宏

```html
<!-- index.html -->
<!-- 1 -->
{% import 'macro.html' as func %}
{{ func.input('username') }}


<!-- 2 -->
{% from 'macro.html' import input %}
{{ input('username') }}

<!-- 3 -->
{% from 'macro.html' import input as inp %}
{{ inp('username') }}
```




