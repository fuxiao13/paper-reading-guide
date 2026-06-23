#!/usr/bin/env python3
"""
抽取 PDF 的章节骨架与图表标题,用于陪读"第一遍 60 秒定位"。
只做轻量提取,不替代真正读全文。

用法:
    python extract_outline.py path/to/paper.pdf
    python extract_outline.py path/to/paper.pdf --max-chars 1200

依赖:PyMuPDF  ->  pip install pymupdf
输出:摘要片段、疑似章节标题、图/表标题(**带页码**,如 `p7: Figure 4 ...`),
     可直接用页码喂给 render_page.py 看图。读不到曲线细节是正常的——脚本只取文字。
"""
import sys
import re
import argparse

CAPTION_RE = re.compile(r'^\s*(figure|fig\.?|table|图|表)\s*\d', re.IGNORECASE)
HEADING_RE = re.compile(
    r'^\s*(\d+(\.\d+)*\s+\S|abstract|introduction|related work|method|methodology|'
    r'experiment|experiments|results|discussion|conclusion|references|引言|摘要|'
    r'方法|实验|结果|讨论|结论|相关工作)',
    re.IGNORECASE,
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--max-chars", type=int, default=1200, help="摘要片段最大字符数")
    args = ap.parse_args()

    try:
        import fitz
    except ImportError:
        sys.exit("缺少 PyMuPDF,请先: pip install pymupdf")

    try:
        doc = fitz.open(args.pdf)
    except Exception as e:
        sys.exit(f"打不开 PDF: {e}")

    full_text = []
    headings = []
    captions = []

    for page_idx, page in enumerate(doc, start=1):
        text = page.get_text("text")
        full_text.append(text)
        for line in text.splitlines():
            s = line.strip()
            if not s:
                continue
            if CAPTION_RE.match(s):
                captions.append((page_idx, s[:160]))
            elif len(s) < 80 and not s.endswith(('.', '。', ',', '，')) and HEADING_RE.match(s):
                headings.append(s[:80])

    joined = "\n".join(full_text)
    abs = ""
    m = re.search(r'(abstract|摘要)', joined, re.IGNORECASE)
    if m:
        abs = joined[m.end(): m.end() + args.max_chars]
        abs = re.sub(r'\s+', ' ', abs).strip()

    print("=" * 60)
    print(f"文件: {args.pdf}  (共 {doc.page_count} 页)")
    print("=" * 60)
    print("\n【摘要片段】")
    print(abs if abs else "(未定位到摘要,需手动看首页)")
    print("\n【疑似章节标题】")
    if headings:
        for h in dict.fromkeys(headings):
            print("  -", h)
    else:
        print("  (未抽到,可能是扫描件或排版特殊)")
    print("\n【图 / 表 标题(含页码)】")
    if captions:
        seen = set()
        for page_no, cap in captions:
            key = (page_no, cap)
            if key in seen:
                continue
            seen.add(key)
            print(f"  p{page_no}: {cap}")
    else:
        print("  (未抽到图表标题)")
    print("\n提示:曲线/热力图细节脚本读不到。用上面的页码渲染来看图:")
    print(f"  python render_page.py \"{args.pdf}\" <页码>")


if __name__ == "__main__":
    main()
