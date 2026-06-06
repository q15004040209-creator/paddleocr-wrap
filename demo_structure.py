#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PaddleOCR 文档结构解析示例 - PDF/图片转结构化数据
PaddleOCR Document Structure Parse Example - PDF/Image to Structured Data
"""

from paddleocr import PPStructureV3, PPOCRv5_Doc
import json
import os


def structure_parse(input_path: str, output_dir: str = './output'):
    """
    文档结构解析 — 将 PDF 或图片转换为 Markdown / JSON

    Args:
        input_path: 输入文件路径（支持 PDF、图片）
        output_dir: 输出目录
    """
    os.makedirs(output_dir, exist_ok=True)

    print(f"[INFO] Parsing document: {input_path}")
    doc_parser = PPOCRv5_Doc(show_log=False)

    # 解析文档
    result = doc_parser.parse(
        input_path,
        output_dir=output_dir,
        return_json=True,
        table_formatter=None
    )

    print(f"[INFO] Output saved to: {output_dir}")
    return result


def structure_with_table_and_kie(input_path: str, output_dir: str = './output'):
    """
    高级文档解析：包含表格识别 + 键值对提取（KIE）

    Args:
        input_path: 输入文件路径
        output_dir: 输出目录
    """
    os.makedirs(output_dir, exist_ok=True)

    table_engine = PPStructureV3(show_log=False)

    print(f"[INFO] Running structure analysis with table + KIE: {input_path}")
    result = table_engine(input_path)

    # 分类保存结果
    for i, item in enumerate(result):
        item_type = item.get('type', 'unknown')
        print(f"  Block {i+1}: {item_type}")

    return result


def save_json(data, output_path: str):
    """保存为 JSON"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[INFO] JSON saved to: {output_path}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        input_path = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) > 2 else './output'
    else:
        input_path = 'document.pdf'
        output_dir = './output'

    # 基础文档解析
    result = structure_parse(input_path, output_dir)
    save_json(result, os.path.join(output_dir, 'structure_result.json'))

    # 高级解析（包含表格 + KIE）
    # result_advanced = structure_with_table_and_kie(input_path, output_dir)
    # save_json(result_advanced, os.path.join(output_dir, 'structure_advanced.json'))
