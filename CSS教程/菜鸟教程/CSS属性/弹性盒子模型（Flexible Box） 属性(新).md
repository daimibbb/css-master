# 弹性盒子模型（Flexible Box） 属性(新)

## flex

```css
flex: flex-grow flex-shrink flex-basis|auto|initial|inherit;
```

- *flex-grow*：一个数字，规定项目将相对于其他灵活的项目进行扩展的量。
- *flex-shrink*：一个数字，规定项目将相对于其他灵活的项目进行收缩的量。
- *flex-basis*：项目的长度。合法值："`auto`"、"`inherit`" 或一个后跟 "`%`"、"`px`"、"`em`" 或任何其他长度单位的数字。
- *auto*：与 `1 1 auto` 相同。
- *none*：与 `0 0 auto` 相同。
- *initial*：设置该属性为它的默认值，即为 `0 1 auto`。
- *inherit*：从父元素继承该属性。

`flex `属性用于设置或检索弹性盒模型对象的子元素如何分配空间。

`flex `属性是 `flex-grow`、`flex-shrink` 和 `flex-basis` 属性的简写属性。

**注意：**如果元素不是弹性盒模型对象的子元素，则 flex 属性不起作用。

```css
#main {
	width: 220px;
	height: 300px;
	border: 1px solid black;
	display: flex;
}

#main div {
	flex: 1;
}
```

```html
<div id="main">
  <div>红色</div>
  <div>蓝色</div>
  <div>带有更多内容的绿色 div</div>
</div>
```



<div id="main" style="width: 220px; height: 300px; border: 1px solid black; display: flex;">
  <div style="background-color:coral; flex: 1">红色</div>
  <div style="background-color:lightblue; flex: 1">蓝色</div>
  <div style="background-color:lightgreen; flex: 1">带有更多内容的绿色 div</div>
</div>


## flex-grow

```css
flex-grow: number|initial|inherit;
```

- *number*：一个数字，规定项目将相对于其他灵活的项目进行扩展的量。默认值是 0。
- *initial*：设置该属性为它的默认值。
- *inherit*：从父元素继承该属性。

让第二个元素的宽度为其他元素的三倍：

```css
#main {
  width: 350px;
  height: 100px;
  border: 1px solid #c3c3c3;
  display: flex;
}
#main div:nth-of-type(1) {flex-grow: 1;}
#main div:nth-of-type(2) {flex-grow: 3;}
#main div:nth-of-type(3) {flex-grow: 1;}
#main div:nth-of-type(4) {flex-grow: 1;}
#main div:nth-of-type(5) {flex-grow: 1;}
```

<div id="main" style="width: 350px; height: 100px; border: 1px solid #c3c3c3; display: flex">
  <div style="background-color:coral; flex: 1;"></div>
  <div style="background-color:lightblue; flex: 3;"></div>
  <div style="background-color:khaki; flex: 1;"></div>
  <div style="background-color:pink; flex: 1;"></div>
  <div style="background-color:lightgrey; flex: 1;"></div>
</div>

##  flex-shrink

```css
flex-shrink: number|initial|inherit;
```

A, B, C 设置` flex-shrink: 1`， D , E 设置为 `flex-shrink: 2`：

```css
#content {
  display: flex;
  width: 500px;
}
#content div {
  flex-basis: 120px;
  border: 3px solid rgba(0,0,0,.2);
}
.box { 
  flex-shrink: 1;
}
.box1 { 
  flex-shrink: 2; 
}
```

<p>div 总宽度为 500px, flex-basic 为 120px。</p>
<p>A, B, C 设置 flex-shrink:1。 D , E 设置为 flex-shrink:2</p>
<p>D , E 宽度与 A, B, C 不同</p>
<div id="content" style="display: flex; width: 500px">
  <div class="box" style="background-color:red; flex-basis: 120px; border: 2px solid rgba(0,0,0,0.2); flex-shrink: 1">A</div>
  <div class="box" style="background-color:lightblue; flex-basis: 120px; border: 2px solid rgba(0,0,0,0.2); flex-shrink: 1">B</div>
  <div class="box" style="background-color:yellow; flex-basis: 120px; border: 2px solid rgba(0,0,0,0.2); flex-shrink: 1">C</div>
  <div class="box1" style="background-color:brown; flex-basis: 120px; border: 2px solid rgba(0,0,0,0.2); flex-shrink: 2">D</div>
  <div class="box1" style="background-color:lightgreen; flex-basis: 120px; border: 2px solid rgba(0,0,0,0.2); flex-shrink: 2">E</div>
</div>

**实例解析：**

`flex-shrink`的默认值为1，如果没有显示定义该属性，将会自动按照默认值1在所有因子相加之后计算比率来进行空间收缩。

本例中A、B、C 显式定义了 `flex-shrink` 为 `1`，D、E 定义了` flex-shrink` 为 `2`，所以计算出来总共将剩余空间分成了 7 份，其中 A、B、C 占 1 份，D、E 占 2 份，即`1:1:1:2:2`

我们可以看到父容器定义为 `500px`，子项被定义为` 120px`，子项相加之后即为 `600 px`，超出父容器 `100px`。那么超出的 `100px` 需要被 A、B、C、D、E 通过收缩因子消化，所以加权综合可得 **100\*1+100\*1+100\*1+100\*2+100\*2=700px**。

于是我们可以计算 A、B、C、D、E 将被移除的溢出量是多少：

```css
A 被移除溢出量：(100*1/700)*100，即约等于14px
B 被移除溢出量：(100*1/700)*100，即约等于14px
C 被移除溢出量：(100*1/700)*100，即约等于14px
D 被移除溢出量：(100*2/700)*100，即约等于28px
E 被移除溢出量：(100*2/700)*100，即约等于28px
```

最后A、B、C、D、E的实际宽度分别为：**120-14=106px, 120-14=106px, 120-14=106px, 120-28=92px,120-28=92px**，此外，这个宽度是包含边框的。

---

## flex-basis

```css
flex-basis: number|auto|initial|inherit;
```

- *number*：一个数字，规定项目将相对于其他灵活的项目进行扩展的量。默认值是 0。
- *auto*：默认值。长度等于灵活项目的长度。如果该项目未指定长度，则长度将根据内容决定。
- *initial*：设置该属性为它的默认值。
- *inherit*：从父元素继承该属性。

```css
#main {
    width: 350px;
    height: 100px;
    border: 1px solid #c3c3c3;
    display: flex;
}
#main div {
    flex-grow: 0;
    flex-shrink: 0;
    flex-basis: 40px;
}

#main div:nth-of-type(2) {
    flex-basis: 80px;
}
```

<div id="main" style="width: 350px; height: 100px; border: 1px solid #c3c3c3; display: flex">
  <div style="background-color:coral; flex-grow: 0; flex-shrink: 0; flex-basis: 40px;"></div>
  <div style="background-color:lightblue;flex-grow: 0; flex-shrink: 0; flex-basis: 80px;"></div>
  <div style="background-color:khaki;flex-grow: 0; flex-shrink: 0; flex-basis: 40px;"></div>
  <div style="background-color:pink;flex-grow: 0; flex-shrink: 0; flex-basis: 40px;"></div>
  <div style="background-color:lightgrey;flex-grow: 0; flex-shrink: 0; flex-basis: 40px;"></div>
</div>
---

## flex-flow

```css
flex-flow: flex-direction flex-wrap|initial|inherit;
```

<table class="reference notranslate">
  <tbody><tr>
    <th style="width:21%">值</th>
    <th style="width:69%">描述</th>   
  </tr>
	<tr>
    <td><em>flex-direction</em></td>
    <td>可能的值：<br><br>row<br>row-reverse<br>column<br>column-reverse<br>initial<br>inherit
		<p>默认值是 "row"。</p>
		<p>规定灵活项目的方向。</p></td>             
    </tr>
	<tr>
    <td><em>flex-wrap</em></td>
    <td>可能的值：<br><br>nowrap<br>wrap<br>wrap-reverse<br>initial<br>inherit
		<p>默认值是 "nowrap"。</p>
		<p>规定灵活项目是否拆行或拆列。</p>
</td>          
    </tr>
	<tr>
    <td>initial</td>
    <td>设置该属性为它的默认值。</td>
    </tr>
	<tr>
    <td>inherit</td>
    <td>从父元素继承该属性。</td>
    </tr>
  </tbody></table>

`lex-flow` 属性是 `flex-direction` 和 `flex-wrap` 属性的复合属性。

`flex-flow` 属性用于设置或检索弹性盒模型对象的子元素排列方式。

`flex-direction` 属性规定灵活项目的方向。

`flex-wrap `属性规定灵活项目是否拆行或拆列。

**注意：**如果元素不是弹性盒对象的元素，则 flex-flow 属性不起作用。

```css
#main {
    width: 200px;
    height: 200px;
    border: 1px solid #c3c3c3;
    display: flex;
    flex-flow: row-reverse wrap;
}
#main div {
    width: 50px;
    height: 50px;
}
```

<div id="main" style="width: 200px; height: 200px; border: 1px solid #c3c3c3; display: flex; flex-flow: row-reverse wrap;">
  <div style="background-color:coral;width: 50px; height: 50px;">A</div>
  <div style="background-color:lightblue;width: 50px; height: 50px;">B</div>
  <div style="background-color:khaki;width: 50px; height: 50px;">C</div>
  <div style="background-color:pink;width: 50px; height: 50px;">D</div>
  <div style="background-color:lightgrey;width: 50px; height: 50px;">E</div>
  <div style="background-color:lightgreen;width: 50px; height: 50px;">F</div>
</div>
---

## flex-direction

```css
flex-direction: row|row-reverse|column|column-reverse|initial|inherit;
```

- *row*：默认值。灵活的项目将水平显示，正如一个行一样。

- *row-reverse*：与 *row* 相同，但是以相反的顺序。

- *column*：灵活的项目将垂直显示，正如一个列一样。

- *column-reverse*：与 *column* 相同，但是以相反的顺序。

- *initial*：设置该属性为它的默认值。

- *inherit*：从父元素继承该属性。

```css
#main {
    display: flex;
    flex-direction:row;
}
  
#main div {
	width: 40px;
	height: 40px;
}
```

<div id="main" style="display: flex; flex-direction: row;">
	<div style="background-color:coral; width: 40px; height: 40px">A</div>
	<div style="background-color:lightblue; width: 40px; height: 40p">B</div>
	<div style="background-color:khaki;width: 40px; height: 40p">C</div>
	<div style="background-color:pink;width: 40px; height: 40p">D</div>
	<div style="background-color:lightgrey;width: 40px; height: 40p">E</div>
	<div style="background-color:lightgreen;width: 40px; height: 40p">F</div>
</div>

```css
#main {
    display: flex;
    flex-direction:row-reverse;
}
  
#main div {
	width: 40px;
	height: 40px;
}
```

<div id="main" style="display: flex; flex-direction: row-reverse;">
	<div style="background-color:coral; width: 40px; height: 40px">A</div>
	<div style="background-color:lightblue; width: 40px; height: 40p">B</div>
	<div style="background-color:khaki;width: 40px; height: 40p">C</div>
	<div style="background-color:pink;width: 40px; height: 40p">D</div>
	<div style="background-color:lightgrey;width: 40px; height: 40p">E</div>
	<div style="background-color:lightgreen;width: 40px; height: 40p">F</div>
</div>

```css
#main {
    display: flex;
    flex-direction:column;
}
  
#main div {
	width: 40px;
	height: 40px;
}
```

<div id="main" style="display: flex; flex-direction: column;">
	<div style="background-color:coral; width: 40px; height: 40px">A</div>
	<div style="background-color:lightblue; width: 40px; height: 40p">B</div>
	<div style="background-color:khaki;width: 40px; height: 40p">C</div>
	<div style="background-color:pink;width: 40px; height: 40p">D</div>
	<div style="background-color:lightgrey;width: 40px; height: 40p">E</div>
	<div style="background-color:lightgreen;width: 40px; height: 40p">F</div>
</div>

```css
#main {
    display: flex;
    flex-direction:column-reverse;
}
  
#main div {
	width: 40px;
	height: 40px;
}
```

<div id="main" style="display: flex; flex-direction: column-reverse;">
	<div style="background-color:coral; width: 40px; height: 40px">A</div>
	<div style="background-color:lightblue; width: 40px; height: 40p">B</div>
	<div style="background-color:khaki;width: 40px; height: 40p">C</div>
	<div style="background-color:pink;width: 40px; height: 40p">D</div>
	<div style="background-color:lightgrey;width: 40px; height: 40p">E</div>
	<div style="background-color:lightgreen;width: 40px; height: 40p">F</div>
</div>

```css
#main {
    display: flex;
    flex-direction:initial;
}
  
#main div {
	width: 40px;
	height: 40px;
}
```

<div id="main" style="display: flex; flex-direction: initial;">
	<div style="background-color:coral; width: 40px; height: 40px">A</div>
	<div style="background-color:lightblue; width: 40px; height: 40p">B</div>
	<div style="background-color:khaki;width: 40px; height: 40p">C</div>
	<div style="background-color:pink;width: 40px; height: 40p">D</div>
	<div style="background-color:lightgrey;width: 40px; height: 40p">E</div>
	<div style="background-color:lightgreen;width: 40px; height: 40p">F</div>
</div>
---

## flex-wrap

```css
flex-wrap: nowrap|wrap|wrap-reverse|initial|inherit;
```

- *nowrap*：默认值。规定灵活的项目不拆行或不拆列。
- *wrap*：规定灵活的项目在必要的时候拆行或拆列。
- *wrap-reverse*：规定灵活的项目在必要的时候拆行或拆列，但是以相反的顺序。
- *initial*：设置该属性为它的默认值。
- *inherit*：从父元素继承该属性。

```css
#main {
    width: 200px;
    height: 200px;
    border: 1px solid #c3c3c3;
    display: -webkit-flex; /* Safari */
    -webkit-flex-wrap: wrap; /* Safari 6.1+ */
    display: flex;
    flex-wrap: wrap;
}
#main div {
    width: 50px;
    height: 50px;
}
```

<div id="main" style="width: 200px; height: 200px; border: 1px solid #c3c3c3; display: flex; flex-wrap: wrap;">
    <div style="background-color:coral; width: 40px; height: 40px">A</div>
	<div style="background-color:lightblue; width: 40px; height: 40px;">B</div>
	<div style="background-color:khaki;width: 40px; height: 40px;">C</div>
	<div style="background-color:pink;width: 40px; height: 40px;">D</div>
	<div style="background-color:lightgrey;width: 40px; height: 40px;">E</div>
	<div style="background-color:lightgreen;width: 40px; height: 40px;">F</div>
</div>
---

## align-content

```css
align-content: stretch|center|flex-start|flex-end|space-between|space-around|initial|inherit;
```

| 值            | 描述                                                         |
| :------------ | :----------------------------------------------------------- |
| stretch       | 默认值。元素被拉伸以适应容器。各行将会伸展以占用剩余的空间。如果剩余的空间是负数，该值等效于'flex-start'。在其它情况下，**剩余空间被所有行平分**，以扩大它们的侧轴尺寸。 |
| center        | 元素位于容器的中心。**各行向弹性盒容器的中间位置堆叠**。各行两两紧靠住同时在弹性盒容器中居中对齐，保持弹性盒容器的侧轴起始内容边界和第一行之间的距离与该容器的侧轴结束内容边界与第最后一行之间的距离相等。（如果剩下的空间是负数，则各行会向两个方向溢出的相等距离。） |
| flex-start    | 元素位于容器的开头。**各行向弹性盒容器的起始位置堆叠**。弹性盒容器中第一行的侧轴起始边界紧靠住该弹性盒容器的侧轴起始边界，之后的每一行都紧靠住前面一行。 |
| flex-end      | 元素位于容器的结尾。各行向弹性盒容器的结束位置堆叠。弹性盒容器中最后一行的侧轴起结束界紧靠住该弹性盒容器的侧轴结束边界，之后的每一行都紧靠住前面一行。 |
| space-between | 元素位于各行之间留有空白的容器内。**各行在弹性盒容器中平均分布**。如果剩余的空间是负数或弹性盒容器中只有一行，该值等效于'flex-start'。在其它情况下，第一行的侧轴起始边界紧靠住弹性盒容器的侧轴起始内容边界，最后一行的侧轴结束边界紧靠住弹性盒容器的侧轴结束内容边界，剩余的行则按一定方式在弹性盒窗口中排列，以保持两两之间的空间相等。 |
| space-around  | 元素位于各行之前、之间、之后都留有空白的容器内。各行在弹性盒容器中平均分布，两端保留子元素与子元素之间间距大小的一半。如果剩余的空间是负数或弹性盒容器中只有一行，该值等效于'center'。在其它情况下，各行会按一定方式在弹性盒容器中排列，以保持两两之间的空间相等，同时第一行前面及最后一行后面的空间是其他空间的一半。 |
| initial       | 设置该属性为它的默认值。                                     |
| inherit       | 从父元素继承该属性。                                         |

`align-content` 属性在弹性容器内的各项没有占用交叉轴上所有可用的空间时对齐容器内的各项（垂直）。

**提示：**使用 `justify-content` 属性对齐主轴上的各项（水平）。

**注意：**容器内必须有多行的项目，该属性才能渲染出效果。

````css
#main {
    width: 70px;
    height: 300px;
    border: 1px solid #c3c3c3;
    display: flex;
    flex-wrap: wrap;
    align-content: stretch;
}
#main div {
    width: 70px;
    height: 70px;
}
````

<div id="main" style="width: 70px; height: 300px; border: 1px solid #c3c3c3; display: flex; flex-wrap: wrap; align-content: stretch">
  <div style="background-color:coral; width: 70px; height: 70px;"></div>
  <div style="background-color:lightblue; width: 70px; height: 70px;"></div>
  <div style="background-color:pink; width: 70px; height: 70px;"></div>
</div>

```css
#main {
    width: 70px;
    height: 300px;
    border: 1px solid #c3c3c3;
    display: flex;
    flex-wrap: wrap;
    align-content: center;
}
#main div {
    width: 70px;
    height: 70px;
}
```

<div id="main" style="width: 70px; height: 300px; border: 1px solid #c3c3c3; display: flex; flex-wrap: wrap; align-content: center">
  <div style="background-color:coral; width: 70px; height: 70px;"></div>
  <div style="background-color:lightblue; width: 70px; height: 70px;"></div>
  <div style="background-color:pink; width: 70px; height: 70px;"></div>
</div>

```css
#main {
    width: 70px;
    height: 300px;
    border: 1px solid #c3c3c3;
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
}
#main div {
    width: 70px;
    height: 70px;
}
```

<div id="main" style="width: 70px; height: 300px; border: 1px solid #c3c3c3; display: flex; flex-wrap: wrap; align-content: flex-start">
  <div style="background-color:coral; width: 70px; height: 70px;"></div>
  <div style="background-color:lightblue; width: 70px; height: 70px;"></div>
  <div style="background-color:pink; width: 70px; height: 70px;"></div>
</div>
```css
#main {
    width: 70px;
    height: 300px;
    border: 1px solid #c3c3c3;
    display: flex;
    flex-wrap: wrap;
    align-content: flex-end;
}
#main div {
    width: 70px;
    height: 70px;
}
```

<div id="main" style="width: 70px; height: 300px; border: 1px solid #c3c3c3; display: flex; flex-wrap: wrap; align-content: flex-end">
  <div style="background-color:coral; width: 70px; height: 70px;"></div>
  <div style="background-color:lightblue; width: 70px; height: 70px;"></div>
  <div style="background-color:pink; width: 70px; height: 70px;"></div>
</div>
```css
#main {
    width: 70px;
    height: 300px;
    border: 1px solid #c3c3c3;
    display: flex;
    flex-wrap: wrap;
    align-content: space-between;
}
#main div {
    width: 70px;
    height: 70px;
}
```

<div id="main" style="width: 70px; height: 300px; border: 1px solid #c3c3c3; display: flex; flex-wrap: wrap; align-content: space-between">
  <div style="background-color:coral; width: 70px; height: 70px;"></div>
  <div style="background-color:lightblue; width: 70px; height: 70px;"></div>
  <div style="background-color:pink; width: 70px; height: 70px;"></div>
</div>

```css
#main {
    width: 70px;
    height: 300px;
    border: 1px solid #c3c3c3;
    display: flex;
    flex-wrap: wrap;
    align-content: space-round;
}
#main div {
    width: 70px;
    height: 70px;
}
```

<div id="main" style="width: 70px; height: 300px; border: 1px solid #c3c3c3; display: flex; flex-wrap: wrap; align-content: space-round">
  <div style="background-color:coral; width: 70px; height: 70px;"></div>
  <div style="background-color:lightblue; width: 70px; height: 70px;"></div>
  <div style="background-color:pink; width: 70px; height: 70px;"></div>
</div>
---

## align-items

```css
align-items: stretch|center|flex-start|flex-end|baseline|initial|inherit;
```

|            |                                                              |
| :--------- | :----------------------------------------------------------- |
| 值         | 描述                                                         |
| stretch    | 默认值。元素被拉伸以适应容器。如果指定侧轴大小的属性值为'auto'，则其值会使项目的边距盒的尺寸尽可能接近所在行的尺寸，但同时会遵照'min/max-width/height'属性的限制。 |
| center     | 元素位于容器的中心。弹性盒子元素在该行的侧轴（纵轴）上居中放置。（如果该行的尺寸小于弹性盒子元素的尺寸，则会向两个方向溢出相同的长度）。 |
| flex-start | 元素位于容器的开头。弹性盒子元素的侧轴（纵轴）起始位置的边界紧靠住该行的侧轴起始边界。 |
| flex-end   | 元素位于容器的结尾。弹性盒子元素的侧轴（纵轴）起始位置的边界紧靠住该行的侧轴结束边界。 |
| baseline   | 元素位于容器的基线上。如弹性盒子元素的行内轴与侧轴为同一条，则该值与'flex-start'等效。其它情况下，该值将参与基线对齐。 |
| initial    | 设置该属性为它的默认值。                                     |
| inherit    | 从父元素继承该属性。                                         |

定义flex子项在flex容器的当前行的侧轴（纵轴）方向上的对齐方式。

```css
#main {
    width: 220px;
    height: 300px;
    border: 1px solid black;
    display: flex;
    align-items: stretch;
}

#main div {
   flex: 1;
}
```

<div id="main" style="width: 220px; height: 300px; border: 1px solid black; display: flex; align-items: stretch;">
  <div style="background-color:coral; flex: 1;">RED</div>
  <div style="background-color:lightblue; flex: 1;">BLUE</div>
  <div style="background-color:lightgreen; flex: 1;">Green div with more content.</div>
</div>

```css
#main {
    width: 220px;
    height: 300px;
    border: 1px solid black;
    display: flex;
    align-items: center;
}

#main div {
   flex: 1;
}
```

<div id="main" style="width: 220px; height: 300px; border: 1px solid black; display: flex; align-items: center;">
  <div style="background-color:coral; flex: 1;">RED</div>
  <div style="background-color:lightblue; flex: 1;">BLUE</div>
  <div style="background-color:lightgreen; flex: 1;">Green div with more content.</div>
</div>

```css
#main {
    width: 220px;
    height: 300px;
    border: 1px solid black;
    display: flex;
    align-items: flex-start;
}

#main div {
   flex: 1;
}
```

<div id="main" style="width: 220px; height: 300px; border: 1px solid black; display: flex; align-items: flex-start;">
  <div style="background-color:coral; flex: 1;">RED</div>
  <div style="background-color:lightblue; flex: 1;">BLUE</div>
  <div style="background-color:lightgreen; flex: 1;">Green div with more content.</div>
</div>

```css
#main {
    width: 220px;
    height: 300px;
    border: 1px solid black;
    display: flex;
    align-items: flex-end;
}

#main div {
   flex: 1;
}
```

<div id="main" style="width: 220px; height: 300px; border: 1px solid black; display: flex; align-items: flex-end;">
  <div style="background-color:coral; flex: 1;">RED</div>
  <div style="background-color:lightblue; flex: 1;">BLUE</div>
  <div style="background-color:lightgreen; flex: 1;">Green div with more content.</div>
</div>

```css
#main {
    width: 220px;
    height: 300px;
    border: 1px solid black;
    display: flex;
    align-items: baseline;
}

#main div {
   flex: 1;
}
```

<div id="main" style="width: 220px; height: 300px; border: 1px solid black; display: flex; align-items: baseline;">
  <div style="background-color:coral; flex: 1;">RED</div>
  <div style="background-color:lightblue; flex: 1;">BLUE</div>
  <div style="background-color:lightgreen; flex: 1;">Green div with more content.</div>
</div>
---

## align-self

```css
align-self: auto|stretch|center|flex-start|flex-end|baseline|initial|inherit;
```

`align-self `属性定义flex子项单独在侧轴（**纵轴**）方向上的对齐方式。

**注意：**`align-self` 属性可重写灵活容器的 `align-items` 属性。

```css
#main {
    width: 220px;
    height: 300px;
    border: 1px solid black;
    display: flex;
    align-items: flex-start;
}

#main div {
    flex: 1;
}

#myBlueDiv {
    align-self: center;
}
```

<div id="main" style="width: 220px; height: 300px; border: 1px solid black; display: flex; align-items: flex-start;">
  <div style="background-color:coral;flex: 1;">RED</div>
  <div style="background-color:lightblue;flex: 1;align-self: center">BLUE</div>
  <div style="background-color:lightgreen;flex: 1">Green div with more content.</div>
</div>
---

## justify-content

```css
justify-content: flex-start|flex-end|center|space-between|space-around|initial|inherit;
```

`justify-content `用于设置或检索弹性盒子元素在主轴（横轴）方向上的对齐方式。

**提示：**使用 `align-content` 属性对齐交叉轴上的各项（垂直）。

```css
#main {
    width: 400px;
    height: 150px;
    border: 1px solid #c3c3c3;
    display: flex;
    justify-content: space-around;
}

#main div {
    width: 70px;
    height: 70px;
}
```

<div id="main" style="width: 400px; height: 150px; border: 1px solid #c3c3c3; display: flex;justify-content: space-around;">
  <div style="background-color:coral; width: 70px; height: 70px;"></div>
  <div style="background-color:lightblue; width: 70px; height: 70px;"></div>
  <div style="background-color:khaki; width: 70px; height: 70px;"></div>
  <div style="background-color:pink; width: 70px; height: 70px;"></div>
</div>
---

## order

```css
order: number|initial|inherit;
```

- *number*：默认值是 0。规定灵活项目的顺序。

order 属性 设置或检索弹性盒模型对象的子元素出现的順序。。

**注意：**如果元素不是弹性盒对象的元素，则 order 属性不起作用。

```css
#main {
    width: 400px;
    height: 150px;
    border: 1px solid #c3c3c3;
    display: -webkit-flex; /* Safari */
    display: flex;
}

#main div {
    width: 70px;
    height: 70px;
}
div#myRedDIV   {order: 2;}
div#myBlueDIV  {order: 4;}
div#myGreenDIV {order: 3;}
div#myPinkDIV  {order: 1;}
```

```html
<div id="main">
  <div style="background-color:coral;" id="myRedDIV"></div>
  <div style="background-color:lightblue;" id="myBlueDIV"></div>
  <div style="background-color:lightgreen;" id="myGreenDIV"></div>
  <div style="background-color:pink;" id="myPinkDIV"></div>
</div>
```

<div id="main" style="width: 400px; height: 150px; border: 1px solid #c3c3c3; display: flex;">
  <div style="background-color:coral; width: 70px; height: 70px; order: 2;" id="myRedDIV"></div>
  <div style="background-color:lightblue; width: 70px; height: 70px; order: 4;" id="myBlueDIV"></div>
  <div style="background-color:lightgreen; width: 70px; height: 70px; order: 3;" id="myGreenDIV"></div>
  <div style="background-color:pink; width: 70px; height: 70px; order: 1;" id="myPinkDIV"></div>
</div>

