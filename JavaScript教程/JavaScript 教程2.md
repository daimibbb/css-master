# JavaScript if...Else 语句

## 条件语句

通常在写代码时，您总是需要为不同的决定来执行不同的动作。您可以在代码中使用条件语句来完成该任务。

在 JavaScript 中，我们可使用以下条件语句：

- **if 语句** - 只有当指定条件为 true 时，使用该语句来执行代码
- **if...else 语句** - 当条件为 true 时执行代码，当条件为 false 时执行其他代码
- **if...else if....else 语句**- 使用该语句来选择多个代码块之一来执行
- **switch 语句** - 使用该语句来选择多个代码块之一来执行

## if 语句

```html
<p>如果时间早于 20:00，会获得问候 "Good day"。</p>
<button onclick="myFunction()">点击这里</button>
<p id="demo"></p>
<script>
function myFunction() {
    var x = "";
    var time = new Date().getHours();
    if (time<20) {
        x = "Good day";
    }
    document.getElementById("demo").innerHTML=x;
}
</script>
```

## if...else 语句

```html
<p>点击这个按钮，获得基于时间的问候。</p>
<button onclick="myFunction()">点击这里</button>
<p id="demo"></p>
<script>
function myFunction() {
    var x = "";
    var time = new Date().getHours();
    if (time<20) {
        x = "Good day";
    } else {
        x = "Good evening";
    }
    document.getElementById("demo").innerHTML=x;
}
</script>
```

## if...else if...else 语句

```html
<script>
var time = new Date().getHours();
if (time<10) {
    document.write("<b>早上好</b>")
} else if(time>=10 && time<16) {
    document.write("<b>今天好</b>");
} else {
    document.write("<b>晚上好!</b>");
}
</script>
<p>这个例子演示了 if..else if...else 语句。</p>
```

<script>
var time = new Date().getHours();
if (time<10) {
    document.write("<b>早上好</b>")
} else if(time>=10 && time<16) {
    document.write("<b>今天好</b>");
} else {
    document.write("<b>晚上好!</b>");
}
</script>
<p>这个例子演示了 if..else if...else 语句。</p>

这个实例演示了一个链接，当您点击链接时，会带您到不同的地方去。每种机会都是 50% 的概率。

```html
<p id="demo"></p>
<script>
var r = Math.random();
var x = document.getElementById("demo");
if (r>0.5) {
    x.innerHTML="<a href='http://www.baidu.com'>百度</a>"
} else {
    x.innerHTML="<a href='http://www.qq.com'>QQ</a>"
}
</script>
```

---

**提一个优化 if 的方法**

可以这样写：

```javascript
const condition = condition1
let obj = {
  'condition1' : () => { ... },
  'condition2' : () => { ... },
  'condition3' : () => { ... },
}
obj[condition]()
```

实例：

```javascript
const condition = 2
let obj = {
  '1' : () => { document.write(1) },
  '2' : () => { document.write(2) },
  '3' : () => { document.write(3) },
}

obj[condition]()
```

---

# JavaScript switch 语句

```javascript
switch(n)
{
    case 1:
        执行代码块 1
        break;
    case 2:
        执行代码块 2
        break;
    default:
        与 case 1 和 case 2 不同时执行的代码
}
```

工作原理：首先设置表达式 *n*（通常是一个变量）。随后表达式的值会与结构中的每个 case 的值做比较。如果存在匹配，则与该 case 关联的代码块会被执行。请使用 **break** 来阻止代码自动地向下一个 case 运行。

```javascript
var d=new Date().getDay(); 
switch (d) { 
  case 0: x="今天是星期日"; break; 
  case 1: x="今天是星期一"; break; 
  case 2: x="今天是星期二"; break; 
  case 3: x="今天是星期三"; break; 
  case 4: x="今天是星期四"; break; 
  case 5: x="今天是星期五"; break; 
  case 6: x="今天是星期六"; break; 
}
```

## default 关键词

请使用 `default `关键词来规定匹配不存在时做的事情：

```javascript
var d = new Date().getDay();
switch (d) {
    case 6: x="今天是星期六"; break;
    case 0: x="今天是星期日"; break;
    default: x="期待周末";
}
document.getElementById("demo").innerHTML=x;
```

---

主要是为了补充当两种情况相同时，`switch `语句的使用，当两种情况相同时，可以只在第二种情况中写要执行的代码，案例如下：

```javascript
// 测试 switch语句，当 两种情况相同时，比如
// 下面的10或者11，都会走 alert("10或者11")
function testSwich() {
    var number = document.getElementById("test").value;
    number = parseInt(number);
    switch (number) {
        case 1: alert(1); break;
        // number = 10 或者 = 11执行相同的操作
        case 10:
        case 11: alert("10或者11"); break;
        default: alert("既不是1，10，11");
    }
}
```

```html
<label>输入一个数字
    <input type="text" id="test">
    <input type="button" value="提交" onclick="testSwich()">
</label>
```

---

# JavaScript for 循环

```javascript
cars = ["BMW","Volvo","Saab","Ford"];
for (var i=0; i<cars.length; i++) {
    document.write(cars[i] + "<br>")
}
```

## 不同类型的循环

JavaScript 支持不同类型的循环：

- **for** - 循环代码块一定的次数
- **for/in** - 循环遍历对象的属性
- **while** - 当指定的条件为 true 时循环指定的代码块
- **do/while** - 同样当指定的条件为 true 时循环指定的代码块

## For 循环

```javascript
function myFunction(){
	var x = "";
	for (var i=0;i<5;i++){
		x = x + "该数字为 " + i + "<br>";
	}
	document.getElementById("demo").innerHTML=x;
}
```

## 语句 1

通常我们会使用语句 1 初始化循环中所用的变量 (var i=0)。

语句 1 是可选的，也就是说不使用语句 1 也可以。

您可以在语句 1 中初始化任意（或者多个）值：

```javascript
cars = ["BMW","Volvo","Saab","Ford"];
for (var i=0; i<cars.length; i++) {
    document.write(cars[i] + "<br>")
}
```

同时您还可以省略语句 1（比如在循环开始前已经设置了值时）：

```javascript
cars = ["BMW","Volvo","Saab","Ford"];
var i=2, len=cars.length;
for (; i<len; i++) {
    document.write(cars[i] + "<br>");
}
```

## 语句 2

通常语句 2 用于评估初始变量的条件。

语句 2 同样是可选的。

如果语句 2 返回 true，则循环再次开始，如果返回 false，则循环将结束。

## 语句 3

通常语句 3 会增加初始变量的值。

语句 3 也是可选的。

语句 3 有多种用法。增量可以是负数 (i--)，或者更大 (i=i+15)。

语句 3 也可以省略（比如当循环内部有相应的代码时）：

```javascript
cars = ["BMW","Volvo","Saab","Ford"];
var i=0, len=cars.length;
for (; i<len; ) {
    document.write(cars[i] + "<br>");
    i++;
}
```

## For/In 循环

JavaScript `for/in` 语句循环遍历对象的属性：

```javascript
function myFunction() {
    var x;
    var txt="";
    var person = {fname: "Bill", lname: "Gates", age: 56};
    for (x in person) {
        txt = txt + person[x];
    }
    document.getElementById("demo").innerHTML = txt;
}
```

---

**for 数组循环**

```javascript
var size=[1,2,3,4,5,6,7];
for (var i=0; i<size.length; i++) {
    document.write(size[i] + " ")
}
```

---

**for in** 循环不仅可以遍历对象的属性，还可以遍历数组。

```javascript
var x;
var nums = [1,3,5];
for (x in nums) {
    document.write(nums[x] + "<br>")
}
```

---

# JavaScript while 循环

```javascript
function myFunction() {
    var x="", i=0;
    while (i<5) {
       x=x + "该数字为 " + i + "<br>";
       console.log(x);
       i++;
    }
    document.getElementById("demo").innerHTML=x;
}
```

## do/while 循环

do/while 循环是 while 循环的变体。该循环会在检查条件是否为真之前执行一次代码块，然后如果条件为真的话，就会重复这个循环。

```javascript
function myFunction(){
	var x="",i=0;
	do {
		x=x + "该数字为 " + i + "<br>";
	    i++;
	} while (i<5)  
	document.getElementById("demo").innerHTML=x;
}
```

## 比较 for 和 while

```javascript
cars=["BMW","Volvo","Saab","Ford"];
var i=0;
for (; cars[i]; ) {
    document.write(cars[i] + "<br>");
    i++;
}
```

```javascript
cars=["BMW","Volvo","Saab","Ford"];
var i=0;
while (cars[i]) {
    document.write(cars[i] + "<br>");
    i++;
}
```

---

# JavaScript break 和 continue 语句

## break 语句

```javascript
function myFunction(){
	var x="", i=0;
	for (i=0; i<10; i++) {
		if (i==3){
    			break;
			}
    	x=x + "该数字为 " + i + "<br>";
    }
	document.getElementById("demo").innerHTML=x;
}
```

## continue 语句

```javascript
function myFunction(){
	var x="",i=0;
	for (i=0; i<10; i++){
  		if (i==3) {
    		continue;
    	}
		x=x + "该数字为 " + i + "<br>";
  	}
	document.getElementById("demo").innerHTML=x;
}
```

## JavaScript 标签

正如您在 `switch `语句那一章中看到的，可以对 JavaScript 语句进行标记。

如需标记 JavaScript 语句，请在语句之前加上冒号：

```javascript
label:
statements
```

`break `和 `continue `语句仅仅是能够跳出代码块的语句。

语法:

```javascript
break labelname; 
 
continue labelname;
```

`continue `语句（带有或不带标签引用）只能用在循环中。

`break `语句（不带标签引用），只能用在循环或 `switch `中。

通过标签引用，break 语句可用于跳出任何 JavaScript 代码块：

```javascript
cars=["BMW","Volvo","Saab","Ford"];
list: {
    document.write(cars[0] + "<br>");
    document.write(cars[1] + "<br>");
    document.write(cars[2] + "<br>");
    break list;
    document.write(cars[3] + "<br>");
    document.write(cars[4] + "<br>");
    document.write(cars[5] + "<br>");
}
```

```
BMW
Volvo
Saab
```

---

关于 JavaScript 标签与 `break `和 `continue `一起使用的理解。

`break `的作用是跳出代码块, 所以 `break `可以使用于循环和 `switch `等

`continue `的作用是进入下一个迭代, 所以 `continue `只能用于循环的代码块。

代码块: 基本上是`{}`大括号之间

然后：

\1. 默认标签的情况（除了默认标签情况，其他时候必须要有名标签，否则会有惊喜）

当 `break` 和 `continue `同时用于循环时，没有加标签，此时默认标签为当前"循环"的代码块。

当 `break `用于 `switch `时，默认标签为当前的 `switch `代码块:

有名标签的情况

```javascript
cars=["BMW","Volvo","Saab","Ford"];
list:
{
    document.write(cars[0] + "");
    document.write(cars[1] + "");
    document.write(cars[2] + "");
    break list;
    document.write(cars[3] + "");
    document.write(cars[4] + "");
    document.write(cars[5] + "");
}
```

上述`break list;`会跳出`list`的代码块。如果将`break`换成`continue`会有惊喜，违反了明确中的第二点，因为`list`只是个普通代码块，而不是循环。除非`list`写成如下形式 `list`:

```javascript
for(var i=0; i<10; ++i)
{
    continue list;
}
```

有了标签，可以使用`break`和`continue`在多层循环的时候控制外层循环。

例如下面：

```javascript
outerloop:
for (var i=0; i<10; i++) {
    innerloop:
    for (var j=0; j<10; j++) {
        if (j>3) {
            break;
        }
        if (i===2) {
            break innerloop;
        }
        if (i===4) {
            break outerloop;
        }
        document.write("i=" + i + " j=" + j + "<br>");
    }
}
```

```
i=0 j=0
i=0 j=1
i=0 j=2
i=0 j=3
i=1 j=0
i=1 j=1
i=1 j=2
i=1 j=3
i=3 j=0
i=3 j=1
i=3 j=2
i=3 j=3
```

---

# JavaScript typeof, null, 和 undefined

## typeof 操作符

你可以使用 `typeof `操作符来检测变量的数据类型。

```javascript
typeof "John"                // 返回 string
typeof 3.14                  // 返回 number
typeof false                 // 返回 boolean
typeof [1,2,3,4]             // 返回 object
typeof {name:'John', age:34} // 返回 object
```

## null

在 JavaScript 中 `null `表示 "什么都没有"。

`null`是一个只有一个值的特殊类型。表示一个空对象引用。

你可以设置为 `null `来清空对象:

```html
<p>对象可以通过设置为 <b>null</b> 来清空。</p>
<p id="demo"></p>
<script>
var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
var person = null;
document.getElementById("demo").innerHTML = typeof person;
</script>
```

你可以设置为 `undefined `来清空对象:

```html
<p>对象可以设置为 <b>undefined</b> 来清空。</p>
<p id="demo"></p>
<script>
var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
var person = undefined;
document.getElementById("demo").innerHTML = typeof person;
</script>
```

<p>对象可以设置为 <b>undefined</b> 来清空。</p>
<p id="demo"></p>
<script>
var person = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};
var person = undefined;
document.getElementById("demo").innerHTML = typeof person;
</script>

## undefined

在 JavaScript 中, **undefined** 是一个没有设置值的变量。

**typeof** 一个没有值的变量会返回 **undefined**。

```javascript
person = undefined;          // 值为 undefined, 类型是undefined
```

```html
<p>变量的值如果不存在则该变量值为 <b>undefined</b>。</p>
<p id="demo"></p>
<script>
var person;
document.getElementById("demo").innerHTML =
	person + "<br>" + typeof person;
</script>
```

```
变量的值如果不存在则该变量值为 undefined。

undefined
undefined
```

## undefined 和 null 的区别

`null `和 `undefined `的值相等，但类型不等：

```javascript
typeof undefined             // undefined
typeof null                  // object
null === undefined           // false
null == undefined            // true
```

---

**1、定义**

-  （1）`undefined`：是所有没有赋值变量的默认值，自动赋值。
-  （2）`null`：主动释放一个变量引用的对象，表示一个变量不再指向任何对象地址。

**2、何时使用null?**

当使用完一个比较大的对象时，需要对其进行释放内存时，设置为 `null`。

**3、null 与 undefined 的异同点是什么呢？**

**共同点**：都是原始类型，保存在栈中变量本地。

不同点：

（1）`undefined`——表示变量声明过但并未赋过值。

它是所有未赋值变量默认值，例如：

```javascript
var a;    // a 自动被赋值为 undefined
```

（2）`null`——表示一个变量将来可能指向一个对象。

一般用于主动释放指向对象的引用，例如：

```javascript
var emps = ['ss','nn'];
emps = null;     // 释放指向数组的引用
```

4、延伸——垃圾回收站

它是专门释放对象内存的一个程序。

-  （1）在底层，后台伴随当前程序同时运行；引擎会定时自动调用垃圾回收期；
-  （2）总有一个对象不再被任何变量引用时，才释放。

---

# JavaScript 类型转换

`Number() `转换为数字， `String()` 转换为字符串，` Boolean() `转化为布尔值。

## JavaScript 数据类型

在 JavaScript 中有 6 种不同的数据类型：

- `string`
- `number`
- `boolean`
- `object`
- `function`
- `symbol`

3 种对象类型：

- `Object`
- `Date`
- `Array`

2 个不包含任何值的数据类型：

- `null`
- `undefined`

## typeof 操作符

你可以使用 **typeof** 操作符来查看 JavaScript 变量的数据类型。

```javascript
typeof "John"                 // 返回 string
typeof 3.14                   // 返回 number
typeof NaN                    // 返回 number
typeof false                  // 返回 boolean
typeof [1,2,3,4]              // 返回 object
typeof {name:'John', age:34}  // 返回 object
typeof new Date()             // 返回 object
typeof function () {}         // 返回 function
typeof myCar                  // 返回 undefined (如果 myCar 没有声明)
typeof null                   // 返回 object
```

请注意：

- `NaN `的数据类型是 `number`
- 数组(`Array`)的数据类型是 `object`
- 日期(`Date`)的数据类型为 `object`
- `null `的数据类型是 `object`
- 未定义变量的数据类型为 `undefined`

如果对象是 JavaScript Array 或 JavaScript Date ，我们就无法通过 **typeof** 来判断他们的类型，因为都是 返回 object。

## constructor 属性

**constructor** 属性返回所有 JavaScript 变量的构造函数。

```javascript
"John".constructor                 // 返回函数 String()  { [native code] }
(3.14).constructor                 // 返回函数 Number()  { [native code] }
false.constructor                  // 返回函数 Boolean() { [native code] }
[1,2,3,4].constructor              // 返回函数 Array()   { [native code] }
{name:'John', age:34}.constructor  // 返回函数 Object()  { [native code] }
new Date().constructor             // 返回函数 Date()    { [native code] }
function () {}.constructor         // 返回函数 Function(){ [native code] }
```

你可以使用 `constructor `属性来查看对象是否为数组 (包含字符串 "Array"):

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
document.getElementById("demo").innerHTML = isArray(fruits);
function isArray(myArray) {
    return myArray.constructor.toString().indexOf("Array") > -1;
}
```

## JavaScript 类型转换

JavaScript 变量可以转换为新变量或其他数据类型：

- 通过使用 JavaScript 函数
- 通过 JavaScript 自身自动转换

## 将数字转换为字符串

全局方法 **String()** 可以将数字转换为字符串。

该方法可用于任何类型的数字，字母，变量，表达式：

```javascript
String(x)         // 将变量 x 转换为字符串并返回
String(123)       // 将数字 123 转换为字符串并返回
String(100 + 23)  // 将数字表达式转换为字符串并返回
```

Number 方法 **toString()** 也是有同样的效果。

```javascript
x.toString()
(123).toString()
(100 + 23).toString()
```

| 方法              | 描述                                                 |
| :---------------- | :--------------------------------------------------- |
| `toExponential()` | 把对象的值转换为指数计数法。                         |
| `toFixed()`       | 把数字转换为字符串，结果的小数点后有指定位数的数字。 |
| `toPrecision()`   | 把数字格式化为指定的长度。                           |

## 将布尔值转换为字符串

全局方法 **String()** 可以将布尔值转换为字符串。

```javascript
String(false)        // 返回 "false"
String(true)         // 返回 "true"
```

Boolean 方法 **toString()** 也有相同的效果。

```javascript
false.toString()     // 返回 "false"
true.toString()      // 返回 "true"
```

## 将日期转换为字符串

Date() 返回字符串。

```javascript
Date()  // "Sat Apr 11 2020 10:49:46 GMT+0800 (中国标准时间)"
```

全局方法 String() 可以将日期对象转换为字符串。

```javascript
String(Date()) 
```

Date 方法 **toString()** 也有相同的效果。

```javascript
obj = new Date();
obj.toString();
```

| 方法                | 描述                                        |
| :------------------ | :------------------------------------------ |
| `getDate()`         | 从 Date 对象返回一个月中的某一天 (1 ~ 31)。 |
| `getDay()`          | 从 Date 对象返回一周中的某一天 (0 ~ 6)。    |
| `getFullYear()`     | 从 Date 对象以四位数字返回年份。            |
| `getHours()`        | 返回 Date 对象的小时 (0 ~ 23)。             |
| `getMilliseconds()` | 返回 Date 对象的毫秒(0 ~ 999)。             |
| `getMinutes()`      | 返回 Date 对象的分钟 (0 ~ 59)。             |
| `getMonth()`        | 从 Date 对象返回月份 (0 ~ 11)。             |
| `getSeconds()`      | 返回 Date 对象的秒数 (0 ~ 59)。             |
| `getTime()`         | 返回 1970 年 1 月 1 日至今的毫秒数。        |

## 将字符串转换为数字

全局方法 **Number()** 可以将字符串转换为数字。

字符串包含数字(如 "3.14") 转换为数字 (如 3.14).

空字符串转换为 0。

其他的字符串会转换为 `NaN `(不是个数字)。

```javascript
Number("3.14")    // 返回 3.14
Number(" ")       // 返回 0
Number("")        // 返回 0
Number("99 88")   // 返回 NaN
```

| 方法           | 描述                               |
| :------------- | :--------------------------------- |
| `parseFloat()` | 解析一个字符串，并返回一个浮点数。 |
| `parseInt()`   | 解析一个字符串，并返回一个整数。   |

## 一元运算符 +

**Operator +** 可用于将变量转换为数字：

```javascript
var y = "5";      // y 是一个字符串
var x = + y;      // x 是一个数字
```

如果变量不能转换，它仍然会是一个数字，但值为 `NaN `(不是一个数字):

```javascript
var y = "John";   // y 是一个字符串
var x = + y;      // x 是一个数字 (NaN)
```

## 将布尔值转换为数字

全局方法 **Number()** 可将布尔值转换为数字。

```javascript
Number(false)     // 返回 0
Number(true)      // 返回 1
```

## 将日期转换为数字

全局方法 **Number()** 可将日期转换为数字。

```javascript
d = new Date();
Number(d)          // 返回 1404568027739
```

## 自动转换类型

当 JavaScript 尝试操作一个 "错误" 的数据类型时，会自动转换为 "正确" 的数据类型。

以下输出结果不是你所期望的：

```javascript
5 + null    // 返回 5         null 转换为 0
"5" + null  // 返回"5null"   null 转换为 "null"
"5" + 1     // 返回 "51"      1 转换为 "1" 
"5" - 1     // 返回 4         "5" 转换为 5
```

## 自动转换为字符串

当你尝试输出一个对象或一个变量时 JavaScript 会自动调用变量的` toString()` 方法：

```javascript
document.getElementById("demo").innerHTML = myVar;

myVar = {name:"Fjohn"}  // toString 转换为 "[object Object]"
myVar = [1,2,3,4]       // toString 转换为 "1,2,3,4"
myVar = new Date()      // toString 转换为 "Fri Jul 18 2014 09:08:55 GMT+0200"
```

数字和布尔值也经常相互转换：

```javascript
myVar = 123             // toString 转换为 "123"
myVar = true            // toString 转换为 "true"
myVar = false           // toString 转换为 "false"
```

----

## 检测数据类型：typeof 与 instanceof

**typeof**

`typeof `用以获取一个变量或者表达式的类型，`typeof `一般只能返回如下几个结果：

```javascript
number,boolean,string,function（函数）,object（NULL,数组，对象）,undefined。
```

实例：

```javascript
document.getElementById("demo").innerHTML = 
typeof "john" + "<br>" + 
typeof 3.14 + "<br>" +
typeof false + "<br>" +
typeof [1,2,3,4] + "<br>" +
typeof {name:'john', age:34};
// "string<br>number<br>boolean<br>object<br>object"
```

我们可以使用 `typeof` 来获取一个变量是否存在，如 **if(typeof a!="undefined"){}**，而不要去使用 if(a) 因为如果 a 不存在（未声明）则会出错。

正因为 `typeof` 遇到 `null`,数组,对象时都会返回 `object `类型，所以当我们要判断一个对象是否是数组时。

或者判断某个变量是否是某个对象的实例则要选择使用另一个关键语法 **instanceof**。

**instanceof**

可通过 `instanceof `操作符来判断对象的具体类型，语法格式:

```javascript
var result = objectName instanceof objectType
```

返回布尔值，如果是指定类型返回 true，否则返回 false：

例：

```javascript
arr = [1,2,3];
if(arr instanceof Array){
    document.write("arr 是一个数组");
} else {
    document.write("arr 不是一个数组");
}
```

---

**undefined 与 null 的区别：**

表面上 `undefined `与 `null `都是什么都没有的意思，但是实际上 `undefined `是未定义（就是变量没有初始化），`null `是一个变量初始化了，但是什么值都没给，只给了一个空对象；进一步说，`undefined `与 `null`是值相等，类型不相等。

---

`NaN `是一个特殊的数值，`NaN `即非数值（`Not a Number`），这个数值用于本来要返回数值的操作数未返回数值的情况。

`NaN `与任何值都不相等，包括 `NaN `本身。

可以通过 `isNaN()` 方法来判断某个数值是否是`NaN`这个特殊的数，使用 `isNaN() `方法会将传入的数值如果是非数值的会将其自动转换成数值类型，若能转换成数值类型，那么这个函数返回 false，若不能转换成数值类型，则这个数就是 `NaN`，即返回 true。

---

字符串转日期：

```javascript
Date.prototype.format = function (fmt) {
    var o = {
        "M+": this.getMonth() + 1,               //月份
        "d+": this.getDate(),                    //日
        "h+": this.getHours(),                   //小时
        "m+": this.getMinutes(),                 //分
        "s+": this.getSeconds(),                 //秒
        "q+": Math.floor((this.getMonth() + 3) / 3), //季度
        "S": this.getMilliseconds()              //毫秒
    };
    //处理年份
    var reYear = /(y+)/;
    var resultYear = reYear.exec(fmt);
    if (resultYear) {
        var yearformatPart = resultYear[0];//匹配到的格式化字符
        var yearVal = (this.getFullYear() + "").substr(4 - yearformatPart.length);
        fmt = fmt.replace(yearformatPart, yearVal);
    }
    for (var k in o) {
        var re = new RegExp("(" + k + ")");
        re = re.exec(fmt);
        if (re) {
            var Val = "" + o[k];//本次需要替换的数据
            var formatPart = re[0];//匹配到的格式化字符
            var replaceVal = (formatPart.length === 1) ? (Val) : (("00" + Val).substr(Val.length));
            fmt = fmt.replace(formatPart, replaceVal);
        }
    }
    return fmt;
};
var time2 = new Date().format("yyyy-MM-dd hh:mm:ss");
```

---

# JavaScript 正则表达式

正则表达式（英语：Regular Expression，在代码中常简写为regex、regexp或RE）使用单个字符串来描述、匹配一系列符合某个句法规则的字符串搜索模式。

搜索模式可用于文本搜索和文本替换。

## 什么是正则表达式？

正则表达式是由一个字符序列形成的搜索模式。

当你在文本中搜索数据时，你可以用搜索模式来描述你要查询的内容。

正则表达式可以是一个简单的字符，或一个更复杂的模式。

正则表达式可用于所有文本搜索和文本替换的操作。

## 语法

```javascript
/正则表达式主体/修饰符(可选)
```

其中修饰符是可选的。

```javascript
var patt = /runoob/i
```

实例解析：

`/runoob/i `是一个正则表达式。

`runoob `是一个正则表达式主体 (用于检索)。

`i` 是一个修饰符 (搜索不区分大小写)。

## 使用字符串方法

在 JavaScript 中，正则表达式通常用于两个字符串方法 : `search()` 和 `replace()`。

**search() 方法** 用于检索字符串中指定的子字符串，或检索与正则表达式相匹配的子字符串，并返回子串的起始位置。

**replace() 方法** 用于在字符串中用一些字符替换另一些字符，或替换一个与正则表达式匹配的子串。

## search() 方法使用正则表达式

使用正则表达式搜索 "Runoob" 字符串，且不区分大小写：

```javascript
var str = "Visit Runoob!"; 
var n = str.search(/Runoob/i);
```

输出结果为：

```
6
```

## search() 方法使用字符串

search 方法可使用字符串作为参数。字符串参数会转换为正则表达式：

```javascript
var str = "Visit Runoob!"; 
var n = str.search("Runoob");
```

输出结果为：

```
6
```

## replace() 方法使用正则表达式

使用正则表达式且不区分大小写将字符串中的 Microsoft 替换为 Runoob :

```javascript
var str = document.getElementById("demo").innerHTML; 
var txt = str.replace(/microsoft/i,"Runoob");
```

输出结果为：

```
Visit Runoob!
```

## replace() 方法使用字符串

`replace()` 方法将接收字符串作为参数：

```javascript
var str = document.getElementById("demo").innerHTML; 
var txt = str.replace("Microsoft","Runoob");
```

## 正则表达式修饰符

**修饰符** 可以在全局搜索中不区分大小写:

| 修饰符 | 描述                                                     |
| :----- | :------------------------------------------------------- |
| `i`    | 执行对大小写不敏感的匹配。                               |
| `g`    | 执行全局匹配（查找所有匹配而非在找到第一个匹配后停止）。 |
| `m`    | 执行多行匹配。                                           |

## 正则表达式模式

方括号用于查找某个范围内的字符：

| 表达式  | 描述                       |
| :------ | :------------------------- |
| `[abc]` | 查找方括号之间的任何字符。 |
| `[0-9]` | 查找任何从 0 至 9 的数字。 |
| `(x|y)` | 查找任何以 \| 分隔的选项。 |

元字符是拥有特殊含义的字符：

| 元字符   | 描述                                        |
| :------- | :------------------------------------------ |
| `\d`     | 查找数字。                                  |
| `\s`     | 查找空白字符。                              |
| `\b`     | 匹配单词边界。                              |
| `\uxxxx` | 查找以十六进制数 xxxx 规定的 Unicode 字符。 |

量词:

| 量词 | 描述                                  |
| :--- | :------------------------------------ |
| `n+` | 匹配任何包含至少一个 *n* 的字符串。   |
| `n*` | 匹配任何包含零个或多个 *n* 的字符串。 |
| `n?` | 匹配任何包含零个或一个 *n* 的字符串。 |

## 使用 RegExp 对象

在 JavaScript 中，`RegExp `对象是一个预定义了属性和方法的正则表达式对象。

## 使用 test()

`test() `方法是一个正则表达式方法。

`test() `方法用于检测一个字符串是否匹配某个模式，如果字符串中含有匹配的文本，则返回 true，否则返回 false。

以下实例用于搜索字符串中的字符 "`e`"：

```javascript
var patt = /e/;
patt.test("The best things in life are free!");
```

字符串中含有 "e"，所以该实例输出为：

```
true
```

你可以不用设置正则表达式的变量，以上两行代码可以合并为一行：

```javascript
/e/.test("The best things in life are free!")
```

## 使用 exec()

`exec()` 方法是一个正则表达式方法。

`exec()` 方法用于检索字符串中的正则表达式的匹配。

该函数返回一个数组，其中存放匹配的结果。如果未找到匹配，则返回值为 `null`。

以下实例用于搜索字符串中的字母 "e":

```javascript
/e/.exec("The best things in life are free!");
```

字符串中含有 "e"，所以该实例输出为:

```
["e"]
```

---

JS 判断输入字符串是否为数字、字母、下划线组成

```javascript
function isValid(str) {
    return /^\w+$/.test(str);
}
str = "1234abd__";
document.write(isValid(str));
document.write("<br>");

str2 = "$32343#";
document.write(isValid(str2));
document.write("<br>");
```

JS 判断输入字符串是否全部为字母

```javascript
function isletter(str) {
    return /^[a-zA-Z]+$/.test(str);
}

val = "123456";
document.write(isletter(val));
document.write("<br>");

val2 = "asaaa";
document.write(isletter(val2));
document.write("<br>");
```

---

正则表达式表单验证实例：

```javascript
/*是否带有小数*/
function sDecimal(strValue )  {
    var  objRegExp= /^\d+\.\d+$/;
    return  objRegExp.test(strValue);  
}  

/*校验是否中文名称组成 */
function ischina(str) {
    var reg=/^[\u4E00-\u9FA5]{2,4}$/;   /*定义验证表达式*/
    return reg.test(str);     /*进行验证*/
}

/*校验是否全由8位数字组成 */
function isStudentNo(str) {
    var reg=/^[0-9]{8}$/;   /*定义验证表达式*/
    return reg.test(str);     /*进行验证*/
}

/*校验电话码格式 */
function isTelCode(str) {
    var reg= /^((0\d{2,3}-\d{7,8})|(1[3584]\d{9}))$/;
    return reg.test(str);
}

/*校验邮件地址是否合法 */
function IsEmail(str) {
    var reg=/^\w+@[a-zA-Z0-9]{2,10}(?:\.[a-z]{2,4}){1,3}$/;
    return reg.test(str);
}
```

---

# JavaScript 错误 - throw、try 和 catch

**try** 语句测试代码块的错误。

**catch** 语句处理错误。

**throw** 语句创建自定义错误。

**finally** 语句在 try 和 catch 语句之后，无论是否有触发异常，该语句都会执行。

## JavaScript 错误

当 JavaScript 引擎执行 JavaScript 代码时，会发生各种错误。

可能是语法错误，通常是程序员造成的编码错误或错别字。

可能是拼写错误或语言中缺少的功能（可能由于浏览器差异）。

可能是由于来自服务器或用户的错误输出而导致的错误。

当然，也可能是由于许多其他不可预知的因素。

## JavaScript 抛出（throw）错误

当错误发生时，当事情出问题时，JavaScript 引擎通常会停止，并生成一个错误消息。

描述这种情况的技术术语是：JavaScript 将**抛出**一个错误。

## JavaScript try 和 catch

**try** 语句允许我们定义在执行时进行错误测试的代码块。

**catch** 语句允许我们定义当 try 代码块发生错误时，所执行的代码块。

JavaScript 语句 **try** 和 **catch** 是成对出现的。

### **语法**

```javascript
try {
    ...    //异常的抛出
} catch(e) {
    ...    //异常的捕获与处理
} finally {
    ...    //结束处理
}
```

## 实例

在下面的例子中，我们故意在 try 块的代码中写了一个错字。

catch 块会捕捉到 try 块中的错误，并执行代码来处理它。

```javascript
var txt=""; 
function message() { 
    try { 
        adddlert("Welcome guest!"); 
    } catch(err) { 
        txt="本页有一个错误。\n\n"; 
        txt+="错误描述：" + err.message + "\n\n"; 
        txt+="点击确定继续。\n\n"; 
        alert(txt); 
    } 
}
```

### finally 语句

finally 语句不论之前的 try 和 catch 中是否产生异常都会执行该代码块。

```javascript
function myFunction() {
    var message, x;
    message = document.getElementById("p01");
    message.innerHTML = "";
    x = document.getElementById("demo").value;
    try {
        if (x==="") throw "值是空的";
        if (isNaN(x)) throw "值不是一个数字";
        x = Number(x);
        if (x>10) throw "太大";
        if (x<5) throw "太小";
    } catch (e) {
        message.innerHTML = "错误：" + e + "。";
    } finally {
        document.getElementById("demo").value = "";
    }
}
```

```html
<p>不管输入是否正确，输入框都会再输入后清空。</p>
<p>请输入 5 ~ 10 之间的数字：</p>
<label>
    <input id="demo" type="text">
    <button type="button" onclick="myFunction()">点我</button>
</label>
<p id="p01"></p>
```

## Throw 语句

throw 语句允许我们创建自定义错误。

正确的技术术语是：创建或**抛出异常**（exception）。

如果把 throw 与 try 和 catch 一起使用，那么您能够控制程序流，并生成自定义的错误消息。

### **语法**

```javascript
throw exception
```

异常可以是 JavaScript 字符串、数字、逻辑值或对象。

## 实例

本例检测输入变量的值。如果值是错误的，会抛出一个异常（错误）。catch 会捕捉到这个错误，并显示一段自定义的错误消息：

```javascript
function myFunction() {
    var message, x;
    message = document.getElementById("message");
    message.innerHTML = "";
    x = document.getElementById("demo").value;
    try { 
        if(x == "")  throw "值为空";
        if(isNaN(x)) throw "不是数字";
        x = Number(x);
        if(x < 5)    throw "太小";
        if(x > 10)   throw "太大";
    } catch(err) {
        message.innerHTML = "错误: " + err;
    }
}
```

---

# JavaScript 调试

在编写 JavaScript 时，如果没有调试工具将是一件很痛苦的事情。

## avaScript 调试

没有调试工具是很难去编写 JavaScript 程序的。

你的代码可能包含语法错误，逻辑错误，如果没有调试工具，这些错误比较难于发现。

通常，如果 JavaScript 出现错误，是不会有提示信息，这样你就无法找到代码错误的位置。

## JavaScript 调试工具

在程序代码中寻找错误叫做代码调试。

调试很难，但幸运的是，很多浏览器都内置了调试工具。

内置的调试工具可以开始或关闭，严重的错误信息会发送给用户。

有了调试工具，我们就可以设置断点 (代码停止执行的位置), 且可以在代码执行时检测变量。

浏览器启用调试工具一般是按下 F12 键，并在调试菜单中选择 "Console" 。

## console.log() 方法

如果浏览器支持调试，你可以使用 `console.log()` 方法在调试窗口上打印 JavaScript 值：

```javascript
a = 5;
b = 6;
c = a + b;
console.log(c);
```

## 设置断点

在调试窗口中，你可以设置 JavaScript 代码的断点。

在每个断点上，都会停止执行 JavaScript 代码，以便于我们检查 JavaScript 变量的值。

在检查完毕后，可以重新执行代码（如播放按钮）。

## debugger 关键字

**debugger** 关键字用于停止执行 JavaScript，并调用调试函数。

这个关键字与在调试工具中设置断点的效果是一样的。

如果没有调试可用，debugger 语句将无法工作。

开启 debugger ，代码在第三行前停止执行。

```javascript
var x = 15 * 5;
debugger;
document.getElementbyId("demo").innerHTML = x;
```

---

# JavaScript 变量提升

JavaScript 中，函数及变量的声明都将被提升到函数的最顶部。

JavaScript 中，变量可以在使用后声明，也就是变量可以先使用再声明。

以下两个实例将获得相同的结果：

### 实例 1

```javascript
x = 5; // 变量 x 设置为 5

elem = document.getElementById("demo"); // 查找元素
elem.innerHTML = x;                     // 在元素中显示 x

var x; // 声明 x
```

### 实例 2

```javascript
var x; // 声明 x
x = 5; // 变量 x 设置为 5

elem = document.getElementById("demo"); // 查找元素
elem.innerHTML = x;                     // 在元素中显示 x
```

要理解以上实例就需要理解 "hoisting(变量提升)"。

变量提升：函数声明和变量声明总是会被解释器悄悄地被"提升"到方法体的最顶部。

## JavaScript 初始化不会提升

JavaScript 只有声明的变量会提升，初始化的不会。

以下两个实例结果结果不相同：

```javascript
var x = 5; // 初始化 x
var y = 7; // 初始化 y

elem = document.getElementById("demo"); // 查找元素
elem.innerHTML = x + " " + y;           // 显示 x 和 y
```

```javascript
var x = 5; // 初始化 x

elem = document.getElementById("demo"); // 查找元素
elem.innerHTML = x + " " + y;           // 显示 x 和 y

var y = 7; // 初始化 y
```

实例 2 的 y 输出了 **undefined**，这是因为变量声明 (var y) 提升了，但是初始化(y = 7) 并不会提升，所以 y 变量是一个未定义的变量。

实例 2 类似以下代码:

```javascript
var x = 5; // 初始化 x
var y;     // 声明 y

elem = document.getElementById("demo"); // 查找元素
elem.innerHTML = x + " " + y;           // 显示 x 和 y

y = 7;    // 设置 y 为 7
```

## 在头部声明你的变量

对于大多数程序员来说并不知道 JavaScript 变量提升。

如果程序员不能很好的理解变量提升，他们写的程序就容易出现一些问题。

为了避免这些问题，通常我们在每个作用域开始前声明这些变量，这也是正常的 JavaScript 解析步骤，易于我们理解。

---

其实主要理解 js 的解析机制就行。

遇到 `script `标签的话 js 就进行预解析，将变量 `var `和 `function `声明提升，但不会执行 `function`，然后就进入上下文执行，上下文执行还是执行预解析同样操作，直到没有 `var `和 `function`，就开始执行上下文。如:

```javascript
a=5;
show();
var a;
function show(){};
```

预解析：

```javascript
function show(){};
var a;
a=5;
show();
```

需要注意都是函数声明提升直接把整个函数提到执行环境的最顶端。

---

除了以上的函数声明方式外，还可以使用匿名函数的方式。

声明：

```javascript
var 变量名称=function(形参列表){
  //函数体
}
```

调用：

```javascript
变量名称(实参列表)
```

**注意**：使用匿名函数的方式不存在函数提升，因为函数名称使用变量表示的，只存在变量提升。例：

```javascript
var getName=function(){
  console.log(2);
};

function getName(){
  console.log(1);
}

getName();
//结果为2
```

可能会有人觉得最后输出的结果是 1。但是 getName 是一个变量，因此这个变量的声明也将提升到顶部，而变量的赋值依然保留在原来的位置。需要注意的是，函数优先，虽然函数声明和变量声明都会被提升，但是函数会首先被提升，然后才是变量。

```javascript
//函数、变量声明提升后
function getName(){    //函数声明提升到顶部
  console.log(1);
}

var getName;    //变量声明提升
getName = function(){    //变量赋值依然保留在原来的位置
  console.log(2);
}

getName();    // 最终输出：2
```

---

# JavaScript 严格模式(use strict)

JavaScript 严格模式（strict mode）即在严格的条件下运行。

## 使用 "use strict" 指令

"use strict" 指令在 JavaScript 1.8.5 (ECMAScript5) 中新增。

它不是一条语句，但是是一个字面量表达式，在 JavaScript 旧版本中会被忽略。

"`use strict`" 的目的是指定代码在严格条件下执行。

严格模式下你不能使用未声明的变量。

## 严格模式声明

严格模式通过在脚本或函数的头部添加 "use strict"; 表达式来声明。

实例中我们可以在浏览器按下 **F12 (或点击"工具>更多工具>开发者工具")** 开启调试模式，查看报错信息。

```java
"use strict";
x = 3.14;       // 报错 (x 未定义)
```

```javascript
"use strict";
myFunction();

function myFunction() {
    y = 3.14;   // 报错 (y 未定义)
}
```

在函数内部声明是局部作用域 (只在函数内使用严格模式):

```javascript
x = 3.14;       // 不报错
myFunction();

function myFunction() {
   "use strict";
    y = 3.14;   // 报错 (y 未定义)
}
```

什么使用严格模式:

消除JavaScript语法的一些不合理、不严谨之处，减少一些怪异行为;

- 消除代码运行的一些不安全之处，保证代码运行的安全；
- 提高编译器效率，增加运行速度；
- 为未来新版本的Javascript做好铺垫。

"严格模式"体现了Javascript更合理、更安全、更严谨的发展方向，包括IE 10在内的主流浏览器，都已经支持它，许多大项目已经开始全面拥抱它。

另一方面，同样的代码，在"严格模式"中，可能会有不一样的运行结果；一些在"正常模式"下可以运行的语句，在"严格模式"下将不能运行。掌握这些内容，有助于更细致深入地理解Javascript，让你变成一个更好的程序员。

## 严格模式的限制

不允许使用未声明的变量：

```javascript
"use strict";
x = 3.14;                // 报错 (x 未定义)
```

```javascript
"use strict";
x = {p1:10, p2:20};      // 报错 (x 未定义)
```

不允许删除变量或对象。

```javascript
"use strict";
var x = 3.14;
delete x;                // 报错
```

不允许删除函数。

```javascript
"use strict";
function x(p1, p2) {};
delete x;                // 报错 
```

不允许变量重名:

```javascript
"use strict";
function x(p1, p1) {};   // 报错
```

不允许使用八进制:

```javascript
"use strict";
var x = 010;             // 报错
```

不允许使用转义字符:

```javascript
"use strict";
var x = \010;            // 报错
```

不允许对只读属性赋值:

```javascript
"use strict";
var obj = {};
Object.defineProperty(obj, "x", {value:0, writable:false});

obj.x = 3.14;            // 报错
```

不允许对一个使用getter方法读取的属性进行赋值

```javascript
"use strict";
var obj = {get x() {return 0} };

obj.x = 3.14;            // 报错
```

不允许删除一个不允许删除的属性：

```javascript
"use strict";
delete Object.prototype; // 报错
```

变量名不能使用 "`eval`" 字符串:

```javascript
"use strict";
var eval = 3.14;         // 报错
```

变量名不能使用 "`arguments`" 字符串:

```javascript
"use strict";
var arguments = 3.14;    // 报错
```

不允许使用以下这种语句:

```java
"use strict";
with (Math){x = cos(2)}; // 报错
```

由于一些安全原因，在作用域 `eval() `创建的变量不能被调用：

```javascript
"use strict";
eval ("var x = 2");
alert (x);               // 报错
```

禁止`this`关键字指向全局对象。

```javascript
function f(){
    return !this;
} 
// 返回false，因为"this"指向全局对象，"!this"就是false

function f(){ 
    "use strict";
    return !this;
} 
// 返回true，因为严格模式下，this的值为undefined，所以"!this"为true。
```

因此，使用构造函数时，如果忘了加new，this不再指向全局对象，而是报错。

```javascript
function f(){
    "use strict";
    this.a = 1;
};
f();// 报错，this未定义
```

## 保留关键字

为了向将来Javascript的新版本过渡，严格模式新增了一些保留关键字：

- `implements`
- `interface`
- `let`
- `package`
- `private`
- `protected`
- `public`
- `static`
- `yield`

```javascript
"use strict";
var public = 1500;      // 报错
```

---

# JavaScript 使用误区

本章节我们将讨论 JavaScript 的使用误区。

## 赋值运算符应用错误

在 JavaScript 程序中如果你在 if 条件语句中使用赋值运算符的等号 (=) 将会产生一个错误结果, 正确的方法是使用比较运算符的两个等号 (`===`)。

**if** 条件语句返回 **false** (是我们预期的)因为 x 不等于 10:

```html
<p id="demo"></p>
<script>
var x = 0;
document.getElementById("demo").innerHTML = Boolean(x===10);
</script>
```

```
false
```

**if** 条件语句返回 **true** (不是我们预期的)因为条件语句执行为 x 赋值 10，10 为 true:

```html
<p id="demo"></p>
<script>
var x = 0;
document.getElementById("demo").innerHTML = Boolean(x=10);
</script>
```

```
false
```

**if** 条件语句返回 **false** (不是我们预期的)因为条件语句执行为 x 赋值 0，0 为 false:

```html
<p id="demo"></p>
<script>
var x = 0;
document.getElementById("demo").innerHTML = Boolean(x=0);
</script>
```

```
false
```

## 比较运算符常见错误

在常规的比较中，数据类型是被忽略的，以下 `if `条件语句返回 true：

```javascript
var x = 10;
var y = "10";
if (x == y)
```

在严格的比较运算中，`===` 为恒等计算符，同时检查表达式的值与类型，以下 `if` 条件语句返回 `false`：

```javascript
var x = 10;
var y = "10";
if (x === y)
```

这种错误经常会在 `switch `语句中出现，`switch `语句会使用恒等计算符(`===`)进行比较:

以下实例会执行 `alert `弹窗：

```javascript
var x = 10;
switch(x) {
    case 10: alert("Hello");
}
```

以下实例由于类型不一致不会执行 `alert `弹窗：

```javascript
var x = 10;
switch(x) {
    case "10": alert("Hello");
}
```

## 加法与连接注意事项

**加法**是两个**数字**相加。

**连接**是两个**字符串**连接。

JavaScript 的加法和连接都使用 + 运算符。

接下来我们可以通过实例查看两个数字相加及数字与字符串连接的区别：

```javascript
var x = 10 + 5;          // x 的结果为 15
var x = 10 + "5";        // x 的结果为 "105"
```

使用变量相加结果也不一致:

```javascript
var x = 10;
var y = 5;
var z = x + y;           // z 的结果为 15

var x = 10;
var y = "5";
var z = x + y;           // z 的结果为 "105"
```

## 浮点型数据使用注意事项

JavaScript 中的所有数据都是以 64 位**浮点型数据(float)** 来存储。

所有的编程语言，包括 JavaScript，对浮点型数据的精确度都很难确定：

```javascript
var x = 0.1;
var y = 0.2;
var z = x + y            // z 的结果为 0.30000000000000004
if (z == 0.3)            // 返回 false
```

为解决以上问题，可以用整数的乘除法来解决：

```javascript
var z = (x * 10 + y * 10) / 10;       // z 的结果为 0.3
```

## JavaScript 字符串分行

JavaScript 允许我们在字符串中使用断行语句:

```javascript
var x =
"Hello World!";
```

但是，在字符串中直接使用回车换行是会报错的：

```javascript
var x = "Hello
World!";
```

字符串断行需要使用反斜杠(`\`)，如下所示:

```javascript
var x = "Hello \
World!";
```

## 错误的使用分号

以下实例中，if 语句失去方法体，原 if 语句的方法体作为独立的代码块被执行，导致错误的输出结果。

由于分号使用错误，if 语句中的代码块就一定会执行：

```javascript
if (x == 19);
{
    // code block 
}
```

## return 语句使用注意事项

JavaScript 默认是在代码的最后一行自动结束。

以下两个实例返回结果是一样的(一个有分号一个没有):

```javascript
function myFunction(a) {
    var power = 10 
    return a * power
}
```

```javascript
function myFunction(a) {
    var power = 10;
    return a * power;
}
```

JavaScript 也可以使用多行来结束一个语句。

以下实例返回相同的结果:

```javascript
unction myFunction(a) {
    var
    power = 10; 
    return a * power;
}
```

但是，以下实例结果会返回 **undefined**：

```javascript
function myFunction(a) {
    var
    power = 10; 
    return
    a * power;
}
```

为什么会有这样的结果呢？因为在 JavaScript 中，实例 4 的代码与下面的代码一致：

```javascript
function myFunction(a) {
    var
    power = 10;  
    return;       // 分号结束，返回 undefined
    a * power;
```

### 解析

如果是一个不完整的语句，如下所示:

```javascript
var
```

JavaScript 将尝试读取第二行的语句：

```javascript
power = 10;
```

但是由于这样的语句是完整的:

```java
return
```

JavaScript 将自动关闭语句:

```java
return;
```

在 JavaScript 中，分号是可选的 。

由于 return 是一个完整的语句，所以 JavaScript 将关闭 return 语句。

## 数组中使用名字来索引

许多程序语言都允许使用名字来作为数组的索引。

使用名字来作为索引的数组称为关联数组(或哈希)。

JavaScript 不支持使用名字来索引数组，只允许使用数字索引。

```javascript
var person = [];
person[0] = "John";
person[1] = "Doe";
person[2] = 46;
var x = person.length;         // person.length 返回 3
var y = person[0];             // person[0] 返回 "John"
```

在 JavaScript 中, **对象** 使用 **名字作为索引**。

如果你使用名字作为索引，当访问数组时，JavaScript 会把数组重新定义为标准对象。

执行这样操作后，数组的方法及属性将不能再使用，否则会产生错误:

```javascript
var person = [];
person["firstName"] = "John";
person["lastName"] = "Doe";
person["age"] = 46;
var x = person.length;         // person.length 返回 0
var y = person[0];             // person[0] 返回 undefined
```

## 定义数组元素，最后不能添加逗号

数组最后一个值的后面添加逗号虽然语法没有问题，但是在不同的浏览器可能得到不同的结果。

```java
var colors = [5, 6, 7,]; //这样数组的长度可能为3 也可能为4。
```

正确的定义方式：

```java
points = [40, 100, 1, 5, 25, 10];
```

## 定义对象，最后不能添加逗号

错误的定义方式：

```java
websites = {site:"菜鸟教程", url:"www.runoob.com", like:460,}
```

正确的定义方式：

```javascript
websites = {site:"菜鸟教程", url:"www.runoob.com", like:460}
```

## Undefined 不是 Null

在 JavaScript 中, **null** 用于对象, **undefined** 用于变量，属性和方法。

对象只有被定义才有可能为 `null`，否则为 `undefined`。

如果我们想测试对象是否存在，在对象还没定义时将会抛出一个错误。

错误的使用方式：

```javascript
if (myObj !== null && typeof myObj !== "undefined") 
```

正确的方式是我们需要先使用 typeof 来检测对象是否已定义：

```javascript
if (typeof myObj !== "undefined" && myObj !== null) 
```

## 程序块作用域

在每个代码块中 JavaScript 不会创建一个新的作用域，一般各个代码块的作用域都是全局的。

以下代码的的变量 `i` 返回 `10`，而不是 `undefined`：

```javascript
for (var i = 0; i < 10; i++) {
    // some code
}
return i;
```

---

# JavaScript 表单

## JavaScript 表单验证

HTML 表单验证可以通过 JavaScript 来完成。

以下实例代码用于判断表单字段(fname)值是否存在， 如果不存在，就弹出信息，阻止表单提交：

```html
<form name="myForm" action="https://www.runoob.com/try/demo_source/demo_form.php" onsubmit="return validateForm()" method="post">
    <label>名字:
        <input type="text" name="fname">
        <input type="submit" value="提交">
    </label>
</form>
<script>
function validateForm() {
    var x = document.forms["myForm"]["fname"].value;
    if (x==null || x==="") {
        alert("需要输入名字");
        return false;
    }
}
</script>
```

## JavaScript 验证输入的数字

JavaScript 常用于对输入数字的验证：

```html
<p>请输入 1 到 10 之间的数字：</p>
<label>
    <input id="numb">
    <button type="button" onclick="myFunction()">提交</button>
</label>
<p id="demo"></p>
<script>
function myFunction() {
    var x, text;
    x = document.getElementById("numb").value;
    if (isNaN(x) || x<1 || x>10) {
        text = "输入错误";
    } else {
        text = "输入正确";
    }
    document.getElementById("demo").innerHTML=text;
}
</script>
```

## HTML 表单自动验证

HTML 表单验证也可以通过浏览器来自动完成。

如果表单字段 (*fname*) 的值为空, **required** 属性会阻止表单提交：

```html
<form action="https://www.runoob.com/try/demo_source/demo_form.php" method="post">
    <label>
        <input type="text" name="fname" required="required">
        <input type="submit" value="提交">
    </label>
</form>
```

## 数据验证

数据验证用于确保用户输入的数据是有效的。

典型的数据验证有：

- 必需字段是否有输入?
- 用户是否输入了合法的数据?
- 在数字字段是否输入了文本?

大多数情况下，数据验证用于确保用户正确输入数据。

数据验证可以使用不同方法来定义，并通过多种方式来调用。

**服务端数据验证**是在数据提交到服务器上后再验证。

**客户端数据验证**是在数据发送到服务器前，在浏览器上完成验证。

## HTML 约束验证

HTML5 新增了 HTML 表单的验证方式：约束验证（constraint validation）。

约束验证是表单被提交时浏览器用来实现验证的一种算法。

HTML 约束验证基于：

- **HTML 输入属性**
- **CSS 伪类选择器**
- **DOM 属性和方法**

### 约束验证 HTML 输入属性

| 属性       | 描述                     |
| :--------- | :----------------------- |
| `disabled` | 规定输入的元素不可用     |
| `max`      | 规定输入元素的最大值     |
| `min`      | 规定输入元素的最小值     |
| `pattern`  | 规定输入元素值的模式     |
| `required` | 规定输入元素字段是必需的 |
| `type `    | 规定输入元素的类型       |

### 约束验证 CSS 伪类选择器

| 选择器      | 描述                                    |
| :---------- | :-------------------------------------- |
| `:disabled` | 选取属性为 "disabled" 属性的 input 元素 |
| `:invalid`  | 选取无效的 input 元素                   |
| `:optional` | 选择没有"required"属性的 input 元素     |
| `:required` | 选择有"required"属性的 input 元素       |
| `:valid`    | 选取有效值的 input 元素                 |

---

# JavaScript 表单验证

## JavaScript 表单验证

JavaScript 可用来在数据被送往服务器前对 HTML 表单中的这些输入数据进行验证。

表单数据经常需要使用 JavaScript 来验证其正确性：

- 验证表单数据是否为空？
- 验证输入是否是一个正确的email地址？
- 验证日期是否输入正确？
- 验证表单输入内容是否为数字型？

## 必填（或必选）项目

下面的函数用来检查用户是否已填写表单中的必填（或必选）项目。假如必填或必选项为空，那么警告框会弹出，并且函数的返回值为 false，否则函数的返回值则为 true（意味着数据没有问题）：

```html
<form action="https://www.runoob.com/try/demo_source/demo_form.php"
      onsubmit="validateForm()" method="post">
    <label>姓:
        <input type="text" name="fname" required="required">
        <input type="submit" value="提交">
    </label>
</form>
<script>
function validateForm() {
    var x = document.forms["myForm"]["fname"].value;
    if (x==null ||x==="") {
        alert("姓必须填写");
        return false;
    }
}
</script>
```

## E-mail 验证

下面的函数检查输入的数据是否符合电子邮件地址的基本语法。

意思就是说，输入的数据必须包含 @ 符号和点号(.)。同时，@ 不可以是邮件地址的首字符，并且 @ 之后需有至少一个点号：

```html
<form action="https://www.runoob.com/try/demo_source/demo_form.php"
      onsubmit="validateForm()" method="post">
    <label>Email: 
        <input type="text" name="email" required="required">
        <input type="submit" value="提交">
    </label>
</form>
<script>
function validateForm() {
    var x = document.forms["myForm"]["email"].value;
    var atpos = x.indexOf("@");
    var dotpos = x.lastIndexOf(".");
    if (atpos<1 || dotpos<atpos+2 ||dotpos+2>=x.length) {
        alert("不是一个有效的 e-mail 地址");
        return false;
    }
}
</script>
```

---

# JavaScript 验证 API

## 约束验证 DOM 方法

| Property              | Description                                                  |
| :-------------------- | :----------------------------------------------------------- |
| `checkValidity()`     | 如果 `input `元素中的数据是合法的返回 `true`，否则返回 false。 |
| `setCustomValidity()` | 设置 `input `元素的 *validationMessage* 属性，用于自定义错误提示信息的方法。使用 *setCustomValidity* 设置了自定义提示后，`validity.customError` 就会变成true，则 checkValidity 总是会返回false。如果要重新判断需要取消自定义提示，方式如下： |

```javascript
setCustomValidity('') 
setCustomValidity(null) 
setCustomValidity(undefined)
```

以下实例如果输入信息不合法，则返回错误信息：

```html
<p>输入数字并点击验证按钮:</p>
<label>
    <input id="id1" type="number" min="100" max="300" required="required">
    <button onclick="myFunction()">验证</button>
</label>
<p>如果输入的数字小于 100 或大于300，会提示错误信息。</p>
<p id="demo"></p>
<script>
function myFunction() {
    var obj = document.getElementById("id1");
    if (obj.checkValidity()===false) {
        document.getElementById("demo").innerHTML = obj.validationMessage;
    } else {
        document.getElementById("demo").innerHTML = "输入正确"
    }
}
</script>
```

## 约束验证 DOM 属性

| 属性                | 描述                                    |
| :------------------ | :-------------------------------------- |
| `validity`          | 布尔属性值，返回 *input* 输入值是否合法 |
| `validationMessage` | 浏览器错误提示信息                      |
| `willValidate`      | 指定 *input* 是否需要验证               |

------

## Validity 属性

*input* 元素的 **validity 属性**包含一系列关于 `validity `数据属性:

| 属性              | 描述                                                         |
| :---------------- | :----------------------------------------------------------- |
| customError       | 设置为 true, 如果设置了自定义的 validity 信息。              |
| `patternMismatch` | 设置为 true, 如果元素的值不匹配它的模式属性。                |
| `rangeOverflow`   | 设置为 true, 如果元素的值大于设置的最大值。                  |
| `rangeUnderflow`  | 设置为 true, 如果元素的值小于它的最小值。                    |
| `stepMismatch`    | 设置为 true, 如果元素的值不是按照规定的 *step* 属性设置。    |
| `tooLong`         | 设置为 true, 如果元素的值超过了 *maxLength* 属性设置的长度。 |
| `typeMismatch`    | 设置为 true, 如果元素的值不是预期相匹配的类型。              |
| `valueMissing`    | 设置为 true，如果元素 (*required* 属性) 没有值。             |
| `valid`           | 设置为 true，如果元素的值是合法的。                          |

如果输入的值大于 100，显示一个信息：

```html
<label>
    <input id="id1" type="number" max="100">
    <button onclick="myFunction()">验证</button>
</label>
<p id="demo"></p>
<script>
function myFunction() {
    var txt = "输入正确";
    if (document.getElementById("id1").validity.rangeOverflow) {
         txt = "输入的值太大了";
    }
    document.getElementById("demo").innerHTML = txt;
}
</script>
```

如果输入的值小于 100，显示一个信息：

```html
<label>
    <input id="id1" type="number" min="100" required>
    <button onclick="myFunction()">验证</button>
</label>
<p>如果输入的数字小于 100 ( input 的 min 属性), 会显示错误信息。</p>
<p id="demo"></p>
<script>
function myFunction() {
    var txt = "";
	var inpObj = document.getElementById("id1");
	if(isNumeric(inpObj.value)) {
		txt = "你输入的不是数字";
	} else if (inpObj.validity.rangeUnderflow) {
        txt = "输入的值太小了";
    } else {
        txt = "输入正确";
    }
    document.getElementById("demo").innerHTML = txt;
}
// 判断输入是否为数字
function isNumeric(n) {
    return isNaN(parseFloat(n)) && !isFinite(n);
}
</script>
```

---

**约束验证中setCustomValidity自定义错误信息的使用**

```html
<p>输入数字并点击验证按钮:</p>
<label>
	<input id="id1" type="number" min="100" max="300" required>
	<button onclick="myFunction()">验证</button>
</label>
<p>如果输入的数字小于 100 或大于300，会提示错误信息。</p>
<p id="demo"></p>
```

```javascript
function myFunction() {
   var inpObj = document.getElementById("id1");
    inpObj.setCustomValidity(''); // 取消自定义提示的方式，，否则下次点击checkValidity总返false
    if (!inpObj.checkValidity()) {
        if(inpObj.value===""){
            inpObj.setCustomValidity("不能为空！");
        }else if(inpObj.value<100 || inpObj.value>300){
            inpObj.setCustomValidity("请重新输入数值（100~300之间）!");
        }
        document.getElementById("demo").innerHTML = inpObj.validationMessage;
    } else {
        document.getElementById("demo").innerHTML = "输入正确";
}
}
```

---

# JavaScript 保留关键字

在 JavaScript 中，一些标识符是保留关键字，不能用作变量名或函数名。

## JavaScript 标准

所有的现代浏览器完全支持 ECMAScript 3（ES3，JavaScript 的第三版，从 1999 年开始）。

ECMAScript 4（ES4）未通过。

ECMAScript 5（ES5，2009 年发布），是 JavaScript 最新的官方版本。

随着时间的推移，我们开始看到，所有的现代浏览器已经完全支持 ES5。

## JavaScript 保留关键字

Javascript 的保留关键字不可以用作变量、标签或者函数名。有些保留关键字是作为 Javascript 以后扩展使用。

<table class="reference"><tbody><tr>
<td>abstract</td>
<td>arguments</td>
<td>boolean</td>
<td>break</td>
<td>byte</td>
</tr>
<tr>
<td>case</td>
<td>catch</td>
<td>char</td>
<td>class*</td>
<td>const</td>
</tr>
<tr>
<td>continue</td>
<td>debugger</td>
<td>default</td>
<td>delete</td>
<td>do</td>
</tr>
<tr>
<td>double</td>
<td>else</td>
<td>enum*</td>
<td>eval</td>
<td>export*</td>
</tr>
<tr>
<td>extends*</td>
<td>false</td>
<td>final</td>
<td>finally</td>
<td>float</td>
</tr>
<tr>
<td>for</td>
<td>function</td>
<td>goto</td>
<td>if</td>
<td>implements</td>
</tr>
<tr>
<td>import*</td>
<td>in</td>
<td>instanceof</td>
<td>int</td>
<td>interface</td>
</tr>
<tr>
<td>let</td>
<td>long</td>
<td>native</td>
<td>new</td>
<td>null</td>
</tr>
<tr>
<td>package</td>
<td>private</td>
<td>protected</td>
<td>public</td>
<td>return</td>
</tr>
<tr>
<td>short</td>
<td>static</td>
<td>super*</td>
<td>switch</td>
<td>synchronized</td>
</tr>
<tr>
<td>this</td>
<td>throw</td>
<td>throws</td>
<td>transient</td>
<td>true</td>
</tr>
<tr>
<td>try</td>
<td>typeof</td>
<td>var</td>
<td>void</td>
<td>volatile</td>
</tr>
<tr>
<td>while</td>
<td>with</td>
<td>yield</td>
<td></td>
<td></td>
</tr>
</tbody></table>

\* 标记的关键字是 ECMAScript5 中新添加的。

## JavaScript 对象、属性和方法

您也应该避免使用 JavaScript 内置的对象、属性和方法的名称作为 Javascript 的变量或函数名：

<table class="reference">
<tbody><tr>
<td>Array</td>
<td>Date</td>
<td>eval</td>
<td>function</td>
<td>hasOwnProperty</td>
</tr>
<tr>
<td>Infinity</td>
<td>isFinite</td>
<td>isNaN</td>
<td>isPrototypeOf</td>
<td>length</td>
</tr>
<tr>
<td>Math</td>
<td>NaN</td>
<td>name</td>
<td>Number</td>
<td>Object</td>
</tr>
<tr>
<td>prototype</td>
<td>String</td>
<td>toString</td>
<td>undefined</td>
<td>valueOf</td>
</tr>
</tbody></table>

## Java 保留关键字

JavaScript 经常与 Java 一起使用。您应该避免使用一些 Java 对象和属性作为 JavaScript 标识符：

<table class="reference">
<tbody><tr>
<td>getClass</td>
<td>java</td>
<td>JavaArray</td>
<td>javaClass</td>
<td>JavaObject</td>
<td>JavaPackage</td>
</tr>
</tbody></table>

## Windows 保留关键字

JavaScript 可以在 HTML 外部使用。它可在许多其他应用程序中作为编程语言使用。

在 HTML 中，您必须（为了可移植性，您也应该这么做）避免使用 HTML 和 Windows 对象和属性的名称作为 Javascript 的变量及函数名：

<table class="reference">
<tbody><tr>
<td>alert</td>
<td>all</td>
<td>anchor</td>
<td>anchors</td>
<td>area</td>
</tr>
<tr>
<td>assign</td>
<td>blur</td>
<td>button</td>
<td>checkbox</td>
<td>clearInterval</td>
</tr>
<tr>
<td>clearTimeout</td>
<td>clientInformation</td>
<td>close</td>
<td>closed</td>
<td>confirm</td>
</tr>
<tr>
<td>constructor</td>
<td>crypto</td>
<td>decodeURI</td>
<td>decodeURIComponent</td>
<td>defaultStatus</td>
</tr>
<tr>
<td>document</td>
<td>element</td>
<td>elements</td>
<td>embed</td>
<td>embeds</td>
</tr>
<tr>
<td>encodeURI</td>
<td>encodeURIComponent</td>
<td>escape</td>
<td>event</td>
<td>fileUpload</td>
</tr>
<tr>
<td>focus</td>
<td>form</td>
<td>forms</td>
<td>frame</td>
<td>innerHeight</td>
</tr>
<tr>
<td>innerWidth</td>
<td>layer</td>
<td>layers</td>
<td>link</td>
<td>location</td>
</tr>
<tr>
<td>mimeTypes</td>
<td>navigate</td>
<td>navigator</td>
<td>frames</td>
<td>frameRate</td>
</tr>
<tr>
<td>hidden</td>
<td>history</td>
<td>image</td>
<td>images</td>
<td>offscreenBuffering</td>
</tr>
<tr>
<td>open</td>
<td>opener</td>
<td>option</td>
<td>outerHeight</td>
<td>outerWidth</td>
</tr>
<tr>
<td>packages</td>
<td>pageXOffset</td>
<td>pageYOffset</td>
<td>parent</td>
<td>parseFloat</td>
</tr>
<tr>
<td>parseInt</td>
<td>password</td>
<td>pkcs11</td>
<td>plugin</td>
<td>prompt</td>
</tr>
<tr>
<td>propertyIsEnum</td>
<td>radio</td>
<td>reset</td>
<td>screenX</td>
<td>screenY</td>
</tr>
<tr>
<td>scroll</td>
<td>secure</td>
<td>select</td>
<td>self</td>
<td>setInterval</td>
</tr>
<tr>
<td>setTimeout</td>
<td>status</td>
<td>submit</td>
<td>taint</td>
<td>text</td>
</tr>
<tr>
<td>textarea</td>
<td>top</td>
<td>unescape</td>
<td>untaint</td>
<td>window</td>
</tr>
</tbody></table>

## HTML 事件句柄

除此之外，您还应该避免使用 HTML 事件句柄的名称作为 Javascript 的变量及函数名。

实例：

<table class="reference">
<tbody><tr>
<td>onblur</td>
<td>onclick</td>
<td>onerror</td>
<td>onfocus</td>
</tr>
<tr>
<td>onkeydown</td>
<td>onkeypress</td>
<td>onkeyup</td>
<td>onmouseover</td>
</tr>
<tr>
<td>onload</td>
<td>onmouseup</td>
<td>onmousedown</td>
<td>onsubmit</td>
</tr><tr>
</tr></tbody></table>

## 非标准 JavaScript

除了保留关键字，在 JavaScript 实现中也有一些非标准的关键字。

一个实例是 **const** 关键字，用于定义变量。 一些 JavaScript 引擎把 const 当作 var 的同义词。另一些引擎则把 const 当作只读变量的定义。

Const 是 JavaScript 的扩展。JavaScript 引擎支持它用在 Firefox 和 Chrome 中。但是它并不是 JavaScript 标准 ES3 或 ES5 的组成部分。**建议：不要使用它**。