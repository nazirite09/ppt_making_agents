# Geist (Vercel Design System) — Deck Design Tokens

> 출처: Vercel **Geist** (https://vercel.com/geist) · 폰트 Geist Sans/Mono (OFL)
> 이 문서는 `교리설교-6강-복습` 덱에 시험 적용한 Geist 룩의 **재사용용 토큰 레퍼런스**다.
> 핵심 정체성: **"무채색 미니멀 — 색을 빼고 타이포·여백·보더로 위계를 만든다."**
> 한글 글리프가 없으므로 **Pretendard 페어** 필수. 아래 "Paste-ready CSS"의 테마 블록을 그대로 붙여 쓴다.

---

## 1. Typography

Geist(영문·숫자) + Pretendard(한글)의 **2폰트 페어**. 영문/숫자는 Geist가, 한글은 Pretendard가 렌더된다.

```html
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/pretendard@1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css" rel="stylesheet">
```

```css
font-family: 'Geist', 'Pretendard Variable', Pretendard,
             system-ui, -apple-system, BlinkMacSystemFont, 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;
```

- 헤드라인 `font-weight: 600`, `letter-spacing: -0.04em`(디스플레이 -0.045em)
- 본문 `400~500`, `line-height: 1.6`, `word-break: keep-all`
- Montage(800 헤비)보다 **한 단계 가벼운 굵기**가 Geist다움 — 무게가 아니라 크기·여백으로 위계.

---

## 2. Colors — 무채 그레이 스케일

```
white  #FFFFFF · #FAFAFA · #F5F5F5 · #EAEAEA · #E0E0E0 · #D4D4D4
gray   #A3A3A3 · #8F8F8F · #666666 · #404040 · #171717 · #0A0A0A · #000000(black)
```

- **강조(accent) = 검정 `#000`.** 색을 쓰지 않는 것이 Geist다움이다(라이트). 다크에서는 흰색 `#FFF`.
- 포인트 컬러가 꼭 필요하면 **Vercel Blue `#0070F3` 한 가지만** 링크/CTA에 한정해서 쓴다. 설교 덱은 **무채 유지를 권장**(차분함의 핵심).
- 상태색(거의 미사용): success `#45A557` · warning `#F5A623` · error `#E5484D`.

---

## 3. Semantic Mapping (light / dark)

| 의미 | Light | Dark |
|---|---|---|
| text (본문) | `#000000` | `#EDEDED` |
| text.secondary | `#666666` | `#8F8F8F` |
| background | `#FFFFFF` / alt `#FAFAFA` | `#000000` / alt `#0A0A0A` |
| surface | `#FFFFFF` | `#0A0A0A` |
| border | `#EAEAEA` | `#1F1F1F` |
| accent (강조) | `#000000` | `#FFFFFF` |
| accent.soft (옅은 면) | `#F4F4F4` | `#1A1A1A` |

---

## 4. Spacing · Radius · Elevation

- **Spacing**(px): `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 104`(여백 넉넉히 — 미니멀의 핵심)
- **Radius**: `sm 6 · md 8 · lg 12`. **pill(999) 지양** — sharp한 모서리가 Geist 톤. (다이어그램 노드 등 곡선이 의미 있는 곳만 예외적으로 크게)
- **Elevation**: 그림자 최소. 분리는 **보더로** 한다.
```
sm  0 1px 2px rgba(0,0,0,.04)
md  0 4px 12px rgba(0,0,0,.06)
lg  0 8px 24px rgba(0,0,0,.08)
```

---

## 5. Paste-ready CSS (visualize 스킬 변수명에 매핑)

```css
html.theme-light {
  --bg:#FFFFFF; --surface:#FFFFFF; --surface-hover:#FAFAFA;
  --border:#EAEAEA;
  --text:#000000; --text-secondary:#666666;
  --accent:#000000; --accent-secondary:#8F8F8F;
  --accent-strong:#000000; --accent-soft:#F4F4F4;
  --positive:#45A557; --negative:#E5484D; --warning:#F5A623;
  --shadow-sm:0 1px 2px rgba(0,0,0,.04);
  --shadow-md:0 4px 12px rgba(0,0,0,.06);
  --shadow-lg:0 8px 24px rgba(0,0,0,.08);
}
html.theme-dark {
  --bg:#000000; --surface:#0A0A0A; --surface-hover:#1A1A1A;
  --border:#1F1F1F;
  --text:#EDEDED; --text-secondary:#8F8F8F;
  --accent:#FFFFFF; --accent-secondary:#8F8F8F;
  --accent-strong:#FFFFFF; --accent-soft:#1A1A1A;
  --positive:#45A557; --negative:#E5484D; --warning:#F5A623;
  --shadow-sm:0 1px 2px rgba(0,0,0,.4);
  --shadow-md:0 4px 12px rgba(0,0,0,.5);
  --shadow-lg:0 8px 24px rgba(0,0,0,.6);
}
```

### 컴포넌트 규칙 (Geist 룩)
- **라이트 우선.** 다크는 순흑(`#000`) 배경.
- **강조는 색이 아니라 weight·검정 채움·보더로.** 핵심 노드는 검정 채움(글자 흰색), 보조는 흰 면 + 1px 보더.
- **카드** = `--surface` + 1px `--border` + radius 8 + 그림자 거의 없음.
- **칩/배지** = 1px 보더 + 무채 텍스트, radius 5~6 (pill 지양). 핵심 번호칩만 검정 채움.
- **여백을 크게**, 좌측 정렬, 타이포 중심. 옅은 워터마크/가는 선으로 리듬.

---

## 6. 주의 / 캐비아트
- Geist엔 **한글 글리프가 없다** → 반드시 Pretendard(또는 Noto Sans KR) 페어. family 순서에서 Geist를 앞에 둬 영문/숫자만 Geist가 잡게 한다.
- **색 절제가 생명** — 블루 등 포인트를 두 곳 이상 쓰면 Geist다움이 무너진다. 위계가 부족하면 색이 아니라 **굵기·크기·여백·보더 굵기**로 푼다.
- CDN 폰트 버전 핀(`pretendard@1.3.9`) 유지 권장.
- Montage 대비: 같은 light-first 모던이지만 **(1) 블루 → 무채 (2) heavy 800 → 600 (3) pill → sharp (4) shadow → border** 로 더 차분·정적.
