# Flask 文件上传

在Flask中处理文件上传非常简单。它需要一个HTML表单，其enctype属性设置为“`multipart/form-data`”，将文件发布到URL。URL处理程序从**request.files[]**对象中提取文件，并将其保存到所需的位置。

每个上传的文件首先会保存在服务器上的临时位置，然后将其实际保存到它的最终位置。目标文件的名称可以是硬编码的，也可以从**request.files[file]**对象的filename属性中获取。但是，建议使用**secure_filename()**函数获取它的安全版本。

可以在Flask对象的配置设置中定义默认上传文件夹的路径和上传文件的最大大小。

| 参数                           | 含义                                       |
| ------------------------------ | ------------------------------------------ |
| app.config[‘UPLOAD_FOLDER’]    | 定义上传文件夹的路径                       |
| app.config[‘MAX_CONTENT_PATH’] | 指定要上传的文件的最大大小（以字节为单位） |

以下代码具有'**/ upload'** URL规则，该规则在templates文件夹中显示'**upload.html'**，以及**'/ upload-file'** URL规则，用于调用**uploader()**函数处理上传过程。

**'upload.html'**有一个文件选择器按钮和一个提交按钮。

```html
<html>
<body>
<form method="POST" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit">
</form>
</body>
</html>
```

您将看到如下所示的界面。

![Flask File Uploading](https://atts.w3cschool.cn/attachments/tuploads/flask/flask_file_uploading.jpg)

选择文件后，单击**提交**。表单的post方法调用**'/ upload_file' URL**。底层函数**uploader()**执行保存操作。

以下是Flask应用程序的Python代码。

```python
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      base_path = os.path.dirname(__file__)
      print(os.getcwd())
      upload_path = os.path.join(base_path, "static/uploads", filename)
      f.save(upload_path)
      return 'file uploaded successfully'
   return render_template('upload.html')
   
if __name__ == '__main__':
   app.run(debug=True)
```

