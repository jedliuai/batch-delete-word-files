> **Chatgpt代充：[aishopvip.com](https://aishopvip.com)**

# Word 文档批量删除工具

[![Release](https://img.shields.io/github/v/release/jedliuai/batch-delete-word-files?display_name=tag&sort=semver)](https://github.com/jedliuai/batch-delete-word-files/releases/latest)
[![License](https://img.shields.io/github/license/jedliuai/batch-delete-word-files)](LICENSE)
[![Windows](https://img.shields.io/badge/platform-Windows-0078D4)](#系统要求)

一个轻量、离线的 Windows 桌面工具：递归查找文件夹及所有子文件夹中的 `.doc` 和 `.docx` 文档，默认全选，让你在确认清单后一次批量删除。

> A lightweight Windows GUI for recursively finding, reviewing, and batch deleting Word `.doc` / `.docx` files.

适合清理归档目录、项目交付目录、历史资料备份等场景。程序不读取 Word 内容、不上传文件，也不需要 Microsoft Word；它只根据扩展名列出文件，并在你确认后执行删除。

## 最快开始

1. 前往 [最新版本下载页](https://github.com/jedliuai/batch-delete-word-files/releases/latest)
2. 下载 `BatchDeleteWordFiles.exe`
3. 双击运行，选择文件夹并扫描
4. 取消勾选需要保留的文档，然后点击“执行删除”

> [!CAUTION]
> 选中的文件会被**直接删除，不会进入回收站**。程序会在删除前再次确认，请务必检查勾选清单。

不想运行 `.exe`？也可以[从源码运行](#从源码运行)，项目只使用 Python 标准库。

## 为什么用它

- **递归扫描**：一次覆盖目标文件夹及全部子文件夹
- **删除前可检查**：所有 Word 文档默认选中，可以逐个取消需要保留的文件
- **范围明确**：只匹配 `.doc` 和 `.docx`，不会处理其他类型
- **本地离线**：不联网、不上传文件、不分析文档内容
- **无需安装 Word**：仅按文件路径和扩展名工作
- **结果可见**：删除后自动刷新，并提示成功数、失败数及失败原因

## 典型使用场景

- 清理项目目录中散落在多层子文件夹里的 Word 文档
- 删除导出、转换或迁移后遗留的 `.doc` / `.docx` 源文件
- 整理历史归档或备份目录，同时手动保留少量重要文档
- 在批量删除前获得一份可勾选、可复核的文件清单

## 使用方法

启动程序后：

1. 点击“选择文件夹”
2. 点击“扫描 Word 文档”
3. 检查默认全选的文件列表
4. 取消勾选不需要删除的文件
5. 点击“执行删除”，并在弹窗中二次确认

如果部分文件正在被占用、权限不足或路径已发生变化，程序会继续处理其他文件，并在结束时列出失败项。

## 能力与边界

| 项目 | 当前行为 |
| --- | --- |
| 支持格式 | `.doc`、`.docx`，扩展名不区分大小写 |
| 扫描范围 | 所选目录及所有子目录 |
| 默认选择 | 扫描结果全部选中 |
| 删除方式 | 直接删除，不进入回收站 |
| 文档内容 | 不读取、不解析、不上传 |
| 支持系统 | Windows |

## 从源码运行

### 系统要求

- Windows
- Python 3.9 或更高版本（需要包含 `tkinter`）

克隆仓库并启动：

```powershell
git clone https://github.com/jedliuai/batch-delete-word-files.git
cd batch-delete-word-files
python main.py
```

在 Windows 资源管理器中，也可以双击 `启动程序.vbs` 静默启动，或双击 `start.bat` 查看启动过程。项目没有第三方运行时依赖。

## 安全与隐私

这个工具的核心操作是删除本地文件，因此建议先在测试目录中熟悉流程。源码集中在 [`main.py`](main.py)，删除动作使用 Python 的 `Path.unlink()`，便于直接审查。程序没有网络请求、遥测或后台服务。

如果你发现问题，请在 [Issues](https://github.com/jedliuai/batch-delete-word-files/issues) 中提交复现步骤、Windows 版本和错误信息；请勿上传包含隐私信息的文件路径或文档。

## 项目结构

```text
.
├─ .github/workflows/release.yml  # 创建标签后自动构建 Windows EXE
├─ main.py                        # 桌面程序
├─ start.bat                      # 可显示错误的启动入口
├─ 启动程序.vbs                   # 无控制台窗口的启动入口
├─ CHANGELOG.md                   # 版本更新记录
├─ LICENSE
└─ README.md
```

## 作者与相关项目

由 [Jed Liu](https://github.com/jedliuai) 维护。作者持续构建实用的 Windows 文件整理、文档处理与自动化工具，例如 [批量发票重命名工具](https://github.com/jedliuai/batch-invoice-renamer) 和 [Windows 右键创建同名文件夹](https://github.com/jedliuai/windows-same-name-folder)。

如果这个小工具确实帮你省下了重复操作，可以 Star 收藏，方便以后再次找到，也能帮助其他有同样需求的人发现它。

## 许可证

本项目采用 [MIT License](LICENSE)。
