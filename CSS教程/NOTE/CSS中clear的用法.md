# CSS中clear：left/right的用法

## 一、理解clear: left/clear: right

当想到`clear: left`的时候，自然会认为是“**清除左浮动**”，`clear: right`是**清除右浮动**。

其实现在想想，这样的理解与表示是不严谨的欠考虑的。

一般，现在中文圈流传的表述是：

```css
 clear: none | left | right | both
```

- *none* : 默认值。允许两边都可以有浮动对象
- *left* : 不允许左边有浮动对象
- *right* : 不允许右边有浮动对象
- *both* : 不允许有浮动对象

w3.org官方的解释是：**「元素盒子的边不能和前面的浮动元素相邻」**。

我个人觉得官方解释更好一点。

无论是我“清除左/右浮动”，还是业界流传的“不允许左/右边有浮动对象”，其意思都是，设置的clear的元素让浮动元素如何如何。也就是我让别人如何如何~~大家可以仔细体会，细细感受下……

而官方的说法则是“设置了clear的元素不能怎样怎样”。也就是我自己如何如何~~大家可以再次感受下……

为何官方解释更好呢？难道是“己所不欲勿施于人”的缘故？哈，这个解释赞的，方便记忆。更通俗的原因是：

务必记住这句话：“`float`是魔鬼，会影响其他相邻元素；但是`clear`是小白，其只会影响自身，不会对其他相邻元素造成影响！”

但是，官方的解释似乎拗口，缺少点灵性。于是，我根据自己的感性认知，做了如下理解：

```css
clear: none | left | right | both
```

- *none* : 默认值。允许两边都可以有浮动对象
- *left* : 左侧抗浮动
- *right* : 右侧抗浮动
- *both* : 两侧抗浮动

“抗”这个拟人化的动词的发起者是设置了`clear`属性的元素，既形象又释义准确。

```css
.clear-title { display: block; padding-top: 15px; clear: both; }
.clear-box { padding: 5px; margin: 8px auto; background-color: #eee; }
.left { float: left; }
.right { float: right; }
.clear-left { clear: left; }
.clear-right { clear: right; }
.clear-both { clear: both; }
```

```html
<strong class="clear-title">clear: left, 左侧抗浮动，右侧沦陷</strong>
<div class="clear-box">
    <img src="//image.zhangxinxu.com/image/study/s/s128/mm1.jpg" class="left">
    <div class="clear-left">我不喜欢你，我不要和你在一起~</div>
</div>
<div class="clear-box">
    <img src="//image.zhangxinxu.com/image/study/s/s128/mm3.jpg" class="right">
    <div class="clear-left">我不喜欢你，我不要和你在一起~</div>
</div>

<strong class="clear-title">clear: right, 右侧抗浮动，左侧沦陷</strong>
<div class="clear-box">
    <img src="//image.zhangxinxu.com/image/study/s/s128/mm1.jpg" class="left">
    <div class="clear-right">我不喜欢你，我不要和你在一起~</div>
</div>
<div class="clear-box">
    <img src="//image.zhangxinxu.com/image/study/s/s128/mm3.jpg" class="right">
    <div class="clear-right">我不喜欢你，我不要和你在一起~</div>
</div>

<strong class="clear-title">clear: left; float: left, 垂直环绕布局</strong>
<div class="clear-box">
    <img src="//image.zhangxinxu.com/image/study/s/s128/mm1.jpg" class="left">
    <img src="//image.zhangxinxu.com/image/study/s/s128/mm3.jpg" class="left clear-left">
    <div>我不喜欢你，我不要和你在一起~</div>
</div>

<strong class="clear-title">clear: right; float: right, 垂直环绕布局</strong>
<div class="clear-box">
    <img src="//image.zhangxinxu.com/image/study/s/s128/mm1.jpg" class="right">
    <img src="//image.zhangxinxu.com/image/study/s/s128/mm3.jpg" class="right clear-right">
    <div>我不喜欢你，我不要和你在一起~字数不够多，...这里省略1000字...</div>
</div>
```

例如上图所示的`clear: left`作用示意：图片左浮动，化身魔鬼，要影响后面相邻的元素。一般的元素都逃不了被影响被束缚的命运。除非拥有`clear`技能。例如，这里`clear: left`左侧抗浮动，也就是，左侧的浮动根本就奈何不了我——我**还是原原本本在下面显示。**但是，如果图片是右浮动，则`clear: left`仍逃不过沦陷的命运，**可以看到父级容器的高度塌陷了！**

单纯的`clear: left`就像是招潮蟹，一侧雄起，一侧不举。因此，考虑到通用性，在抗浮动的处理中，我们都是使用`clear: both`. 用意很明显：我不必关心你是左浮动还是右浮动，我都通通免疫。

<p><strong class="clear-title" style="display: block; padding-top: 15px; clear: both;">clear: left, 左侧抗浮动，右侧沦陷</strong></p>
<div class="clear-box" style="padding: 5px; margin: 8px auto; background-color: #eee; ">
    <img src="//image.zhangxinxu.com/image/study/s/s128/mm1.jpg" class="left" style="float:left">
    <div class="clear-left" style="clear: left;">我不喜欢你，我不要和你在一起~</div>
</div>
<div class="clear-box" style="padding: 5px; margin: 8px auto; background-color: #eee; ">
    <img src="//image.zhangxinxu.com/image/study/s/s128/mm3.jpg" class="right" style="float: right">
    <div class="clear-left" style="clear: left;">我不喜欢你，我不要和你在一起~</div>
</div>





---

<p><strong class="clear-title" style="display: block; padding-top: 15px; clear: both;">clear: right, 右侧抗浮动，左侧沦陷</strong></p>
<div class="clear-box" style="padding: 5px; margin: 8px auto; background-color: #eee; ">
    <img src="//image.zhangxinxu.com/image/study/s/s128/mm1.jpg" class="left" style="float:left">
    <div class="clear-left" style="clear: right;">我不喜欢你，我不要和你在一起~</div>
</div>
<div class="clear-box" style="padding: 5px; margin: 8px auto; background-color: #eee; ">
    <img src="//image.zhangxinxu.com/image/study/s/s128/mm3.jpg" class="right" style="float: right">
    <div class="clear-left" style="clear: right;">我不喜欢你，我不要和你在一起~</div>
</div>

---

## 理解CSS clear:both/left/right的含义以及应用

### 一、什么是浮动，标准文档流又是个啥

​    所谓的文档流，指的是元素排版布局过程中，元素会自动从左往右，从上往下的流式排列。并最终窗体自上而下分成一行行, 并在每行中按从左至右的顺序排放元素。脱离文档流即是元素打乱了这个排列，或是从排版中拿走。

   当前所知的脱离文档流的方式有两种：**浮动和定位**。

   在了解什么是浮动之前，  首先要知道，`div`是块级元素，在页面中独占一行，自上而下排列，也就是传说中的流。我们看看下面的效果：

```css
div.container {
    border: 1px solid;
    border-collapse: collapse;
    height: 320px;
    overflow: hidden;
}
div.div1 {
    background: yellow;
    border: 1px solid;
    width: 160px;
    height: 80px;
} 
div.div2 {
    background: #e1c76e;
    border: 1px solid;
    width: 220px;
    height: 80px;
    /*float: left;*/
} 
div.div3 {
    background: firebrick;
    border: 1px solid;
    width: 160px;
    height: 160px;
} 
div.div4 {
    background: forestgreen;
    border: 1px solid;
    width: 100px;
    height: 80px;
}
```

```css
<div class="container">
    <div class="div1">div1</div>
    <div class="div2">div2</div>
    <div class="div3">div3</div>
    <div class="div4">div4</div>
</div>
```

<div class="container" style="border: 1px solid;
    border-collapse: collapse;
    height: 320px;
    overflow: hidden;">
    <div class="div1" style=" background: yellow;
    border: 1px solid;
    width: 160px;
    height: 80px;">div1</div>
    <div class="div2" style="background: #e1c76e;
    border: 1px solid;
    width: 220px;
    height: 80px;
    /*float: left;*/">div2</div>
    <div class="div3" style="background: firebrick;
    border: 1px solid;
    width: 160px;
    height: 160px;">div3</div>
    <div class="div4" style="background: forestgreen;
    border: 1px solid;
    width: 100px;
    height: 80px;">div4</div>
</div>

可以看出，即使*div1*的宽度很小，页面中一行可以容下*div1*和*div2*，*div2*也不会排在*div1*后边，因为`div`元素是独占一行的。以上这些理论，是指标准流中的`div`。无论多么复杂的布局，其基本出发点均是：“如何在一行显示多个`div`元素”。

显然标准流已经无法满足需求，这就要用到浮动。    

​    ***\*浮动可以理解为让某个div元素脱离标准文档流，漂浮在标准文档流之上，和标准文档流不是一个层次。\****

   例如，假设上图中的*div2*左浮动（`float: left`），那么它将脱离标准文档流，但*div1*、*div3*仍然在标准文档流当中，所以*div3*会自动向上移动，占据*div2*的位置，重新组成一个流。如图：

```css
div.div2 {
    background: #e1c76e;
    border: 1px solid;
    width: 220px;
    height: 80px;
    float: left;
} 
```

<div class="container" style="border: 1px solid;
    border-collapse: collapse;
    height: 320px;
    overflow: hidden;">
    <div class="div1" style=" background: yellow;
    border: 1px solid;
    width: 160px;
    height: 80px;">div1</div>
    <div class="div2" style="background: #e1c76e;
    border: 1px solid;
    width: 220px;
    height: 80px;
    float: left;">div2</div>
    <div class="div3" style="background: firebrick;
    border: 1px solid;
    width: 160px;
    height: 160px;">div3
      </div>
    <div class="div4" style="background: forestgreen;
    border: 1px solid;
    width: 100px;
    height: 80px;">div4</div>
</div>

从图中可以看出，由于对*div2*设置左浮动(`float: left;`)，因此它不再属于标准文档流，*div3*自动上移顶替*div2*的位置，div1、div3、div4依次排列，成为一个新的流。又因为浮动是漂浮在标准流之上的，因此*div2*挡住了一部分*div3*，div3看起来变“矮”了。
    这里div2用的是左浮动(`float: left;`)，可以理解为漂浮起来后靠左排列，右浮动(`float: right;`)当然就是靠右排列。这里的靠左、靠右是说页面的左、右边缘。
    如果我们把*div2*采用右浮动，会是如下效果：

```css
div.div2 {
    background: #e1c76e;
    border: 1px solid;
    width: 220px;
    height: 80px;
    float: right;
} 
```

<div class="container" style="border: 1px solid;
    border-collapse: collapse;
    height: 320px;
    overflow: hidden;">
    <div class="div1" style=" background: yellow;
    border: 1px solid;
    width: 160px;
    height: 80px;">div1</div>
    <div class="div2" style="background: #e1c76e;
    border: 1px solid;
    width: 220px;
    height: 80px;
    float: right;">div2</div>
    <div class="div3" style="background: firebrick;
    border: 1px solid;
    width: 160px;
    height: 160px;">div3
      </div>
    <div class="div4" style="background: forestgreen;
    border: 1px solid;
    width: 100px;
    height: 80px;">div4</div>
</div>

此时*div2*靠页面右边缘排列，不再遮挡*div3*，读者可以清晰的看到上面所讲的*div1*、*div3*组成的流。以上我们看到的是只有一个`div`设置浮动，那么如果设置多个`div`浮动，效果又是怎么样呢？我设置*div2*右浮动，*div3*左浮动，效果如下：

```css
div.div2 {
    background: #e1c76e;
    border: 1px solid;
    width: 220px;
    height: 80px;
    float: right;
} 
div.div3 {
    background: firebrick;
    border: 1px solid;
    width: 160px;
    height: 160px;
    float: left;
} 
div.div4 {
    background: forestgreen;
    border: 1px solid;
    width: 100px;
    height: 80px;
    float: left;
}
```

<div class="container" style="border: 1px solid;
    border-collapse: collapse;
    height: 320px;
    overflow: hidden;">
    <div class="div1" style=" background: yellow;
    border: 1px solid;
    width: 160px;
    height: 80px;">div1</div>
    <div class="div2" style="background: #e1c76e;
    border: 1px solid;
    width: 220px;
    height: 80px;
    float: right;">div2</div>
    <div class="div3" style="background: firebrick;
    border: 1px solid;
    width: 160px;
    height: 160px;float: left;">div3</div>
    <div class="div4" style="background: forestgreen;
    border: 1px solid;
    width: 100px;
    height: 80px;float: left;">div4</div>
</div>

 同理，由于div2、div3浮动，它们不再属于标准文档流，因此div4会自动上移，与div1组成一个“新”标准流，而浮动是漂浮在标准文档流之上，因此div2又挡住了div4。

​    当同时对div2、div3设置浮动之后，div3会跟随在div2之后，div2在每个例子中都是浮动的，但并没有跟随到div1之后。因此，我们可以得出一个重要结论：
​    假如某个div元素A是浮动的，如果A元素上一个元素也是浮动的，那么A元素会跟随在上一个元素的后边(如果一行放不下这两个元素，那么A元素会被挤到下一行)；如果A元素上一个元素是标准流中的元素，那么A的相对垂直位置不会改变，也就是说A的顶部总是和上一个元素的底部对齐。

---







