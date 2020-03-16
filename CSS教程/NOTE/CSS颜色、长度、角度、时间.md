# CSS中的颜色、长度、角度、时间

## 一、颜色的表示方法

　　颜色是通过对红、绿和蓝光的组合来显示的。

### 1、颜色名　　　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        h1 {
            background: red;
        }
    </style>
</head>
<body>
<h1>字母xYZ</h1>
</body>
</html>
```

### 2.十六进制颜色

十六进制颜色是这样规定的：`#RRGGBB`，其中的 `RR`（红色）、`GG`（绿色）、`BB`（蓝色）十六进制整数规定了颜色的成分。所有值必须介于 `0` 与 `FF` 之间。

举例说，`#0000ff` 值显示为蓝色，这是因为蓝色成分被设置为最高值（`ff`），而其他成分被设置为 `0`。类似`#ff00ff`的可以简写成`#f0f`;　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        h1 {
            background: #ff00ff;
        }
    </style>
</head>
<body>
<h1>字母xYZ</h1>
</body>
</html>
```

### 3、RGB颜色

　　RGB 颜色值是这样规定的：`rgb(red, green, blue)`。每个参数 (red、green 以及 blue) 定义颜色的强度，可以是介于` 0 `与 `255 `之间的整数，或者是百分比值（从 `0%` 到` 100%`）。举例说，`rgb(0,0,255)` 值显示为蓝色，这是因为 `blue `参数被设置为最高值（`255`），而其他被设置为 `0`。同样地，下面的值定义了相同的颜色：`rgb(0,0,255)` 和 `rgb(0%,0%,100%)`。　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        h1 {
            background: rgb(255,0,0);
        }
    </style>
</head>
<body>
<h1>字母xYZ</h1>
</body>
</html>
```

### 4、RGBA颜色　　

RGBA 颜色值得到以下浏览器的支持：IE9+、Firefox 3+、Chrome、Safari 以及 Opera 10+。

RGBA 颜色值是 RGB 颜色值的扩展，带有一个 alpha 通道 - 它规定了对象的不透明度。

RGBA 颜色值是这样规定的：`rgba(red, green, blue, alpha)`。alpha 参数是介于 0.0（完全透明）与 1.0（完全不透明）的数字。　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        h1 {
            background: rgba(255,0,0,1.0);
        }
        h2 {
            background: rgba(255,0,0,0.8);
        }
        h3 {
            background: rgba(255,0,0,0.6);
        }
        h4 {
            background: rgba(255,0,0,0.4);
        }
        h5 {
            background: rgba(255,0,0,0.2);
        }
        h6 {
            background: rgba(255,0,0,0.0);
        }
    </style>
</head>
<body>
<h1>字母xYZ</h1>
<h2>字母xYZ</h2>
<h3>字母xYZ</h3>
<h4>字母xYZ</h4>
<h5>字母xYZ</h5>
<h6>字母xYZ</h6>
</body>
</html>
```

![img](https://images2017.cnblogs.com/blog/1252860/201802/1252860-20180208003129185-480445564.png)

### 5、HSL颜色

HSL 颜色值得到以下浏览器的支持：IE9+、Firefox、Chrome、Safari 以及 Opera 10+。

HSL 指的是 `hue`（色调）、`saturation`（饱和度）、`lightness`（亮度） - 表示颜色柱面坐标表示法。

HSL 颜色值是这样规定的：`hsl(hue, saturation, lightness)`。

- **Hue** 是色盘上的度数（从 `0` 到 `360`） `0` (或 `360`) 是红色，`120 `是绿色，`240 `是蓝色。
- **Saturation** 是百分比值；`0%` 意味着灰色，而 `100%` 是全彩。
- **Lightness** 同样是百分比值；`0%` 是黑色，`100%` 是白色。　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        h1 {
            background: hsl(240,50%,50%);
        }

    </style>
</head>
<body>
<h1>字母xYZ</h1>
</body>
</html>
```

### 6、HSLA颜色　　

HSLA 颜色值得到以下浏览器的支持：IE9+、Firefox 3+、Chrome、Safari 以及 Opera 10+。

HSLA 颜色值是 HSL 颜色值的扩展，带有一个 alpha 通道 - 它规定了对象的不透明度。

HSLA 颜色值是这样规定的：`hsla(hue, saturation, lightness, alpha)`，其中的 *alpha* 参数定义不透明度。*alpha* 参数是介于 `0.0`（完全透明）与 `1.0`（完全不透明）的数字。　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        h1 {
            background: hsla(240,50%,50%,1.0);
        }
        h2 {
            background: hsla(240,50%,50%,0.8);
        }
        h3 {
            background: hsla(240,50%,50%,0.6);
        }
        h4 {
            background: hsla(240,50%,50%,0.4);
        }
        h5 {
            background: hsla(240,50%,50%,0.2);
        }
        h6 {
            background: hsla(240,50%,50%,0.0);
        }
    </style>
</head>
<body>
<h1>字母xYZ</h1>
<h2>字母xYZ</h2>
<h3>字母xYZ</h3>
<h4>字母xYZ</h4>
<h5>字母xYZ</h5>
<h6>字母xYZ</h6>
</body>
</html>
```

![img](https://images2017.cnblogs.com/blog/1252860/201802/1252860-20180208002706920-261978474.png)

---

## 二.长度单位

### 1、绝对长度

- a、`in`(英寸)

- b、`cm`（厘米）

- c、`mm`(毫米)

- d、`pt`  (磅) `1pt = 1/72in`

- e、`pc`   `1pc = 12pt`

- f、`px `(像素)  `1px = 1/96in　`

```jade
 1in = 2.54cm =25.4mm=72pt=12pc=96px
```

### 2、相对长度

a、`em`

`em`是相对元素内容的字体而言的。　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        p {
            background: grey;
            color: white;
            font-size: 15pt;
            height: 2em;
        }
    </style>
</head>
<body>
<p>字母xYZ</p>
<p style="font-size: 12pt">字母xYZ</p>
</body>
</html>
```

由于第二个p元素的字体高度是12pt小于第一个，所以p元素的高度比第一个小。

![img](https://images2017.cnblogs.com/blog/1252860/201802/1252860-20180208004309310-1547271035.png)

---

b、`ex`

`ex`值得是当前字体中小写字母$x$的高度，也即是字体基线到中线的距离，一般与字母$x$的高度相当，通常`1ex=0.5em`;　　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        p {
            background: grey;
            color: red;
            font-size: 100pt;
            height: 2ex;
        }
    </style>
</head>
<body>
<p>字母xYZ</p>
</body>
</html>
```

![img](https://images2017.cnblogs.com/blog/1252860/201802/1252860-20180208014758373-402906225.png)

---

c、rem

`rem`是根据html元素的字号而定的。　　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        html {
            font-size: 0.2in;
        }
        p {
            background: grey;
            color: red;
            font-size: 2rem;
        }
    </style>
</head>
<body>
<p>字母xYZ</p>
</body>
</html>
```

### 3、百分比

使用百分比属性会遇到两个麻烦，一是不是所有的属性都能用这个单位，二是对于能用百分比的属性，那个百分比挂钩的其他属性各不相同。　

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        p {
            background: grey;
            color: red;
            font-size: 200%;
            width: 50%;
        }
    </style>
</head>
<body>
<p>字母xYZ</p>
</body>
</html>
```

与`font-size`属性挂钩是继承来的`font-size`值，而`width`是根据父元素宽度的百分比来计算的。其他使用百分比单位的，应根据css属性具体分析。

当元素使用的`width`是百分比，如果元素时绝对定位，那么元素的宽度取决于最近的不为`static`定位的祖先元素的`content+padding`。如果元素是`fixed`定位，那么元素的宽度取决于`viewport`的宽度，如果是`relative`定位或者`static`,那么元素的宽度取决于最近的块级父元素的`content`的宽度。

当元素是`relative`或者`static`定位时,元素最近的块级父元素时`body`，那么这使设置的百分比高度不会生效；

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        div {
            width: 30%;
            background: #2a7db5;
            height: 100%;
        }
    </style>
</head>
<body>
<div></div>
</body>
</html>
```

如果我们一定要使用百分比，那么需要给`body`和`html`设置`height`为`100%`；

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        html {
            height: 100%;
        }
        body {
            height: 100%;
        }
        div {
            width: 30%;
            background: #2a7db5;
            height: 100%;
        }
    </style>
</head>
<body>
<div></div>
</body>
</html>
```

---

### 4、vh、vw、vmin、vmax

`vh`、和`vw`是相对于`viewport`的高和宽来计算的，给一个元素设置宽度为`100vh`,相当于对这个元素设置`fixed`定位并把元素的宽度设置为`100%`。　

`vmin`是使用`viewport`中`vh`和`vw`中较小的来设置的，而`vmax`正好相反。　

如我们设置一个元素的字体100vmin,vh为(`1/100)*viewport`高度，vw为`(1/100)*viewport`宽度，当vh小于vw时，字体的宽度为100vh,当vw<vh时，为100vw.

---

## 三、CSS角度

- `deg`度（取值0~360deg）

- `grad  `百分度（取值范围：0~400grad）

- `rad`　 弧度（取值为0到2π弧度）

- `turn`  圆周（1turn=360deg）

---

## 四、CSS时间

- `s`            秒

- `ms`        毫秒（1s=1000ms）　

---

