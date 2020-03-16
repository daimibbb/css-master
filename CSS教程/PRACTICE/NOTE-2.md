## DIV CSS绝对定位布局案例 position布局实例

### 一、用到CSS样式和HTML标签及相应解释 

 1、要用到CSS样式单词及解释

- `position`：绝对定位样式实现DIV定位布局其设置值*absolute*和*relative*应用
- `width`：宽度，设置对象宽度
- `height`：高度，设置对象高度
- `line-height`：行高，设置文本行高
- `left`：设置div对象靠左距离
- `right`：设置div对象靠左距离
- `top`：设置div对象靠左距离
- `bottom`：设置div对象靠左距离
- `background`：背景，设置背景图片和颜色
- `color`：设置字体颜色
- `font-size`：设置字体大小
- `font-weight`：设置字体加粗

2、用到HTML标签及解释

- `div`标签：用于布局结构框架
- ul li标签：用于布局列表型数据列表
  h3标签：用于布局栏目标题

### 三、绝对定位案例

```css
body, div, ul, li, h3 {
    margin: 0;
    padding-left: 5px;
    font-style: normal;
    /* \5B8B\4F53 代表 宋体 */
    font: 12px/22px "\5B8B\4F53", Arial, Helvetica, sans-serif;
}
ol, ul, li {
    list-style-type: none;
}
body {
    color: #fff;
    background: #fff;
    text-align: center;
}
a {
    color: #fff;
    text-decoration: none;
}
/*根据本实例 设置超链接字体与没有超链接字体演示为白色*/
a:hover {
    color: #ba2636;
    text-decoration: underline;
}
#wrapper {
    margin: 0 auto;
    position: relative;
    width: 610px;
    height: 559px;
    background: goldenrod;
}
.box1 {
    background: rgb(133,28,25);
    position: absolute;
    width: 147px;
    height: 140px;
    left: 198px;
    top: 14px;
}
.box2 {
    background: linear-gradient(to right, rgb(75,184,107), rgb(33,140,45));
    position: absolute;
    width: 141px;
    height: 186px;
    left: 31px;
    bottom: 17px;
}
.box3 {
    background: rgb(27,101,133);
    position: absolute;
    width: 132px;
    height: 186px;
    right: 28px;
    bottom: 67px;
}
h3.title {
    height: 32px;
    line-height: 32px;
    font-size: 14px;
    font-weight: bold;
    text-align: left;
}
ul.list {
    text-align: left;
    width: 100%;
    padding-top: 8px;
}
/*加了overflow:hidden防止内容过多后自动换行 隐藏超出内容*/
ul.list li {
    width: 100%;
    text-align: left;
    height: 22px;
    overflow: hidden;
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
<div id="wrapper">
    <div class="box1">
        <h3 class="title">新闻动态</h3>
            <ul class="list">
            <li><a href="http://www.divcss5.com/wenji/w558.shtml">不会程序能学会CSS吗？</a></li>
            <li><a href="http://www.divcss5.com/wenji/w556.shtml">DIVCSS学习难吗？</a></li>
            <li><a href="http://www.divcss5.com/peixun/">我要参加DIVCSS5的培训</a></li>
            <li><a href="http://www.divcss5.com/css-tool/t720.shtml">jQuery所以版本集合整理</a></li>
        </ul>
    </div>
    <div class="box2">
        <h3 class="title">DIVCSS5栏目</h3>
        <ul class="list">
            <li><a href="http://www.divcss5.com/html/">CSS基础教程</a></li>
            <li><a href="http://www.divcss5.com/htmlrumen/">HTML基础教程</a></li>
            <li><a href="http://www.divcss5.com/wenji/">CSS问题</a></li>
            <li><a href="http://www.divcss5.com/css-tool/">CSS制作工具</a></li>
            <li><a href="http://www.divcss5.com/jiqiao/">DIV CSS技巧</a></li>
        <li><a href="http://www.divcss5.com/css-texiao/">DIV+CSS+JS特效</a></li>
    </ul>
    </div>
        <div class="box3">
        <h3 class="title">网站栏目</h3>
        <ul class="list">
            <li><a href="http://www.divcss5.com/cssrumen/">DIV CSS入门</a></li>
            <li><a href="http://www.divcss5.com/htmlrumen/">HTML入门教程</a></li>
            <li><a href="http://www.divcss5.com/shili/">CSS实例</a></li>
            <li><a href="http://www.divcss5.com/">DIVCSS5首页</a></li>
            <li><a href="http://www.divcss5.com/template/">DIV CSS模块模板</a></li>
            <li><a href="http://www.divcss5.com/w3c/">DIV CSS WEB标准</a></li>
        </ul>
    </div>
</div>

</body>
</html>
```


