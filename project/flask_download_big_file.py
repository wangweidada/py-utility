# coding:utf-8
import os.path

from flask import Flask, request, Response,stream_with_context
import urllib.parse
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
filepath = 'E:/study'
# 登录路由示例
@app.route('/login', methods=['POST'])
def login():
    # 处理登录逻辑...
    return '登录成功'

# 大文件下载路由
def generate_file_data(file_path):
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):  # 读取固定大小的块，例如 4096 字节
            yield chunk

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(filename,filename)
    # file_path = f"/path/to/your/large/files/{filename}"
    safe_filename = urllib.parse.quote(filename)  # 使用 urllib.parse.quote 对文件名进行 URL 编码
    response = Response(stream_with_context(generate_file_data(file_path)))
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers['Content-Disposition'] = f"attachment; filename*=UTF-8''{safe_filename}"
    return response

@app.route('/download-limit-speed/<filename>')
# 限制下载速度
def download_file(filename):


    file_path = f"E:/study/{filename}"
    # file_path = f"/path/to/your/large/files/{filename}"
    safe_filename = urllib.parse.quote(filename)  # 使用 urllib.parse.quote 对文件名进行 URL 编码
    response = Response(stream_with_context(generate_file_data(file_path)))
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers['Content-Disposition'] = f"attachment; filename*=UTF-8''{safe_filename}"
    return response
if __name__ == '__main__':
    app.run()
