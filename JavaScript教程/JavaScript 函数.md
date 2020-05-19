# JavaScript 函数定义

JavaScript 使用关键字 **function** 定义函数。

函数可以通过声明定义，也可以是一个表达式。

## 函数声明

在之前的教程中，你已经了解了函数声明的语法 :

```javascript
function functionName(parameters) {
  执行的代码
}
```

函数声明后不会立即执行，会在我们需要的时候调用到。

```javascript
function myFunction(a, b) {
    return a * b;
}
```

## 函数表达式

JavaScript 函数可以通过一个表达式定义。

函数表达式可以存储在变量中：

```javascript
var x = function (a, b) {return a * b};
```

在函数表达式存储在变量后，变量也可作为一个函数使用：

```javascript
var x = function (a, b) {return a * b};
var z = x(4, 3);
```

以上函数实际上是一个 **匿名函数** (函数没有名称)。

函数存储在变量中，不需要函数名称，通常通过变量名来调用。

## Function() 构造函数

在以上实例中，我们了解到函数通过关键字 **function** 定义。

函数同样可以通过内置的 JavaScript 函数构造器（`Function()`）定义。

```javascript
var myFunction = new Function("a", "b", "return a * b");
var x = myFunction(4, 3);
```

实际上，你不必使用构造函数。上面实例可以写成：

```javascript
var myFunction = function (a, b) {return a * b};
var x = myFunction(4, 3);
```

## 函数提升（Hoisting）

在之前的教程中我们已经了解了 "hoisting(提升)"。

提升（Hoisting）是 JavaScript 默认将当前作用域提升到前面去的的行为。

提升（Hoisting）应用在变量的声明与函数的声明。

因此，函数可以在声明之前调用：

```javascript
myFunction(5);

function myFunction(y) {
    return y * y;
}
```

使用表达式定义函数时无法提升。

## 自调用函数

函数表达式可以 "自调用"。

自调用表达式会自动调用。

如果表达式后面紧跟 `() `，则会自动调用。

不能自调用声明的函数。

通过添加括号，来说明它是一个函数表达式：

```javascript
(function () {
    var x = "Hello!!";      // 我将调用自己
})();
```

以上函数实际上是一个 **匿名自我调用的函数** (没有函数名)。

## 函数可作为一个值使用

JavaScript 函数作为一个值使用：

```javascript
function myFunction(a, b) {
    return a * b;
}

var x = myFunction(4, 3);
```

JavaScript 函数可作为表达式使用：

```javascript
function myFunction(a, b) {
    return a * b;
}

var x = myFunction(4, 3) * 2;
```

## 函数是对象

在 JavaScript 中使用 **typeof** 操作符判断函数类型将返回 "function" 。

但是JavaScript 函数描述为一个对象更加准确。

JavaScript 函数有 **属性** 和 **方法**。

`arguments.length` 属性返回函数调用过程接收到的参数个数：

```javascript
function myFunction(a, b) {
    return arguments.length;
}
```

`toString() `方法将函数作为一个字符串返回:

```javascript
function myFunction(a, b) {
    return a * b;
}

var txt = myFunction.toString();
```

## 箭头函数

ES6 新增了箭头函数。

箭头函数表达式的语法比普通函数表达式更简洁。

```javascript
(参数1, 参数2, …, 参数N) => { 函数声明 }

(参数1, 参数2, …, 参数N) => 表达式(单一)
// 相当于：(参数1, 参数2, …, 参数N) =>{ return 表达式; }
```

当只有一个参数时，圆括号是可选的：

```javascript
(单一参数) => {函数声明}
单一参数 => {函数声明}
```

没有参数的函数应该写成一对圆括号:

```javascript
() => {函数声明}
```

```javascript
// ES5
var x = function(x, y) {
     return x * y;
}

// ES6
const x = (x, y) => x * y;
```

有的箭头函数都没有自己的 **this**。 不适合定义一个 **对象的方法**。

当我们使用箭头函数的时候，箭头函数会默认帮我们绑定外层 this 的值，所以在箭头函数中 this 的值和外层的 this 是一样的。

箭头函数是不能提升的，所以需要在使用之前定义。

使用 **const** 比使用 **var** 更安全，因为函数表达式始终是一个常量。

如果函数部分只是一个语句，则可以省略 `return `关键字和大括号 `{}`，这样做是一个比较好的习惯:

```javascript
const x = (x, y) => { return x * y };
```

---

匿名函数自动调用表达式：

```javascript
(function(){})()
```

例如：

```html
<p id="demo"></p>

<script>
(function(){document.getElementById("demo").innerHTML = "hello kity";})()
</script>
```

---

ES6 里自调用可以写成箭头函数形式。

匿名自调用表达式:

```javascript
(()=>{})()
```

---

对于函数自调用，必须通过把函数表达式外面添加括号(来说明它是一个函数表达式)再调用，否则会报错，如下实例:

```javascript
function () { document.write( "Hello! 我是自己调用的" );}();
// 报错：Uncaught SyntaxError: Unexpected token (
```

正确写法：

```javascript
(function () { document.write( "Hello! 我是自己调用的" );})();
```

现在我们知道函数表达式后面紧跟 **()** 会自动调用，但是如果把函数表达式赋给一个变量则不需要添加括号也可以直接调用，下方的代码中，函数表达式的主体部分会执行，并且会返回一个字符串给 **a**:

```javascript
var a = function () {
    document.write("Hello! 我是自己调用的" + "<br />");
    return '返回的东西';
}();

document.write(a);
```

---

# JavaScript 函数参数

JavaScript 函数对参数的值没有进行任何的检查。

## 函数显式参数(Parameters)与隐式参数(Arguments)

在先前的教程中，我们已经学习了函数的显式参数:

```javascript
functionName(parameter1, parameter2, parameter3) {
    // 要执行的代码……
}
```

函数显式参数在函数定义时列出。

函数隐式参数在函数调用时传递给函数真正的值。

## 参数规则

JavaScript 函数定义显式参数时没有指定数据类型。

JavaScript 函数对隐式参数没有进行类型检测。

JavaScript 函数对隐式参数的个数没有进行检测。

## 默认参数

ES5 中如果函数在调用时未提供隐式参数，参数会默认设置为： **undefined**

有时这是可以接受的，但是建议最好为参数设置一个默认值：

```java
function myFunction(x, y) {
    if (y === undefined) {
          y = 0;
    } 
}
```

或者，更简单的方式：

```javascript
function myFunction(x, y) {
    y = y || 0;
}
```

### ES6 函数可以自带参数

ES6 支持函数带有默认参数，就判断 `undefined `和 `|| `的操作：

```javascript
function myFunction(x, y = 10) {
    // y is 10 if not passed or undefined
    return x + y;
}

myFunction(0, 2) // 输出 2
myFunction(5); // 输出 15, y 参数的默认值
```

## arguments 对象

JavaScript 函数有个内置的对象 `arguments `对象。

`argument `对象包含了函数调用的参数数组。

通过这种方式你可以很方便的找到最大的一个参数的值：

```javascript
x = findMax(1, 123, 500, 115, 44, 88);

function findMax() {
    var i, max = arguments[0];
    if (arguments.length<2) return max;
    for (i=0; i<arguments.length; i++) {
        if (arguments[i]>max) {
            max = arguments[i];
        }
    }
    return max;
}
```

或者创建一个函数用来统计所有数值的和：

```javascript
x = sumAll(1, 123, 500, 115, 44, 88);

function sumAll() {
    var i, sum = 0;
    for (i = 0; i < arguments.length; i++) {
        sum += arguments[i];
    }
    return sum;
}
```

## 通过值传递参数

在函数中调用的参数是函数的隐式参数。

JavaScript 隐式参数通过值来传递：函数仅仅只是获取值。

如果函数修改参数的值，不会修改显式参数的初始值（在函数外定义）。

隐式参数的改变在函数外是不可见的。

## 通过对象传递参数

在JavaScript中，可以引用对象的值。

因此我们在函数内部修改对象的属性就会修改其初始的值。

修改对象属性可作用于函数外部（全局变量）。

修改对象属性在函数外是可见的。

---

# JavaScript 函数调用

JavaScript 函数有 4 种调用方式。

每种方式的不同在于 **this** 的初始化。

## ***this*** 关键字

一般而言，在Javascript中，this指向函数执行时的当前对象。

## 调用 JavaScript 函数

在之前的章节中我们已经学会了如何创建函数。

函数中的代码在函数被调用后执行。

## 作为一个函数调用

```javascript
function myFunction(a, b) {
    return a * b;
}
myFunction(10, 2);           // myFunction(10, 2) 返回 20
```

以上函数不属于任何对象。但是在 JavaScript 中它始终是默认的全局对象。

在 HTML 中默认的全局对象是 HTML 页面本身，所以函数是属于 HTML 页面。

在浏览器中的页面对象是浏览器窗口(window 对象)。以上函数会自动变为 window 对象的函数。

`myFunction()` 和 `window.myFunction()` 是一样的：

```javascript
function myFunction(a, b) {
    return a * b;
}
window.myFunction(10, 2);    // window.myFunction(10, 2) 返回 20
```

## 全局对象

当函数没有被自身的对象调用时 **this** 的值就会变成全局对象。

在 web 浏览器中全局对象是浏览器窗口（window 对象）。

该实例返回 **this** 的值是 window 对象:

```javascript
function myFunction() {
    return this;
}
myFunction();                // 返回 window 对象
```

## 函数作为方法调用

在 JavaScript 中你可以将函数定义为对象的方法。

以下实例创建了一个对象 (**myObject**), 对象有两个属性 (**firstName** 和 **lastName**), 及一个方法 (**fullName**):

```javascript
var myObject = {
    firstName:"John",
    lastName: "Doe",
    fullName: function () {
        return this.firstName + " " + this.lastName;
    }
}
myObject.fullName();         // 返回 "John Doe"
```

**fullName** 方法是一个函数。函数属于对象。 **myObject** 是函数的所有者。

**this**对象，拥有 JavaScript 代码。实例中 **this** 的值为 **myObject** 对象。

测试以下！修改 **fullName** 方法并返回 **this** 值:

```javascript
var myObject = {
    firstName:"John",
    lastName: "Doe",
    fullName: function () {
        return this;
    }
}
myObject.fullName();          // 返回 [object Object] (所有者对象)
```

## 使用构造函数调用函数

如果函数调用前使用了 **new** 关键字, 则是调用了构造函数。

这看起来就像创建了新的函数，但实际上 JavaScript 函数是重新创建的对象：

```javascript
// 构造函数:
function myFunction(arg1, arg2) {
    this.firstName = arg1;
    this.lastName  = arg2;
}

// This    creates a new object
var x = new myFunction("John","Doe");
x.firstName;                             // 返回 "John"
```

## 作为函数方法调用函数

在 JavaScript 中, 函数是对象。JavaScript 函数有它的属性和方法。

**call()** 和 **apply()** 是预定义的函数方法。 两个方法可用于调用函数，两个方法的第一个参数必须是对象本身。

```javascript
function myFunction(a, b) {
    return a * b;
}
myObject = myFunction.call(myObject, 10, 2);     // 返回 20
```

```javascript
function myFunction(a, b) {
    return a * b;
}
myArray = [10, 2];
myObject = myFunction.apply(myObject, myArray);  // 返回 20
```

两个方法都使用了对象本身作为第一个参数。 两者的区别在于第二个参数： `apply`传入的是一个**参数数组**，也就是将**多个参数**组合成为一个数组传入，而`call`则作为`call`的参数传入（从第二个参数开始）。

在 JavaScript 严格模式`(strict mode`)下, 在调用函数时第一个参数会成为 **this** 的值， 即使该参数不是一个对象。

在 JavaScript 非严格模式(non-strict mode)下, 如果第一个参数的值是 null 或 undefined, 它将使用全局对象替代。

---

`this `是 JavaScript 语言的一个关键字。

它代表函数运行时，自动生成的一个内部对象，只能在函数内部使用。比如：

```javascript
function test() {
    this.x = 1;
}
```

随着函数使用场合的不同，this 的值会发生变化。但是有一个总的原则，那就是this指的是，调用函数的那个对象。

---

# JavaScript 闭包

JavaScript 变量可以是局部变量或全局变量。

私有变量可以用到闭包。

## 全局变量

函数可以访问由函数内部定义的变量，如：

```javascript
function myFunction() {
    var a = 4;
    return a * a;
}
```

函数也可以访问函数外部定义的变量，如：

```javascript
var a = 4;
function myFunction() {
    return a * a;
}
```

后面一个实例中， **a** 是一个 **全局** 变量。

在web页面中全局变量属于 window 对象。

全局变量可应用于页面上的所有脚本。

在第一个实例中， **a** 是一个 **局部** 变量。

局部变量只能用于定义它函数内部。对于其他的函数或脚本代码是不可用的。

全局和局部变量即便名称相同，它们也是两个不同的变量。修改其中一个，不会影响另一个的值。

## 变量生命周期

全局变量的作用域是全局性的，即在整个JavaScript程序中，全局变量处处都在。

而在函数内部声明的变量，只在函数内部起作用。这些变量是局部变量，作用域是局部性的；函数的参数也是局部性的，只在函数内部起作用。

## 计数器困境

设想下如果你想统计一些数值，且该计数器在所有函数中都是可用的。

你可以使用全局变量，函数设置计数器递增：

```javascript
var counter = 0;

function add() {
   return counter += 1;
}

add();
add();
add();

// 计数器现在为 3
```

计数器数值在执行 add() 函数时发生变化。

但问题来了，页面上的任何脚本都能改变计数器，即便没有调用 add() 函数。

如果我在函数内声明计数器，如果没有调用函数将无法修改计数器的值：

```javascript
function add() {
    var counter = 0;
    return counter += 1;
}

add();
add();
add();

// 本意是想输出 3, 但事与愿违，输出的都是 1 !
```

以上代码将无法正确输出，每次我调用 add() 函数，计数器都会设置为 1。

**JavaScript 内嵌函数可以解决该问题。**

## JavaScript 内嵌函数

所有函数都能访问全局变量。 

实际上，在 JavaScript 中，所有函数都能访问它们上一层的作用域。

JavaScript 支持嵌套函数。嵌套函数可以访问上一层的函数变量。

该实例中，内嵌函数 **plus()** 可以访问父函数的 **counter** 变量：

```javascript
function add() {
    var counter = 0;
    function plus() {counter += 1;}
    plus();    
    return counter; 
}
```

如果我们能在外部访问 **plus()** 函数，这样就能解决计数器的困境。

我们同样需要确保 **counter = 0** 只执行一次。

**我们需要闭包。**

## JavaScript 闭包

还记得函数自我调用吗？该函数会做什么？

```javascript
var add = (function () {
    var counter = 0;
    return function () {return counter += 1;}
})();

add();
add();
add();

// 计数器为 3
```

## 实例解析

变量 **add** 指定了函数自我调用的返回字值。

自我调用函数只执行一次。设置计数器为 0。并返回函数表达式。

add变量可以作为一个函数使用。非常棒的部分是它可以访问函数上一层作用域的计数器。

这个叫作 JavaScript **闭包。**它使得函数拥有私有变量变成可能。

计数器受匿名函数的作用域保护，只能通过 add 方法修改。