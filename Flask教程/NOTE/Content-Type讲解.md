# Content-Type讲解

`MediaType`，即是`Internet Media Type`，互联网媒体类型；也叫做`MIME`类型，在`Http`协议消息头中，使用`Content-Type`来表示具体请求中的媒体类型信息。

类型格式：

```html
type/subtype(;parameter)? type
```

- *type*: 主类型，任意的字符串，如`text`，如果是`*`号代表所有；  

- *subtype*: 子类型，任意的字符串，如`html`，如果是`*`号代表所有；  

- *parameter*: 可选，一些参数，如`Accept`请求头的`q`参数， `Content-Type`的`charset`参数。

```html
Content-Type: text/html;charset:utf-8;
```

 常见的媒体格式类型如下：

```python
text/html    # HTML格式
text/plain   # 纯文本格式      
text/xml     # XML格式
image/gif    # gif图片格式    
image/jpeg   # jpg图片格式 
image/png    # png图片格式
```

以`application`开头的媒体格式类型：

```python
application/xhtml+xml    # XHTML格式
application/xml          # XML数据格式
application/atom+xml     # Atom XML聚合格式    
application/json         # JSON数据格式
application/pdf          # pdf格式  
application/msword       # Word文档格式
application/octet-stream # 二进制流数据（如常见的文件下载）
application/x-www-form-urlencoded # <form encType=””>中默认的encType，form表单数据被编码为
                                  # key/value格式发送到服务器（表单默认的提交数据的格式）
```

另外一种常见的媒体格式是上传文件之时使用的：

```python
multipart/form-data # 需要在表单中进行文件上传时，就需要使用该格式
```

以上就是我们在日常的开发中，经常会用到的若干`Content-Type`的内容格式。

要学习`Content-Type`，必须事先知道它到底是什么，是干什么用的。  

HTTP协议（RFC2616）采用了请求/响应模型。客户端向服务器发送一个请求，请求头包含请求的方法、URI、协议版本、以及包含请求修饰符、客户信息和内容的类似于`MIME`的消息结构。服务器以一个状态行作为响应，相应的内容包括消息协议的版本，成功或者错误编码加上包含服务器信息、实体元信息以 及可能的实体内容。  

通常HTTP消息由一个起始行，一个或者多个头域，一个只是头域结束的空行和可选的消息体组成。HTTP的头域包括通用头，请求头，响应头和实体头四个部分。每个头域由一个域名，冒号（:）和域值三部分组成。域名是大小写无关的，域值前可以添加任何数量的空格符，头域可以被扩展为多行，在每行开始处，使用至少一个空格或制表符。  

请求消息和响应消息都可以包含实体信息，实体信息一般由实体头域和实体组成。实体头域包含关于实体的原信息，实体头包括Allow、 Content- Base、Content-Encoding、Content-Language、 Content-Length、Content-Location、Content-MD5、Content-Range、Content-Type、 Etag、Expires、Last-Modified、extension-header。  

`Content-Type`是返回消息中非常重要的内容，表示后面的文档属于什么MIME类型。

```html
Content-Type: [type]/[subtype]; parameter
```

例如最常见的就是`text/html`，它的意思是说返回的内容是文本类型，这个文本又是HTML格式的。原则上浏览器会根据`Content-Type`来决定如何显示返回的消息体内容。  

*type*有下面的形式。  

- `Text`：用于标准化地表示的文本信息，文本消息可以是多种字符集和或者多种格式的；  

- `Multipart`：用于连接消息体的多个部分构成一个消息，这些部分可以是不同类型的数据；  

- `Application`：用于传输应用程序数据或者二进制数据；  

- Message：用于包装一个E-mail消息；  

- Image：用于传输静态图片数据；  

- Audio：用于传输音频或者音声数据；  

- Video：用于传输动态影像数据，可以是与音频编辑在一起的视频数据格式。  

*subtype*用于指定*type*的详细形式。`content-type/subtype`配对的集合和与此相关的参数，将随着时间而增长。为了确保这些值在一个有序而且公开的状态下开发，MIME使用Internet Assigned Numbers Authority (IANA)作为中心的注册机制来管理这些值。  

*parameter*可以用来指定附加的信息，更多情况下是用于指定`text/plain`和`text/html`等的文字编方式的`charset`参数。`MIME`根据*type*制定了默认的*subtype*，当客户端不能确定消息的*subtype*的情况下，消息被看作默认的*subtype*进行处理。`Text`默认是`text/plain`，`Application`默认是`application/octet-stream`而`Multipart`默认情况下被看作`multipart/mixed`。  
MIME定义在RFC-2046 MIME Part 2: Media Types 。  
