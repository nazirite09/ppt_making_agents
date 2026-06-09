# -*- coding: utf-8 -*-
"""03-slides (Montage) -> 03-slides-geist (무채 Geist) 일괄 변환.
변수 블록·폰트·하드코딩 블루·weight·radius를 치환한다. 원본은 건드리지 않는다."""
import re, pathlib

base = pathlib.Path(r"C:\Users\user\OneDrive\Desktop\PPT 제작 에이전트\sermons\교리설교-6강-복습")
src = base / "03-slides"
dst = base / "03-slides-geist"
dst.mkdir(exist_ok=True)

GEIST_LIGHT = """html.theme-light {
    --bg: #FFFFFF; --surface: #FFFFFF; --surface-hover: #FAFAFA;
    --border: #EAEAEA;
    --text: #000000; --text-secondary: #666666;
    --accent: #000000; --accent-secondary: #8F8F8F;
    --accent-strong: #000000; --accent-soft: #F4F4F4;
    --positive: #45A557; --negative: #E5484D; --warning: #F5A623;
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.04);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.06);
    --shadow-lg: 0 8px 24px rgba(0,0,0,0.08);
  }"""

GEIST_DARK = """html.theme-dark {
    --bg: #000000; --surface: #0A0A0A; --surface-hover: #1A1A1A;
    --border: #1F1F1F;
    --text: #EDEDED; --text-secondary: #8F8F8F;
    --accent: #FFFFFF; --accent-secondary: #8F8F8F;
    --accent-strong: #FFFFFF; --accent-soft: #1A1A1A;
    --positive: #45A557; --negative: #E5484D; --warning: #F5A623;
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.4);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.5);
    --shadow-lg: 0 8px 24px rgba(0,0,0,0.6);
  }"""

GEIST_FONT_LINK = '<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap" rel="stylesheet">'

# 하드코딩 블루 hex -> 무채 (변수로 안 잡히는 그라데이션/글로우용)
BLUE_MAP = {
    "#0066FF": "#000000", "#005EEB": "#000000", "#0054D1": "#000000",
    "#003E9C": "#000000", "#002966": "#000000", "#001536": "#000000",
    "#1A75FF": "#FFFFFF", "#3385FF": "#FFFFFF", "#4F95FF": "#FFFFFF",
    "#69A5FF": "#CCCCCC", "#9EC5FF": "#E0E0E0", "#C9DEFE": "#EAEAEA",
    "#BFD7FF": "#E0E0E0", "#EAF2FE": "#F4F4F4", "#F1F6FF": "#FAFAFA",
    "#F7FBFF": "#FAFAFA",
}

def restyle(text):
    text = re.sub(r"html\.theme-light\s*\{.*?\}", GEIST_LIGHT, text, count=1, flags=re.S)
    text = re.sub(r"html\.theme-dark\s*\{.*?\}", GEIST_DARK, text, count=1, flags=re.S)
    text = re.sub(r'<link[^>]*wanted-sans[^>]*>', GEIST_FONT_LINK, text)
    text = re.sub(r"'Wanted Sans Variable',\s*'Wanted Sans',", "'Geist',", text)
    # 블루 rgba (그라데이션/글로우)
    text = re.sub(r"rgba\(\s*0\s*,\s*102\s*,\s*255", "rgba(0,0,0", text)
    text = re.sub(r"rgba\(\s*0\s*,\s*94\s*,\s*235", "rgba(0,0,0", text)
    text = re.sub(r"rgba\(\s*51\s*,\s*133\s*,\s*255", "rgba(255,255,255", text)
    # 블루 hex
    for k, v in BLUE_MAP.items():
        text = text.replace(k, v).replace(k.lower(), v)
    # heavy -> Geist weight
    text = re.sub(r"font-weight:\s*800", "font-weight: 600", text)
    # pill -> sharp
    text = re.sub(r"border-radius:\s*999px", "border-radius: 8px", text)
    return text

WATCH = ["0066FF", "0066ff", "102,255", "133,255", "F1F6FF", "EAF2FE", "wanted-sans", "Wanted Sans"]
count = 0
for f in sorted(src.glob("*.html")):
    t2 = restyle(f.read_text(encoding="utf-8"))
    (dst / f.name).write_text(t2, encoding="utf-8")
    count += 1
    leftover = [w for w in WATCH if w in t2]
    flag = ("  ⚠ leftover: " + ", ".join(leftover)) if leftover else ""
    print(f"wrote {f.name}{flag}")
print(f"\n총 {count}개 파일 변환 -> {dst}")
