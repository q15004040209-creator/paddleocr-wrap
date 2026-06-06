#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PaddleOCR 表格识别示例
PaddleOCR Table Recognition Example
"""

from paddleocr import PaddleOCR
import json
import os


def table_recognition(image_path: str, output_dir: str = './output'):
    """
    表格识别 — 从图片中提取表格结构

    Args:
        image_path: 图片路径
        output_dir: 输出目录
    """
    os.makedirs(output_dir, exist_ok=True)

    print(f"[INFO] Initializing table OCR...")
    ocr = PaddleOCR(
        use_angle_cls=True,
        lang='ch',
        table=True,          # 启用表格识别
        show_log=False
    )

    print(f"[INFO] Recognizing table from: {image_path}")
    result = ocr.ocr(image_path, structure=True)

    # 解析表格结果
    tables = []
    for i, block in enumerate(result):
        block_type = block.get('type', 'unknown') if isinstance(block, dict) else 'table'
        if isinstance(block, dict) and block.get('type') == 'table':
            html = block.get('res', {}).get('html', '')
            tables.append({'index': i, 'html': html})
            print(f"\n[TABLE {i+1}]")
            print(html[:500] if len(html) > 500 else html)
        else:
            print(f"  Block {i+1}: {str(block)[:100]}")

    return result, tables


def batch_table_recognition(image_dir: str, output_dir: str = './output'):
    """
    批量表格识别

    Args:
        image_dir: 图片目录
        output_dir: 输出目录
    """
    os.makedirs(output_dir, exist_ok=True)

    ocr = PaddleOCR(use_angle_cls=True, lang='ch', table=True, show_log=False)

    extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    image_files = [f for f in os.listdir(image_dir)
                   if f.lower().endswith(extensions)]

    if not image_files:
        print(f"[WARN] No image files found in {image_dir}")
        return

    print(f"[INFO] Processing {len(image_files)} images for table recognition...\n")

    all_results = {}
    for filename in image_files:
        image_path = os.path.join(image_dir, filename)
        print(f"\n{'='*50}")
        print(f"[FILE] {filename}")
        print('='*50)

        result, tables = table_recognition(image_path, output_dir)
        base_name = os.path.splitext(filename)[0]
        all_results[filename] = {'tables': tables}

        # 保存每个文件的 HTML 表格
        for j, table in enumerate(tables):
            html_path = os.path.join(output_dir, f"{base_name}_table_{j+1}.html")
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(table['html'])
            print(f"[INFO] Table HTML saved: {html_path}")

    return all_results


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) > 2 else './output'
    else:
        image_path = 'table.png'
        output_dir = './output'

    result, tables = table_recognition(image_path, output_dir)

    # 保存结果
    output_json = os.path.join(output_dir, 'table_result.json')
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump({'result': str(result), 'tables': tables}, f, ensure_ascii=False, indent=2)
    print(f"\n[INFO] Full result saved to: {output_json}")
