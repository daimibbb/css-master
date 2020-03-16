# 盒子(Box) 属性

## overflow-x

```css
verflow-x: visible|hidden|scroll|auto|no-display|no-content;
```

如果内容溢出了元素内容区域，是否对内容的左/右边缘进行裁剪。

| 值           | 描述                                   |
| :----------- | :------------------------------------- |
| *visible*    | 不裁剪内容，可能会显示在内容框之外。   |
| *hidden*     | 裁剪内容 - 不提供滚动机制。            |
| *scroll*     | 裁剪内容 - 提供滚动机制。              |
| *auto*       | 如果溢出框，则应该提供滚动机制。       |
| *no-display* | 如果内容不适合内容框，则删除整个框。   |
| *no-content* | 如果内容不适合内容框，则隐藏整个内容。 |

```css
div {
	width: 110px;
	height: 110px;
	border: thin solid black;
	overflow-x: hidden;
	overflow-y: hidden;
}
```

<div style="width: 100px; height: 100px; border: thin solid black; overflow-x: hidden; overflow-y: hidden; margin: auto;"><p style="width:140px">
In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.
'Whenever you feel like criticizing anyone,' he told me, 'just remember that all the people in this world haven't had the advantages that you've had.' 
</p></div>

- `overflow-x`指定是否要剪辑的左/右边缘的内容.

- `overflow-y`指定是否要剪辑的顶部/底部边缘的内容

```css
div {
	width: 110px;
	height: 110px;
	border: thin solid black;
	overflow-x: scroll;
	overflow-y: scroll;
}
```

<div style="width: 100px; height: 100px; border: thin solid black; overflow-x: scroll; overflow-y: scroll; margin: auto;"><p style="width:140px">
In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.
'Whenever you feel like criticizing anyone,' he told me, 'just remember that all the people in this world haven't had the advantages that you've had.' 
</p></div>

```css
div {
	width: 210px;
	height: 110px;
	border: thin solid black;
	overflow-x: visible;
	overflow-y: visible;
}
```

<div style="width: 310px; height: 110px; border: thin solid black; overflow-x: visible; overflow-y: visible; margin: auto;"><p style="width:240px">
In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.
'Whenever you feel like criticizing anyone,' he told me, 'just remember that all the people in this world haven't had the advantages that you've had.' 
</p></div>





## overflow-y

```css
overflow-y: visible|hidden|scroll|auto|no-display|no-content;
```














