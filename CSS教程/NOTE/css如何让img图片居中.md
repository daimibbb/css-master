# css如何让img图片居中

首先我们来了解一下`display`属性实现图片居中的两种方法是什么？

1、利用`display`的`table-cell`属性值，再配合`text-align: center`;与`vertical-align: middle`;设置图片居中

2、设置`display: flex`;，利用弹性布局`flex`来设置img图片的居中

下面我们通过简单的代码示例，详细了解一下这两种方法是怎么实现图片居中的。

#### 1、利用`display:table-cell`来实现img标签图片的水平和垂直居中

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>img图片居中</title>
    <style>
        .demo{
            width: 400px;
            height: 300px;
            border: 1px dashed #000;
            display: table-cell ; /*主要是这个属性*/
            vertical-align: middle;
            text-align: center;
        }
        .demo img{
            width: 200px;
            height: 150px;
        }
    </style>
</head>
<body>
<div class="demo">
    <img src="data/1.jpg" alt="demo"/>
</div>
</body>
</html>
```

**说明：**

在`demo`盒子中设置`display: table-cell;`会让`demo`盒子作为一个表格单元格显示（类似` <td>` 和` <th>`），在设置`text-align: center;`就会让`img`图片水平居中，设置`vertical-align: middle;`让`img`图片垂直居中。

#### 2、弹性布局`flex`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>img图片居中</title>
    <style>
        *{margin: 0; padding: 0;}
        .demo{
            width: 400px;
            height: 300px;
            margin: 50px auto;
            border: 1px dashed #000;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .demo img{
            width: 200px;
            height: 150px;
        }
    </style>
</head>
<body>
<div class="demo">
    <img src="data/1.jpg" alt="demo"/>
</div>
</body>
</html>
```

说明：

设置`display: flex;`实现`flex`弹性布局，在设置`justify-content: center;`让图片水平居中对齐，设置`align-items: center;`让图片垂直居中对齐。

---

