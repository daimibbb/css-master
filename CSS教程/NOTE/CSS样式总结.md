# CSS样式总结

## 一、内联样式

内联样式通过`style`属性来设置，属性值可以任意的CSS样式。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<p style="background: red">I love China!</p>
</body>
</html>
```

## 二、内部样式

内部样式定义在文档的`head`部分，通过``style``标签来设置。需要使用元素选择器（`p`）来关联样式和要设置样式的标签（`p`标签）。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        p {
            background: green;
        }
    </style>
</head>
<body>
<p>I love China!</p>
</body>
</html>
```

## 三、外部样式

在文档外的`*.css`定义`css`样式，然后在文档的`head`部分通过`link`元素引入。

```css
/*style.css*/
p {
    background: yellow;
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<p>I love China!</p>
</body>
</html>
```

a. 在一个外部样式表中导入其他样式表的样式

`combine.css`文件中导入上面的`style.css`

```css
/*combine.css*/
@import "style.css";
body {
    background: red;
}
```

HTML文件中引入`combine.css`文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="combine.css">
</head>
<body>
<p>I love China!</p>
</body>
</html>
```

b. 声明样式表的字符编码　

```css
/*style.css*/
@charset "UTF-8";
p {
    background: yellow !important;
}
```

---

## 四、元素样式的层叠和继承

### 1、样式层叠

　　样式表允许以多种方式规定样式信息。样式可以规定在单个的 HTML 元素中，在 HTML 页的头元素中，或在一个外部的 CSS 文件中。甚至可以在同一个 HTML 文档内部引用多个外部样式表。一般而言，所有的样式会根据下面的规则**层叠**于一个新的虚拟样式表中，其中数字 4 拥有最高的优先权。　　

1. 浏览器缺省设置（浏览器的默认样式）
2. 外部样式表
3. 内部样式表（位于 `<head>` 标签内部）
4. 内联样式（在 HTML 元素内部）
5. 同一样式表中，CSS选择器越准确的，优先级越高。

　　不同优先级的样式表定义元素的不同`css`属性都会作用在元素上，相同的`css`属性只有优先级最高的会对元素起作用。相同优先级样式表中`css`选择器准确的样式起作用，同一样式表中`css`选择器一样的后边会覆盖前边的样式。

用重要样式（`！important`）可以调整层叠次序　

```css
/*style.css*/
p {
    background: yellow !important;
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
<p style="background: red">I love China!</p>
</body>
</html>
```

`important`标记的样式会有最高的优先级。

在谷歌浏览器的开发者工具中我们可以查看元素的优先级，同一个元素的最上面的样式的优先级最高。

![img](https://img2018.cnblogs.com/blog/1252860/201901/1252860-20190127015043697-121344092.png)

### 2、样式继承

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        p {
            color: white;
            background: grey;
            border: 2px solid black;
        }
    </style>
</head>
<body>
<p> I  <span>love</span>  China!</p>
</body>
</html>
```

`span`元素并没设置字体颜色，但是却是用前景色`white`，这个值有父元素`p`继承来。可以从一个元素的祖先元素继承样式，继承来的样式的优先级是最低的（比浏览器的默认样式的优先级都低）。

并非所有的css属性均可继承，只有与元素外观相关的元素会继承。元素在页面布局相关的样式不会继承，css中可以使用`inherit`强行实行继承。　　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        p {
            color: white;
            background: grey;
            border: 2px solid black;
        }
        span {
            border: inherit;
        }
    </style>
</head>
<body>
<p> I  <span>love</span>  China!</p>
</body>
</html>
```

### 3.继承属性和通用元素选择器

我们有时候给所有元素的设置某个样式，如字体等，我们一般会使用通用选择器来设置。但是对所有元素都起作用，效率较低，这个时候我们可以考虑给`body`元素设置字体，`body`的子元素会默认继承字体。

---

