```html
<ol type="a">
    <li>内容一</li>
    <li>内容二</li>
    <li>内容三</li>
    <li>内容四</li>
</ol>
```

<ol type="a">
    <li>内容一</li>
    <li>内容二</li>
    <li>内容三</li>
    <li>内容四</li>
</ol>
---

```html
<ol type="A">
    <li>内容一</li>
    <li>内容二</li>
    <li>内容三</li>
    <li>内容四</li>
</ol>
```

<ol type="A">
    <li>内容一</li>
    <li>内容二</li>
    <li>内容三</li>
    <li>内容四</li>
</ol>
---

```html
<ol type="i">
    <li>内容一</li>
    <li>内容二</li>
    <li>内容三</li>
    <li>内容四</li>
</ol>
```

<ol type="i">
    <li>内容一</li>
    <li>内容二</li>
    <li>内容三</li>
    <li>内容四</li>
</ol>
---

```html
<ol type="I">
    <li>内容一</li>
    <li>内容二</li>
    <li>内容三</li>
    <li>内容四</li>
</ol>
```

<ol type="I">
    <li>内容一</li>
    <li>内容二</li>
    <li>内容三</li>
    <li>内容四</li>
</ol>
---

```html
<ol>
  <li>列表项
    <ol>
      <li>列表项
        <ol>
          <li>列表项</li>
          <li>列表项</li>
          <li>列表项</li>
        </ol>
      </li>
    </ol>
  </li>
</ol>
```

```css
ol {padding: 0 0 0 20px; margin: 0; list-style-type: none}
li:before {color: #f00; font-family: "Times New Roman"}
li {counter-increment: a 1;}
li:before {content: counter(a)". ";}
li li {counter-increment: b 1;}
li li:before {content: counter(a)". "counter(b)". ";}
li li li {counter-increment: c 1;}
li li li:before {content: counter(a)". "counter(b)". "counter(c)". ";}
```

<style>
ol {padding: 0 0 0 20px; margin: 0; list-style-type: none}
li:before {color: #f00; font-family: "Times New Roman"}
li {counter-increment: a 1;}
li:before {content: counter(a)". ";}
li li {counter-increment: b 1;}
li li:before {content: counter(a)". "counter(b)". ";}
li li li {counter-increment: c 1;}
li li li:before {content: counter(a)". "counter(b)". "counter(c)". ";}
</style>
<ol>
  <li>列表项
    <ol>
      <li>列表项
        <ol>
          <li>列表项</li>
          <li>列表项</li>
          <li>列表项</li>
        </ol>
      </li>
    </ol>
  </li>
</ol>

---

# HTML+CSS实现圆圈里面有个数字

```css
span {
    border-radius: 50%;
    height: 20px;
    width: 20px;
    display: inline-block;
    background: #f30303;
    vertical-align: top;
}
span span {
    display: block;
    color: #fff;
    height: 20px;
    line-height: 20px;
    text-align: center;
}
```

```html
<p>异常<span><span>99</span></span></p>
```

<p>异常<span style=" border-radius: 50%;
    height: 20px;
    width: 20px;
    display: inline-block;
    background: #f30303;
    vertical-align: top;"><span style="display: block;
    color: #fff;
    height: 20px;
    line-height: 20px;
    text-align:center;">99</span></span></p>

----

