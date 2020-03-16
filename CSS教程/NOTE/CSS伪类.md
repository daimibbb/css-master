# CSS伪类

`:hover`表示当鼠标选定在`a`标签上时`a`标签的样式变化。

这是css中伪类的使用格式。

伪类（Pseudo classes）是选择符的螺栓，用来指定一个或者与其相关的选择符的状态。它们的形式是`selector:pseudo class { property: value; }`，简单地用一个半角英文冒号（`:`）来隔开选择符和伪类。CSS很多的建议并没有得到浏览器的支持，但有四个可以安全用在超链接上的伪类：

- `:link`用在未访问的连接上。

- `:visited`用在已经访问过的连接上。

- `:active`用于获得焦点（比如，被点击）的连接上。

- `:hover` 用于鼠标光标置于其上的连接。

在Html代码中给出一个超链接

```html
<a href="#">我是一个超链接。</a>
```


设置鼠标悬停的css样式

```css
a:hover {
    color:red; /*设置颜色为红色*/
    font-size:20px; /*字体变大*/
    text-decoration: none; /*去掉下划线*/
}
```

