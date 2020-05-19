from flask import Flask, render_template, jsonify, request, make_response,\
    send_from_directory, abort
from werkzeug.utils import secure_filename
import time
import os
import base64
import datetime
import random

app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.dirname(__file__)
ALLOWED_EXTENSIONS = {'.png', '.jpg', '.gif'}

def allowed_file(filename):
    return '.' in filename and os.path.splitext(filename)[1].lower() in ALLOWED_EXTENSIONS

class Pic_str:
    def create_uuid(self):
        # 生成唯一的图片的名称字符串，防止图片显示时的重名问题
        nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        randomNum = random.randint(0, 100)
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum)
        uniqueNum = str(nowTime) + str(randomNum)
        return uniqueNum

@app.route('/upload')
def upload_test():
    return render_template('upload.html')

@app.route('/up_photo', methods=['POST', 'GET'])
def upload_photo():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['photo']
    if request.method == 'POST':
        if f and allowed_file(f.filename):
            fname = secure_filename(f.filename)
            ext = os.path.splitext(fname)[1]
            new_filename = Pic_str().create_uuid() + ext
            f.save(os.path.join(file_dir, new_filename))
            print(f'上传头像成功，上传的用户是：{request.form.get("name")}')
            return jsonify({"success": 0, "msg": "上传成功"})
    return jsonify({"error": 1001, "msg": "上传失败"})

@app.route('/download/<string:filename>', methods=['GET'])
def download(filename):
    if request.method == "GET":
        if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
            return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/show/<string:filename>', methods=['GET'])
def show_photo(filename):
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open(os.path.join(file_dir, filename), "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/png'
            return response
    else:
        pass

if __name__ == "__main__":
    app.run(debug=True)