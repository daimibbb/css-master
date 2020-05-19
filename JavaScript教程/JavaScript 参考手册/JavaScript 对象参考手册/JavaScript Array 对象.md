# JavaScript Array 对象

## Array 对象

Array 对象用于在单个的变量中存储多个值。

### 创建 Array 对象的语法：

```javascript
new Array();
new Array(size);
new Array(element0, element1, ..., elementn);
```

### 参数

- 参数 *size* 是期望的数组元素个数。返回的数组，`length `字段将被设为 *size* 的值。

- 参数 *element* ..., *elementn* 是参数列表。当使用这些参数来调用构造函数 `Array()` 时，新创建的数组的元素就会被初始化为这些值。它的 `length `字段也会被设置为参数的个数。

### 返回值

返回新创建并被初始化了的数组。

- 当调用构造函数 `Array()` 时没有使用参数，那么返回的数组为空，`length `字段为 0。

- 当调用构造函数时只传递给它一个数字参数，该构造函数将返回具有指定个数、元素为 `undefined `的数组。

- 当其他参数调用 `Array()` 时，该构造函数将用参数指定的值初始化数组。

- 当把构造函数作为函数调用，不使用 `new `运算符时，它的行为与使用 `new `运算符调用它时的行为完全一样。

## Array 对象属性

| 属性          | 描述                               |
| :------------ | :--------------------------------- |
| `constructor` | 返回对创建此对象的数组函数的引用。 |
| `length`      | 设置或返回数组中元素的数目。       |
| `prototype`   | 使您有能力向对象添加属性和方法。   |

## Array 对象方法

| 方法                                                         | 描述                                                 |
| :----------------------------------------------------------- | :--------------------------------------------------- |
| [concat()](https://www.runoob.com/jsref/jsref-concat-array.html) | 连接两个或更多的数组，并返回结果。                   |
| [copyWithin()](https://www.runoob.com/jsref/jsref-copywithin.html) | 从数组的指定位置拷贝元素到数组的另一个指定位置中。   |
| [entries()](https://www.runoob.com/jsref/jsref-entries.html) | 返回数组的可迭代对象。                               |
| [every()](https://www.runoob.com/jsref/jsref-every.html)     | 检测数值元素的每个元素是否都符合条件。               |
| [fill()](https://www.runoob.com/jsref/jsref-fill.html)       | 使用一个固定值来填充数组。                           |
| [filter()](https://www.runoob.com/jsref/jsref-filter.html)   | 检测数值元素，并返回符合条件所有元素的数组。         |
| [find()](https://www.runoob.com/jsref/jsref-find.html)       | 返回符合传入测试（函数）条件的数组元素。             |
|                                                              |                                                      |
| [findIndex()](https://www.runoob.com/jsref/jsref-findindex.html) | 返回符合传入测试（函数）条件的数组元素索引。         |
|                                                              |                                                      |
| [forEach()](https://www.runoob.com/jsref/jsref-foreach.html) | 数组每个元素都执行一次回调函数。                     |
| [from()](https://www.runoob.com/jsref/jsref-from.html)       | 通过给定的对象中创建一个数组。                       |
|                                                              |                                                      |
| [includes()](https://www.runoob.com/jsref/jsref-includes.html) | 判断一个数组是否包含一个指定的值。                   |
| [indexOf()](https://www.runoob.com/jsref/jsref-indexof-array.html) | 搜索数组中的元素，并返回它所在的位置。               |
| [isArray()](https://www.runoob.com/jsref/jsref-isarray.html) | 判断对象是否为数组。                                 |
| [join()](https://www.runoob.com/jsref/jsref-join.html)       | 把数组的所有元素放入一个字符串。                     |
| [keys()](https://www.runoob.com/jsref/jsref-keys.html)       | 返回数组的可迭代对象，包含原始数组的键(key)。        |
| [lastIndexOf()](https://www.runoob.com/jsref/jsref-lastindexof-array.html) | 搜索数组中的元素，并返回它最后出现的位置。           |
| [map()](https://www.runoob.com/jsref/jsref-map.html)         | 通过指定函数处理数组的每个元素，并返回处理后的数组。 |
| [pop()](https://www.runoob.com/jsref/jsref-pop.html)         | 删除数组的最后一个元素并返回删除的元素。             |
| [push()](https://www.runoob.com/jsref/jsref-push.html)       | 向数组的末尾添加一个或更多元素，并返回新的长度。     |
|                                                              |                                                      |
| [reduce()](https://www.runoob.com/jsref/jsref-reduce.html)   | 将数组元素计算为一个值（从左到右）。                 |
|                                                              |                                                      |
| [reduceRight()](https://www.runoob.com/jsref/jsref-reduceright.html) | 将数组元素计算为一个值（从右到左）。                 |
| [reverse()](https://www.runoob.com/jsref/jsref-reverse.html) | 反转数组的元素顺序。                                 |
| [shift()](https://www.runoob.com/jsref/jsref-shift.html)     | 删除并返回数组的第一个元素。                         |
| [slice()](https://www.runoob.com/jsref/jsref-slice-array.html) | 选取数组的的一部分，并返回一个新数组。               |
| [some()](https://www.runoob.com/jsref/jsref-some.html)       | 检测数组元素中是否有元素符合指定条件。               |
| [sort()](https://www.runoob.com/jsref/jsref-sort.html)       | 对数组的元素进行排序。                               |
| [splice()](https://www.runoob.com/jsref/jsref-splice.html)   | 从数组中添加或删除元素。                             |
| [toString()](https://www.runoob.com/jsref/jsref-tostring-array.html) | 把数组转换为字符串，并返回结果。                     |
| [unshift()](https://www.runoob.com/jsref/jsref-unshift.html) | 向数组的开头添加一个或更多元素，并返回新的长度。     |
| [valueOf()](https://www.runoob.com/jsref/jsref-valueof-array.html) | 返回数组对象的原始值。                               |

---

# Array.constructor

```javascript
array.constructor
```

Example

```java
var test = new Array();
if (test.constructor===Array) {
    document.write("This is an Array");
} else if (test.constructor===Boolean) {
    document.write("This is an Boolean");
} else if (test.constructor===Date) {
    document.write("This is an Date");
} else if (test.constructor===String) {
    document.write("This is an String");
}
```

```out
This is an Array
```

```javascript
function Employee(name, job, born) {
    this.name = name;
    this.job = job;
    this.born = born;
}
var bill = new Employee("Bill Gates", "Engineer", 1985);
document.write(bill.constructor);
```

```out
function employee(name, job, born)
{this.name = name; this.job = job; this.born = born;}
```

---

# Array.length

```javascript
array.length
```

Example

```javascript
var arr = new Array(3);
arr[0] = "John";
arr[1] = "Andy";
arr[2] = "Wendy";
document.write("Original length: " + arr.length);
document.write("<br>");

arr.length = 5;
document.write("New length: " + arr.length);
```

```out
Original length: 3
New length: 5
```

---

# Array.prototype

```javascript
array.prototype.name = value
```

Example

```javascript
function Employee(name, job, born) {
    this.name = name;
    this.job = job;
    this.born = born;
}

var bill = new Employee("Bill Gates", "Engineer", 1985);
Employee.prototype.salary = null;
bill.salary = 20000;
document.write(bill.salary);
```

```out
20000
```

---

# Array.concat()

```javascript
array1.concat(array2, array3, ..., arrayX)
```

Example

```javascript
var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"

var arr2 = new Array(3)
arr2[0] = "James"
arr2[1] = "Adrew"
arr2[2] = "Martin"

document.write(arr.concat(arr2))
```

```out
George,John,Thomas,James,Adrew,Martin
```

---

# Array.copyWithin()

```javascript
array.copyWithin(target, start, end)
```

Example

复制数组的前面两个元素到后面两个元素上：

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.copyWithin(2, 0);
```

```out
Banana,Orange,Banana,Orange
```

复制数组的前面两个元素到第三和第四个位置上：

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango", "Kiwi", "Papaya"];
fruits.copyWithin(2, 0, 2);
```

```out
Banana,Orange,Banana,Orange,Kiwi,Papaya
```

---

# Array.entries()

```javascript
// 返回数组的可迭代对象。
array.entries()
```

Example

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
var x = fruits.entries();
var p1 = document.createElement('p');
var p2 = document.createElement('p');
var p3 = document.createElement('p');
var body = document.getElementsByTagName('body');
body[0].appendChild(p1);
body[0].appendChild(p2);
body[0].appendChild(p3);
p1.innerHTML = x.next().value;
p2.innerHTML = x.next().value;
p3.innerHTML = x.next().value;
```

```out
0,Banana
1,Orange
2,Apple
```

---

# Array.every()

```javascript
array.every(function(currentValue,index,arr), thisValue)
```

Example

检测数组 *ages* 的所有元素是否都大于等于 18 :

```html
<p>点击按钮检测数组的所有元素是否都大于 18 :</p>
<button onclick="myFunction()">点我</button>
<p id="demo"></p>
<script>
var ages = [32, 33, 16, 40];
function checkAdult(age) {
    return age >= 18;
}
function myFunction() {
    document.getElementById("demo").innerHTML = ages.every(checkAdult);
}
</script>
```

---

# Array.fill()

`fill() `方法用于将一个固定值替换数组的元素。

```javascript
array.fill(value, start, end)
```

Example

使用固定值填充数组：

```html
<p>点击按钮使用 “Runoob” 填充所有数组元素。</p>
<button onclick="myFunction()">点我</button>
<p id="demo"></p>
<script>
var fruits = ["Banana", "Orange", "Apple", "Mango"];
document.getElementById("demo").innerHTML = fruits;
function myFunction() {  
    document.getElementById("demo").innerHTML = fruits.fill("Runoob");
}
</script>
```

---

# Array.filter()

filter() 方法创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素。

```javascript
array.filter(function(currentValue,index,arr), thisValue)
```

Example

返回数组 *ages* 中所有元素都大于 18 的元素:

```javascript
var ages = [32, 33, 16, 40];

function checkAdult(age) {
    return age >= 18;
}

function myFunction() {
    document.getElementById("demo").innerHTML = ages.filter(checkAdult);
}
```

```out
32,33,40
```

---

#  Array.find()

find() 方法返回通过测试（函数内判断）的数组的第一个元素的值。

```javascript
array.find(function(currentValue, index, arr),thisValue)
```

Example

获取数组中年龄大于 18 的第一个元素

```javascript
var ages = [3, 10, 18, 20];
 
function checkAdult(age) {
    return age >= 18;
}
 
function myFunction() {
    document.getElementById("demo").innerHTML = ages.find(checkAdult);
}
```

```out
18
```

---

# Array.findIndex()

findIndex() 方法返回传入一个测试条件（函数）符合条件的数组第一个元素位置。

```javascript
array.findIndex(function(currentValue, index, arr), thisValue)
```

获取数组中年龄大于等于 18 的第一个元素索引位置

```javascript
var ages = [3, 10, 18, 20];
 
function checkAdult(age) {
    return age >= 18;
}
 
function myFunction() {
    document.getElementById("demo").innerHTML = ages.findIndex(checkAdult);
}
```

```out
2
```

# Array.forEach()

forEach() 方法用于调用数组的每个元素，并将元素传递给回调函数。

```javascript
array.forEach(function(currentValue, index, arr), thisValue)
```

列出数组的每个元素：

```html
<button onclick="numbers.forEach(myFunction)">点我</button>
<p id="demo"></p>
 
<script>
demoP = document.getElementById("demo");
var numbers = [4, 9, 16, 25];
 
function myFunction(item, index) {
    demoP.innerHTML = demoP.innerHTML + "index[" + index + "]: " + item + "<br>"; 
}
</script>
```

```out
index[0]: 4
index[1]: 9
index[2]: 16
index[3]: 25
```

# Array.from()

from() 方法用于通过拥有 length 属性的对象或可迭代的对象来返回一个数组。

```javascript
Array.from(object, mapFunction, thisValue)
```

下面的实例返回集合中包含的对象数组。

```javascript
var setObj = new Set(["a", "b", "c"]);
var objArr = Array.from(setObj);
```

下面的实例演示如何使用箭头语法和映射函数更改元素的值。

```javascript
var arr = Array.from([1, 2, 3], x => x*10);
```

# Array.includes()

includes() 方法用来判断一个数组是否包含一个指定的值，如果是返回 true，否则false。

```javascript
arr.includes(searchElement)
arr.includes(searchElement, fromIndex)
```

如果fromIndex 大于等于数组长度 ，则返回 false 。该数组不会被搜索:

```javascript
var arr = ['a', 'b', 'c'];
 
arr.includes('c', 3);   //false
arr.includes('c', 100); // false
```

检测数组 *site* 是否包含 runoob :

```javascript
let site = ['runoob', 'google', 'taobao'];
 
site.includes('runoob'); 
// true 
 
site.includes('baidu'); 
// false
```

# Array.indexOf()

indexOf() 方法可返回数组中某个指定的元素位置。

```javascript
array.indexOf(item,start)
```

查找数组中的 "Apple" 元素：

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
var a = fruits.indexOf("Apple");
```

```out
2
```

# Array.isArray()

isArray() 方法用于判断一个对象是否为数组。

```javascript
Array.isArray(obj)
```

判断对象是否为数组：

```javascript
function myFunction() {
    var fruits = ["Banana", "Orange", "Apple", "Mango"];
    var x = document.getElementById("demo");
    x.innerHTML = Array.isArray(fruits);
}
```

# Array.join()

join() 方法用于把数组中的所有元素转换一个字符串。

元素是通过指定的分隔符进行分隔的。

```javascript
array.join(separator)
```

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
var energy = fruits.join();
```

```out
Banana,Orange,Apple,Mango
```

---

# Array.keys()

keys() 方法用于从数组创建一个包含数组键的可迭代对象。

```javascript
array.keys()
```

从数组 fruit 创建一个数组迭代对象， 该对象包含了数组的键：

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
var x = fruits.keys();

document.getElementById("demo1").innerHTML = x.next().value;
document.getElementById("demo2").innerHTML = x.next().value;
document.getElementById("demo3").innerHTML = x.next().value;
```

---

# Array.lastIndexOf()

lastIndexOf() 方法可返回一个指定的元素在数组中最后出现的位置，从该字符串的后面向前查找。

```javascript
array.lastIndexOf(item,start)
```

---

# Array.map()

map() 方法返回一个新数组，数组中的元素为原始数组元素调用函数处理后的值。

```javascript
array.map(function(currentValue,index,arr), thisValue)
```

返回一个数组，数组中元素为原始数组的平方根:

```javascript
var numbers = [4, 9, 16, 25];

function myFunction() {
    x = document.getElementById("demo")
    x.innerHTML = numbers.map(Math.sqrt);
}
```



# Array.pop()

```javascript
arrayObject.pop()
```

Example

```javascript
var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"
document.write(arr.pop())
```

```out
Thomas
```

---

# Array.push()

```javascript
arrayObject.push(newelement1, newelement2, ..., newelementX)
```

Example

```javascript
var arr = new Array(3);
arr[0] = "George";
arr[1] = "John";
arr[2] = "Thomas";

document.write(arr + "<br>");
document.write(arr.push("James") + "<br>");
document.write(arr);
```

```out
George,John,Thomas
4
George,John,Thomas,James
```

---

# Array.reverse()

```javascript
arrayObject.reverse()
```

Example

```javascript
var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"

document.write(arr + "<br/>")
document.write(arr.reverse())
```

```out
George,John,Thomas
Thomas,John,George
```

---

# Array.shift()

```javascript
// 删除并返回数组的第一个元素。
arrayObject.shift()
```

Example

```javascript
var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"

document.write(arr + "<br/>")
document.write(arr.shift() + "<br/>")
document.write(arr)
```

```out
George,John,Thomas
George
John,Thomas
```

---

# Array.slice()

```javascript
rrayObject.slice(start,end)
```

Example

```javascript
var arr = new Array(3)
arr[0] = "George"
arr[1] = "John"
arr[2] = "Thomas"

document.write(arr + "<br/>")
document.write(arr.slice(1) + "<br/>")
document.write(arr)
```

```out
George,John,Thomas
John,Thomas
George,John,Thomas
```

---

# Array.sort()

```javascript
arrayObject.sort(sortby)
```

Example

```javascript
var arr = new Array(6);
arr[0] = "George";
arr[1] = "John";
arr[2] = "Thomas";
arr[3] = "James";
arr[4] = "Adrew";
arr[5] = "Martin";

document.write(arr + "<br>");
document.write(arr.sort());
```

```out
George,John,Thomas,James,Adrew,Martin
Adrew,George,James,John,Martin,Thomas
```

```javascript
function sortNumber(a, b) {
    return a - b;
}

var arr = new Array(6);
arr[0] = "10";
arr[1] = "5";
arr[2] = "40";
arr[3] = "25";
arr[4] = "1000";
arr[5] = "1";

document.write(arr + "<br>");
document.write(arr.sort(sortNumber));
```

```out
10,5,40,25,1000,1
1,5,10,25,40,1000
```

---

# Array.splice()

splice() 方法用于添加或删除数组中的元素。

```javascript
arrayObject.splice(index, howmany, item1, ..., itemX)
```

Example

```javascript
var arr = new Array(6);
arr[0] = "George";
arr[1] = "John";
arr[2] = "Thomas";
arr[3] = "James";
arr[4] = "Adrew";
arr[5] = "Martin";

document.write(arr + "<br>");
arr.splice(2, 0, "William");
document.write(arr);
```

```out
George,John,Thomas,James,Adrew,Martin
George,John,William,Thomas,James,Adrew,Martin
```

---

# Array.toString()

```javascript
arrayObject.toSource()
```

