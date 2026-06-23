#!/usr/bin/env python3
"""
把 PDF 的指定页渲染成 PNG,用于"看图"——曲线、热力图、网络结构图等用文字读不到的内容。
"""
import sys
import os
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("pages", help="页码,1 起算,逗号分隔,如 5 或 5,7,8")
    ap.add_argument("--dpi", type=int, default=150)
    ap.add_argument("--out", default="figures")
    args = ap.parse_args()

    try:
        import fitz
    except ImportError:
        sys.exit("缺少 PyMuPDF,请先: pip install pymupdf")

    try:
        doc = fitz.open(args.pdf)
    except Exception as e:
        sys.exit(f"打不开 PDF: {e}")

    try:
        pages = [int(p) for p in args.pages.replace(" ", "").split(",") if p]
    except ValueError:
        sys.exit("页码格式错误,应为 5 或 5,7,8")

    os.makedirs(args.out, exist_ok=True)
    base = os.path.splitext(os.path.basename(args.pdf))[0]
    zoom = args.dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)

    for p in pages:
        if p < 1 or p > doc.page_count:
            print(f"  跳过第 {p} 页(超出范围 1–{doc.page_count})")
            continue
        page = doc[p - 1]
        text_len = len(page.get_text("text").strip())
        pix = page.get_pixmap(matrix=mat)
        out_path = os.path.join(args.out, f"{base}_p{p}.png")
        pix.save(out_path)
        flag = "  ⚠ 该页几乎无文字层,可能是扫描件/图片页(纯文本工具会抽空)" if text_len < 40 else ""
        print(f"  已导出: {out_path}  ({pix.width}x{pix.height}, 文字字符数≈{text_len}){flag}")

    print("\n提示:把导出的 PNG 给带视觉的模型(或自己看)来读曲线/热力图细节。")


if __name__ == "__main__":
    main()
