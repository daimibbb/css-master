# 正则表达式中g的用法

表达式加上参数`g`之后，表明可以进行全局匹配，注意这里“可以”的含义。我们详细叙述：

1）对于表达式对象的`exec`方法，不加入`g`，则只返回第一个匹配，无论执行多少次均是如此，如果加入`g`，则第一次执行也返回第一个匹配，再执行返回第二个匹配，依次类推。例如

```javascript
var regx = /user\d/;
var str = "user18dsdfuser2dsfsd";
var rs = regx.exec(str);
var rs2 = regx.exec(str);
```

```
user1
user1
```

```javascript
var regx = /user\d/g;
var str = "user18dsdfuser2dsfsd";
var rs = regx.exec(str);
var rs2 = regx.exec(str);
```

```
user1
user2
```

2）对于`String`对象的`match`方法，不加入`g`，也只是返回第一个匹配，一直执行`match`方法也总是返回第一个匹配，加入`g`，则一次返回所有的匹配（注意这与表达式对象的`exec`方法不同，对于`exec`而言，表达式即使加上了`g`，也不会一次返回所有的匹配）。例如：

```javascript
var regx = /user\d/;
var str = "user18dsdfuser2dsfsd";
var rs = str.match(regx);
var rs2 = str.match(regx);
console.log(rs);
console.log(rs2);
```

```
["user1"]
["user1"]
```

---

```javascript
var regx = /user\d/g;
var str = "user18dsdfuser2dsfsd";
var rs = str.match(regx);
var rs2 = str.match(regx);
console.log(rs);
console.log(rs2);
```

```
["user1", "user2"]
["user1", "user2"]
```

4）对于`String`对象的*replace*方法，表达式不加入`g`，则只替换第一个匹配，如果加入`g`，则替换所有匹配。

5）对于`String`对象的*split*方法，加上`g`与不加`g`是一样的，即：

```javascript
var sep = /user\d/;
var str = "user1dfsfuser2dfsf";
var array = str.split(sep);
```

```
["", "dfsf", "dfsf"]
```

6）对于`String`对象的*search*方法，加不加`g`也是一样的。

---

# 正则表达式test()，慎用g

 今天在将这个表达式时，发现了一个问题：test()检测指定字符串是否存在返回一个布尔值

```javascript
var reg=/cat/g;
var str='this a cat,this a dog'; 
document.write(reg.test(str)); 
document.write(reg.test(str)); 
```

按道理两次打印出来都应该是`true`, `true`，而最终结果为`true`, `false`。

此时我们需要注意啦，在我们定义的正则表达式中后面加上了搜索的方式，`g`表示全文查找。而且在正则表达式内部有一个*lastIndex*来记录匹配的位置，第一次调用`test()`后，那么*lastIndex*就不再等于`0`，而是`10`，当下次在调用该方法的时候，字符串的匹配会从*lastIndex*位置进行匹配，故最终返回`false`，所以不要随意添加`g`。

遇到此种情况后的解决方法：

1. 去除`g`；
2. 在第二次使用前，设置`reg.lastIndex=0`即可。

---

