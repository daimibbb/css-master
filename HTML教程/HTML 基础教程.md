# HTML 基础教程

# HTML 简介

## 实例

```html
<html>
<body>

<h1>我的第一个标题</h1>

<p>我的第一个段落。</p>

</body>
</html>
```

## 什么是 HTML？

HTML 是用来描述网页的一种语言。

- HTML 指的是超文本标记语言 (**H**yper **T**ext **M**arkup **L**anguage)
- HTML 不是一种编程语言，而是一种**标记语言** (markup language)
- 标记语言是一套**标记标签** (markup tag)
- HTML 使用**标记标签**来描述网页

## HTML 标签

HTML 标记标签通常被称为 HTML 标签 (HTML tag)。

- HTML 标签是由**尖括号**包围的关键词，比如 `<html>`
- HTML 标签通常是**成对出现**的，比如 `<b>` 和 `</b>`
- 标签对中的第一个标签是**开始标签**，第二个标签是**结束标签**
- 开始和结束标签也被称为**开放标签**和**闭合标签**

## HTML 文档 = 网页

- HTML 文档**描述网页**
- HTML 文档包含 **HTML 标签**和**纯文本**
- HTML 文档也被称为**网页**

Web 浏览器的作用是读取 HTML 文档，并以网页的形式显示出它们。浏览器不会显示 HTML 标签，而是使用标签来解释页面的内容：

```html
<html>
<body>

<h1>我的第一个标题</h1>

<p>我的第一个段落。</p>

</body>
</html>
```

### 例子解释

- `<html>` 与 `</html>` 之间的文本描述网页
- `<body>` 与` </body>` 之间的文本是可见的页面内容
- `<h1>` 与` </h1>` 之间的文本被显示为标题
- `<p>` 与 `</p>` 之间的文本被显示为段落

---

# HTML 基础

## HTML 标题

HTML 标题（Heading）是通过 `<h1>` - `<h6>` 等标签进行定义的。

### 实例

```html
<h1>This is a heading</h1>
<h2>This is a heading</h2>
<h3>This is a heading</h3>
```

## HTML 段落

HTML 段落是通过` <p>` 标签进行定义的。

### 实例

```html
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
```

## HTML 链接

HTML 链接是通过 `<a>` 标签进行定义的。

### 实例

```html
<a href="http://www.w3school.com.cn">This is a link</a>
```

> **注释：**在 `href `属性中指定链接的地址。

## HTML 图像

HTML 图像是通过 `<img>` 标签进行定义的。

### 实例

```html
<img src="w3school.jpg" width="104" height="142" />
```

> **注释：**图像的名称和尺寸是以属性的形式提供的。

---

