# Basic

## div和span

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
<span style="color: green; font-size: 30px">栏目一</span><br/>
<span style="color: orange; font-size: 16px">栏目二</span><br/>
<span style="color: blue; font-size: 16px; font-style: italic">栏目三</span><br/>
<span style="color: green; font-size: 16px; font-weight: bold">栏目四</span><br/>
<span style="color: navy; font-size: 16px">栏目五</span>
</body>
</html>
```

<span style="color: green; font-size: 30px">栏目一</span><br/>
<span style="color: orange; font-size: 16px">栏目二</span><br/>
<span style="color: blue; font-size: 16px; font-style: italic">栏目三</span><br/>
<span style="color: green; font-size: 16px; font-weight: bold">栏目四</span><br/>

<span style="color: navy; font-size: 16px">栏目五</span>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style type="text/css">
        .style1 {
            color: green;
            font-size: 30px;
            font-style: italic;
        }
    </style>
</head>
<body>
<span class="style1">栏目一</span><br/>
<span class="style1">栏目二</span><br/>
<span class="style1">栏目三</span><br/>
<span class="style1">栏目四</span><br/>
<span class="style1">栏目五</span><br/>
</body>
</html>
```

## 把一个网站的所有图片都为成黑白色或者模糊



---

## 合并单元格

```html
<table id="tabledemo" style="border: 1px black; width: 100%; height: 300px; text-align: center">
    <thead>
    <tr>
        <td colspan="6" height="30px">一、减税项目</td>
    </tr>
    <tr>
        <td rowspan="2" height="30px">减税性质代码及名称</td>
        <td height="30px">初期余额</td>
        <td height="30px">本期发生额</td>
        <td height="30px">本期应抵减税额</td>
        <td height="30px">本期实际抵减税额</td>
        <td height="30px">期末余额</td>
    </tr>
    <tr>
        <td height="30px">1</td>
        <td height="30px">2</td>
        <td height="30px">3=1+2</td>
        <td height="30px">4≤3</td>
        <td height="30px"><5=3-4/td>
    </tr>
    </thead>
</table>
```

<table id="tabledemo" style="border: 1px black; width: 100%; height: 300px; text-align: center">
    <thead>
    <tr>
        <td colspan="6" height="30px">一、减税项目</td>
    </tr>
    <tr>
        <td rowspan="2" height="30px">减税性质代码及名称</td>
        <td height="30px">初期余额</td>
        <td height="30px">本期发生额</td>
        <td height="30px">本期应抵减税额</td>
        <td height="30px">本期实际抵减税额</td>
        <td height="30px">期末余额</td>
    </tr>
    <tr>
        <td height="30px">1</td>
        <td height="30px">2</td>
        <td height="30px">3=1+2</td>
        <td height="30px">4≤3</td>
        <td height="30px"><5=3-4/td>
    </tr>
    </thead>
</table>
---

## 柱形图

```css
body {
    padding: 0;
    margin: 0;
    background: #fff;
}
.container {
    width: 400px;
    height: 300px;
    position: relative;
}
.red {
    position: absolute;
    background: #f00;
    width: 10%;
    height: 30%;
    left: 0;
    top: 210px;
    margin-right: 20px;
}
.gray {
    position: absolute;
    background: #ddd;
    width: 10%;
    height: 80%;
    left: 50px;
    top: 60px;
    margin-right: 20px;
}
.green {
    position: absolute;
    background: #0fd;
    width: 10%;
    height: 70%;
    left: 100px;
    top: 90px;
    margin-right: 20px;
}
.yellow {
    position: absolute;
    background: #ff0;
    width: 10%;
    height: 60%;
    left: 150px;
    top: 120px;
    margin-right: 20px;
}
.black {
    position: absolute;
    background: #234;
    width: 10%;
    height: 90%;
    left: 200px;
    top: 30px;
    margin-right: 20px;
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="style.css" type="text/css">
</head>
<body>
<div class="container">
    <div class="red"></div>
    <div class="gray"></div>
    <div class="green"></div>
    <div class="yellow"></div>
    <div class="black"></div>
</div>
</body>
</html>
```

<div class="container" style="width: 400px;
    height: 300px;
    position: relative;">
    <div class="red" style="position: absolute;
    background: #f00;
    width: 10%;
    height: 30%;
    left: 0;
    top: 210px;
    margin-right: 20px;"></div>
    <div class="gray" style="position: absolute;
    background: #ddd;
    width: 10%;
    height: 80%;
    left: 50px;
    top: 60px;
    margin-right: 20px;"></div>
    <div class="green" style="position: absolute;
    background: #0fd;
    width: 10%;
    height: 70%;
    left: 100px;
    top: 90px;
    margin-right: 20px;"></div>
    <div class="yellow" style="position: absolute;
    background: #ff0;
    width: 10%;
    height: 60%;
    left: 150px;
    top: 120px;
    margin-right: 20px;"></div>
    <div class="black" style="position: absolute;
    background: #234;
    width: 10%;
    height: 90%;
    left: 200px;
    top: 30px;
    margin-right: 20px;"></div>
</div>
---

## 图片居中方式

```css
div {
    width: 200px;
    height: 200px;
    border: 3px solid purple;
}
```

<div style="width: 200px;
    height: 200px;
    border: 3px solid purple;">
    <img src="graph/image-20200311110917082.png" alt="image-20200311110917082" />
</div>

解决方法一：

```css
img {
    position: relative;
    left: 50%;
    top: 50%;
    margin: -70px 0 0 -70px;
}
```

给`img`标签设置`position`定位，`position: relative; left: 50%; top: 50%`分别指将改元素向右移动一半父容器宽度的距离以及向下移动一半父容器高度的距离，由于移动的距离是以父容器为标准的一半高度宽度距离，效果如下：

<div style="width: 200px;
    height: 200px;
    border: 3px solid purple;">
    <img src="graph/image-20200311110917082.png" alt="image-20200311110917082" style="position: relative;
    left: 50%;
    top: 50%;"/>
</div>



因为这张图片较大，所以超出了div的范围。。。

之后要将`img`往回移动，才能使`img`元素居中显示，`margin:  -70px 0 0 -70px;`指的是将`img`元素向左移动`70px`，向上移动`70px`（因为用的图片素材的宽高为`140*140`），这样便能使得图片居中了。

<div style="width: 200px;
    height: 200px;
    border: 3px solid purple;">
    <img src="graph/image-20200311110917082.png" alt="image-20200311110917082" style="position: relative;
    left: 50%;
    top: 50%;                                                                                     margin: -70px 0 0 -70px;"/>
</div>

解决方法二：

```css
img {
    position: relative;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
}
```

其实这里跟上面的方法是类似的，但是个人觉得这种比较实用，因为方法一有个麻烦的地方，就是`margin`值必须跟着`img`元素的大小变化，如果说`img`元素都是一样的大小倒无所谓，但是这种要求未免有些高。

这种做法是用的2d转换，`transform：translate(x轴移动的数值, y轴移动的值)`，这个方法的好处便在于不用去测量`img`元素的宽高，直接设置百分比，在`transform: translate()`中，使用的百分比其实是相对于元素自身宽高的。

<div style="width: 200px;
    height: 200px;
    border: 3px solid purple;">
    <img src="graph/image-20200311110917082.png" alt="image-20200311110917082" style="position: relative;
    left: 50%;
    top: 50%;                                                                                     transform: translate(-50%,-50%);"/>
</div>

解决方法三：

```css
div.container {
    display: table;
    text-align: center;
}
div.container div {
    display: table-cell;
    vertical-align: middle;
}
```

```html
<div class="container">
    <div>
        <img src="graph/image-20200311110917082.png" alt="image-20200311110917082" />
    </div>
</div>
```

<div style="width: 200px;
    height: 200px;
    border: 3px solid purple; display: table;
    text-align: center;">
    <div style="display: table-cell;
    vertical-align: middle;">
    <img src="graph/image-20200311110917082.png" alt="image-20200311110917082"/>
        </div>
</div>

设置为两级父容器，第一级设置`display: table`，将第一级父容器转换成表格类型，之后在第二级，也就是`img`的上一级父容器设置`display: table-cell`，在第一级父容器中设置`text-align: center`，第二级设置`vertical-align: middle`，便可以达到将图片居中的目的

**对父级使用`text-align: center; `会对行级块以及行级元素`span`有居中的效果。**

解决方法四：

```css
div.container {
    display: flex;
    justify-content: space-around;
    align-items: center;
}
```

给父容器设置`display: flex`，将父容器转换成伸缩盒子，因为应用主侧轴对齐方式就需要这样。之后再设置主轴对齐方式为 `justify-content:  space-around;` 接着设置父容器的侧轴对齐方式，`align-items: center;`

<div style="width: 200px;
    height: 200px;
    border: 3px solid purple;display: flex;
    justify-content: space-around;
    align-items: center;">
    <img src="graph/image-20200311110917082.png" alt="image-20200311110917082" "/>
</div>
---

## text-align的用法

`text-align`运用在块级元素中，使其中的文本对齐。事实上这句话的意思是运用在块级元素中`text-align`会使其包含行内元素对齐。

```css
.test {
    width: 300px;
    height: 300px;
    text-align: center;
    background: pink;
}
.test div {
    border: 1px solid black;
}
.test p {
    width: 150px;
    height: 50px;
    background: red;
}
span {
    border: 1px solid black;
}
h1 {
    border: 1px solid black;
}
img {
    width: 20%;
    height: 20%;
}
```

```html
<div class="test">
        <div>我是div</div>
        <p>我是块级元素p</p>
        <span>我是行级元素span</span>
        <h1>我是h2，块级</h1>
        <img src="graph/image-20200311110917082.png" alt=""/>
</div>
```

<div class="test" style="width: 300px;
    height: 300px;
    text-align: center;
    background: pink;">
        <div style="border: 1px solid black;">我是div</div>
        <p style="width: 150px;
    height: 50px;
    background: red;">我是块级元素p</p>
        <span style="border: 1px solid black;">我是行级元素span</span>
        <h1 style="border: 1px solid black;">我是h2，块级</h1>
        <img src="graph/image-20200311110917082.png" alt=""style="width: 20%;
    height: 20%;">
</div>
如上图所示：

- 我们发现对父级使用`text-align: center; `会对行级块以及行级元素`span`有居中的效果。
- 而对块级元素`div`以及`h2`看似也有居中效果？这是为什么呢？
- 观察可以发现我们并没有给`div`和`h2`设置宽高，当没有设置宽高的时候，其宽度继承了父级的，高度是由文本撑开，当然也继承了父级的`text-align: center;`
- 但是我们观察块级元素`p`标签，`p`元素我们给你设置了宽高，此时它本身不是水平居中，而其文本是居中的，也就是说，给父级设置`text-align`这个属性，只会对其子元素是行级以及行级块元素起作用，且子元素会继承`text-align`这个属性对其文本起作用。
- 当我们把`p`元素转换为行级块元素的时候，你会发现，不仅`p`元素中的文本居中了，其自身也居中了。

---

## 设置表格的布局

```css
table.one {
    table-layout: auto;
}
table.two {
    table-layout: fixed;
}
```

```html
<table class="one" style="border: 1px solid; width: 100%">
    <tr>
        <td style="width: 20%">1000000000000000000000000000</td>
        <td style="width: 40%">10000000</td>
        <td style="width: 40%">100</td>
    </tr>
</table>
<br/>
<table class="two" style="border: 1px solid; width: 100%">
    <tr>
        <td style="width: 20%">1000000000000000000000000000</td>
        <td style="width: 40%">10000000</td>
        <td style="width: 40%">100</td>
    </tr>
</table>
```

<table class="one" style="border: 1px solid; width: 100%; table-layout: auto;">
    <tr>
        <td style="width: 20%">1000000000000000000000000000</td>
        <td style="width: 40%">10000000</td>
        <td style="width: 40%">100</td>
    </tr>
</table>

<table class="two" style="border: 1px solid; width: 100%; table-layout: fixed;">
    <tr>
        <td style="width: 20%">1000000000000000000000000000</td>
        <td style="width: 40%">10000000</td>
        <td style="width: 40%">100</td>
    </tr>
</table>
---

## 显示表格中的空单元

```css
table, tr, td {
    border: 1px solid;
    border-collapse: separate;
    empty-cells: hide;
}
```

<table style="border: 1px solid;
    border-collapse: separate;
    empty-cells: hide;width: 100px">
    <tr style="border: 1px solid;
    border-collapse: separate;
    empty-cells: hide;">
        <td style="border: 1px solid;
    border-collapse: separate;
    empty-cells: hide;">Adams</td>
        <td style="border: 1px solid;
    border-collapse: separate;
    empty-cells: hide;">John</td>
    </tr>
    <tr style="border: 1px solid;
    border-collapse: separate;
    empty-cells: hide;">
        <td style="border: 1px solid;
    border-collapse: separate;
    empty-cells: hide;">Bush</td>
        <td style="border: 1px solid;
    border-collapse: separate;
    empty-cells: hide;"></td>
    </tr>
</table>
---

## 合并表格边框

```css
table {
    border-collapse: collapse;
}
table, tr, td {
    border: 1px solid black;
}
```

<table style="border-collapse: collapse;border: 1px solid black;width: 200px">
    <tr style="border: 1px solid black;">
        <th style="border: 1px solid black;">Firstname</th>
        <th style="border: 1px solid black;">Lastname</th>
    </tr>
    <tr style="border: 1px solid black;">
        <td style="border: 1px solid black;">Bill</td>
        <td style="border: 1px solid black;">Gates</td>
    </tr>
    <tr style="border: 1px solid black;">
        <td style="border: 1px solid black;">Steven</td>
        <td style="border: 1px solid black;">Jobs</td>
    </tr>
</table>
---

## 设置表格边框之间的空白

```css
table {
    border-collapse: separate;
    border-spacing: 10px;
}

table, tr, td {
    border: 1px solid black;
}
```

<table style="border-collapse: separate;
    border-spacing: 10px;border: 1px solid black;width: 200px">
    <tr style="border: 1px solid black;">
         <td style="border: 1px solid black;">Carter</td>
         <td style="border: 1px solid black;">Thomas</td>
    </tr>
    <tr style="border: 1px solid black;">
         <td style="border: 1px solid black;">Gates</td>
         <td style="border: 1px solid black;">Bill</td>
    </tr>
</table>
---

## 设置表格标题的位置

```css
caption {
	caption-side:bottom
}
```

<table style="border-collapse: collapse;
    border: 1px solid black;width: 200px">
    <caption style="caption-side: bottom">This is a caption</caption>
    <tr style="border: 1px solid black;">
         <td style="border: 1px solid black;">Carter</td>
         <td style="border: 1px solid black;">Thomas</td>
    </tr>
    <tr style="border: 1px solid black;">
         <td style="border: 1px solid black;">Gates</td>
         <td style="border: 1px solid black;">Bill</td>
    </tr>
</table>
---

## 在元素周围画线

```css
p {
    border: red solid thin;
    outline: #00ff00 dotted thick;
}
```

<p style="border: red solid thin;
    outline: #00ff00 dotted thick;">This is a papagraph</p>
---

## 使用百分比设置行间距

```css
p.small {line-height: 90%}
p.big {line-height: 200%}
```

---

## 如何把元素显示为内联元素

```css
p {display: inline}
div {display: none}
```

```html
<p>本例中的样式表把段落元素设置为内联元素。</p>
<p>而 div 元素不会显示出来！</p>
<div>div 元素的内容不会显示出来！</div>
```

<p style="display: inline">本例中的样式表把段落元素设置为内联元素。</p>
<p style="display: inline">而 div 元素不会显示出来！</p>

---

## 如何把元素显示为块级元素

```css
span {
	display: block;
}
```

<div><span style="display: block">本例中的样式表把 span 元素设置为块级元素。</span>
    <span style="display: block">两个 span 元素之间产生了一个换行行为。</span>
</div>
---

## 使图像浮动于一个段落的右侧。

```css
img {
	float:right;
}
```

```html
<p>在下面的段落中，我们添加了一个样式为 <b>float:right</b> 的图像。结果是这个图像会浮动到段落的右侧。</p>
<p><img src="/i/eg_cute.gif" /></p>
```

---

## 将带有边框和边界的图像浮动于段落的右侧

```css
img {
    float: right;
    border: 1px dotted black;
    margin: 0px 0px 15px 20px;
}
```

---

## 带标题的图像浮动于右侧

```css
div {
    float: right;
    width: 120px;
    margin: 0 0 15px 20px;
    padding: 15px;
    border: 1px solid black;
    text-align: center;
}
```

---

## 使段落的首字母浮动于左侧

```css
span {
    float: left;
    width: 0.7em;
    font-size: 400%;
    font-family: algerian, courier;
    line-height: 80%;
}
```

<p >
    <span style="float: left;
    width: 0.7em;
    font-size: 400%;
    font-family: algerian, courier;
    line-height: 80%;">T</span>his is some text.</p>


---

## 创建水平菜单

```css
ul {
    float: left;
    width: 100%;
    padding: 0;
    margin: 0;
    list-style-type: none;
}
a {
    float: left;
    width: 7em;
    text-decoration: none;
    color: white;
    background: purple;
    padding: 0.2em 0.6em;
    border-right: 1px solid white;
}
a:hover {
    background: #ff3300;
}
```

```html
<ul>
    <li><a href="#">Link one</a></li>
    <li><a href="#">Link two</a></li>
    <li><a href="#">Link three</a></li>
    <li><a href="#">Link four</a></li>
</ul>
```

<ul style="float: left;
    width: 100%;
    padding: 0;
    margin: 0;
    list-style-type: none;">
    <li><a href="#" style="float: left;
    width: 7em;
    text-decoration: none;
    color: white;
    background: purple;
    padding: 0.2em 0.6em;
    border-right: 1px solid white;">Link one</a></li>
    <li><a href="#" style="float: left;
    width: 7em;
    text-decoration: none;
    color: white;
    background: purple;
    padding: 0.2em 0.6em;
    border-right: 1px solid white;">Link two</a></li>
    <li><a href="#" style="float: left;
    width: 7em;
    text-decoration: none;
    color: white;
    background: purple;
    padding: 0.2em 0.6em;
    border-right: 1px solid white;">Link three</a></li>
    <li><a href="#" style="float: left;
    width: 7em;
    text-decoration: none;
    color: white;
    background: purple;
    padding: 0.2em 0.6em;
    border-right: 1px solid white;">Link four</a></li>
</ul>
---

## 使用浮动来创建拥有页眉、页脚、左侧目录和主体内容的首页

```css
div.container {
    width: 100px;
    margin: 0;
    border: 1px solid grey;
    line-height: 150%;
}
div.header, div.footer {
    padding: 0.5em;
    color: white;
    background: grey;
    clear: left;
    text-align: center;
}
h1.header {
    padding: 0;
    margin: 0;
}
div.left {
    float: left;
    width: 160px;
    margin: 0;
    padding: 1em;
}
div.content {
    margin-left: 190px;
    border-left: 1px solid grey;
    padding: 1em;
}
```

```html
<div class="container">
    <div class="header">
        <h1 class="header">W3School.com.cn</h1>
    </div>
    <div class="left">
        <p>"Never increase, beyond what is necessary, the number of entities required to explain anything." William of Ockham (1285-1349)</p>
    </div>
    <div class="content">
        <h2>Free Web Building Tutorials</h2>
        <p>At W3School.com.cn you will find all the Web-building tutorials you need,
        from basic HTML and XHTML to advanced XML, XSL, Multimedia and WAP.</p>
        <p>W3School.com.cn - The Largest Web Developers Site On The Net!</p>
    </div>
    <div class="footer">
        Copyright 2008 by YingKe Investment.
    </div>
</div>
```

<div class="container" style="width: 100%;
    margin: 0;
    border: 1px solid grey;
    line-height: 150%;">
    <div class="header" style="padding: 0.5em;
    color: white;
    background: grey;
    clear: left;">
        <h1 class="header" style="padding: 0;
    margin: 0;text-align: center;">W3School.com.cn</h1>
    </div>
    <div class="left" style="float: left;
    width: 160px;
    margin: 0;
    padding: 1em;">
        <p>"Never increase, beyond what is necessary, the number of entities required to explain anything." William of Ockham (1285-1349)</p>
    </div>
    <div class="content" style="margin-left: 190px;
    border-left: 1px solid grey;
    padding: 1em;">
        <h2>Free Web Building Tutorials</h2>
        <p>At W3School.com.cn you will find all the Web-building tutorials you need,
        from basic HTML and XHTML to advanced XML, XSL, Multimedia and WAP.</p>
        <p>W3School.com.cn - The Largest Web Developers Site On The Net!</p>
    </div>
    <div class="footer" style="padding: 0.5em;
    color: white;
    background: grey;
    clear: left;text-align: center;">
        Copyright 2008 by YingKe Investment.
    </div>
</div>
---

```html
<div style="display: flex; justify-content: center;text-align: center">
    <div>
   		<img src="graph/image-20200314102238849.png" alt="image-20200314102238849" style="zoom:80%;" />
    	<p>RLC并联电路</p>
    </div>
</div>
```

---

## 如何相对于一个元素的正常位置来对其定位

```css
h2.pos_left {
    position: relative;
    left: -20px;
}
h2.pos_right {
    position: relative;
    left: 20px;
}
```

```html
<h2>这是位于正常位置的标题</h2>
<h2 class="pos_left">这个标题相对于其正常位置向左移动</h2>
<h2 class="pos_right">这个标题相对于其正常位置向右移动</h2>
<p>相对定位会按照元素的原始位置对该元素进行移动。</p>
<p>样式 "left:-20px" 从元素的原始左侧位置减去 20 像素。</p>
<p>样式 "left:20px" 向元素的原始左侧位置增加 20 像素。</p>
```

<h2>这是位于正常位置的标题</h2>
<h2 class="pos_left" style="position: relative;
    left: -20px;">这个标题相对于其正常位置向左移动</h2>
<h2 class="pos_right" style="position: relative;
    left: 20px;">这个标题相对于其正常位置向右移动</h2>
<p>相对定位会按照元素的原始位置对该元素进行移动。</p>
<p>样式 "left:-20px" 从元素的原始左侧位置减去 20 像素。</p>
<p>样式 "left:20px" 向元素的原始左侧位置增加 20 像素。</p>

---

## 如何相对于浏览器窗口来对元素进行定位

```css
h2.pos_abs {
    left: 100px;
    top: 150px;
}
```

---

## 如何使元素不可见

```css
h1.visible {visibility: visible}
h1.invisible {visibility: hidden}
```

<h1 class="visible" style="visibility:visible">这是可见的标题</h1>
<h1 class="invisible" style="visibility:hidden">这是不可见的标题</h1>

---

## 如何使表格元素叠加

```css
table, tr, td {
    border: 1px solid black;
}
tr.coll {
    visibility: collapse;
}
```

```html
<table>
    <tr>
        <td>Adams</td>
        <td>John</td>
    </tr>
    <tr class="coll">
        <td>Bush</td>
        <td>George</td>
    </tr>
</table>
```

<table>
    <tr>
        <td>Adams</td>
        <td>John</td>
    </tr>
    <tr class="coll" style="visibility: collapse;">
        <td>Bush</td>
        <td>George</td>
    </tr>
</table>
---

## 改变光标

```html
<p>请把鼠标移动到单词上，可以看到鼠标指针发生变化：</p>
<span style="cursor: auto">Auto</span><br />
<span style="cursor: crosshair">Crosshair</span><br />
<span style="cursor: default">Default</span><br />
<span style="cursor: pointer">Pointer</span><br />
<span style="cursor: move">Move</span><br />
<span style="cursor: e-resize">e-resize</span><br />
<span style="cursor: ne-resize">ne-resize</span><br />
<span style="cursor: nw-resize">nw-resize</span><br />
<span style="cursor: n-resize">n-resize</span><br />
<span style="cursor: se-resize">se-resize</span><br />
<span style="cursor: sw-resize">sw-resize</span><br />
<span style="cursor: s-resize">s-resize</span><br />
<span style="cursor: w-resize">w-resize</span><br />
<span style="cursor: text">text</span><br />
<span style="cursor: wait">wait</span><br />
<span style="cursor: help">help</span>
```

<p>请把鼠标移动到单词上，可以看到鼠标指针发生变化：</p>
<span style="cursor: auto">Auto</span><br />
<span style="cursor: crosshair">Crosshair</span><br />
<span style="cursor: default">Default</span><br />
<span style="cursor: pointer">Pointer</span><br />
<span style="cursor: move">Move</span><br />
<span style="cursor: e-resize">e-resize</span><br />
<span style="cursor: ne-resize">ne-resize</span><br />
<span style="cursor: nw-resize">nw-resize</span><br />
<span style="cursor: n-resize">n-resize</span><br />
<span style="cursor: se-resize">se-resize</span><br />
<span style="cursor: sw-resize">sw-resize</span><br />
<span style="cursor: s-resize">s-resize</span><br />
<span style="cursor: w-resize">w-resize</span><br />
<span style="cursor: text">text</span><br />
<span style="cursor: wait">wait</span><br />
<span style="cursor: help">help</span>

----

## 定位：固定定位

```css
p.one {
    position: fixed;
    left: 5px;
    top: 5px;
}
```

---

## 设置元素的形状

```css
img {
    position: absolute;
    clip: rect(0 50px 200px 0);
}
```

---

## 如何使用滚动条来显示元素内溢出的内容

```css
div {
    background: #0ff;
    width: 150px;
    height: 150px;
    overflow: scroll;
}
```

---

## 如何隐藏溢出元素中溢出的内容

```css
div {
    background: #0ff;
    width: 150px;
    height: 150px;
    overflow: hidden;
}
```

---

## 如何设置浏览器来自动地处理溢出

```css
div {
    background: #0ff;
    width: 150px;
    height: 150px;
    overflow: auto;
}
```

---

## 如何在文本中垂直排列图象

```css
img.top {
    vertical-align: text-top;
}
img.bottom {
    vertical-align: text-bottom;
}
```

```css
<p>这是一幅<img class="top" border="0" src="/i/eg_cute.gif" />位于段落中的图像。</p> 
<p>这是一幅<img class="bottom" border="0" src="/i/eg_cute.gif" />位于段落中的图像。</p>
```

---

## 使用固定值设置图像的上边缘

```css
img {
    position: absolute;
    top: 0;
}
```

---

## 使用百分比设置图像的上边缘

```css
img {
    position: absolute;
    top: 5%;
}
```

----

## 使用像素值设置图像的底部边缘

```css
img {
    position: absolute;
    bottom: 0;
}
```

---

## 使用百分比设置图像的底部边缘

```css
img {
    position: absolute;
    bottom: 5%;
}
```

---

## 如何向文档中的超链接添加不同的颜色。

```css
a:link {color: #f00}
a:visited {color: #0f0}
a:hover{color: #f0f}
a:active{color: #00f}
```

> **注释：**在 CSS 定义中，`a:hover` 必须位于` a:link` 和` a:visited` 之后，这样才能生效！
>
> **注释：**在 CSS 定义中，`a:active` 必须位于 `a:hover` 之后，这样才能生效！

---

## 超链接：:focus 的使用

```css
input:focus {
    background: yellow;
}

```

```html
<form action="form_action.asp" method="get">
    First name: <input type="text" name="fname" ><br/>
    First name: <input type="text" name="fname" ><br/>
    <input type="submit" value="Submit">
</form>
```



<style>
    input:focus {
    background: yellow;
}
</style>
<form action="form_action.asp" method="get">
    First name: <input type="text" name="fname" ><br/>
    First name: <input type="text" name="fname" ><br/>
    <input type="submit" value="Submit">
</form>
---

## :first-child（首个子对象）

```css
p:first-child {font-weight: bold}
li:first-child {text-transform: uppercase}
```

```html
<div>
    <p>These are the necessary steps:</p>
    <ul>
        <li>Intert Key</li>
        <li>Turn key clockwise</li>
        <li>Push accelerator</li>
    </ul>
    <p>Do push the brake at the same time as the accelerator.</p>
</div>
```



---

## 制作首字母特效

```css
p:first-letter {
    color: #f00; 
    font-size: xx-large
}
```

----

## 制作首行特效

```css
p:first-line {color: #f00; font-variant: small-caps}
```









