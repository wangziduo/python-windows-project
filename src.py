import os
import sys
import webbrowser
import socket
import threading
from flask import Flask, render_template, request
import atexit
import signal

# 获取打包后的资源路径
def resource_path(relative_path):
    try:
        # PyInstaller 创建的临时文件夹
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# 设置模板和静态文件路径
template_dir = resource_path('templates')
static_dir = resource_path('static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# 定义信号处理函数
def signal_handler(signum, frame):
    cleanup()
    os._exit(0)

# 注册信号处理函数
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    os.kill(os.getpid(), signal.SIGTERM)  # 发送 SIGTERM 信号
    return 'Server shutting down...'

def cleanup():
    print("Cleaning up and shutting down server...")
    # 执行清理操作

atexit.register(cleanup)

def get_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 0))
        return s.getsockname()[1]

def open_browser(port):
    webbrowser.open_new(f'http://127.0.0.1:{port}/')

