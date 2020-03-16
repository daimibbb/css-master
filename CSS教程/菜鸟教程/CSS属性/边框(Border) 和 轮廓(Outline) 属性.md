# 边框(Border) 和 轮廓(Outline) 属性

## border

```css
border: border-width border-style border-color
```

- `border-width`：指定边框的宽度
- `border-style`：指定边框的样式
- `border-color`：指定边框的颜色
- `inherit`：指定应该从父元素继承border属性值

```css
p {border: 2px solid red;}
```

<p style="border: 2px solid red; text-align: center;">段落中的一些文本。</p>

## border-bottom

```css
border-bottom: border-bottom-width border-bottom-style border-bottom-color
```

- *border-bottom-width*：指定底部边框宽度
- *border-bottom-style*：指定底部边框样式
- *border-bottom-color*：指定底部边框颜色

```css
p {
    border-style: solid;
    border-bottom: thick dotted #ff0000;
}
```

<p style="border-style: solid;
    border-bottom: thick dotted #ff0000;text-align: center">段落中的一些文本。</p>


## border-bottom-color

```css
border-bottom-color: color|transparent(default)
```

- *color*：指定背景颜色。
- *transparent*：指定边框的颜色应该是透明的。这是默认
- *inherit*：指定边框的颜色，应该从父元素继承

```css
p {
    border-style: solid;
    border-bottom-color: #ff0000;
}
```

<p style="border-style: solid;border-bottom-color: #ff0000;text-align:center">段落中的一些文本。</p>

## border-bottom-style

```css
border-bottom-style: none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset|inherit
```

<table class="reference">
  <tbody><tr>
    <th width="11%" align="left">值</th>
    <th width="76%" align="left">说明</th></tr>  
    <tr>
      <td>none</td>
      <td>指定无边框</td>   
    </tr>
    <tr>
      <td>hidden</td>
      <td>与"none" 相同。不过应用于表时除外，对于表，hidden 用于解决边框冲突。</td>
    </tr>
    <tr>
      <td>dotted</td>
      <td>指定点状边框</td>
    </tr>
    <tr>
      <td>dashed</td>
      <td>指定虚线边框</td>
    </tr>
    <tr>
      <td>solid</td>
      <td>指定实线边框</td>
    </tr>
    <tr>
      <td>double</td>
      <td>指定一个双边框</td>
    </tr>
    <tr>
      <td>groove</td>
      <td>定义双线。双线的宽度等于 border-width 的值</td>
    </tr>
    <tr>
      <td>ridge</td>
      <td>定义三维菱形边框。其效果取决于 border-color 的值</td>
    </tr>
    <tr>
      <td>inset</td>
      <td>定义三维凹边框。其效果取决于 border-color 的值</td>
    </tr>
    <tr>
      <td>outset</td>
      <td>定义三维凸边框。其效果取决于 border-color 的值</td>
    </tr>
    <tr>
      <td>inherit</td>
      <td>指定应该从父元素继承边框样式</td>
    </tr>
</tbody></table>
```css
p {border-style: solid;}
p.none {border-bottom-style: none;}
p.dotted {border-bottom-style: dotted;}
p.dashed {border-bottom-style: dashed;}
p.solid {border-bottom-style: solid;}
p.double {border-bottom-style: double;}
p.groove {border-bottom-style: groove;}
p.ridge {border-bottom-style: ridge;}
p.inset {border-bottom-style: inset;}
p.outset {border-bottom-style: outset;}
```

<p class="none" style="border-style: solid; border-bottom-style: none; text-align: center;">无底边界。</p>
<p class="dotted" style="border-style: solid; border-bottom-style: dotted; text-align: center;">点底边界。</p>
<p class="dashed" style="border-style: solid; border-bottom-style: dashed; text-align: center;">虚线底边界。</p>
<p class="solid" style="border-style: solid; text-align: center;">实线底边界。</p>
<p class="double" style="border-style: solid; border-bottom-style: double; text-align: center;">双线底边界。</p>
<p class="groove" style="border-style: solid; border-bottom-style: groove; text-align: center">凹槽底边界。</p>
<p class="ridge" style="border-style: solid; border-bottom-style: ridge; text-align: center">垄状底边界。</p>
<p class="inset" style="border-style: solid; border-bottom-style: inset; text-align: center">嵌入底边界。</p>
<p class="outset" style="border-style: solid; border-bottom-style: outset; text-align: center">外凸底边界。</p>

## border-bottom-width

```css
border-bottom-width: thin|medium|thick|length|inherit
```

- *thin*：定义细的下边框
- *medium*：默认值。定义中等的下边框
- *thick*：定义粗的下边框
- *length*：允许您自定义下边框的宽度
- *inherit*：规定应该从父元素继承边框宽度

```css
p {
    border-style: solid;
    border-bottom-width: 5px;
}
```

<p style="border-style: solid;
    border-bottom-width: 5px;"><b>注意:</b> "border-bottom-width" 属性单独使用无效. 要先使用 "border-style"属性设置borders .</p>

## border-color

```css
border-color: color1, color2,...|transparent
```

- *color*：指定背景颜色。
- *transparent*：指定边框的颜色应该是透明的。这是默认
- *inherit*：指定边框的颜色，应该从父元素继承

`border-color`属性设置一个元素的四个边框颜色。此属性可以有一到四个值。

实例:

**border-color:红，绿，蓝,粉红色;**

- 上边框是红色
- 右边框是绿色
- 底部边框是蓝
- 左边框是粉红色

**border-color：红，绿，蓝;**

- 上边框是红色
- 左，右边框是绿色
- 底部边框是蓝

**border-color：红，绿;**

- 顶部和底部边框是红色
- 左右边框是绿色

**border-color：红色;**

- 所有四个边框是红色

**注意：**请始终把 `border-style` 属性声明到` border-color` 属性之前。元素必须在您改变其颜色之前获得边框。

```css
p.one{
	border-style: solid;
	border-color: #0000ff;
}
p.two {
	border-style: solid;
	border-color: #ff0000 #0000ff;
}
p.three {
	border-style: solid;
	border-color: #ff0000 #00ff00 #0000ff;
}
p.four{
	border-style: solid;
	border-color: #ff0000 #00ff00 #0000ff rgb(250,0,255);
}
```

<p class="one" style="border-style: solid; border-color: #0000ff; text-align: center;">One-colored border!</p>
<p class="two" style="border-style: solid; border-color: #ff0000 #0000ff; text-align: center;">Two-colored border!</p>
<p class="three" style="border-style: solid; border-color: #ff0000 #00ff00 #0000ff; text-align: center;">Three-colored border!</p>
<p class="four" style="border-style: solid; border-color: #ff0000 #00ff00 #0000ff rgb(255,0,255); text-align: center;" >Four-colored border!</p>

## border-left

```css
border-left: border-left-width border-left-style border-left-color
```

- *border-left-width*：规定左边框的宽度。

- *border-left-style*：规定左边框的样式。

- *border-left-color*：规定左边框的颜色。

- *inherit*：规定应该从父元素继承 border-left 属性的设置。

```css
p {
    border-style: solid;
    border-left: thick double #ff0000;
}
```

<p style="border-style: solid; border-left: thick double #ff0000; text-align: center;">This is some text in a paragraph.</p>

## border-left-color

```css
border-left-color: color|transparent
```

```css
p  {
    border-style: solid;
    border-left-color: #ff0000;
}
```

<p style="border-style: solid; border-left-color: #ff0000; text-align: center;">This is some text in a paragraph.</p>

## border-left-style

```css
border-left-style: none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset|inherit
```

```css
p.none {border-left-style: none;}
p.dotted {border-left-style: dotted;}
p.dashed {border-left-style: dashed;}
p.solid {border-left-style: solid;}
p.double {border-left-style: double;}
p.groove {border-left-style: groove;}
p.ridge {border-left-style: ridge;}
p.inset {border-left-style: inset;}
p.outset {border-left-style: outset;}
```

## border-left-width

```css
border-left-width: thin|medium|thick|length|inherit
```

```css
p {
	border-style: solid;
	border-left-width: 5px;
}
```

<p style="border-style: solid; border-left-width: 5px"><b>注意:</b>"border-left-width" 单独使用没有效果.要先使用 "border-style" 属性设置borders.</p>

## border-right

```css
border-right: border-right-width border-right-style border-right-color
```

## border-right-color

```css
border-right-color: color|transparent
```

## border-right-style

```css
border-right-style: none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset|inherit
```

## border-right-width

```css
border-right-width: thin|medium|thick|length|inherit
```

## border-style

```css
border-style: none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset|inherit
```

`border-style`属性设置一个元素的四个边框的样式。此属性可以有一到四个值。

实例:

**border-style:dotted solid double dashed;**

- 上边框是点状
- 右边框是实线
- 下边框是双线
- 左边框是虚线

**border-style:dotted solid double;**

- 上边框是点状
- 右边框和左边框是实线
- 下边框是双线

**border-style:dotted solid;**

- 上边框和下边框是点状
- 右边框和左边框是实线

**border-style:dotted;**

- 所有4个边框都是点状

## border-top

```css
border-top: border-top-width border-top-style border-top-color
```

<p style="border-style: solid; border-top: thick double #ff0000; text-align: center">段落中的一些文本。</p>

## border-top-color

```css
border-top-color: color|transparent
```

## border-top-style

```css
border-top-style: none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset|inherit
```

## border-top-width

```css
border-top-width: thin|medium|thick|length|inherit
```

## border-width

```css
border-width: thin|medium|thick|length|inherit
```

```css
p.one {
	border-style: solid;
	border-width: thin;
}
p.two {
	border-style: solid;
	border-width: medium;
}
p.three {
	border-style: solid;
	border-width: thick;
}
```

<p class="one" style="border-style: solid; border-width: thin; text-align: center">一些文本。</p>
<p class="two" style="border-style: solid; border-width: medium; text-align: center">一些文本。</p>
<p class="three" style="border-style: solid; border-width: thick; text-align: center">一些文本。</p>

## outline

```css
outline: outline-color outline-style outline-width
```

```css
p {
	border: 1px solid red;
	outline: green dotted thick;
}
```

<p style="border: 1px solid red; outline: green dotted thick; text-align: center">一些文本。</p>

## outline-color

```css
outline-color: color|invert|inherit
```

| 值      | 描述                                                         |
| :------ | :----------------------------------------------------------- |
| *color* | 指定轮廓颜色。                                               |
| invert  | 默认。执行颜色反转（逆向的颜色）。可使轮廓在不同的背景颜色中都是可见。 |
| inherit | 规定应该从父元素继承轮廓颜色的设置。                         |

## outline-style

```css
outline-style: none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset|inherit
```

## outline-width

```css
outline-width: thin|medium|thick|length|inherit
```

## border-bottom-left-radius

```css
border-bottom-left-radius: length|%;
```

为`div`元素的左下角添加圆角边框：

```css
div {
    border: 2px solid;
    border-bottom-left-radius: 2em;
}
```

<div style="border: 2px solid; padding: 10px; background: #ddd; border-bottom-left-radius: 2em; text-align: center;"><span style="color: blue">border-bottom-left-radius</span>  属性允许您向左下角添加圆角边框。</div>

## border-bottom-right-radius

```css
border-bottom-right-radius: length|%;
```

```css
div {
    border:2px solid;
    border-bottom-right-radius: 2em;
}
```

<div style="border: 2px solid; padding: 10px; background: #ddd; border-bottom-right-radius: 2em; text-align: center;"><span style="color: blue">border-bottom-right-radius</span>  属性允许您向右下角添加圆角边框。</div>

## border-image

```css
border-image: source slice width outset repeat|initial|inherit;
```

| 值                    | 描述                                                         |
| :-------------------- | :----------------------------------------------------------- |
| *border-image-source* | 用于指定要用于绘制边框的图像的位置                           |
| *border-image-slice*  | 图像边界向内偏移                                             |
| *border-image-width*  | 图像边界的宽度                                               |
| *border-image-outset* | 用于指定在边框外部绘制 border-image-area 的量                |
| *border-image-repeat* | 用于设置图像边界是否应重复（*repeat*）、拉伸（*stretch*）或铺满（*round*）。 |

```css
#borderimg1 { 
    border: 10px solid transparent;
    padding: 15px;
    border-image: url(border.png) 30 round;
}

#borderimg2 { 
    border: 10px solid transparent;
    padding: 15px;
    border-image: url(border.png) 30 stretch;
}
```

`border-image `属性用于指定一个元素的边框图像。

<p id="borderimg1" style="border: 10px solid transparent; padding: 15px; border-image: url(https://www.runoob.com/images/border.png) 30 round">在这里，图像平铺（重复），以填补该地区。</p>
<p id="borderimg2" style="border: 10px solid transparent; padding: 15px; border-image: url(https://www.runoob.com/images/border.png) 30 stretch">在这里，图像被拉伸以填补该地区</p>

<p>这是原始图片:</p><img src="https://www.runoob.com/images/border.png">

## border-image-outset

```css
border-image-outset: length|number;
```

| 值       | 描述                                                |
| :------- | :-------------------------------------------------- |
| *length* | 设置边框图像与边框（border-image）的距离，默认为0。 |
| *number* | 代表相应的 border-width 的倍数                      |

```css
#myDIV {
    border: 15px solid transparent;
    padding: 15px;   
    border-image: url(border.png);
    border-image-slice: 30;
    border-image-repeat: round;
    border-image-outset:10px 5px 2px;
}
```

<div id="myDIV" style="border: 15px solid transparent; padding: 15px; border-image: url(https://www.runoob.com/images/border.png); border-image-slice: 30; border-image-repeat: round; border-image-outset: 10px 5px 2px'">
	<b>Note:</b> Internet Explorer 10 及其更早版本不支持 border-image-outset 属性。
  </div>

```css
#myDIV {
    border: 15px solid transparent;
    padding: 15px;   
    border-image: url(border.png);
    border-image-slice: 30;
    border-image-repeat: round;
    border-image-outset: 1 0 1 1;
}
```

<div id="myDIV" style="border: 15px solid transparent; padding: 15px; border-image: url(https://www.runoob.com/images/border.png); border-image-slice: 30; border-image-repeat: round; border-image-outset: 1 0 1 1'">
	<b>Note:</b> Internet Explorer 10 及其更早版本不支持 border-image-outset 属性。
  </div>

## border-image-repeat

```css
border-image-repeat: stretch|repeat|round|initial|inherit;
```

| 值        | 描述                                                         |
| :-------- | :----------------------------------------------------------- |
| *stretch* | 默认值。拉伸图像来填充区域                                   |
| *repeat*  | 平铺（repeated）图像来填充区域。                             |
| *round*   | 类似 repeat 值。如果无法完整平铺所有图像，则对图像进行缩放以适应区域。 |
| *space*   | 类似 repeat 值。如果无法完整平铺所有图像，扩展空间会分布在图像周围 |
| *initial* | 将此属性设置为默认值。                                       |
| *inherit* | 从父元素中继承该属性。                                       |

```css
div {
    background-color: lightgrey;
    border: 30px solid transparent;
    border-image: url('border.png');
    border-image-slice: 30;
    border-image-repeat: repeat;
}
```

<div style="border: 10px solid transparent; border-image: url(https://www.runoob.com/images/border.png); border-image-slice: 30; border-image-repeat: repeat;">
    DIV 使用图像边框。
</div>

## border-image-slice

```css
border-image-slice: number|%|fill;
```

```css
div {
    border-image-source: url(border.png);
    border-image-slice: 50% 50%;
}
```

`border-image` 切割 image 的参数的具体意义，解析如下图：

![img](https://www.runoob.com/wp-content/uploads/2013/08/241f95cad1c8a786fa8afe6f6109c93d70cf502a.gif)

根据图示，切割完 border 的背景切片后，并且也已经设置了 border 的宽度（重要）。将相应的切片填充到 border 的相应位置。

需要注意的是：不论 border 的宽度设置的多大，后面切割的参数都是根据 border-image 引入图片的尺寸设置的参数, 或者说是根据引入图片大小设置的切割参数。

切割后的四周的八个切片，四个角根据 border 设置的大小全尺寸自动缩放显示到 border 对应的四个角。

除四个角外的其他中间切片（上中，右中间，下中，左中间），可以根据设置做拉伸或重复的设置操作显示到对应的 border 位置。

## border-image-source

```css
border-image-source: none|image;
```

```css
div {
border-image-source: url(border.png);
}
```

## border-image-width

```css
border-image-width: number|%|auto;
```

| 值       | 说明                                                         |
| :------- | :----------------------------------------------------------- |
| *number* | 表示相应的border-width 的倍数                                |
| *%*      | 边界图像区域的大小：横向偏移的宽度的面积，垂直偏移的高度的面积 |
| auto     | 如果指定了，宽度是相应的image slice的内在宽度或高度          |

```css
div {
    border-image-source: url(border.png);
    border-image-width: 30 30;
}
```

## border-radius

```css
border-radius: 1-4 length|% / 1-4 length|%;
```

**注意:** 每个半径的四个值的顺序是：左上角，右上角，右下角，左下角。如果省略左下角，右上角是相同的。如果省略右下角，左上角是相同的。如果省略右上角，左上角是相同的。

```css
div {
    border-radius: 2em;

    is equivalent to:

    border-top-left-radius: 2em;
    border-top-right-radius: 2em;
    border-bottom-right-radius: 2em;
    border-bottom-left-radius: 2em;
}
```

```css
div {
    border-radius: 2em 1em 4em / 0.5em 3em;

    is equivalent to:

    border-top-left-radius: 2em 0.5em;
    border-top-right-radius: 1em 3em;
    border-bottom-right-radius: 4em 0.5em;
    border-bottom-left-radius: 1em 3em;
}
```

## box-shadow

```css
box-shadow: h-shadow v-shadow blur spread color inset;
```

**注意：**boxShadow 属性把一个或多个下拉阴影添加到框上。该属性是一个用逗号分隔阴影的列表，每个阴影由 2-4 个长度值、一个可选的颜色值和一个可选的 inset 关键字来规定。省略长度的值是 0。 

| 值         | 说明                                         |
| :--------- | :------------------------------------------- |
| *h-shadow* | 必需的。水平阴影的位置。允许负值             |
| *v-shadow* | 必需的。垂直阴影的位置。允许负值             |
| *blur*     | 可选。模糊距离                               |
| *spread*   | 可选。阴影的大小                             |
| *color*    | 可选。阴影的颜色。                           |
| inset      | 可选。从外层的阴影（开始时）改变阴影内侧阴影 |

```css
div {
	width: 300px;
	height: 100px;
	background-color: yellow;
	box-shadow: 10px 10px 5px #888888;
}
```

<div style="width: 300px; height: 100px; background-color: yellow; box-shadow: 10px 10px 5px #888888; margin: auto"></div>