import threading
import src

if __name__ == '__main__':
    # 启动一个线程，在Flask应用启动后打开浏览器
    port = src.get_free_port()
    threading.Timer(1, src.open_browser, args=(port,)).start()
    src.app.run(port=port,debug=False)  # 关闭调试模式以避免不必要的输出


# pyinstaller --onefile --noconsole --add-data "templates;templates" --add-data "static;static" --windowed main.py