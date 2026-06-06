#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PaddleOCR 基础示例 - 通用文字识别
PaddleOCR Basic Example - Text Recognition
"""

from paddleocr import PaddleOCR
import sys
import os

def basic_ocr(image_path: str, lang: str = 'ch'):
    """
    基础 OCR 识别

    Args:
        image_path: 图片路径
        lang: 语言代码，默认中文 'ch'
              可选: ch, en, japan, korean, latin, arabic, cyrillic, devanagari, etc.
    """
    print(f"[INFO] Initializing PaddleOCR (lang={lang})...")
    ocr = PaddleOCR(use_angle_cls=True, lang=lang, show_log=False)

    print(f"[INFO] Recognizing: {image_path}")
    result = ocr.ocr(image_path)

    if not result or not result[0]:
        print("[INFO] No text found.")
        return []

    print(f"[INFO] Found {len(result[0])} text regions:\n")
    texts = []
    for i, line in enumerate(result[0], 1):
        text = line[1][0]
        confidence = line[1][1]
        bbox = line[0]
        texts.append({'text': text, 'confidence': confidence, 'bbox': bbox})
        print(f"  [{i}] {text} (置信度: {confidence:.4f})")

    return texts


def batch_ocr(image_dir: str, lang: str = 'ch'):
    """
    批量识别目录下所有图片

    Args:
        image_dir: 图片目录
        lang: 语言代码
    """
    ocr = PaddleOCR(use_angle_cls=True, lang=lang, show_log=False)

    extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')
    image_files = [f for f in os.listdir(image_dir)
                   if f.lower().endswith(extensions)]

    if not image_files:
        print(f"[WARN] No image files found in {image_dir}")
        return

    print(f"[INFO] Processing {len(image_files)} images...\n")
    for filename in image_files:
        image_path = os.path.join(image_dir, filename)
        print(f"\n{'='*50}")
        print(f"[FILE] {filename}")
        print('='*50)
        basic_ocr(image_path, lang)


def save_result(result: list, output_path: str):
    """将识别结果保存为 JSON 文件"""
    import json
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"[INFO] Result saved to {output_path}")


if __name__ == '__main__':
    # 示例用法
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        lang = sys.argv[2] if len(sys.argv) > 2 else 'ch'
    else:
        # 默认示例图片路径（替换为实际图片路径）
        image_path = 'example.jpg'
        lang = 'ch'

    result = basic_ocr(image_path, lang)
    save_result(result, 'ocr_result.json')
