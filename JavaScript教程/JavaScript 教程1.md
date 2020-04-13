# JavaScript 教程

JavaScript 是 Web 的编程语言。

所有现代的 HTML 页面都使用 JavaScript。

JavaScript 非常容易学。

本教程将教你学习从初级到高级JavaScript知识。

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
<script>
function displayDate() {
	document.getElementById("demo").innerHTML=Date();
}
</script>
</head>
<body>
<h1>我的第一个 JavaScript 程序</h1>
<p id="demo">这是一个段落</p>
<button type="button" onclick="displayDate()">显示日期</button>
</body>
</html>
```

[效果：](https://htmlpreview.github.io/?https://github.com/daimibbb/css-master/blob/master/JavaScript%E6%95%99%E7%A8%8B/code/tryjs_events.html)

## 为什么学习 JavaScript?

JavaScript web 开发人员必须学习的 3 门语言中的一门：

1. **HTML** 定义了网页的内容
2. **CSS** 描述了网页的布局
3. **JavaScript** 网页的行为

本教程是关于 JavaScript 及介绍 JavaScript 如何与 HTML 和 CSS 一起工作。

---

# JavaScript 简介

JavaScript 是互联网上最流行的脚本语言，这门语言可用于 HTML 和 web，更可广泛用于服务器、PC、笔记本电脑、平板电脑和智能手机等设备。

## JavaScript 是脚本语言

JavaScript 是一种轻量级的编程语言。

JavaScript 是可插入 HTML 页面的编程代码。

JavaScript 插入 HTML 页面后，可由所有的现代浏览器执行。

JavaScript 很容易学习。

## 您将学到什么

下面是您将在本教程中学到的主要内容。

## JavaScript：直接写入 HTML 输出流

```javascript
document.write("<h1>这是一个标题</h1>");
document.write("<p>这是一个段落。</p>");
```

[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_intro_document_write)

>您只能在 HTML 输出中使用 `document.write`。如果您在文档加载后使用该方法，会覆盖整个文档。

## JavaScript：对事件的反应

```javascript
<button type="button" onclick="alert('欢迎!')">点我!</button>
```

[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_intro_alert)

`alert()` 函数在 JavaScript 中并不常用，但它对于代码测试非常方便。*onclick* 事件只是您即将在本教程中学到的众多事件之一。

## JavaScript：改变 HTML 内容

使用 JavaScript 来处理 HTML 内容是非常强大的功能。

```javascript
function myFunction() {
	x = document.getElementById("demo");  // 找到元素
	x.innerHTML = "Hello JavaScript!";    // 改变内容
}
```

[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_intro_inner_html)

您会经常看到` document.getElementById("some id")`。这个方法是 HTML DOM 中定义的。

DOM (**D**ocument **O**bject **M**odel)（文档对象模型）是用于访问 HTML 元素的正式 W3C 标准。

您将在本教程的多个章节中学到有关 HTML DOM 的知识。

## JavaScript：改变 HTML 图像

本例会动态地改变 HTML `<image>` 的来源（src）：

```html
<script>
function changeImage() {
    element=document.getElementById('myimage')
    if (element.src.match("bulbon")) {
        element.src="/images/pic_bulboff.gif";
    } else {
        element.src="/images/pic_bulbon.gif";
    }
}
</script>
<img id="myimage" onclick="changeImage()" src="/images/pic_bulboff.gif" width="100" height="180">
```

```html
以上实例中代码 element.src.match("bulbon") 的作用意思是：检索 <img id="myimage" onclick="changeImage()" src="/images/pic_bulboff.gif" width="100" height="180"> 里面 src 属性的值有没有包含 bulbon 这个字符串，如果存在字符串 bulbon，图片 src 更新为 bulboff.gif，若匹配不到 bulbon 字符串，src 则更新为 bulbon.gif
```

## JavaScript：改变 HTML 样式

改变 HTML 元素的样式，属于改变 HTML 属性的变种。

```javascript
x = document.getElementById("demo")  //找到元素 
x.style.color = "#ff0000";           //改变样式
```

[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_intro_style)

## JavaScript：验证输入

JavaScript 常用于验证用户的输入。

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
<script>
    function myFunction() {
        var x=document.getElementById("demo").value;
        if (x==""||isNaN(x)) {
            alert("不是数字")
        }
    }
</script>
</head>
<body>
<h1>我的第一个 JavaScript 程序</h1>
<p>请输入数字。如果输入值不是数字，浏览器会弹出提示框。</p>
<input id="demo" type="text">
<button type="button" onclick="myFunction()">提交</button>
</body>
</html>
```

[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_intro_validate)

以上实例只是普通的验证，如果要在生产环境中使用，需要严格判断，如果输入的空格，或者连续空格 isNaN 是判别不出来的。可以添加正则来判断（后续章节会说明）：

```javascript
if (isNaN(x)||x.replace(/(^\s*)|(\s*$)/g,"")=="") {
    alert("不是数字");
}
```

关于上面切换图片的例子，用三目运算比较简洁。

```javascript
function changeImage() {
    var s = document.getElementById("demo");
     s.src = s.src.match('bulboff')?"/images/pic_bulbon.gif":"/images/pic_bulboff.gif";
}
```

----

# JavaScript 用法

HTML 中的脚本必须位于 `<script> `与 `</script>` 标签之间。

脚本可被放置在 HTML 页面的 `<body>` 和` <head>` 部分中。

## \<script> 标签

如需在 HTML 页面中插入 JavaScript，请使用 `<script>` 标签。

`<script>` 和 `</script>` 会告诉 JavaScript 在何处开始和结束。

`<script>` 和 `</script>` 之间的代码行包含了 JavaScript:

```html
<script>
alert("我的第一个 JavaScript");
</script>
```

您无需理解上面的代码。只需明白，浏览器会解释并执行位于` <script>` 和 `</script>`之间的 JavaScript 代码 

## \<body> 中的 JavaScript

在本例中，JavaScript 会在页面加载时向 HTML 的 `<body>` 写文本：

```html
<!DOCTYPE html>
<html>
<body>
.
.
<script>
document.write("<h1>这是一个标题</h1>");
document.write("<p>这是一个段落</p>");
</script>
.
.
</body>
</html>
```

## JavaScript 函数和事件

上面例子中的 JavaScript 语句，会在页面加载时执行。

通常，我们需要在某个事件发生时执行代码，比如当用户点击按钮时。

如果我们把 JavaScript 代码放入函数中，就可以在事件发生时调用该函数。

您将在稍后的章节学到更多有关 JavaScript 函数和事件的知识。

## 在 \<head> 或者 \<body> 的JavaScript

您可以在 HTML 文档中放入不限数量的脚本。

脚本可位于 HTML 的 \<body> 或 \<head> 部分中，或者同时存在于两个部分中。

通常的做法是把函数放入 \<head> 部分中，或者放在页面底部。这样就可以把它们安置到同一处位置，不会干扰页面的内容。

## \<head> 中的 JavaScript 函数

在本例中，我们把一个 JavaScript 函数放置到 HTML 页面的 `<head>` 部分。

该函数会在点击按钮时被调用：

```javascript
<!DOCTYPE html>
<html>
<head>
<script>
function myFunction()
{
    document.getElementById("demo").innerHTML="我的第一个 JavaScript 函数";
}
</script>
</head>
<body>
<h1>我的 Web 页面</h1>
<p id="demo">一个段落</p>
<button type="button" onclick="myFunction()">尝试一下</button>
</body>
</html>
```

<script>
function myFunction()
{
    document.getElementById("demo").innerHTML="我的第一个 JavaScript 函数";
}
</script>
<h1>我的 Web 页面</h1>
<p id="demo">一个段落</p>
<button type="button" onclick="myFunction()">尝试一下</button>

## \<body> 中的 JavaScript 函数

在本例中，我们把一个 JavaScript 函数放置到 HTML 页面的 `<body>` 部分。

该函数会在点击按钮时被调用：

```html
<!DOCTYPE html>
<html>
<body>
<h1>我的 Web 页面</h1>
<p id="demo">一个段落</p>
<button type="button" onclick="myFunction()">尝试一下</button>
<script>
function myFunction()
{
    document.getElementById("demo").innerHTML="我的第一个 JavaScript 函数";
}
</script>
</body>
</html>
```

## 外部的 JavaScript

也可以把脚本保存到外部文件中。外部文件通常包含被多个网页使用的代码。

外部 JavaScript 文件的文件扩展名是 .js。

如需使用外部文件，请在 `<script>` 标签的 "src" 属性中设置该 .js 文件：

```html
<!DOCTYPE html>
<html>
<body>
<script src="myScript.js"></script>
</body>
</html>
```

你可以将脚本放置于` <head>` 或者 `<body>`中，放在 `<script>` 标签中的脚本与外部引用的脚本运行效果完全一致。

myScript.js 文件代码如下：

```javascript
function myFunction()
{
    document.getElementById("demo").innerHTML="我的第一个 JavaScript 函数";
}
```

---

# JavaScript 输出

JavaScript 没有任何打印或者输出的函数。

## JavaScript 显示数据

JavaScript 可以通过不同的方式来输出数据：

- 使用 **window.alert()** 弹出警告框。
- 使用 **document.write()** 方法将内容写到 HTML 文档中。
- 使用 **innerHTML** 写入到 HTML 元素。
- 使用 **console.log()** 写入到浏览器的控制台。

## 使用 window.alert()

你可以弹出警告框来显示数据：

```html
<!DOCTYPE html>
<html>
<body>
<h1>我的第一个页面</h1>
<p>我的第一个段落。</p>
<script>
window.alert(5 + 6);
</script>
</body>
</html>
```

## 操作 HTML 元素

如需从 JavaScript 访问某个 HTML 元素，您可以使用 document.getElementById(*id*) 方法。

请使用 "id" 属性来标识 HTML 元素，并 innerHTML 来获取或插入元素内容：

```html
<!DOCTYPE html>
<html>
<body>

<h1>我的第一个 Web 页面</h1>

<p id="demo">我的第一个段落</p>

<script>
document.getElementById("demo").innerHTML = "段落已修改。";
</script>

</body>
</html>
```

## 写到 HTML 文档

出于测试目的，您可以将JavaScript直接写在HTML 文档中：

```html
<!DOCTYPE html>
<html>
<body>

<h1>我的第一个 Web 页面</h1>

<p>我的第一个段落。</p>

<script>
document.write(Date());
</script>

</body>
</html>
```

<script>
document.write(Date());
</script>

如果在文档已完成加载后执行 document.write，整个 HTML 页面将被覆盖。

```html
<!DOCTYPE html>
<html>
<body>

<h1>我的第一个 Web 页面</h1>

<p>我的第一个段落。</p>

<button onclick="myFunction()">点我</button>

<script>
function myFunction() {
   	document.write(Date());
}
</script>

</body>
</html>
```

## 写到控制台

如果您的浏览器支持调试，你可以使用 **console.log()** 方法在浏览器中显示 JavaScript 值。

浏览器中使用 F12 来启用调试模式， 在调试窗口中点击 "Console" 菜单。

```html
<!DOCTYPE html>
<html>
<body>

<h1>我的第一个 Web 页面</h1>

<script>
a = 5;
b = 6;
c = a + b;
console.log(c);
</script>

</body>
</html>
```

---

**DOM 解释**

您会经常看到 **document.getElementById("id")**。

这个方法是 HTML DOM 中定义的。

DOM (Document Object Model)（文档对象模型）是用于访问 HTML 元素的正式 W3C 标准。

格式\<script>

那些老旧的实例可能会在 \<script> 标签中使用 type="text/javascript"。

现在已经不必这样做了。

JavaScript 是所有现代浏览器以及 HTML5 中的默认脚本语言。

**脚本位置**

在 \<head> 或者 \<body> 的JavaScript

外部脚本不能包含 \<script> 标签。

**输出数据**

- window.alert() 弹出警告框。

- document.write() 方法将内容写到 HTML 文档中。

- innerHTML 写入到 HTML 元素。

- console.log() 写入到浏览器的控制台。

**输出内容**

使用 document.write() 向文档输出写内容。

如果在文档已完成加载后执行 document.write，整个 HTML 页面将被覆盖

**写到控制台(调试模式)**

使用 console.log() 方法在浏览器中显示 JavaScript 值。

F12 启用调试模式， 在调试窗口中点击 "Console" 菜单。

---

**window.alert 的补充:**

**window.alert(5+6)** 与 **window.alert("5+6")** 输出的值是不一样的。window.alert(5+6) 会输出 11，而window.alert("5+6") 会输出 5+6。这是因为当用引号时会认为引号中是字符串，从而直接将引号中的内容打印出来。

---

# JavaScript 语法

JavaScript 是一个程序语言。语法规则定义了语言结构。

## JavaScript 语法

JavaScript 是一个脚本语言。

它是一个轻量级，但功能强大的编程语言。

## JavaScript 字面量

在编程语言中，一般固定值称为字面量，如 3.14。

**数字（Number）字面量** 可以是整数或者是小数，或者是科学计数(`e`)。

```javascript
3.14
1001
123e5
```

**字符串（String）字面量** 可以使用单引号或双引号:

```javascript
"John Doe"
'John Doe'
```

**表达式字面量** 用于计算：

```javascript
5 + 6
5 * 10
```

**数组（Array）字面量** 定义一个数组：

```javascript
[40, 100, 1, 5, 25, 10]
```

**对象（Object）字面量** 定义一个对象：

```javascript
{firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"}
```

**函数（Function）字面量** 定义一个函数：

```javascript
function myFunction(a, b) { return a * b;}
```

## JavaScript 变量

在编程语言中，变量用于存储数据值。

JavaScript 使用关键字 **var** 来定义变量， 使用等号来为变量赋值：

```javascript
var length;
length = 6;
document.getElementById("demo").innerHTML = length;
```

## JavaScript 操作符

JavaScript使用 **算术运算符** 来计算值:

```javascript
(5 + 6) * 10
```

JavaScript使用**赋值运算符**给变量赋值：

```javascript
x = 5
y = 6
z = (x + y) * 10
```

avaScript语言有多种类型的运算符：

| 类型                   | 实例      | 描述                   |
| :--------------------- | :-------- | :--------------------- |
| 赋值，算术和位运算符   | = + - * / | 在 JS 运算符中描述     |
| 条件，比较及逻辑运算符 | == != < > | 在 JS 比较运算符中描述 |

## JavaScript 语句

在 HTML 中，JavaScript 语句向浏览器发出的命令。

语句是用分号分隔：

```javascript
x = 5 + 6;
y = x * 10;
```

## JavaScript 关键字

JavaScript 关键字用于标识要执行的操作。

和其他任何编程语言一样，JavaScript 保留了一些关键字为自己所用。

**var** 关键字告诉浏览器创建一个新的变量：

```javascript
var x = 5 + 6;
var y = x * 10;
```

JavaScript 同样保留了一些关键字，这些关键字在当前的语言版本中并没有使用，但在以后 JavaScript 扩展中会用到。

以下是 JavaScript 中最重要的保留字（按字母顺序）：

<table class="reference">
<tbody><tr>
<td>abstract</td>
<td>else</td>
<td>instanceof</td>
<td>super</td>
</tr><tr>
</tr><tr>
<td>boolean</td>
<td>enum</td>
<td>int</td>
<td>switch</td>
</tr><tr>
</tr><tr>
<td>break</td>
<td>export</td>
<td>interface</td>
<td>synchronized</td>
</tr><tr>
</tr><tr>
<td>byte</td>
<td>extends</td>
<td>let</td>
<td>this</td>
</tr><tr>
</tr><tr>
<td>case</td>
<td>false</td>
<td>long</td>
<td>throw</td>
</tr><tr>
</tr><tr>
<td>catch</td>
<td>final</td>
<td>native</td>
<td>throws</td>
</tr><tr>
</tr><tr>
<td>char</td>
<td>finally</td>
<td>new</td>
<td>transient</td>
</tr><tr>
</tr><tr>
<td>class</td>
<td>float</td>
<td>null</td>
<td>true</td>
</tr><tr>
</tr><tr>
<td>const</td>
<td>for</td>
<td>package</td>
<td>try</td>
</tr><tr>
</tr><tr>
<td>continue</td>
<td>function</td>
<td>private</td>
<td>typeof</td>
</tr><tr>
</tr><tr>
<td>debugger</td>
<td>goto</td>
<td>protected</td>
<td>var</td>
</tr><tr>
</tr><tr>
<td>default</td>
<td>if</td>
<td>public</td>
<td>void</td>
</tr><tr>
</tr><tr>
<td>delete</td>
<td>implements</td>
<td>return</td>
<td>volatile</td>
</tr><tr>
</tr><tr>
<td>do</td>
<td>import</td>
<td>short</td>
<td>while</td>
</tr><tr>
</tr><tr>
<td>double</td>
<td>in</td>
<td>static</td>
<td>with</td>
</tr><tr>
</tr></tbody></table>

## JavaScript 注释

不是所有的 JavaScript 语句都是"命令"。双斜杠 **//** 后的内容将会被浏览器忽略：

```javascript
// 我不会执行
```

## JavaScript 数据类型

JavaScript 有多种数据类型：数字，字符串，数组，对象等等：

```javascript
var length = 16;                                  // Number 通过数字字面量赋值 
var points = x * 10;                              // Number 通过表达式字面量赋值
var lastName = "Johnson";                         // String 通过字符串字面量赋值
var cars = ["Saab", "Volvo", "BMW"];              // Array  通过数组字面量赋值
var person = {firstName:"John", lastName:"Doe"};  // Object 通过对象字面量赋值
```

## 数据类型的概念

编程语言中，数据类型是一个非常重要的内容。

为了可以操作变量，了解数据类型的概念非常重要。

如果没有使用数据类型，以下实例将无法执行：

```javascript
16 + "Volvo"
```

16 加上 "Volvo" 是如何计算呢? 以上会产生一个错误还是输出以下结果呢？

```javascript
"16Volvo"
```

## JavaScript 函数

JavaScript 语句可以写在函数内，函数可以重复引用：

**引用一个函数** = 调用函数(执行函数内的语句)。

```javascript
// 返回 a 乘以 b 的结果
function myFunction(a, b) {
   	return a * b;                               
}
```

## JavaScript 字母大小写

JavaScript 对大小写是敏感的。

当编写 JavaScript 语句时，请留意是否关闭大小写切换键。

函数 **getElementById** 与 **getElementbyID** 是不同的。

同样，变量 **myVariable** 与 **MyVariable** 也是不同的。

## JavaScript 字符集

JavaScript 使用 Unicode 字符集。

Unicode 覆盖了所有的字符，包含标点等字符。

----

JavaScript是弱类型编程语言,定义变量都使用 `var` 定义,与 Java 这种强类型语言有区别.

在定义后可以通过 **typeOf()** 来获取JavaScript中变量的数据类型.

```javascript
// Number 通过数字字面量赋值 
// Number 通过表达式字面量赋值
// String 通过字符串字面量赋值
// Array  通过数组字面量赋值 
// Object 通过对象字面量赋值
```

有个情况需要特别注意: **typeof 不能用来判断是 Array 还是Object**

```javascript
var arr = [] typeof(arr) === 'object' // true
```

结果为 **true**。

当然你可以使用其他方式来判断：

**1、使用 isArray 方法**

```javascript
var cars=new Array();
cars[0]="Saab";
cars[1]="Volvo";
cars[2]="BMW";
// 判断是否支持该方法
if (Array.isArray) {
    if(Array.isArray(cars)) {
        document.write("该对象是一个数组。") ;
    }
}
```

**2、使用 instanceof 操作符**

```javascript
var cars=new Array();
cars[0]="Saab";
cars[1]="Volvo";
cars[2]="BMW";

if (cars instanceof Array) {
    document.write("该对象是一个数组。") ;
}
```

---

# JavaScript 语句

JavaScript 语句向浏览器发出的命令。语句的作用是告诉浏览器该做什么。

## JavaScript 语句

JavaScript 语句是发给浏览器的命令。

这些命令的作用是告诉浏览器要做的事情。

下面的 JavaScript 语句向 id="demo" 的 HTML 元素输出文本 "你好 Dolly" ：

```javascript
document.getElementById("demo").innerHTML = "你好 Dolly";
```

## 分号 ;

分号用于分隔 JavaScript 语句。

通常我们在每条可执行的语句结尾添加分号。

使用分号的另一用处是在一行中编写多条语句。

```javascript
a = 5;
b = 6;
c = a + b;
```

以上实例也可以这么写:

```javascript
a = 5; b = 6; c = a + b;
```

## JavaScript 代码

JavaScript 代码是 JavaScript 语句的序列。

浏览器按照编写顺序依次执行每条语句。

本例向网页输出一个标题和两个段落：

```javascript
document.getElementById("demo").innerHTML="你好 Dolly";
document.getElementById("myDIV").innerHTML="你最近怎么样?";
```

## JavaScript 代码块

JavaScript 可以分批地组合起来。

代码块以左花括号开始，以右花括号结束。

代码块的作用是一并地执行语句序列。

本例向网页输出一个标题和两个段落：

```javascript
function myFunction() {
    document.getElementById("demo").innerHTML="你好Dolly";
    document.getElementById("myDIV").innerHTML="你最近怎么样?";
}
```

## JavaScript 语句标识符

JavaScript 语句通常以一个 **语句标识符** 为开始，并执行该语句。

语句标识符是保留关键字不能作为变量名使用。

下表列出了 JavaScript 语句标识符 (关键字) ：

| 语句         | 描述                                                         |
| :----------- | :----------------------------------------------------------- |
| break        | 用于跳出循环。                                               |
| catch        | 语句块，在 try 语句块执行出错时执行 catch 语句块。           |
| continue     | 跳过循环中的一个迭代。                                       |
| do ... while | 执行一个语句块，在条件语句为 true 时继续执行该语句块。       |
| for          | 在条件语句为 true 时，可以将代码块执行指定的次数。           |
| for ... in   | 用于遍历数组或者对象的属性（对数组或者对象的属性进行循环操作）。 |
| function     | 定义一个函数                                                 |
| if ... else  | 用于基于不同的条件来执行不同的动作。                         |
| return       | 退出函数                                                     |
| switch       | 用于基于不同的条件来执行不同的动作。                         |
| throw        | 抛出（生成）错误 。                                          |
| try          | 实现错误处理，与 catch 一同使用。                            |
| var          | 声明一个变量。                                               |
| while        | 当条件语句为 true 时，执行语句块。                           |

## 空格

JavaScript 会忽略多余的空格。您可以向脚本添加空格，来提高其可读性。下面的两行代码是等效的：

```javascript
var person="Hege";
var person = "Hege";
```

## 对代码行进行折行

您可以在文本字符串中使用反斜杠对代码行进行换行。下面的例子会正确地显示：

```javascript
document.write("你好 \
世界!");
```

---

# JavaScript 注释

JavaScript 注释可用于提高代码的可读性。

## JavaScript 注释

JavaScript 不会执行注释。

我们可以添加注释来对 JavaScript 进行解释，或者提高代码的可读性。

单行注释以 `//` 开头。

本例用单行注释来解释代码：

```javascript
// 输出标题：
document.getElementById("myH1").innerHTML="欢迎来到我的主页";
// 输出段落：
document.getElementById("myP").innerHTML="这是我的第一个段落。";
```

## JavaScript 多行注释

多行注释以 `/*` 开始，以 `*/` 结尾。

下面的例子使用多行注释来解释代码：

```javascript
/*
下面的这些代码会输出
一个标题和一个段落
并将代表主页的开始
*/
document.getElementById("myH1").innerHTML="欢迎来到我的主页";
document.getElementById("myP").innerHTML="这是我的第一个段落。";
```

## 使用注释来阻止执行

在下面的例子中，注释用于阻止其中一条代码行的执行（可用于调试）：

```javascript
// document.getElementById("myH1").innerHTML="欢迎来到我的主页";
document.getElementById("myP").innerHTML="这是我的第一个段落。";
```

在下面的例子中，注释用于阻止代码块的执行（可用于调试）：

```java
/*
document.getElementById("myH1").innerHTML="欢迎来到我的主页";
document.getElementById("myP").innerHTML="这是我的第一个段落。";
*/
```

## 在行末使用注释

在下面的例子中，我们把注释放到代码行的结尾处：

```javascript
var x=5;    // 声明 x 并把 5 赋值给它
var y=x+2;  // 声明 y 并把 x+2 赋值给它
```

----

# JavaScript 变量

变量是用于存储信息的"容器"。

```javascript
var x=5;
var y=6;
var z=x+y;
```

## JavaScript 变量

与代数一样，JavaScript 变量可用于存放值（比如 x=5）和表达式（比如 z=x+y）。

变量可以使用短名称（比如 x 和 y），也可以使用描述性更好的名称（比如 age, sum, totalvolume）。

- 变量必须以字母开头
- 变量也能以 $ 和 _ 符号开头（不过我们不推荐这么做）
- 变量名称对大小写敏感（y 和 Y 是不同的变量）

## JavaScript 数据类型

JavaScript 变量还能保存其他数据类型，比如文本值 (`name="Bill Gates"`)。

在 JavaScript 中，类似 "Bill Gates" 这样一条文本被称为字符串。

JavaScript 变量有很多种类型，但是现在，我们只关注数字和字符串。

当您向变量分配文本值时，应该用双引号或单引号包围这个值。

当您向变量赋的值是数值时，不要使用引号。如果您用引号包围数值，该值会被作为文本来处理。

```javascript
var pi=3.14;
var person="John Doe";
var answer='Yes I am!';
```

## 声明（创建） JavaScript 变量

在 JavaScript 中创建变量通常称为"声明"变量。

我们使用 `var `关键词来声明变量：

```javascript
var carname;
```

量声明之后，该变量是空的（它没有值）。

如需向变量赋值，请使用等号：

```javascript
carname = "Volvo";
```

不过，您也可以在声明变量时对其赋值：

```javascript
var carname = "Volvo";
```

在下面的例子中，我们创建了名为 carname 的变量，并向其赋值 "Volvo"，然后把它放入 id="demo" 的 HTML 段落中：

```javascript
var carname="Volvo";
document.getElementById("demo").innerHTML=carname;
```

## 一条语句，多个变量

您可以在一条语句中声明很多变量。该语句以 var 开头，并使用逗号分隔变量即可：

```javascript
var lastname="Doe", age=30, job="carpenter";
```

声明也可横跨多行：

```javascript
var lastname="Doe",
age=30,
job="carpenter";
```

一条语句中声明的多个不可以赋同一个值:

```javascript
var x,y,z=1;
```

x,y 为 `undefined`， z 为 1。

## Value = undefined

在计算机程序中，经常会声明无值的变量。未使用值来声明的变量，其值实际上是 undefined。

在执行过以下语句后，变量 *carname* 的值将是 `undefined`：

```javascript
var carname;
```

## 重新声明 JavaScript 变量

如果重新声明 JavaScript 变量，该变量的值不会丢失：

在以下两条语句执行后，变量 carname 的值依然是 "Volvo"：

```javascript
var carname="Volvo"; 
var carname;
```

## JavaScript 算数

您可以通过 JavaScript 变量来做算数，使用的是 = 和 + 这类运算符：

```javascript
y = 5;
x = y+2;
```

---

**介绍JS中的let变量:**

```javascript
let var1 [= value1] [, var2 [= value2]] [, ..., varN [= valueN]];
```

`let`允许你声明一个作用域被限制在块级中的变量、语句或者表达式。在Function中局部变量推荐使用`let`变量，避免变量名冲突。

**作用域规则**

`let `声明的变量只在其声明的块或子块中可用，这一点，与`var`相似。二者之间最主要的区别在于`var`声明的变量的作用域是整个封闭函数。

```javascript
function varTest() {
    var x = 1;
    if (true) {
        var x = 2;       // 同样的变量!
        console.log(x);  // 2
    }
    console.log(x);  // 2
}

function letTest() {
    let x = 1;
    if (true) {
        let x = 2;       // 不同的变量    
        console.log(x);  // 2  
    }
    console.log(x);  // 1
}
```

---

avascript声明变量的时候，虽然用var关键字声明和不用关键字声明，很多时候运行并没有问题，但是这两种方式还是有区别的。可以正常运行的代码并不代表是合适的代码。

```javascript
// num1为全局变量，num2为window的一个属性
var num1 = 1;
num2 = 2;
// delete num1;  无法删除
// delete num2;  删除
function model() {
    var num1 = 1; // 本地变量
    num2 = 2;     // window的属性
        // 匿名函数
        (function(){
            var num = 1; // 本地变量
            num1 = 2; // 继承作用域（闭包）
            num3 = 3; // window的属性
        }())
}
```

---

`const `关键字用来声明 JavaScript中的常量（与变量相对，不可修改，但同样是用于存储信息的"容器"。），常量的值不能通过重新赋值来改变，并且不能重新声明。

代码：

```javascript
//定义常量a并赋值为0
const a = 0;

//报错（不能重新赋值）
a = 1;

//报错（不能重新声明）
const a = 2;

//输出0
console.log("a is: " + a);
```

---

**JavaScript 允许重复声明变量，后声明的覆盖之前的**

```javascript
var a = 1;
var a = 'x';
console.log(a);
// 输出 'x'
```

**JavaScript 允许重复定义函数**

JavaScript 没有重载这个概念，它仅依据函数名来区分函数。**后定义的同名函数覆盖之前的，与参数无关。**

```javascript
function test() {
    console.log("test");
}
test();     //输出 "test arg0 + undefined"

function test(arg1) {
    console.log("test arg" + arguments.length + " + " + arg1);
}
test(1,2);  //输出 "test arg2 + 1"
```

实参个数如果比形参少，那么剩下的默认赋值为 **undefined**，如果实参传的比形参数量多，那么是全部都会被传进去的，只不过没有对应的形参可以引用（但可以用 arguments 来获取剩下的参数）。

```javascript
function test(arg1) {
    for(var i=0; i<arguments.length; i++) {
        console.log(arguments[i]);
    }
}
test(1,2); //输出 1 2
```

**变量与函数重名的时候，变量生效**

这涉及到了变量和函数的预解析：

- 变量声明会被顶置，函数声明也会被顶置且比变量更先声明。
- 变量的声明和赋值语句一起写时，JS引擎在解析时，会将其拆成声明和赋值2部分，声明置顶，赋值保留在原来位置。
- 声明过的变量不会再重复声明。

```javascript
var a = 100;
function a() {
    return "function";
}
console.log(a);     //输出 100
console.log(a());   
/*
报错
Uncaught TypeError: a is not a function
    (anonymous function) @test.html:9
*/
```

JS 中有两种函数，一种是普通函数，一种是函数对象。下面的这种就是“函数对象”，它实际上是声明一个匿名函数，然后将该函数的 init 方法赋值给该变量。

```javascript
var a = 100;
var a = function() {
    return "function";
}
console.log(a);
/* 
输出
function() {
    return "function";
}
*/

console.log(a());   //输出 "function"
```

**函数与内部变量重名**

定义普通函数，即在 window 变量下，定义一个 key，它的名字为该函数名，值为该函数的地址。函数内部的 this 指向 window 对象。

```javascript
function a() {
    console.log(this);  //输出 window{...}
    this.a = 1;         //即 window.a = 1，此时window下的function a已经被该变量覆盖了。
    var a = 5;          //下面的这几个变量都是局部变量，仅在花括号范围内有效。  
    a = 10;
    var v = "value"
    return "function";
}
console.log(a);         //输出 function a {...}
console.log(a());       //输出 "function"
console.log(a);         //输出 1
console.log(v);
/*
输出
Uncaught ReferenceError: v is not defined
    (anonymous function) @ mycolor.html:15
*/
```

---

# JavaScript 数据类型

**值类型(基本类型)**：字符串（String）、数字(Number)、布尔(Boolean)、对空（Null）、未定义（Undefined）、Symbol。

**引用数据类型**：对象(Object)、数组(Array)、函数(Function)。

>**注：***Symbol 是 ES6 引入了一种新的原始数据类型，表示独一无二的值。*

## JavaScript 拥有动态类型

JavaScript 拥有动态类型。这意味着相同的变量可用作不同的类型：

```javascript
var x;               // x 为 undefined
var x = 5;           // 现在 x 为数字
var x = "John";      // 现在 x 为字符串
```

## JavaScript 字符串

字符串是存储字符（比如 "Bill Gates"）的变量。

字符串可以是引号中的任意文本。您可以使用单引号或双引号：

```javascript
var carname="Volvo XC60";
var carname='Volvo XC60';
```

您可以在字符串中使用引号，只要不匹配包围字符串的引号即可：

```javascript
var answer="It's alright";
var answer="He is called 'Johnny'";
var answer='He is called "Johnny"';
```

## JavaScript 数字

JavaScript 只有一种数字类型。数字可以带小数点，也可以不带：

```javascript
var x1=34.00;      //使用小数点来写
var x2=34;         //不使用小数点来写
```

大或极小的数字可以通过科学（指数）计数法来书写：

```javascript
var y=123e5;      // 12300000
var z=123e-5;     // 0.00123
```

## JavaScript 布尔

布尔（逻辑）只能有两个值：true 或 false。

```javascript
var x=true;
var y=false;
```

```javascript
var cars=new Array();
cars[0]="Saab";
cars[1]="Volvo";
cars[2]="BMW";
```

或者 (condensed array):

```javascript
var cars=new Array("Saab","Volvo","BMW");
```

```javascript
var cars=["Saab","Volvo","BMW"];
```

## JavaScript 对象

对象由花括号分隔。在括号内部，对象的属性以名称和值对的形式 (name : value) 来定义。属性由逗号分隔：

```javascript
var person={firstname:"John", lastname:"Doe", id:5566};
```

上面例子中的对象 (person) 有三个属性：firstname、lastname 以及 id。

空格和折行无关紧要。声明可横跨多行：

```javascript
var person={
firstname : "John",
lastname  : "Doe",
id        :  5566
};
```

对象属性有两种寻址方式：

```javascript
name=person.lastname;
name=person["lastname"];
```

## Undefined 和 Null

Undefined 这个值表示变量不含有值。

可以通过将变量的值设置为 null 来清空变量。

```javascript
cars=null;
person=null;
```

## 声明变量类型

当您声明新变量时，可以使用关键词 "`new`" 来声明其类型：

```javascript
var carname = new String;
var x = new Number;
var y = new Boolean;
var cars = new Array;
var person = new Object;
```

---

数组有四种方式：

```javascript
var arr1 = new Array('a', 'b', 'c');    //这是一个预定义的数组，在创建时初始化
var arr2 = ['a', 'b', 'c' ];       //同样是在创建时初始化，但是这种创建更为简洁直观
var arr3 = new Array( );   var arr4 = [ ];     //这两种是创建空的数组
```

在数组操作中，最值得注意的是下标的使用，容易出错

对象的创建，一般推荐使用

```javascript
var people = {name : 'Tom', age : 21 , eat : function(){  }    }
```

也可先创建对象再追加属性和方法

```javascript
var people = new Object();
people.name = 'Tom';   
people.age = 21;  
people.eat = function(){  }
```

---

**最常用的对象创建方式:**

第一种：

```javascript
function Demo(){
    var obj=new Object();
    obj.name="张思";
    obj.age=12;
    obj.firstF=function(){
    }
    obj.secondF=function(){
    }
    return obj;
}

var one=Demo();
// 调用输出
document.write(one.age);
```

第二种：

```javascript
function Demo(){
    this.name="张思";
    this.age=12;
    this.firstF=function(){
    }
    this.secondF=function(){
    }
}

var one=new Demo

// 调用输出
document.write(one.age);
```

---

就算变量定义的是数组格式，**typeof** 返回的数据类型还是 **object** :

```javascript
var cars=new Array();
cars[0]="Saab";
cars[1]="Volvo";
cars[2]="BMW";
document.write(typeof cars); // object
```

如果你要判断该对象是否为数组，可以使用以下两种方法:

**1、使用 isArray 方法**

```javascript
var cars=new Array();
cars[0]="Saab";
cars[1]="Volvo";
cars[2]="BMW";
// 判断是否支持该方法
if (Array.isArray) {
    if(Array.isArray(cars)) {
        document.write("该对象是一个数组。") ;
    }
}
```

**2、使用 instanceof 操作符**

```javascript
var cars=new Array();
cars[0]="Saab";
cars[1]="Volvo";
cars[2]="BMW";

if (cars instanceof Array) {
    document.write("该对象是一个数组。") ;
}
```

---

注意 `undefined `和 `null `都是小写，并且。

```javascript
var x, y;
if(x == null){
    document.write(x);
}
if(y == undefined){
    document.write(y);
}
```

二者都会输出 **undefined**

---

利用 `toString()` 方法可以把数值转换为字符串。

```javascript
var a = 100;
var c = a.toString();
alert(typeof(c));      //typeof()方法验证转换后的数据类型
```

使用 `parseInt()` 和 `parseFloat()` 方法可以把字符串转换为数值。

```javascript
var str = "123.30";
var a = parseInt(str);    //parseInt()方法把字符串转换为整数，parseFloat()方法把字符串转换为浮点数
var b = parseFloat(str);
```

要把任何值转换为布尔型数据，在值的前面增加两个 **!!** 感叹号即可，**!!0** 为 **False**，其余的均为 **True**。

---

# JavaScript 对象

JavaScript 对象是拥有属性和方法的数据。

## JavaScript 对象

在 JavaScript中，几乎所有的事物都是对象。

以下代码为变量 **car** 设置值为 "Fiat" :

```javascript
var car = "Fiat";
```

对象也是一个变量，但对象可以包含多个值（多个变量）。

```javascript
var car = {type:"Fiat", model:500, color:"white"};
```

在以上实例中，3 个值 ("Fiat", 500, "white") 赋予变量 car。

在以上实例中，3 个变量 (type, model, color) 赋予变量 car。

## 对象定义

你可以使用字符来定义和创建 JavaScript 对象:

```javascript
var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
```

## 对象属性

可以说 "JavaScript 对象是变量的容器"。

但是，我们通常认为 "JavaScript 对象是键值对的容器"。

键值对通常写法为 **name : value** (键与值以冒号分割)。

键值对在 JavaScript 对象通常称为 **对象属性**。

对象键值对的写法类似于：

- PHP 中的关联数组
- Python 中的字典
- C 语言中的哈希表
- Java 中的哈希映射
- Ruby 和 Perl 中的哈希表

## 访问对象属性

你可以通过两种方式访问对象属性:

```javascript
person.lastName;
```

```javascript
person["lastName"];
```

## 对象方法

对象的方法定义了一个函数，并作为对象的属性存储。

对象方法通过添加 `()` 调用 (作为一个函数)。

该实例访问了 person 对象的 fullName() 方法:

```javascript
name = person.fullName();
```

如果你要访问 person 对象的 fullName 属性，它将作为一个定义函数的字符串返回：

```javascript
name = person.fullName;
```

## 访问对象方法

你可以使用以下语法创建对象方法：

```javascript
methodName : function() { code lines }
```

你可以使用以下语法访问对象方法：

```javascript
objectName.methodName()
```

通常 fullName() 是作为 person 对象的一个方法， fullName 是作为一个属性。

有多种方式可以创建，使用和修改 JavaScript 对象。

同样也有多种方式用来创建，使用和修改属性和方法。

---

JavaScript对象:属性和方法的容器;

对象的属性之间一定要用逗号隔开;

对象的方法定义了一个函数，并作为对象的属性存储。

对象方法通过添加 **()** 调用 (作为一个函数)。

比如:

```javascript
var person = {
    "name": "小明",
    "age": "18",
    "like": function () {
        return "喜欢打篮球,弹吉他";
    }
}
```

---

javaScript对象也可以先创建，再添加属性和属性值，比如：

```javascript
var person = new Object();
person.name = "小明";
person.sex = "男";
person.method = function () {
    return this.name + this.sex;
}
```

---

JavaScript对象中属性具有唯一性（这里的属性包括方法），如果有两个重复的属性，则以最后赋值为准。比如同时存在两个play:

```javascript
var person = {
    name: "小明",
    age: 18,
    sex: "男",
    play: "football",
    play: function () {
        return "like paly football";
    }
};
```

----

JavaScript 对象是键值对的容器，“键”必须为字符串，“值”可以是 JavaScript 中除 null 和 undefined 以外的任意数据类型。

代码实例：

```javascript
var bird = {
    "name" : "Amy",
    "age" : 1,
    "color" : "white",
    "skill" : function () {
        console.log("Fly");
    },
    "nickname" : null //非法
}
```

---

使用 **var name = person.fullName();** 调用对象函数时，fullName 会被立即执行：

```javascript
var person = {
    firstName: "John",
    lastName : "Doe",
    id : 5566,
    fullName : function() 
    {
      console.log("person.fullName");
    }
};

var name = person.fullName();
console.log(name);
```

控制台会先打印 **person.fullName** ，再打印 **name**。

---

# JavaScript 函数

函数是由事件驱动的或者当它被调用时执行的可重复使用的代码块。

## JavaScript 函数语法

函数就是包裹在花括号中的代码块，前面使用了关键词 function：

```javascript
function functionname()
{
  // 执行代码
}
```

当调用该函数时，会执行函数内的代码。

可以在某事件发生时直接调用函数（比如当用户点击按钮时），并且可由 JavaScript 在任何位置进行调用。

## 调用带参数的函数

在调用函数时，您可以向其传递值，这些值被称为参数。

这些参数可以在函数中使用。

您可以发送任意多的参数，由逗号 (,) 分隔：

```javascript
myFunction(argument1, argument2)
```

当您声明函数时，请把参数作为变量来声明：

```javascript
function myFunction(var1,var2) {
	// 代码
}
```

变量和参数必须以一致的顺序出现。第一个变量就是第一个被传递的参数的给定的值，以此类推。

```html
<p>点击这个按钮，来调用带参数的函数。</p>
<button onclick="myFunction('Harry Potter','Wizard')">点击这里</button>
<script>
function myFunction(name,job){
    alert("Welcome " + name + ", the " + job);
}
</script>
```

上面的函数在按钮被点击时会提示 "Welcome Harry Potter, the Wizard"。

函数很灵活，您可以使用不同的参数来调用该函数，这样就会给出不同的消息：

```html
<button onclick="myFunction('Harry Potter','Wizard')">点击这里</button>
<button onclick="myFunction('Bob','Builder')">点击这里</button>
```

根据您点击的不同的按钮，上面的例子会提示 "Welcome Harry Potter, the Wizard" 或 "Welcome Bob, the Builder"。

## 带有返回值的函数

有时，我们会希望函数将值返回调用它的地方。

通过使用 return 语句就可以实现。

在使用 return 语句时，函数会停止执行，并返回指定的值。

```javascript
function myFunction()
{
  var x=5;
  return x;
}
```

上面的函数会返回值 5。

**注意：** 整个 JavaScript 并不会停止执行，仅仅是函数。JavaScript 将继续执行代码，从调用函数的地方。

函数调用将被返回值取代：

```javascript
var myVar = myFunction();
```

`myVar `变量的值是 5，也就是函数 "myFunction()" 所返回的值。

即使不把它保存为变量，您也可以使用返回值：

```javascript
document.getElementById("demo").innerHTML=myFunction();
```

"demo" 元素的 innerHTML 将成为 5，也就是函数 "myFunction()" 所返回的值。

您可以使返回值基于传递到函数中的参数：

```javascript
function myFunction(a,b) {
    return a*b;
}
document.getElementById("demo").innerHTML=myFunction(4,3);
```

"demo" 元素的 innerHTML 将是：

```
12
```

在您仅仅希望退出函数时 ，也可使用 `return `语句。返回值是可选的：

```javascript
function myFunction(a,b) {
    if (a>b) {
        return;
    }
    x = a + b;
}
```

如果 a 大于 b，则上面的代码将退出函数，并不会计算 a 和 b 的总和。

## 局部 JavaScript 变量

在 JavaScript 函数内部声明的变量（使用 var）是*局部*变量，所以只能在函数内部访问它。（该变量的作用域是局部的）。

您可以在不同的函数中使用名称相同的局部变量，因为只有声明过该变量的函数才能识别出该变量。

只要函数运行完毕，本地变量就会被删除。

## 全局 JavaScript 变量

在函数外声明的变量是*全局*变量，网页上的所有脚本和函数都能访问它。

## JavaScript 变量的生存期

JavaScript 变量的生命期从它们被声明的时间开始。

局部变量会在函数运行以后被删除。

全局变量会在页面关闭后被删除。

## 向未声明的 JavaScript 变量分配值

如果您把值赋给尚未声明的变量，该变量将被自动作为 window 的一个属性。

这条语句：

```javascript
carname = "Volvo";
```

将声明 window 的一个属性 carname。

非严格模式下给未声明变量赋值创建的全局变量，是全局对象的可配置属性，可以删除。

```javascript
var var1 = 1; // 不可配置全局属性
var2 = 2; // 没有使用 var 声明，可配置全局属性

console.log(this.var1); // 1
console.log(window.var1); // 1

delete var1; // false 无法删除
console.log(var1); //1

delete var2; 
console.log(delete var2); // true
console.log(var2); // 已经删除 报错变量未定义
```

---

在使用 `return `语句时，函数会停止执行，并返回指定的值。例如：

```javascript
function sayHi(name,message) {
    document.write("return 语句执行前。");
    return;
    alert("hello" + name + "," + message);//这一行永远不会被调用
}

sayHi();
```

----

使用 HTML 、JavaScript 创建一个简单的计算器，包含加、减、乘、除四个功能：

```javascript
var result;

// 加法
function add() {
    var a = getFirstNumber();
    var b = getSecondNumber();
    var result = Number(a) + Number(b);
    sendResult(result);
}
// 减法
function subract() {
    var a = getFirstNumber();
    var b = getSecondNumber();
    var result = Number(a) - Number(b);
    sendResult(result);
}
// 乘法
function multiply() {
    var a = getFirstNumber();
    var b = getSecondNumber();
    var result = Number(a) * Number(b);
    sendResult(result);
}
// 除法
function devide() {
    var a = getFirstNumber();
    var b = getSecondNumber();
    var result = Number(a) / Number(b);
    sendResult(result);
}
// 给p标签传值
function sendResult(result) {
    var num = document.getElementById("result");
    num.innerHTML = result;
}
// 获取第一位数字
function getFirstNumber() {
    return document.getElementById("first").value;
}
// 获取第二位数字
function getSecondNumber() {
    return document.getElementById("second").value;
}
```

```html
<p>简单计算器:</p>
<table style="border: 1px solid black; position: center">
    <tr>
        <td>第一个数：</td>
        <td><input type="text" id="first"></td>
    </tr>
    <tr>
        <td>第二个数：</td>
        <td><input type="text" id="second"></td>
    </tr>
    <tr>
        <td colspan="2">
            &nbsp;<button style="width: inherit" onclick="add()">+</button>
            &nbsp;<button style="width: inherit" onclick="subract()">-</button>
            &nbsp;<button style="width: inherit" onclick="multiply()">*</button>
            &nbsp;<button style="width: inherit" onclick="devide()">/</button>
        </td>
    </tr>
    <tr>
        <td colspan="2" rowspan="2"><p id="result"></p></td>
    </tr>
</table>
```

[尝试一下 »](https://c.runoob.com/codedemo/2815)

JavaScript 多选框多选与取消多选实例：

```javascript
function checkboxed(objName) {
    var objNameList = document.getElementsByName(objName);
    if (objNameList!=null) {
        alert("全选操作");
        for (var i=0; i<objNameList.length; i++) {
            objNameList[i].checked = "checked";
        }
    }
}
function uncheckboxed(objName) {
    var objNameList = document.getElementsByName(objName);
    if (objNameList!=null) {
        alert("取消全选操作");
        for (var i=0; i<objNameList.length; i++) {
            objNameList[i].checked = "";
        }
    }
}
```

```html
看书：<input type="checkbox" name="checkbox" value="1"><br/>
写字：<input type="checkbox" name="checkbox" value="2"><br/>
打飞机：<input type="checkbox" name="checkbox" value="3"><br/>
玩游戏：<input type="checkbox" name="checkbox" value="4"><br/>
<button onclick="checkboxed('checkbox')">全选</button>
<button onclick="uncheckboxed('checkbox')">取消全选</button>
```

---

对于上述同学的笔记里JavaScript 多选框多选与取消多选实例，这次用按钮来统一实现:

```javascript
var checkAll = false;
function allcheck() {
    checkAll = !checkAll;
    var inputs = document.getElementsByName("checkbox");
    for (var i=0; i< inputs.length; i++) {
        inputs[i].checked = checkAll;
    }
}
```

```html
看书：<input type="checkbox" name="checkbox" value="1"><br/>
写字：<input type="checkbox" name="checkbox" value="2"><br/>
打飞机：<input type="checkbox" name="checkbox" value="3"><br/>
玩游戏：<input type="checkbox" name="checkbox" value="4"><br/>
<button onclick="allcheck()">全选/取消</button>
```

---

作为参数的的变量称为**形参**,带入的参数称为**实参**。

```javascript
function myFunction(a,b){ return a*b;}  // 形参
document.getElementById("demo").innerHTML=myFunction(4,3);  // 实参
```

---

ES6 新增箭头函数，定义函数时更加简洁、易读。

```javascript
// 传统定义函数方式
function Test () {
  //
}

const Test = function () {
  //
}

// 使用箭头函数定义函数时可以省略 function 关键字
const Test = (...params) => {
  //
}

// 该函数只有一个参数时可以简写成：
const Test = param => {
  return param;
}

console.log(Test('hello'));   // hello
```

---

JavaScript 复选框实现全选、取消全选 、反选实例：

```javascript
function opcheckboxed(objName, type) {
    var objNameList = document.getElementsByName(objName);
    if (null != objNameList) {
        for (var i=0; i<objNameList.length; i++) {
            if (objNameList[i].checked == true) {
                if (type != 'checkall') {
                    objNameList[i].checked = false;
                }
            } else {
                if (type != 'uncheckall') {
                    objNameList[i].checked = true
                }
            }
        }
    }
}
```

```html
看书：<input type="checkbox" name="checkbox" value="1"><br/>
写字：<input type="checkbox" name="checkbox" value="2"><br/>
打飞机：<input type="checkbox" name="checkbox" value="3"><br/>
玩游戏：<input type="checkbox" name="checkbox" value="4"><br/>
<button onclick="opcheckboxed('checkbox', 'checkall')">全选</button>
<button onclick="opcheckboxed('checkbox', 'uncheckall')">取消全选</button>
<button onclick="opcheckboxed('checkbox', 'reversecheck')">反选</button>
```

---

```html
看书: <input type="checkbox" name="cb" value="1"><br/>
写字: <input type="checkbox" name="cb" value="2"><br/>
游戏: <input type="checkbox" name="cb" value="3"><br/>
<button type="button" onclick="checkAll(this)">全选/取消全选</button>
<script>
function checkAll(){
    var element = document.getElementsByName("cb");
    for (let e in element) {
        element[e].checked = !element[e].checked;
    }
}
</script>
```

----

# JavaScript 作用域

作用域是可访问变量的集合。

## JavaScript 作用域

在 JavaScript 中, 对象和函数同样也是变量。

**在 JavaScript 中, 作用域为可访问变量，对象，函数的集合。**

JavaScript 函数作用域: 作用域在函数内修改。

## JavaScript 局部作用域

变量在函数内声明，变量为局部作用域。

局部变量：只能在函数内部访问。

```javascript
// 此处不能调用 carName 变量
function myFunction() {
    var carName = "Volvo";
    // 函数内可调用 carName 变量
}
```

[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_scope_local)

因为局部变量只作用于函数内，所以不同的函数可以使用相同名称的变量。

局部变量在函数开始执行时创建，函数执行完后局部变量会自动销毁。

## JavaScript 全局变量

变量在函数外定义，即为全局变量。

全局变量有 **全局作用域**: 网页中所有脚本和函数均可使用。 

```javascript
var carName = " Volvo";
 
// 此处可调用 carName 变量
function myFunction() {
    // 函数内可调用 carName 变量
}
```

如果变量在函数内没有声明（没有使用 `var `关键字），该变量为全局变量。

以下实例中 carName 在函数内，但是为全局变量。

```javascript
// 此处可调用 carName 变量
 
function myFunction() {
    carName = "Volvo";
    // 此处可调用 carName 变量
}
```

## JavaScript 变量生命周期

JavaScript 变量生命周期在它声明时初始化。

局部变量在函数执行完毕后销毁。

全局变量在页面关闭后销毁。

## 函数参数

函数参数只在函数内起作用，是局部变量。

## HTML 中的全局变量

在 HTML 中, 全局变量是 `window `对象: 所有数据变量都属于 `window `对象。

```javascript
//此处可使用 window.carName
 
function myFunction() {
    carName = "Volvo";
}
```

---

局部变量：在函数中通过`var`声明的变量。

全局变量：在函数外通过`var`声明的变量。

没有声明就使用的变量，默认为全局变量，不论这个变量在哪被使用。

---

函数内未声明即使用的变量情况：

```javascript
function func(){
  undefined_var=110
}
```

在 `func() `被第一次调用之前， `undefined_var `变量是不存在的即 `undefined`。`func() `被调用过之后，`undefined_var `成为全局变量。

---

**let 和 var的区别**

 基本用法

ES6 新增了`let`命令，用来声明变量。它的用法类似于`var`，但是所声明的变量，只在`let`命令所在的代码块内有效。

```javascript
{
  let a = 10;
  var b = 1;
}

a // ReferenceError: a is not defined.
b // 1
```

上面代码在代码块之中，分别用`let`和`var`声明了两个变量。然后在代码块之外调用这两个变量，结果`let`声明的变量报错，`var`声明的变量返回了正确的值。这表明，`let`声明的变量只在它所在的代码块有效。

`for`循环的计数器，就很合适使用`let`命令。

```javascript
for (let i = 0; i < 10; i++) {
  // ...
}

console.log(i);
// ReferenceError: i is not defined
```

上面代码中，计数器i只在for循环体内有效，在循环体外引用就会报错。

下面的代码如果使用var，最后输出的是10。

```javascript
var a = [];
for (var i = 0; i < 10; i++) {
  a[i] = function () {
    console.log(i);
  };
}
a[6](); // 10
```

上面代码中，变量i是var命令声明的，在全局范围内都有效，所以全局只有一个变量i。每一次循环，变量i的值都会发生改变，而循环内被赋给数组a的函数内部的console.log(i)，里面的i指向的就是全局的i。也就是说，所有数组a的成员里面的i，指向的都是同一个i，导致运行时输出的是最后一轮的i的值，也就是 10。

如果使用let，声明的变量仅在块级作用域内有效，最后输出的是 6。

```javascript
var a = [];
for (let i = 0; i < 10; i++) {
  a[i] = function () {
    console.log(i);
  };
}
a[6](); // 6
```

上面代码中，变量i是let声明的，当前的i只在本轮循环有效，所以每一次循环的i其实都是一个新的变量，所以最后输出的是6。你可能会问，如果每一轮循环的变量i都是重新声明的，那它怎么知道上一轮循环的值，从而计算出本轮循环的值？这是因为 JavaScript 引擎内部会记住上一轮循环的值，初始化本轮的变量i时，就在上一轮循环的基础上进行计算。

另外，for循环还有一个特别之处，就是设置循环变量的那部分是一个父作用域，而循环体内部是一个单独的子作用域。

```javascript
for (let i = 0; i < 3; i++) {
  let i = 'abc';
  console.log(i);
}
// abc
// abc
// abc
```

上面代码正确运行，输出了 3 次abc。这表明函数内部的变量i与循环变量i不在同一个作用域，有各自单独的作用域。

---

# JavaScript 事件

## HTML 事件

HTML 事件可以是浏览器行为，也可以是用户行为。

以下是 HTML 事件的实例：

- HTML 页面完成加载
- HTML input 字段改变时
- HTML 按钮被点击

通常，当事件发生时，你可以做些事情。

在事件触发时 JavaScript 可以执行一些代码。

HTML 元素中可以添加事件属性，使用 JavaScript 代码来添加 HTML 元素。

单引号:

```javascript
<some-HTML-element some-event='JavaScript 代码'>
```

双引号:

```javascript
<some-HTML-element some-event="JavaScript 代码">
```

在以下实例中，按钮元素中添加了 `onclick `属性 (并加上代码):

```html
<button onclick="getElementById('demo').innerHTML=Date()">现在的时间是?</button>
<p id="demo"></p>
```

以上实例中，JavaScript 代码将修改 id="demo" 元素的内容。

在下一个实例中，代码将修改自身元素的内容 (使用 **this**.innerHTML):

```html
<button onclick="this.innerHTML=Date()">现在的时间是?</button>
```

JavaScript代码通常是几行代码。比较常见的是通过事件属性来调用：

```html
<p>点击按钮执行 <em>displayDate()</em> 函数.</p>
<button onclick="displayDate()">点这里</button>
<p id="demo"></p>
<script>
function displayDate(){
	document.getElementById("demo").innerHTML=Date();
}
</script>
```

## 常见的HTML事件

下面是一些常见的HTML事件的列表:

| 事件          | 描述                         |
| :------------ | :--------------------------- |
| `onchange`    | HTML 元素改变                |
| `onclick`     | 用户点击 HTML 元素           |
| `onmouseover` | 用户在一个HTML元素上移动鼠标 |
| `onmouseout`  | 用户从一个HTML元素上移开鼠标 |
| `onkeydown`   | 用户按下键盘按键             |
| `onload`      | 浏览器已完成页面的加载       |

## JavaScript 可以做什么?

事件可以用于处理表单验证，用户输入，用户行为及浏览器动作:

- 页面加载时触发事件
- 页面关闭时触发事件
- 用户点击按钮执行动作
- 验证用户输入内容的合法性
- 等等 ...

可以使用多种方法来执行 JavaScript 事件代码：

- HTML 事件属性可以直接执行 JavaScript 代码
- HTML 事件属性可以调用 JavaScript 函数
- 你可以为 HTML 元素指定自己的事件处理程序
- 你可以阻止事件的发生。
- 等等 ...

---

注意，当在 JS 文件中为相关元素设置事件时，其写法与 HTML 事件属性写法相同，例如：

```html
<button id="test" onclick="changeContent()">更换内容</button>
```

在 JS 中则需要这样写：

```javascript
var test = document.getElementById("test");
test.onclick = changeContent(){
    //......
}
```

注意：在为元素添加事件句柄或者删除元素事件句柄的过程中，不要将 `event` 参数设置为 `onclick`，而必须写成 `click`，去掉事件名称中的 `on` 即可。

添加事件句柄函数原型:

```javascript
element.addEventListener(event, function, [useCapture])
```

删除事件句柄的函数原型:

```javascript
element.removeEventListener(event, function, [useCapture])
```

---

添加事件句柄实例：

```html
<input id="test" type="button" value="提交">
<script>
window.onload = function () { 
    var test = document.getElementById("test");
    test.addEventListener("click", myfun1);
    test.addEventListener("click", myfun2);
};
function myfun1() {
    alert("你好1");
}function myfun2() {
    alert("你好2");
}
</script>
```

---

# JavaScript 字符串

符串可以是插入到引号中的任何字符。你可以使用单引号或双引号：

```javascript
var carname = "Volvo XC60";
var carname = 'Volvo XC60';
```

你可以使用索引位置来访问字符串中的每个字符：

```javascript
var character = carname[7];
```

字符串的索引从 `0` 开始，这意味着第一个字符索引值为 `[0]`,第二个为 `[1]`, 以此类推。

你可以在字符串中使用引号，字符串中的引号不要与字符串的引号相同:

```javascript
var answer = "It's alright";
var answer = "He is called 'Johnny'";
var answer = 'He is called "Johnny"';
```

你也可以在字符串添加转义字符来使用引号：

```javascript
var x = 'It\'s alright';
var y = "He is called \"Johnny\"";
```

## 字符串长度

可以使用内置属性 **length** 来计算字符串的长度：

```javascript
var txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var sln = txt.length;
```

## 特殊字符

在 JavaScript 中，字符串写在单引号或双引号中。

因为这样，以下实例 JavaScript 无法解析：

```javascript
 "We are the so-called "Vikings" from the north."
```

字符串` "We are the so-called " `被截断。

如何解决以上的问题呢？可以使用反斜杠 (`\`) 来转义 "`Vikings`" 字符串中的双引号，如下:

```javascript
 "We are the so-called \"Vikings\" from the north."
```

 反斜杠是一个**转义字符**。 转义字符将特殊字符转换为字符串字符：

转义字符 (`\`) 可以用于转义撇号，换行，引号，等其他特殊字符。

下表中列举了在字符串中可以使用转义字符转义的特殊字符：

| 代码 | 输出        |
| :--- | :---------- |
| `\'` | 单引号      |
| `\"` | 双引号      |
| `\\` | 反斜杠      |
| `\n` | 换行        |
| `\r`   | 回车        |
| `\t`   | tab(制表符) |
| `\b`   | 退格符      |
| `\f`   | 换页符      |

## 字符串可以是对象

通常， JavaScript 字符串是原始值，可以使用字符创建： 

```javascript
var firstName = "John"
```

但我们也可以使用 `new `关键字将字符串定义为一个对象：

```javascript
var firstName = new String("John");
```

```html
<p id="demo"></p>
<script>
var x = "John";              // x是一个字符串
var y = new String("John");  // y是一个对象
document.getElementById("demo").innerHTML = typeof x + " " + typeof y;
</script>
```

> 不要创建 `String `对象。它会拖慢执行速度，并可能产生其他副作用：

```html
<p id="demo"></p>
<script>
var x = "John";              // x 是字符串
var y = new String("John");  // y 是一个对象
document.getElementById("demo").innerHTML = x===y;
</script>
<p>=== 为绝对相等，即数据类型与值都必须相等。</p>
```

## 字符串属性和方法

原始值字符串，如 "John", 没有属性和方法(因为他们不是对象)。

原始值可以使用 JavaScript 的属性和方法，因为 JavaScript 在执行方法和属性时可以把原始值当作对象。

**字符串方法我们将在下一章节中介绍。**

## 字符串属性

| 属性          | 描述                       |
| :------------ | :------------------------- |
| `constructor` | 返回创建字符串属性的函数   |
| `length`      | 返回字符串的长度           |
| `prototype`   | 允许您向对象添加属性和方法 |

## 字符串方法

| 方法                  | 描述                                                         |
| :-------------------- | :----------------------------------------------------------- |
| `charAt()`            | 返回指定索引位置的字符                                       |
| `charCodeAt()`        | 返回指定索引位置字符的 Unicode 值                            |
| `concat()`            | 连接两个或多个字符串，返回连接后的字符串                     |
| `fromCharCode()`      | 将 Unicode 转换为字符串                                      |
| `indexOf()`           | 返回字符串中检索指定字符第一次出现的位置                     |
| `lastIndexOf()`       | 返回字符串中检索指定字符最后一次出现的位置                   |
| `localeCompare()`     | 用本地特定的顺序来比较两个字符串                             |
| `match()`             | 找到一个或多个正则表达式的匹配                               |
| `replace()`           | 替换与正则表达式匹配的子串                                   |
| `search()`            | 检索与正则表达式相匹配的值                                   |
| `slice()`             | 提取字符串的片断，并在新的字符串中返回被提取的部分           |
| `split()`             | 把字符串分割为子字符串数组                                   |
| `substr()`            | 从起始索引号提取字符串中指定数目的字符                       |
| `substring()`         | 提取字符串中两个指定的索引号之间的字符                       |
| `toLocaleLowerCase()` | 根据主机的语言环境把字符串转换为小写，只有几种语言（如土耳其语）具有地方特有的大小写映射 |
| `toLocaleUpperCase()` | 根据主机的语言环境把字符串转换为大写，只有几种语言（如土耳其语）具有地方特有的大小写映射 |
| `toLowerCase()`       | 把字符串转换为小写                                           |
| `toString()`          | 返回字符串对象值                                             |
| `toUpperCase()`       | 把字符串转换为大写                                           |
| `trim()`              | 移除字符串首尾空白                                           |
| `valueOf()`           | 返回某个字符串对象的原始值                                   |

---

## JavaScript == 与 === 区别

1、对于 `string`、`number `等基础类型，`==` 和 `===` 是有区别的

- a）不同类型间比较，`==` 之比较 "转化成同一类型后的值" 看 "值" 是否相等，`===` 如果类型不同，其结果就是不等。
-  b）同类型比较，直接进行 "值" 比较，两者结果一样。

2、对于 `Array`,`Object` 等高级类型，`==` 和 `=== `是没有区别的，进行 "指针地址" 比较

3、基础类型与高级类型，== 和 === 是有区别的

- a）对于 ==，将高级转化为基础类型，进行 "值" 比较
-  b）因为类型不同，=== 结果为 false

4、`!=` 为 `==` 的非运算，`!==` 为 `===` 的非运算

```javascript
var num = 1;
var str = "1";
var test = 1;

test == num   //true　相同类型　相同值 
test === num  //true　相同类型　相同值 
test !== num  //false test与num类型相同，其值也相同,　非运算肯定是false 

num == str   //true 　把str转换为数字，检查其是否相等。 
num != str   //false  == 的 非运算 
num === str  //false  类型不同，直接返回false 
num !== str  //true   num 与 str类型不同 意味着其两者不等　非运算自然是true啦
```

---

```javascript
var x = "JohnJohn";     	// x 是字符串
y = x.charAt(2);        	// h
y = x.charCodeAt(2);    	// 104
y = x.concat(y, y);     	// JohnJohn104104, x+y+y
y = x.indexOf('h');     	// 2, 索引从0开始
y = x.lastIndexOf('h'); 	// 6
y = x.slice();
y = x.split('o');       	//J,hnJ,hn
y = x.substr(2);  			// hnJohn
y = x.substring(2,4);   	// hn，[2,3]
y = x.toLocaleLowerCase();  // johnjohn,小写
y = x.toLocaleUpperCase();  // JOHNJOHN,大写
y = x.toString();           // 转成Stirng
y = x.toUpperCase();        // JOHNJOHN,大写
y = x.trim();               // JohnJohn,去除两端的空格
y = x.valueOf();            // 返回某个字符串对象的原始值
```

---

# JavaScript 运算符

## 用于字符串的 + 运算符

\+ 运算符用于把文本值或字符串变量加起来（连接起来）。

如需把两个或多个字符串变量连接起来，请使用 + 运算符。

```javascript
txt1 = "What a very";
txt2 = "nice day";
txt3 = txt1 + txt2;
// What a verynice day
```

要想在两个字符串之间增加空格，需要把空格插入一个字符串之中：

```javascript
txt1 = "What a very ";
txt2 = "nice day";
txt3 = txt1 + txt2;
// What a very nice day
```

或者把空格插入表达式中：:

```javascript
txt1 = "What a very";
txt2 = "nice day";
txt3 = txt1 + " " + txt2;
// What a very nice day
```

## 对字符串和数字进行加法运算

两个数字相加，返回数字相加的和，如果数字与字符串相加，返回字符串，如下实例：

```javascript
x = 5 + 5;
y = "5" + 5;
z = "Hello" + 5;
```

*x*,*y*, 和 *z* 输出结果为:

```javascript
10
55
Hello5
```

**规则:**如果把数字与字符串相加，结果将成为字符串！

---

```javascript
var result1 = 5+5+"abc"; //结果将是"10abc"
var result2 = ""+5+5+"abc"; //结果将是"55abc"
```

---

空文本 **+** 数字得到的运算结果都是把数字转成字符串，无论文本有多少个空格。但是空格会计入长度。

```javascript
var result1=""+5;         // 得到的结果是"5"
var result2=" "+5;        // 得到的结果是" 5"
var result3="       "+5;  // 得到的结果是"       5"
```

---

1、字符串一个很能强大的数据类型；在执行加 **+** 时,将被加的对象统一处理为字符串。

2、bool 类型在与数字类型进行相加时，视为 0 或者 1 处理。

3、null 类型与数字类型进行累加时，视为 0 处理。

4、bool 类型与 null 类型进行累加时，视为其与整数类型累加处理。

5、undefined 除了与字符串进行累加时有效（undefined 视为字符串"undefined"处理），其他情况皆返回 NaN。

6、求模 **%** 运算，运算结果只取决于第一个数字的正负。

```
-12 % -8 = -4; 
12 % -8 =  4;
-12 % 8 = -4;
```

7、查看 String 数据类型支持的方法和属性：

打开网页后 F12 进行开发调试环境，找到 console 标签页面，执行：

```
var str = new String('string');   
str 
```

点开列表下拉箭头即可:

![img](https://www.runoob.com/wp-content/uploads/2019/12/30994114-FE40-416F-A993-F49210EF0374.jpg)

---

# JavaScript 比较 和 逻辑运算符

比较和逻辑运算符用于测试 *true* 或者 *false*。

## 比较运算符

比较运算符在逻辑语句中使用，以测定变量或值是否相等。

`x=5`，下面的表格解释了比较运算符：

<table class="reference ">
    <tbody>
    <tr>
        <th style="width: 15%; text-align: left;">运算符</th>
        <th style="width: 15%; text-align: left;">描述</th>
        <th style="width: 15%; text-align: left;">比较</th>
        <th style="width: 15%; text-align: left;">返回值</th>
    </tr>
    <tr style="background-color: #ffffff">
        <td rowspan="2" style="vertical-align: top">==</td>
        <td rowspan="2" style="vertical-align: top">等于</td>
        <td style="vertical-align: top">x==8</td>
        <td style="vertical-align: top"><em>false</em></td>
    </tr>
    <tr style="background-color:#ffffff">
        <td style="vertical-align: top">x==5</td>
        <td style="vertical-align: top"><em>true</em></td>
    </tr>
    <tr class="fixzebra">
        <td style="vertical-align: top" rowspan="2">===</td>
        <td style="vertical-align: top" rowspan="2">绝对等于（值和类型均相等）</td>
        <td style="vertical-align: top">x==="5"</td>
        <td style="vertical-align: top"><em>false</em></td>
    </tr>
    <tr class="fixzebra">
        <td style="vertical-align: top">x===5</td>
        <td style="vertical-align: top"><em>true</em></td>
    </tr>
    <tr>
        <td style="vertical-align: top">!=</td>
        <td style="vertical-align: top">&nbsp;不等于</td>
        <td style="vertical-align: top">x!=8</td>
        <td style="vertical-align: top"><em>true</em></td>
    </tr>
    <tr>
        <td style="vertical-align: top" rowspan="2">!==</td>
        <td style="vertical-align: top" rowspan="2">&nbsp;不绝对等于（值和类型有一个不相等，或两个都不相等）</td>
        <td style="vertical-align: top">x!=="5"</td>
        <td style="vertical-align: top"><em>true</em></td>
    </tr>
    <tr class="fixzebra">
    <td style="vertical-align: top">x!==5</td>
    <td style="vertical-align: top"><em>false</em></td>
    </tr>
    <tr style="background-color:#ffffff">
        <td style="vertical-align: top">&gt;</td>
        <td style="vertical-align: top">&nbsp;大于</td>
        <td style="vertical-align: top">x&gt;8</td>
        <td style="vertical-align: top"><em>false</em></td>
    </tr>
    <tr class="fixzebra">
        <td style="vertical-align: top">&lt;</td>
        <td style="vertical-align: top">&nbsp;小于</td>
        <td style="vertical-align: top">x&lt;8</td>
        <td style="vertical-align: top"><em>true</em></td>
    </tr>
    <tr style="background-color:#ffffff">
        <td style="vertical-align: top">&gt;=</td>
        <td style="vertical-align: top">&nbsp;大于或等于</td>
        <td style="vertical-align: top">x&gt;=8</td>
        <td style="vertical-align: top"><em>false</em></td>
    </tr>
        <tr class="fixzebra">
        <td style="vertical-align: top">&lt;=</td>
        <td style="vertical-align: top">&nbsp;小于或等于</td>
        <td style="vertical-align: top">x&lt;=8</td>
        <td style="vertical-align: top"><em>true</em></td>
    </tr>
    </tbody>
</table>

------

## 如何使用

可以在条件语句中使用比较运算符对值进行比较，然后根据结果来采取行动：

```javascript
if (age<18) x="Too young";
```

您将在本教程的下一节中学习更多有关条件语句的知识。

## 逻辑运算符

逻辑运算符用于测定变量或值之间的逻辑。

给定 x=6 以及 y=3，下表解释了逻辑运算符：

| 运算符 | 描述 | 例子                        |
| :----- | :--- | :-------------------------- |
| `&&`   | and  | `(x < 10 && y > 1)` 为 true |
| `||`   | or   | `(x==5 || y==5)` 为 false   |
| `!`    | not  | `!(x==y)` 为 true           |

## 条件运算符

JavaScript 还包含了基于某些条件对变量进行赋值的条件运算符。

### 语法

```javascript
variablename = (condition) ? value1 : value2 
```

如果变量 *age* 中的值小于 18，则向变量 *voteable* 赋值 "年龄太小"，否则赋值 "年龄已达到"。

```javascript
voteable = (age<18) ? "年龄太小" : "年龄已达到";
```

---

## JavaScript多元运算符

```javascript
function test(p){
    var a=5,b=12;
    return p>1 ? p<b?p>b:p=6 : p=3; // 这一行中出现了多个问号和冒号，看起来很乱怎么办呢
}

document.write(test(9));
```

其实很简单，寻找到多元运算符的头 **?** 和尾 **:** 就好办多了

就成了这样:

```javascript
p>1?p<b?p>b:p=6:p=3

p>1? 整体 :p=3
```

1、当 `p>1` 时返回` p<b ? p>b : p=6`

- 1.1、当` p<b` 时返回` p>b`
-  1.2、当 `p>=b` 时返回 `p=6`

2、当 `p<=1` 是返回 `p=3` 所以先执行 1

3、实例中当 p＝9 的时候，返回 p<b?p>b:p=6 接着执行 1.1，当 p＝9<12 时，返回 p>b，即 9>12，条件不成立所以最终结果为 false。