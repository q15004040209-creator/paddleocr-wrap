# PaddleOCR-Wrap

<div align="center">

![PaddleOCR](https://raw.githubusercontent.com/cuichengren01/PaddleOCR_doc_images/main/images/paddleocr/Banner.png)

**PaddleOCR Python 封装 — 100+语言 OCR / PDF 转结构化数据 Python 工具**

[![Stars](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR?style=flat-square&label=Stars)](https://github.com/PaddlePaddle/PaddleOCR)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)](https://pypi.org/project/PaddleOCR/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green?style=flat-square)](LICENSE)

[English](README.md) | [中文](README_zh.md)

</div>

---

## 📖 项目简介

PaddleOCR-Wrap 是对百度 [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) 的 Python 封装，提供开箱即用的 OCR 能力。

**核心特性：**

- 🌐 **100+ 语言支持** — 内置 PP-OCRv5 单模型方案，覆盖中文、英文、日文、韩文等全球主流语言
- 📄 **文档结构解析** — 支持 PDF / 图片转结构化数据（Markdown / JSON）
- ⚡ **高精度识别** — PP-OCRv5 在 OmnioDocBench v1.6 达到 **96.3%** 准确率
- 🧩 **表格识别** — 复杂表格、发票、证件、试卷均可处理
- 🖥️ **版面分析** — 文档、场景文本、印章、曲线图表均可识别
- 🚀 **轻量快速** — 极小的模型体积，适合边缘/云端部署

---

## 🛠️ 安装

```bash
pip install paddleocr paddlepaddle
```

> ⚠️ 推荐使用 GPU 版本以获得最佳性能：
> ```bash
> pip install paddlepaddle-gpu
> ```

---

## 📚 快速开始

### 1. 通用 OCR（图片文字识别）

```python
from paddleocr import PaddleOCR

# 初始化（首次运行自动下载模型）
ocr = PaddleOCR(use_angle_cls=True, lang='ch')

# 识别图片
result = ocr.ocr('example.jpg')

# 打印结果
for line in result[0]:
    print(f"文字: {line[1][0]}, 置信度: {line[1][1]:.4f}, 位置: {line[0]}")
```

### 2. 文档版面分析（PDF 转结构化）

```python
from paddleocr import PP-OCRv5_Doc,
                     PP-StructureV3

# 文档结构解析（PDF 转 Markdown / JSON）
doc_parser = PP-OCRv5_Doc()
result = doc_parser.parse('document.pdf', output_dir='./output')
print(result)
```

### 3. 表格识别

```python
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='ch', table=True)
result = ocr.ocr('table.png', structure=True)

for block in result:
    print(block)
```

### 4. 多语言批量识别

```python
from paddleocr import PaddleOCR
import glob

# 支持的语言：ch, en, japan, korean, latin, arabic, cyrillic, devanagari 等
ocr = PaddleOCR(use_angle_cls=True, lang='en')

for img_path in glob.glob('images/*.png'):
    result = ocr.ocr(img_path)
    print(f"文件: {img_path}")
    for line in result[0]:
        print(f"  → {line[1][0]}")
```

### 5. 方向分类器（自动旋转纠正）

```python
from paddleocr import PaddleOCR

# 启用角度分类器，自动检测并旋转图片方向
ocr = PaddleOCR(use_angle_cls=True, lang='ch')
result = ocr.ocr('rotated_image.jpg')
```

---

## 🌐 支持语言

| 语言 | 代码 | 语言 | 代码 |
|------|------|------|------|
| 中文 | `ch` | 日语 | `japan` |
| 英语 | `en` | 韩语 | `korean` |
| 繁体中文 | `cht` | 拉丁语 | `latin` |
| 阿拉伯语 | `arabic` | 西里尔文 | `cyrillic` |
| 梵文 | `devanagari` | ... | 100+ |

> 完整语言列表请参考 [PaddleOCR 语言支持](https://github.com/PaddlePaddle/PaddleOCR)。

---

## 📂 项目结构

```
paddleocr-wrap/
├── README.md              # 英文说明
├── README_zh.md           # 中文说明
├── demo.py                # 基础示例
├── demo_structure.py      # 文档结构解析示例
├── demo_table.py          # 表格识别示例
├── requirements.txt       # Python 依赖
└── .gitignore
```

---

## 🔗 相关项目

- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) — 官方仓库
- [PaddleOCR-VL](https://github.com/PaddlePaddle/PaddleOCR-VL) — 视觉语言模型
- [PP-StructureV3](https://github.com/PaddlePaddle/PP-StructureV3) — 文档结构解析
- [Diffy](https://github.com/langenious/Diffy) — 生产级 RAG 文档引擎
- [RAGFlow](https://github.com/infiniflow/RAGFlow) — 基于深度文档理解的 RAG 引擎

---

## 📄 许可证

本项目继承 [Apache 2.0 许可证](LICENSE)。

---

## ⭐ Stars 趋势

[![Star History](https://api.star-history.org/svg?repos=PaddlePaddle/PaddleOCR&type=Date)](https://star-history.org/#PaddlePaddle/PaddleOCR)

---

> 💡 **提示**: 如果项目对您有帮助，请给 [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) 点个 Star！
