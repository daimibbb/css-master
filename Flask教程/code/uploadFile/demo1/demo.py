from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

path = 'static/uploads'
base_path = os.path.dirname(__file__)
path = os.path.join(base_path, path)
app = Flask(__name__)
app.debug = True
app.secret_key = 'this is a test'

def createFloders():
    if not os.path.exists(path):
        os.makedirs(path)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        upload_path = os.path.join(path, secure_filename(f.filename))
        createFloders()
        f.save(upload_path)
        return "文件上传成功!!"
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()