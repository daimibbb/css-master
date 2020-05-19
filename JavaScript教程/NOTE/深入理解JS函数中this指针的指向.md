# 深入理解JS函数中this指针的指向

函数在执行时，会在函数体内部自动生成一个`this`指针。谁直接调用产生这个`this`指针的函数，`this`就指向谁。

怎么理解指向呢，我认为指向就是等于。例如直接在js中输入下面的等式：

```javascript
console.log(this===window); //true
```

 情况不同，`this`指向的对象也不同。例如：

### 1. 函数声明的情况

```javascript
var bj=10;
function add(){
    var bj=20;
    console.log(this); //window
    console.log(this.bj); //10
    console.log(bj); //20
    console.log(this.bj+bj); //30
}
add();
window.add();
```

（1） 执行了`add()`之后，此时的`this`指向的是`window`对象，为什么呢？因为这时候`add`是全局函数，是通过`window`**直接调用**的。所以下面我专门写了个`window.add()`就是为了说明，全局函数的`this`都是指向的`window`。

（2） 就像`alert()`自带的警告弹窗一样，`window.alert()`执行之后也是一样的效果。所以只要是  `window`。这种调用方式都可以省略掉，因此警告弹窗可以直接使用`alert()`。

### 2. 函数表达式

```javascript
var bj=10;
var zjj=function(){
    var bj=30;
    console.log(this); //window
    console.log(this.bj); //10
    console.log(bj); //30
    console.log(this.bj+bj); //40
}
console.log(typeof zjj); //function
zjj();
window.zjj();
```

（1） 执行了`zjj()`之后，函数中的`this`也是指向`window`对象。原因和第一个是一样的，都是通过`window`这个对象**直接调用**。

### 3. 函数作为对象的属性去调用：例一

```javascript
var bj=10;
var obj={
    name: "八戒",
    age: "500",
    say: function(){
        var bj=40;
        console.log(this); //就是obj这个对象
        console.log(this.bj); //undefined
        console.log(this.name); //八戒
    }
}
obj.say();
window.obj.say();    
```

（1） 当`obj.say()`被执行的时候，此时的`this`指向的是`obj`这个对象，为什么呢？因为`say`函数是通过`obj`这个对象**直接调用**的。

（2） 那有人可能会问了，`obj`对象实际上也是通过`window`对象调用的，为什么`this`不指向`window`呢？我认为是因为`say`这个函数是通过 **obj** 对象**直接调用**的，而没有通过 `window `对象**直接调用**，因此`this`不会指向`window`。看下面的例子就明白了。

#### 3.1 函数作为对象的属性去调用：例二

```javascript
var bj=10;
var obj={
    name: "八戒",
    age: 500,
    say: function(){
        console.log(this); //是obj这个对象
        console.log(this.bj); //undefined
        console.log(this.name) //八戒
    },
    action: {
        name: "悟空",
        age: 1000,
        say: function(){
            console.log(this); //是action这个对象
            console.log(this.bj); //undefined
            console.log(this.name) //悟空
        }
    }
}
obj.say();
obj.action.say();
window.obj.action.say();
```

（1） `obj.say()`执行之后，此时这个函数里的`this`指向的是`obj`对象，原因是因为`say`函数是通过`obj`**直接调用**的。

（2）` obj.action.say()`执行之后，此时这个函数里的`this`指向的是`action`对象，原因是因为`say`函数是通过`action`对象**直接调用**的。并没有通过`obj`**直接调用**。也没有通过 `window `**直接调用**，所以此时`action`对象中`say`函数里的的`this`指向并不会是`obj`或者`window`。

#### 3.2 函数作为对象的属性去调用：例三

```javascript
var bj=10;
var obj={
    name: "八戒",
    age: 500,
    say: function(){
        console.log(this); //就是obj这个对象
        console.log(this.bj); //undefined
        console.log(this.name) //八戒
        function wk(){
            console.log(this); //window
            console.log(this.bj); //10
            console.log(this.name); //这里显示的是为空
        }
        wk();        
    },
}
obj.say();
```

（1） 这种情况下，`say`函数里的`this`指针还是指向的`obj`，原因是因为`say`函数是通过`obj`**直接调用**。

（2） 但是这时候`wk`函数中的`this`就是指向的是`window`了。为什么呢？因为`wk()`函数在`say()`函数中，是属于普通函数调用，但是并没有通过`say`或者`obj`**直接调用**，只是自执行，这个时候，`wk`就是一个全局函数，因此该函数的`this`指向的就是`window`。

（3） 那为什么`this.name`是显示的为空呢？因为` window `对象中本身就有一个 `name`值，并不是某处添加的，如果把`name`换成`age`，得到的就是`undefined`了。

（4） 那怎样让`wk()`函数中的`this`指向`obj`呢。一种方式就是在`say`函数中把`say()`函数的`this`用变量保存起来，即 `var that=this;` 然后`wk()`函数使用`that`就能达到指向`obj`的目的了。另外的方式是通过`apply`或者`call`来改变。

（5） 那`wk()`在这里能不能写成`window.wk()`呢？这样是不行的，会报错，*window.wk is not a function*。为什么不行呢，`this`不是指向`window`吗，为什么`widow`对象里灭有`wk()`这个函数。。这个嘛，我也不知道，先留个坑，后面再来填 。

#### 3.3 函数作为对象的属性去调用：例四

```javascript
var bj=10;
var obj={
    name:"八戒",
    age:"500",
    say:function(){
        var bj=40;
        console.log(this);//window
        console.log(this.bj);//10
        console.log(this.name);//这里没有输出内容
    }
}
var elseObj=obj.say;
elseObj();
```

 （1） 执行了`elseObj()`函数之后，为什么`say`函数中的`this`却指向了`window`呢？首先要理解这句话：谁直接调用产生这个`this`指针的函数，`this`就指向谁。当`obj.say`赋值给`elseObj`的时候，`elseObj`只是一个函数，而并没有执行，因此`this`指针的指向并不明确，这个时候执行到` var elseObj=obj.say`的时候，整程序相当于：

```javascript
var bj=10;
var elseObj=function(){
    var bj=40;
    console.log(this);
    console.log(this.bj);
    console.log(this.name);
}
elseObj();
```

这就和第2种函数表达式的情况一样了。所以，当执行`elseObj()`的时候，`this`就指向`window`，`this.obj`为`10`，因为这时候`elseObj()`是通过 `window `**直接调用**的

（2） `this.name`为空是因为 `window` 对象中本身就有一个 `name `值，并不是某处添加的，如果把`name`换成其它的比如`age`，得到的就是`undefined`了，因为全局并没有`age`属性。

#### 3.4 函数作为对象的属性去调用：例五

```javascript
var bj=10;
var obj={
    name:"八戒",
    age:500,
    say:function(){
        return function(){
            console.log(this);//window
            console.log(this.bj);//10
            console.log(this.age);//undefined
        }
    }
}
obj.say()();
// var elseObj=obj.say();
// elseObj();
```

（1） `obj.say()()`为什么会有两个括号？因为`obj.say()`执行之后返回的是一个函数，并没有执行，再加一个括号就是执行返回的那个匿名函数。

（2） 如果不习惯也可以使用上面注释的那种方式，是一样的效果。

（3） 执行了函数之后，为什么返回的函数中`this`是指向`window`的呢？那是因为执行`obj.say()`的时候，只是一个函数，相当于就是注释里的第一行代码，这时候返回的函数并未被执行。当再加一个括号的时候，就是执行了返回的那个函数，这个时候返回的函数就相当于是一个全局函数，是通过`window`**直接调用**，因此`this`就是指向的是`window`。

### 4. 工厂模式中this的指向：例一

```javascript
var bj=10;
function fun(a, b){　　 
    console.log(this);//window对象
    var bj=20;
    var sun=new Object();
    sun.one=a;
    sun.two=b;
    sun.say=function() {
        console.log(this);//是sun对象，{one: 2, two: 3, say: ƒ()}
        console.log(this.bj);//undefined
        console.log(this.one);//2
    }
    return sun;
}
var wk=fun(2, 3);
wk.say();
```

 （1） 话说为什么叫工厂模式，我搞不太清楚，不过这个不重要，重要的是通过这个模式，在每次调用函数的时候，虽然每次都返回的是`sun`这个对象，但是每个对象都是不相似的，即使内容一样，比如  ：

```javascript
var sf=fun(2, 3); 
console.log(sf===wk);//false
```

（2） 那为什么`say()`函数执行之后，`this`是指向返回的那个对象呢？这个很明显嘛，`say()`是通过`wk`这个对象**直接调用**的，而`wk`是`fun`函数返回的`sun`对象。所以这里的`this`就指向的是返回的这个对象。所以`this.bj`为`undefined`，因为返回的对象中没有`bj`属性。

（3） 我认为这种模式最重要的还是 `renturn sun`这个返回语句，这个是必不可少的。

（4） `fun(a,b)`这个函数中的`this`指向的是`window`，原因是执行 `var wk=fun(2,3);` 的时候，`fun`函数已经被执行了，并且**直接调用**它的就是`window`，所以这时的`this`是指向的`window`。

#### 4.1 工厂模式中this的指向：例二

```javascript
var bj=10;
function fun(a,b){　　 
    console.log(this);//window对象
    var bj=20;
    var sun=new Object();
    sun.one=a;
    sun.two=b;
    sun.say=function(){
        console.log(this);//是sun对象，{one: 2, two: 3, say: ƒ()}
        return function(){
            console.log(this);//是window对象
        }
    }
    return sun;
}
var wk=fun(2,3);
var ss=wk.say();
ss();
```

 （1） 为什么`say`函数中`return `的函数中`this`是指向的`window`对象呢？首先，执行到 `var wk=fun(2,3);` 的时候，`wk`是一个对象。继续执行下一句代码，`ss`这时候是一个函数，就是通过`say`函数返回之后赋值的。这时候返回的函数还未执行，`this`指向并不明确。当执行到最后一句代码，`ss()`函数执行了。这时候，`ss`函数就是一个全局函数，是通过`window`**直接调用**的。所以这时的`this`指向的是`window`。

（2） 如果`say`中返回的是一个对象，对象中又有个函数，像下面一样：

```javascript
sun.say=function(){
    console.log(this);//是sun对象，{one: 2, two: 3, say: ƒ()}
    return {
        wk:"1",
        say:function(){
            console.log(this);
        }
    }
}
```

这时候执行到`ss.say()`的时候，this指向的就是`ss`这个对象，即通过`say`函数返回的那个对象。原因还是一样，`say`函数是通过`ss`直接调用的，而`ss`对象是`wk.say()`返回的对象。

### 5. 构造函数中this的指向

```javascript
var bj=10;
function Add(){
    var bj=20;
    this.bj=30;
    this.say=function(){
        console.log(this);//Add {bj: 30, say: ƒ()}
        console.log(this.bj);//30
    }
    console.log(this) ;//Add {bj: 30, say: ƒ()}
}
var obj=new Add();
console.log(typeof obj);//object
obj.say();
```

 （1） 要明白构造函数的`this`指向，我们需要明白调用构造函数经历的步骤：

　　a. 创建一个新对象。

　　b. 将构造函数的作用域赋给新对象（因此`this`就指向了这个新对象）。

　　c. 执行构造函数中的代码（为这个新对象添加属性）。

　　d. 返回新对象。

（2） 构造函数与工厂模式相比：

　　a. 没有显示的创建对象。

　　b. 没有`return`语句。

　　c. 直接将属性和方法赋值给 `this` 对象。

（3） 首先，`obj.say()`执行之后，`say`函数中`this`的指向是`obj`对象，这个很明显，不再赘述。在不用`new`操作符的时候，`Add()`函数里的`this`指向的就是`window`；但是使用了`new`操作符之后，`Add()`函数中` console.log(this)` 这个`this`为什么是`obj`对象，而不是`window`呢？

（4）  这个原因我认为在js权威指南4.6节对象创建表达式和8.2.3构造函数使用中，有所说明。使用`new`操作符的时候，js先创建一个新的空对象，然后，js传入指定的参数并将这个新对象当做`this`的值来调用一个指定的函数。这个函数可以使用`this`来初始化这个新创建对象的属性。所以当使用`new`操作符之后，函数中的`this`指向的是新创建的对象。所以构造函数中的`this`就是指向`new`出来的那个对象。

（5） 如果构造函数中有`return`语句，那么此时 `var obj=new Add()`; `obj`就是`return`出来的内容，但是`Add`函数中的`this`还是指向的创建的新对象`Add`；

### 6. 原型对象中this的指向

```javascript
var bj=10;
function Add() {　　
    console.log(this);//Add{}
};
Add.prototype.bj=10;
Add.prototype.say=function() {
    console.log(this);//Add{}
    return function(){
        console.log(this);//window
    }
}
var obj=new Add;//没传参数可以省略括号
obj.say()();
```

 （1） `obj.say()()`执行的时候，`this`指向的是`window`，这个还是因为`obj.say()`执行时返回的是一个函数，然后再加一个括号，就执行返回的这个函数，此时这个函数属于全局函数，所以，`this`会指向`window`。

（2） `Add()`这个构造函数中的`this`指向的是`Add{}`，原因和上面构造函数中`this`的指向一样。

（3） `Add.prototype.say=function(){ console.log(this) }` 这里面的`this `也是指向的是`Add{}`，至于原因，我认为是因为`say()`这个函数是通过obj直接调用的，所以this指向的是obj，所以是Add{}。

**总结：**

　　要想判断函数中this的指向，只要知道谁直接调用产生this指针的函数，this就指向谁了。只是要注意使用了new 操作符之后，构造函数内部的this指向的是新对象，通俗点讲就是new出来的新实例。

------

更新： 

再来一个例子说明一下，通俗的理解一下this指针的指向：**谁直接调用产生 this 指针的函数，这函数里的 this 指针就指向谁。**

```javascript
var factory = function() {
  this.a = 'first-A';  
  this.b = 'first-B';
  this.c = {
    a: 'second-A',
    b: function() {
        console.log(this.a)
        return this.a
    }
  }    
}
new factory().c.b(); // second-A
```

（1） 这个代码首先考的是运算符的优先级。[MDN运算符优先级 ](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Operator_Precedence) 可以先查看优先级再思考。

（2） `new`的优先级和点运算符等级一样，从左至右执行，所以先执行 `new factory()` 然后在执行 点运算符。

（3） 执行了 `new `操作之后。然后发现函数调用的优先级和成员访问运算符的优先级一样，然后遵循从左到有的执行方式。因此就先执行 成员访问运算符 `.c`

（4） 这时 `.c` 就是一个对象，然后再取 `b` 属性，是个函数。这个时候 `this` 指针已经产生， 而产生这个`this`指针的是`b`函数，而且是通过 `c` 调用的。因此此时 `this` 的指向就是 `c` 对象。所以最后打印出`second-A`

（5） 如果想要 c 里面的 b函数中 this指向的是 factory 实例。要么使用 bind.apply,call等方法来强行改变。 要么就把 b 函数写成 es6箭头函数的方式。这样 b 函数就没有this指针，而 b 函数里面的this，就是上一级的 this。

然后再来说一下**回调函数**，**立即执行函数（IIFE），点击事件** 的 this 的指向。

弄清楚这个之前，我们要知道，函数传参是按值传递，如果是**基本数据类型**，则是直接复制数据的值传过去。如果是**引用类型**，比如对象，函数这种，传递的就是该数据 **在堆中存放的地址**。

举个例子来证明： 

```javascript
var obj = {
    a: 10,
    getA: function(){
        console.log(this.a);
    }
}
function active(fn) {
    console.log(fn===obj.getA) // true
    fn();
}
active(obj.getA);
```

（1） 形参 fn 与 obj.getA 全等，就说明了 传的是存放的地址，而不是内容。因为对象就算内容相同，存放地址不同的话，也不会相等。

那么，回调函数就是传的 **函数在堆中的地址**，也就是说，**回调函数中 this 的指向，决定于执行回调函数 时的执行上下文环境。**

**首先是 setTimeout，setInterval 这种类型的回调函数。**

**setTimeout的回调：例一**

```javascript
setTimeout(function(){
   console.log(this) 
})
```

（1） 这是最最常用的常见的定时器用法，回调函数里的this指向的是window。

（2） 由`setTimeout()`调用的代码运行在与所在函数完全分离的执行环境上。这会导致，这些代码中包含的 `this` 关键字在非严格模式会指向 `window` (或全局)对象，严格模式下为 undefined，这和所期望的`this`的值是不一样的。**在严格模式下，setTimeout( )的回调函数里面的this仍然默认指向window对象， 并不是undefined**。 这几句话是 MDN上，[setTimeout中 关于 this 的问题](https://developer.mozilla.org/zh-CN/docs/Web/API/Window/setTimeout) 里对 this 指向的解释。

（3） 我的理解是：由于setTimeout属于宏任务，它的回调在延时之后才进入到主线程执行，而函数执行的时候才明确 this 的指向。执行的时候，由于没有设置内部this的指向。相当于是普通函数调用。所以会默认指向window

**setTimeout的回调 --- 例二**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
var obj = {
    age:10,
    getage:function(){
        console.log(this.age)
    }
}

setTimeout(obj.getage,1000)   // undefined

setTimeout(function(){
    obj.getage()  // 10
},1000)
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

（1） 第一个setTimeout，执行obj.getage 之后，相当于setTimeout的回调是一个匿名函数，执行的时候，函数内部未设置this的指向。相当于是普通函数调用。所以this默认指向window，所以结果是undefined。

（2） 第二个setTimeout，传给setTimeout的也是一个匿名回调函数，执行匿名函数，执行到 obj.getage() 的时候，getage函数里的this，指向的就是obj了，所以能打印出10。**还是遵循 谁调用产生 this指针的函数，this就指向谁的规则**

**对于 数组的遍历方法：**

**foreach，map，filter，some**，每次 `callback` 函数被调用的时候，`this` 都会指向 最后一个参数 `thisArg` 的这个对象。如果省略了 `thisArg ``参数,``或者赋值为 null` 或 `undefined`，则 this 指向全局对象 。在严格模式下则是undefined（未传值的时候）。如果用箭头函数的写法，就要看当前上一层的 this 指向的是哪里了

reduce 累加器的参数中并没有 thisArg 对象可以传，但是在回调函数中，this指向的是window。如果用箭头函数的写法，就要看当前上一层的 this 指向的是哪里了

**对于 点击，移入移出等类似事件的回调函数 的 this 指向。**

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
<button type="button" id="btn">点我啊</button>

function getDom(){
    console.dir(this)
}

// 第一种调用方法
document.getElementById('btn').addEventListener('click',function(){
    getDom(); 
})

// 第二种调用方法
document.getElementById('btn').onclick = getDom()

// 第三种调用方法
document.getElementById('btn').addEventListener('click',getDom)

// 第四种调用方法
<button type="button" id="btn" onclick="console.log(this)">点我啊</button>
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

（1） 第一种调用方法，this指向的是window。虽然在function(){} 回调函数里的 this 指向的是button这个DOM对象，但是getDom是在这里面调用的，和普通函数调用没什么区别。所以也指向window

（2） 第二种都不用点击，直接触发，this指向window。因为直接当做普通函数调用了。

（3） 第三种方法，this指向 button这个DOM对象。回调函数传入的是函数执行的地址，执行的时候相当于是在window环境下执行，所以getDom的this指向的是window

（4） 第四种方式，this指向 button 这个DOM对象。

 **当函数被用作事件处理函数时，它的`this`指向触发事件的元素（一些浏览器在使用非`addEventListener`的函数动态添加监听函数时不遵守这个约定）。 --- MDN**

**对于 立即执行函数 IIFE 中 this的指向，指向的是window**

```
(function(){
 console.log(this) // window
})()
```

到这里，我还是没搞懂下面这种情况：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
var obj={
  age:10,
  say:function(){
     function get(){
        console.log(this)   // window
    }
    get();
  }  
}
obj.say();
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

get函数里的this指向的是window，因为get函数 独立调用，并没有为内部 this 明确指向。所以会指向 window 。如果是严格模式，则指向undefined。

不明白的是：

（1）既然 this 指向的是window，为什么get函数在window上不能访问？

（2）这种在函数内部定义并执行的方式，和立即执行函数有没有区别？

（3）词法分析的时候，这个函数是被怎样处理的？

------

更新：

以前没搞懂为什么上面内部申明的 get（）方法不能在window上访问，其实很简单，只是自己想复杂了而已：

get函数是在say函数里面 创建的，也就是说，不管怎么调用，get函数的作用域都只能是在say函数里面。而get方法是自执行，并没有其它任何对象直接调用，所以this是指向window，但是作用域是say函数里面，却不是window。感觉和立即执行函数没缺别。

由于js是采用的静态作用域（也叫词法作用域），这就意味着函数的执行依赖于函数定义的时候所产生（而不是函数调用的时候产生的）的变量作用域。

所以，函数的作用域是基于函数创建（可以理解为函数定义的时候）的地方，也就是函数在哪里创建，不管是否返回这个函数，或者返回带括号（已执行）的函数，都不用在意，只要知道是在哪里定义即创建的就知道函数的作用域是什么内容了。

在全局作用域中“定义”一个函数的时候，只会创建包含全局作用域的作用域链。只有“执行”该函数的时候，才会复制创建时的作用域，并将当前函数的局部作用域放在作用域链的顶端。

去取变量值的时候，首先看本函数里有没有该值，如果没有再到函数定义的外部去找