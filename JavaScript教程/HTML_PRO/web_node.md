```css
text-shadow: h-shadow v-shadow blur color;
linear-gradient(direction, color-stop1, color-stop2, ...);
```

在本例中，当输入框获得焦点时，其背景颜色将改变：

```html
<html>
<head>
<script>
function setStyle(x) {
	document.getElementById(x).style.background="yellow"
}
</script>
</head>

<body>

First name: <input type="text" onfocus="setStyle(this.id)" id="fname" />
<br />
Last name: <input type="text" onfocus="setStyle(this.id)" id="lname" />

</body>
</html>
```

