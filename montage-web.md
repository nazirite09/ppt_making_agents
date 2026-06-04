# Montage (Wanted Design System) — Deck Design Tokens

> 출처: [`wanteddev/montage-web`](https://github.com/wanteddev/montage-web) · `packages/wds-theme/src/theme`
> 이 문서는 `하나님은-누구신가-v2.html`(및 이후 덱)에 적용한 Montage 디자인 시스템을 정리한 **재사용용 토큰 레퍼런스**입니다.
> 슬라이드를 만들 때 아래 "Paste-ready CSS"의 `:root`/테마 블록을 그대로 붙여 쓰면 됩니다.

---

## 1. Typography (폰트)

Montage는 **산세리프 전용** 시스템입니다 (Wanted Sans + Pretendard). 세리프 없음.

```html
<!-- Wanted Sans (브랜드 시그니처, 분할 가변 = 한글 동적 서브셋) -->
<link href="https://cdn.jsdelivr.net/gh/wanteddev/wanted-sans@1.0.3/packages/wanted-sans/fonts/webfonts/variable/split/WantedSansVariable.min.css" rel="stylesheet">
<!-- Pretendard (폴백) -->
<link href="https://cdn.jsdelivr.net/npm/pretendard@1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css" rel="stylesheet">
```

```css
font-family: 'Wanted Sans Variable', 'Wanted Sans', 'Pretendard Variable', Pretendard,
             -apple-system, BlinkMacSystemFont, system-ui, 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;
```

- 한글 본문 `line-height: 1.6`, 제목 `letter-spacing: -0.03em` (디스플레이 -0.04em)
- 굵기: h1/h2 `800`, h3 `700`, 본문 `400`, 강조 `600~700`

---

## 2. Atomic Colors (원자 팔레트 — 소스 그대로)

```
blue        10 #001536 · 20 #002966 · 30 #003E9C · 40 #0054D1 · 45 #005EEB · 50 #0066FF*
            55 #1A75FF · 60 #3385FF · 65 #4F95FF · 70 #69A5FF · 80 #9EC5FF · 90 #C9DEFE
            95 #EAF2FE · 99 #F7FBFF                                  (* 브랜드 Primary)

coolNeutral  5 #0F0F10 · 7 #141415 · 10 #171719 · 15 #1B1C1E · 17 #212225 · 20 #292A2D
            22 #2E2F33 · 23 #333438 · 25 #37383C · 30 #46474C · 40 #5A5C63 · 50 #70737C
            60 #878A93 · 70 #989BA2 · 80 #AEB0B6 · 90 #C2C4C8 · 95 #DBDCDF · 96 #E1E2E4
            97 #EAEBEC · 98 #F4F4F5 · 99 #F7F7F8

neutral     10 #171717 (그림자 베이스) · 50 #737373 · 99 #F7F7F7
green       40 #009632 · 50 #00BF40 · 60 #1ED45A      (status positive)
orange      39 #D17600 · 50 #FF9200 · 60 #FFA938      (status cautionary)
red         40 #E52222 · 50 #FF4242 · 60 #FF6363      (status negative)
common       0 #000000 · 100 #FFFFFF
```

---

## 3. Semantic Mapping (의미 토큰 — light / dark)

| 의미 | Light | Dark |
|---|---|---|
| primary.normal (브랜드) | `blue/50` #0066FF | `blue/60` #3385FF |
| primary.strong | `blue/45` #005EEB | `blue/55` #1A75FF |
| label.normal (본문) | `coolNeutral/10` #171719 | `coolNeutral/99` #F7F7F8 |
| label.alternative (보조) | `coolNeutral/40` ~#5A5C63 | `coolNeutral/80` #AEB0B6 |
| background.normal | #FFFFFF / alt `coolNeutral/99` #F7F7F8 | `coolNeutral/15` #1B1C1E / alt #0F0F10 |
| background.elevated | #FFFFFF | `coolNeutral/17` #212225 |
| line.normal (보더) | `coolNeutral/50` @ 22% | `coolNeutral/50` @ 30% |
| status positive / cautionary / negative | #00BF40 / #FF9200 / #FF4242 | #1ED45A / #FFA938 / #FF6363 |

---

## 4. Spacing · Radius · Elevation

**Spacing scale** (px): `0 · 2 · 4 · 6 · 8 · 10 · 12 · 14 · 16 · 20 · 24 · 32 · 40 · 48 · 56 · 64 · 72 · 80`

**Radius** (wds-theme에는 토큰이 없어 덱 적용 시 사용한 값): `sm 12 · md 14~16 · lg 18 · pill 999`

**Elevation shadow** (light, base = neutral/10 #171717):
```
xsmall  0 1px 2px -1px rgba(23,23,23,.10)
small   0 2px 4px -2px rgba(23,23,23,.06), 0 4px 6px -1px rgba(23,23,23,.06)
medium  0 4px 6px -2px rgba(23,23,23,.07), 0 10px 15px -3px rgba(23,23,23,.07)
large   0 6px 10px -4px rgba(23,23,23,.08), 0 16px 24px -6px rgba(23,23,23,.08)
xlarge  0 10px 15px -5px rgba(23,23,23,.10), 0 24px 38px -10px rgba(23,23,23,.12)
```
(dark는 토큰이 거의 안 보여서, 덱에서는 가독성을 위해 `rgba(0,0,0,.3~.55)`로 강화함)

---

## 5. Paste-ready CSS (visualize 스킬 변수명에 매핑)

visualize 스킬 필수 변수명(`--bg, --surface, ... --warning`)은 유지하고 값만 Montage로 채웁니다.
`--accent-soft / --accent-strong / --shadow-*` 는 Montage 룩 재현용 추가 변수.

```css
html.theme-light {
  --bg: #F7F7F8; --surface: #FFFFFF; --surface-hover: #F4F4F5;
  --border: rgba(112,115,124,0.22);
  --text: #171719; --text-secondary: #5A5C63;
  --accent: #0066FF; --accent-secondary: #70737C;
  --accent-strong: #005EEB; --accent-soft: #EAF2FE;
  --positive: #00BF40; --negative: #FF4242; --warning: #FF9200;
  --shadow-sm: 0 2px 4px -2px rgba(23,23,23,0.06), 0 4px 6px -1px rgba(23,23,23,0.05);
  --shadow-md: 0 4px 6px -2px rgba(23,23,23,0.07), 0 10px 15px -3px rgba(23,23,23,0.07);
  --shadow-lg: 0 6px 10px -4px rgba(23,23,23,0.08), 0 16px 24px -6px rgba(23,23,23,0.08);
}
html.theme-dark {
  --bg: #1B1C1E; --surface: #212225; --surface-hover: #2E2F33;
  --border: rgba(112,115,124,0.30);
  --text: #F7F7F8; --text-secondary: #AEB0B6;
  --accent: #3385FF; --accent-secondary: #989BA2;
  --accent-strong: #1A75FF; --accent-soft: rgba(51,133,255,0.16);
  --positive: #1ED45A; --negative: #FF6363; --warning: #FFA938;
  --shadow-sm: 0 2px 4px -2px rgba(0,0,0,0.40), 0 4px 6px -1px rgba(0,0,0,0.30);
  --shadow-md: 0 4px 6px -2px rgba(0,0,0,0.45), 0 10px 15px -3px rgba(0,0,0,0.40);
  --shadow-lg: 0 8px 14px -4px rgba(0,0,0,0.55), 0 18px 28px -8px rgba(0,0,0,0.45);
}
```

### 컴포넌트 규칙 (Montage 룩)
- **라이트 우선** — 기본 테마 `theme-light`.
- **강조색은 블루** — 라벨/태그는 `--accent-soft` 배경 + `--accent` 글자, pill(999) 형태.
- **카드** — `--surface` + 1px `--border` + radius 16 + `--shadow-sm`(hover 시 `--shadow-md` + `translateY(-3px)`).
- **아이콘 칩** — `--accent-soft` 배경 + `--accent` 색.
- **강조 블록**(예: 핵심 카드)은 `--accent-soft` 배경 + 블루 보더로 부각.

---

## 6. 주의 / 캐비아트
- 본 시스템은 **산세리프 전용**. 세리프(경건체)가 필요하면 별도 결정 필요(절충본 가능).
- CDN 폰트는 변경될 수 있음 — 버전 핀(`@1.0.3`, `@1.3.9`) 유지 권장.
- `wds-theme`에는 typography 스케일/radius 토큰이 없음(컴포넌트/엔진 측에 존재). 위 radius·타입 스케일은 덱 적용 시의 합리적 선택값.
