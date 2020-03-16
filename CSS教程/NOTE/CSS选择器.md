# CSS选择器

## 一、css的基本语法

```css
css选择器{
    css属性：值;
    css属性：值;　
}　
```

```css
body{
    background: red;
    color: white;
}
```

## 二、基本的css选择器

### 1、通用选择器

该选择器会匹配文档中的所有元素，包括`html`和`body`元素。

```css
* {
    margin: 0;
    padding: 0;
}
```

上面的css样式用来取消文档中所有元素的内边距和外边距。

### 2、元素选择器

用来选择文档中该元素的所有实例。　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        p {
            color: red;
        }
    </style>
</head>
<body>
<p> I  love  China!</p>
<p> I  love  China!</p>
</body>
</html>
```

### 3、类选择器

类选择采用全局属性`class`匹配指定类的元素。　　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .p1 {
            color: red;
        }
    </style>
</head>
<body>
<p class="p1"> I  love  China!</p>
<p> I  love  China!</p>
<p class="p1"> I  love  China!</p>
</body>
</html>
```

1、`*.class2`和`.class2`是一样，我们可以将前面的通用选择器换成其他元素选择器，来缩小选择范围。当`class`属性有多个值时，用**空格**隔开。  

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        p.p1 {
            color: red;
        }
    </style>
</head>
<body>
<p class="p1"> I  love  China!</p>
<p> I  love  China!</p>
<span class="p1"> I  love  China!</span>
</body>
</html>
```

2、一个元素用于多个类选择器，同一css属性的优先级**取决于样式表中的先后顺序**，与类列表的先后顺序无关。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .red {
            color: red;
        }
        .green {
            color: green;
        }
    </style>
</head>
<body>
<h1 class="red green">多个类选择器</h1>
</body>
</html>
```

![img](https://img2018.cnblogs.com/blog/1252860/201902/1252860-20190219225338104-1832925634.png)

---

交换`style`标签中两个类选择器的顺序。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .green {
            color: green;
        }
        .red {
            color: red;
        }
    </style>
</head>
<body>
<h1 class="green red">多个类选择器</h1>
</body>
</html>
```

![img](https://img2018.cnblogs.com/blog/1252860/201902/1252860-20190219225511296-841382864.png)

---

### 4、id选择器

使用全局属性`id`的值选择元素。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        #p1 {
            color: red;
        }

    </style>
</head>
<body>
<p id="p1"> I  love  China!</p>
<p> I  love  China!</p>
<span>I  love  China!</span>
</body>
</html>
```

---

### 5、属性选择器

根据元素的属性来进行选择。

a、`[attribute]`　　        选择器用于选取带有指定属性的元素，忽略属性值　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        [id] {
            color: red;
        }

    </style>
</head>
<body>
<p> I  love  China!</p>
<p id="p1"> I  love  China!</p>
<span>I  love  China!</span>
</body>
</html>
```

b、`[attribute="value"]  `   选择器用于选取带有指定属性和值的元素　　　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        [title="abc"] {
            color: red;
        }

    </style>
</head>
<body>
<p> I  love  China!</p>
<p title="abc"> I  love  China!</p>
<span>I  love  China!</span>
</body>
</html>
```

c、`[attribute^="value"] `   选择器用于选取带有指定属性且属性值以`value`字符开头的元素　　　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        [title^="a"] {
            color: red;
        }

    </style>
</head>
<body>
<p title="abc"> I  love  China!</p>
<p> I  love  China!</p>
<span title="a1">I  love  China!</span>
</body>
</html>
```

d、`[attribute*="value"]  `  选择器用于选取带有指定属性和属性值包含`value`字符的元素　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        [title*="a"] {
            color: red;
        }

    </style>
</head>
<body>
<p title="bac"> I  love  China!</p>
<p> I  love  China!</p>
<span title="a1">I  love  China!</span>
</body>
</html>
```

e、`[attribute~=value] `   选择器用于选取带有指定属性、属性值具有多个值且其中一个值是`value`的元素　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        [class~="class1"] {
            color: red;
        }

    </style>
</head>
<body>
<p class="class1 class2"> I  love  China!</p>
<p> I  love  China!</p>
<span class="class1 class1">I  love  China!</span>
</body>
</html>
```

e、` [attribute|="value"] `    选择器用于选取带有指定属性、属性值为（可以是0个）连字符分割多个值且其中第一个值是value的元素　　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        [class|="a1"] {
            color: red;
        }

    </style>
</head>
<body>
<p class="a1"> I  love  China!</p>
<p> I  love  China!</p>
<span class="a1-2">I  love  China!</span>
</body>
</html>
```

---

## 三、复合选择器

### 1、并集选择器

用于单个选择器匹配到的所有元素的并集。语法：`选择器1, 选择器2 { }　`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        p, a {
            color: red;
        }

    </style>
</head>
<body>
<p>
    <a href="http://www.baidu.com">百度</a>
</p>
</body>
</html>
```

### 2、后代选择器

后代选择器用于匹配第一个元素的后代，且匹配第二个元素。匹配第一个元素中的元素，而不仅仅是直接元素。语法：`选择器1  选择器2{ }　`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        p span {
            background: red;
        }

    </style>
</head>
<body>
<p>I  <span>love</span> China!</p>
<a href="http://www.baidu.com">百度</a>
</body>
</html>
```

### 3、选择子元素

用于匹配第一个选择器的元素的直接后代，且匹配第二个元素。语法：`选择器1 > 选择器2{ }　`　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        p>span {
            background: red;
        }

    </style>
</head>
<body>
<p>I  <span>love</span> China!</p>
<a href="http://www.baidu.com">百度</a>
</body>
</html>
```

### 4、选择兄弟元素

#### a、相邻兄弟选择器

目标元素紧跟第一个选择器匹配的元素且匹配第二个元素。语法：`选择器1 + 选择器2{ }`　　　　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        p+a {
            background: red;
        }

    </style>
</head>
<body>
<a href="http://www.baidu.com">百度</a>
<p>I  <span>love</span> China!</p>
<a href="http://www.baidu.com">百度</a>
<a href="http://www.sina.com">新浪</a>
</body>
</html>
```

#### b、普通兄弟选择器

目标元素位于匹配第一个选择器的元素之后，且匹配第二个选择器。语法：`选择器1 ~ 选择器2{ }　`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        p~a {
            background: red;
        }

    </style>
</head>
<body>
<a href="http://www.baidu.com">百度</a>
<p>I  <span>love</span> China!</p>
<a href="http://www.baidu.com">百度</a>
<a href="http://www.sina.com">新浪</a>
</body>
</html>
```

## 三、伪元素选择器

前面的元素选择器通过选择元素来操作文档内容。伪元素实际上并不存在，为了便于你选中文档的内容。　

1、`::firtst-line`用来匹配文本块的首行。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        ::first-line {
            background: yellow;
        }

    </style>
</head>
<body>
<a href="http://www.baidu.com">百度</a>
<p>I  <span>love</span> China!<br>I like apple!</p>
<p>aaaaaa</p>
</body>
</html>
```

`::first-line`和`:first-line`是一样。该选择器还可以和其他选择器结合使用，如`p:first-line`;用来选择`p`元素的首行。

 2、`:first-letter`（`::first-letter`）选择文本块的首字母。　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        ::first-letter {
            background: yellow;
        }

    </style>
</head>
<body>
<a href="http://www.baidu.com">百度</a>
<p>I  <span>love</span> China!<br>I like apple!</p>
<p>aaaaaa</p>
</body>
</html>
```

3、`::before`和`::after`选择器在元素的前面、后面插出内容　　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        a::before {
            content: "click here: ";
        }

    </style>
</head>
<body>
<a href="http://www.baidu.com">百度</a>
</body>
</html>
```

4、CSS计数器

a.创建计数器

```css
body{
    counter-reset:paracount;
}
```

这行代码会初始化一个计数器`paracount`，初始值为`0`.

指定初始值：

```css
body{
    counter-reset:paracount 10;
}
```

创建多个计数器：

```css
counter-reset: paracount othercount;
counter-reset: paracount 10 othercount 2;
```

使用方法：　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        body {
            counter-reset: paracount 0;
        }
        p::before {
            content: counter(paracount) ".";
            counter-increment: paracount 1;
        }

    </style>
</head>
<body>
<p>I love China!</p>
<p>I love apple!</p>
</body>
</html>
```

```
1. I love China!
2. I love apple!
```

`counter(计数器，数值格式)`；用来说明使用哪个计数器和数值的格式。数值格式可以是`list-style-type`中的值。例如`counter(paracount, lower-alpha)`. 

" `.`"是数值和内容之间的分割符，也可以是其他的字符。常用的是句号和空格。

`counter-increment`属性用来设置计数器的增量。默认是`1`.

---

## 四、伪类选择器

伪类元素选择器不是直接针对文档元素的，而是为你基于某些特征选择元素提供方便的。

### 1、结构伪类选择器

结构伪类是根据元素在文档中的位置选择元素的。

**a、根元素选择器**

`:root`选择文档的根元素。总数返回`html`元素。　　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        :root {
            border: thin black solid;
        }
    </style>
</head>
<body>
<p>I love China!</p>
<p>I love apple!</p>
</body>
</html>
```

边框会包裹着整个文档。

**b、使用子元素选择器(可以和其他选择器结合使用)**

`:first-child` 选择元素的第一个子元素。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        p>span:first-child {
            border: 2px solid red;
        }
    </style>
</head>
<body>
<p><span>I</span> <span>love</span> <span>China!</span></p>
<p>I love apple!</p>
</body>
</html>
```

`:last-child` 选择元素的最后一个子元素。　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        body>p:last-child {
            border: 2px solid red;
        }
    </style>
</head>
<body>
<p>I love apple!</p>
<p>I love apple!</p>
</body>
</html>
```

`:only-child `选择元素中唯一一个子元素。 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        p>span:only-child {
            border: 2px solid red;
        }
    </style>
</head>
<body>
<p>I <span>love</span> apple!</p>
<p>I <span>love</span> <span>apple!</span></p>
</body>
</html>
```

`:only-of-type `选择元素指定类型的唯一子元素。　　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        span:only-of-type {
            border: 2px solid red;
        }
    </style>
</head>
<body>
<p>I <span>love</span> apple!</p>
<p>I <span>love</span> <span>apple!</span></p>
</body>
</html>
```

- `:nth-child`选择器

- `:nth-child(n) `选择父元素的第n个子元素。

- `:nth-last-child(n)` 选择父元素的倒数第n个子元素

- `:nth-of-type(n)` 选择父元素定义类型的第n个子元素

- `:nth-last-of-type(n)`  选择父元素定义类型的倒数第n个子元素　　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        body>p:nth-of-type(2) {
            border: 2px solid red;
        }
    </style>
</head>
<body>
<p>I <span>love</span> apple!</p>
<a href="http://www.baidu.com">百度</a>
<p>I <span>love</span> <span>apple!</span></p>
</body>
</html>
```

---

### 2、UI伪类选择器

UI伪类选择器是根据元素的状态匹配元素。

a、`:enabled`和`:disabled`　选择启用和禁用的元素　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        :enabled {
            border: 2px solid red;
        }
    </style>
</head>
<body>
<input type="text" disabled value="test">
<br/>
<input type="text">
</body>
</html>
```

b、选择已经勾选的元素（只用于单选框和复选框）　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        :checked+span {
            border: 2px solid red;
        }
    </style>
</head>
<body>
<input type="checkbox" name="likes"><span>likes</span>
<input type="checkbox" name="likes"><span>likes2</span>
</body>
</html>
```

c、选择有效和无效的`input`元素

`:invalid`和`:valid`选择器用来匹配不符合和符合输入验证要求的`input`元素。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        :valid {
            border: 2px solid red;
        }
    </style>
</head>
<body>
<input type="text" required="" value="test">
<br/>
<input type="text" required="">
<button type="submit">提交</button>
</body>
</html>
```

![img](https://images2017.cnblogs.com/blog/1252860/201802/1252860-20180206180428451-1674871728.png)

d.选择限定范围的`input`元素

`:in-range`和`:out-of-range`　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        :in-range {
            border: 2px solid red;
        }
        :out-of-range {
            border: 2px solid yellow;
        }
    </style>
</head>
<body>
<input type="number" min="0" max="5">
</body>
</html>
```

e、选择必需的可选的`input`元素

`:required`匹配具有`required`属性的元素。`:optional`匹配没有`required`属性的元素。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        :required {
            border: 2px solid red;
        }
        :optional {
            border: 2px solid yellow;
        }
    </style>
</head>
<body>
name: <input type="text" required="">
<br/>
password: <input type="text">
</body>
</html>
```

![img](https://images2017.cnblogs.com/blog/1252860/201802/1252860-20180206181609076-152955168.png)

### 3、动态伪类选择器

动态伪类选择器可以根据条件改变匹配元素。

- `a.:link`和`:visited`选择器

- `:link`   选择链接元素

- `:visited` 选择用户已经访问的链接；　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        :link {
            border: 2px solid red;
        }
        :visited {
            border: 2px solid yellow;
        }
    </style>
</head>
<body>
<a href="http://www.baidu.com">百度</a>
<a href="http://www.sina.com">新浪</a>
</body>
</html>
```

链接没有访问的时候背景颜色是红的，访问后背景颜色是黄色。

b、`:hover`选择器` :hover`选择器匹配用户鼠标悬停在其上的任意元素。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        a:hover {
            background: red;
        }
    </style>
</head>
<body>
<a href="http://www.baidu.com">百度</a>
<a href="http://www.sina.com">新浪</a>
</body>
</html>
```

c、`:active`选择器 匹配用户激活的元素。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        a:active {
            background: green;
        }
    </style>
</head>
<body>
<a href="http://www.baidu.com">百度</a>
<a href="http://www.sina.com">新浪</a>
</body>
</html>
```

d、使用`:focus`选择器 用于匹配当前获得焦点的元素。　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        input:focus {
            border: 2px solid red;
        }
    </style>
</head>
<body>
<input type="text" autofocus>
</body>
</html>
```

### 4、其他选择器

a、否定选择器`:not`(选择器) 对任意选择器取反　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        a:not([href*="baidu"]) {
            border: 2px solid red;
        }
    </style>
</head>
<body>
<a href="http://www.baidu.com">百度</a>
<a href="http://www.sina.com">新浪</a>
</body>
</html>
```

b、`:empty`选择器 用于匹配没有定义任何子元素的元素。匹配的元素没有任何内容。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        :empty {
            border: 2px solid red;
        }
    </style>
</head>
<body>
<p></p>
<a href="http://www.baidu.com">百度</a>
<a href="http://www.sina.com">新浪</a>
</body>
</html>
```

![img](https://images2017.cnblogs.com/blog/1252860/201802/1252860-20180206185131732-1664270344.png)

c、`:lang`选择器 匹配基于`lang`全局属性的元素。　

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        :lang(en) {
            border: 2px solid red;
        }
    </style>
</head>
<body>
<p></p>
<a href="http://www.baidu.com" lang="en">百度</a>
<a href="http://www.sina.com" lang="en-us">新浪</a>
</body>
</html>
```

d、使用`:target`选择器 匹配URL片段标识符指向的元素。请求expample.html#mytaget页面会导航到该页面指定id的元素上。　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        :target {
            border: 2px solid red;
        }
    </style>
</head>
<body>
<p></p>
<a href="http://www.baidu.com" id="baidu">百度</a>
<a href="http://www.sina.com" id="sina">新浪</a>
</body>
</html>
```

