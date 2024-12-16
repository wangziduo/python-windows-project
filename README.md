# python-windows-project

## 项目简介
这是一个基于 Flask 构建的windows桌面端程序，用于在 Windows 系统上运行。
其主要具备以下功能：
- 可访问主页（`/`），展示一个基础的 HTML 页面。
- 设有`/shutdown`接口，能以优雅的方式关闭服务器并执行相关清理操作。
- 同时支持用 pyinstaller 打包成exe文件，打包后的文件放到dist目录中，可以在windows电脑上无依赖执行

## 环境要求
- Python 版本需在 3.6 及以上。
- Flask 版本为 2.0.1 或更高版本。

## 安装依赖
1. **克隆项目仓库**：
   ```sh
   git clone https://github.com/yourusername/python-project.git
   cd python-project  
    ```

### 创建并激活虚拟环境
- **Windows 系统**：
   ```sh
   python -m venv venv
  .\venv\Scripts\activate
   ```
- **Linux/Mac 系统**：
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

### 安装依赖包
```sh
pip install -r requirements.txt
```

## 项目结构
- `python-project/`：
  - `main.py`：作为项目的入口文件，承担启动 Flask 应用并打开浏览器的任务。
  - `src.py`：包含了 Flask 应用的定义、路由处理逻辑以及辅助函数。
  - `templates/`：此目录用于存放 HTML 模板文件，例如`index.html`。
  - `static/`：存放如 CSS、JavaScript 等静态资源文件，如`style.css`。
  - `venv/`：虚拟环境目录。
  - `requirements.txt`：详细列出了项目运行所需的所有依赖包及其对应的版本信息。

## 运行项目
1. **激活虚拟环境**：
  - **Windows 系统**：
     ```sh
    .\venv\Scripts\activate
     ```
  - **Linux/Mac 系统**：
     ```sh
     source venv/bin/activate
     ```
2. **启动项目**：
   ```sh
   python main.py
   ```
3. **打包项目**：
    ```sh
    pyinstaller --onefile --noconsole --add-data "templates;templates" --add-data "static;static" --windowed main.py
    ```
    生成的exe会再目录的dist文件夹下。双击打开

启动成功后，浏览器会自动开启并显示主页（`http://127.0.0.1:<port>/`）。

## API 文档
- **主页**：
  - **URL**：`/`
  - **方法**：GET
  - **描述**：返回主页的 HTML 内容。
- **关闭服务器**：
  - **URL**：`/shutdown`
  - **方法**：POST
  - **描述**：向当前进程发送 SIGTERM 信号，从而触发信号处理函数执行清理操作并关闭服务器。

## 贡献指南
欢迎为该项目贡献力量！以下是一些基本的贡献步骤：
1. **Fork 项目**：
点击页面右上角的“Fork”按钮，将项目复制到您自己的 GitHub 账户。
2. **克隆项目**：
   ```sh
   git clone https://github.com/yourusername/python-project.git
   cd python-project
   ```
3. **创建新分支**：
   ```sh
   git checkout -b feature/your-feature-name
   ```
4. **提交更改**：
   ```sh
   git add.
   git commit -m "Add your feature"
   git push origin feature/your-feature-name
   ```
5. **创建 Pull Request**：
访问您的 GitHub 仓库页面，点击“Compare & pull request”按钮，填写相关信息并提交。

## 许可证
本项目采用 MIT 许可证。

希望这份 README 文件能够助力您更好地管理与使用项目。若您有任何疑问或建议，欢迎随时提出！ 