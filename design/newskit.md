# NewsKit (News UK Design System) — Deck Design Tokens

> 출처: [`newscorp-ghfb/newskit`](https://github.com/newscorp-ghfb/newskit) · `src/theme/`
> 라이선스: **BSD 3-Clause** (© News UK & Ireland Ltd) · 폰트 **SIL OFL 1.1**(DM Sans · Poppins · Bitter · DM Mono · Noto Sans · Source Serif Pro).
> 이 문서는 NewsKit의 **실제 토큰 값**(소스에서 추출)을 우리 **visualize 스킬**의 필수 CSS 변수에 매핑한 **재사용 토큰 레퍼런스**입니다.
> 슬라이드/HTML을 만들 때 아래 "Paste-ready CSS"의 폰트 링크 + `:root`/`.theme-*` 블록을 그대로 붙이고, 컴포넌트 레시피로 NewsKit 룩을 재현하면 됩니다.
> ⚠️ 모든 값은 NewsKit `newskit-light`(기본) / `newskit-dark` 테마에서 그대로 가져온 **정확한 값**입니다. (예외: **다크 그림자**만 가독성을 위해 강화 — 아래 표기.)

---

## 0. 적용 방법 (visualize 스킬과 함께)

visualize 스킬은 `--bg, --surface, --surface-hover, --border, --text, --text-secondary, --accent, --accent-secondary, --positive, --negative, --warning` **11개 변수 이름**과 `.theme-light/.theme-dark` 클래스 구조를 요구합니다(이름 고정, 값 자유). NewsKit 적용 = **그 값과 폰트만 NewsKit으로 교체**:

1. 스켈레톤의 **Inter `<link>`를 §1의 NewsKit 폰트 링크로 교체**(폰트 override는 스킬이 명시적으로 허용 — "override only when user requests it").
2. 스켈레톤의 테마 블록을 §5 **Paste-ready CSS**(`:root` + `.theme-light` + `.theme-dark`)로 교체. 11개 필수 변수 + NewsKit 추가 변수 포함.
3. `body`/`h1~h4`의 `font-family`를 §5의 `--font-*` 변수로 지정.
4. 카드·버튼·칩·인용 등은 §6 **컴포넌트 레시피**를 사용.
5. 결과물 주석에 출처 한 줄 남기기: `<!-- Design tokens: NewsKit (BSD-3-Clause, © News UK). Fonts: OFL 1.1. -->`

---

## 1. Typography (폰트)

NewsKit은 **3개 패밀리**를 역할별로 씁니다. 모두 Google Fonts에 있어 CDN 임베드 가능.

| 토큰 | 패밀리 | 역할 |
|---|---|---|
| `fontFamily010` | **DM Sans** (sans) | 본문·문단·메타 (Body) |
| `fontFamily030` | **Poppins** (sans) | Utility 헤딩·라벨·버튼·인용 (Display/UI) |
| `fontFamily020` | **Bitter** (serif) | Editorial 디스플레이·헤드라인 (편집형) |
| (mono) | **DM Mono** | 코드·수치 모노 |

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bitter:ital,wght@0,400;0,500;0,600;0,700;1,400&family=DM+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Poppins:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
```
> 한글: NewsKit이 본래 **Noto Sans** 계열을 쓰므로 한글 본문은 **Noto Sans KR**로 자연스럽게 연결됩니다. Editorial(세리프) 헤딩에 한글을 크게 쓸 땐 `Noto+Serif+KR`도 링크에 추가하세요.

**폰트 스택 (한글 폴백 포함):**
```css
--font-body:     'DM Sans','Noto Sans KR',system-ui,-apple-system,'Malgun Gothic',sans-serif;
--font-display:  'Poppins','Noto Sans KR',system-ui,'Malgun Gothic',sans-serif;     /* Utility 헤딩 */
--font-editorial:'Bitter','Noto Serif KR',Georgia,'Apple SD Gothic Neo',serif;       /* Editorial 헤딩 */
--font-mono:     'DM Mono',ui-monospace,'SFMono-Regular',monospace;
```

### 1.1 두 가지 헤딩 모드 (NewsKit의 핵심 선택)
NewsKit은 **두 헤딩 시스템**을 제공합니다 — 슬라이드 톤에 맞게 하나를 고르세요.
- **Editorial (Bitter, serif, weight 500)** — 신문·아티클·진중·격조. 디스플레이/헤드라인에 사용. 라인하이트 1.125, 자간 0.
- **Utility (Poppins, sans, weight 700)** — 제품 UI·앱·명료·모던. 라인하이트 1.125, 자간 0.
> 둘 다 NewsKit 정식 룩입니다. **본문은 항상 DM Sans 400**, 라벨/아이브로/버튼/인용은 **Poppins**입니다.

### 1.2 Type scale (폰트 사이즈 토큰, px)
`fontSize010~160`: **12 · 14 · 16(base) · 18 · 20 · 22 · 24 · 28 · 32 · 36 · 40 · 44 · 48 · 56 · 64 · 80**
라인하이트 `010~060`: **1 · 1.125 · 1.25 · 1.5 · 1.75 · 2** | 굵기 `010~040`: **400 · 500 · 600 · 700** | 자간 `010~050`: **−0.5 · −0.25 · 0 · 0.25 · 0.5 px**

### 1.3 Typography presets (실제 매핑 — px/weight/line-height)
| Preset | 폰트 | px | weight | line-height |
|---|---|---|---|---|
| editorialDisplay 010/020/030 | Bitter | 56 / 64 / 80 | 500 | 1.125 |
| editorialHeadline 010–080 | Bitter | 18·20·24·28·32·36·40·48 | 500 | 1.125 |
| editorialSubheadline 010–050 | Bitter | 16·20·22·24·28 | 400 | 1.125 |
| editorialParagraph 010–030 | DM Sans | 14·16·18 | 400 | **1.5** |
| editorialQuote 010/020 | Poppins | 22 / 28 | 400 | 1.25 |
| editorialLabel 010–030 | Poppins | 12·14·16 | 500 | 1.125 |
| editorialCaption 010 | DM Sans | 14 | 500 | 1.5 |
| utilityHeading 010–050 | **Poppins** | 16·18·20·22·24 | **700** | 1.125 |
| utilitySubheading 010–050 | Poppins/DM Sans | 14·16·18·20·22 | 500 | 1.125 |
| utilityBody 010–030 | DM Sans | 12·14·16 | 400 | **1.5** |
| utilityLabel 010–030 | Poppins | 12·14·16 | 500 | 1.5 |
| utilityMeta 010/020 | DM Sans | 12·14 | 500 | 1.5 |
| utilityButton 010–030 | Poppins | (=label) | 500 | 1.5 |

### 1.4 슬라이드(16:9) 헤딩 스케일 권장
| 역할 | 권장 preset | px | 비고 |
|---|---|---|---|
| 표지 타이틀 | editorialDisplay030 / utilityHeading↑ | 64–80 | Bitter500 또는 Poppins700 |
| 섹션 타이틀 | editorialHeadline080 | 48 | |
| 슬라이드 헤딩 | editorialHeadline050–060 | 32–36 | |
| 서브헤딩 | utilitySubheading040 | 20–22 | Poppins/DM Sans 500 |
| 본문 | editorialParagraph020/030 | 16–18 | DM Sans 400, lh 1.5 |
| 아이브로/키커 | editorialLabel020/030 | 14–16 | Poppins 500, 대문자·자간 |

---

## 2. Atomic Colors (원자 팔레트 — 소스 그대로)

```
blue    010 #ECF1FF · 020 #D5E0FC · 030 #AEBFFF · 040 #8BA6F6 · 050 #708DE9 · 055 #446BE4
        060 #3358CC* · 070 #254CAC · 080 #12387A · 090 #03264D · 100 #060F2C   (* Primary/Brand)
teal    010 #E6F4F6 · 020 #C7E7EA · 030 #97D0D6 · 040 #5EB8C0 · 050 #289FAB · 055 #06808E
        060 #017582 · 070 #005B65 · 080 #004249 · 090 #002B30 · 100 #001314     (Informative/2차 강조)
green   010 #E5F4EA · 020 #C8E4D0 · 030 #95CAA3 · 040 #6DB681 · 050 #41A05B · 060 #007B22 …100 #001506  (Positive)
red     010 #FEECEC · 020 #FED8D8 · 030 #FEB3B3 · 040 #FE8888 · 050 #FB5959 · 060 #D60000 …100 #2D0000  (Negative)
amber   010 #FFEDE1 · 020 #FDDCC6 · 030 #FEB788 · 040 #F79247 · 050 #CD6900 · 060 #A75500 …100 #1D0D02  (Caution/Warning)
neutral 010 #F1F1F1 · 020 #E2E2E2 · 030 #C6C6C6 · 040 #ABABAB · 050 #919191 · 060 #6A6A6A
        070 #525252 · 080 #3B3B3B · 090 #262626 · 100 #111111
purple  050 #8883F6 · 055 #6E61E4 · 060 #6454E3 · 070 #4C33CC …  (Visited)
black #0A0A0A · white #FFFFFF · focus #3768FB · blackTint010–090 rgba(0,0,0,.1–.9) · whiteTint010–090 rgba(255,255,255,.1–.9)
```
> **NewsKit의 시그니처 = blue060 `#3358CC`(프라이머리)** + **teal `#017582/#06808E`(인포메이티브/2차)**. 팔레트는 채도가 절제된 **에디토리얼/뉴스 제품** 톤입니다.

---

## 3. Semantic tokens (light = 기본 / dark = 오버라이드) — 실제 해석값

| 의미 토큰 | Light | Dark |
|---|---|---|
| inkBase (본문) | neutral080 `#3B3B3B` | neutral020 `#E2E2E2` |
| inkContrast (헤딩·강조) | neutral100 `#111111` | white `#FFFFFF` |
| inkSubtle (보조) | neutral060 `#6A6A6A` | neutral040 `#ABABAB` |
| inkNonEssential (비활성) | neutral040 `#ABABAB` | neutral050 `#919191` |
| interfaceBackground (페이지 bg) | white `#FFFFFF` | neutral100 `#111111` |
| interface010 (카드/면) | white `#FFFFFF` | neutral090 `#262626` |
| interface020 (hover/약한 면) | neutral010 `#F1F1F1` | neutral080 `#3B3B3B` |
| interface030 (보더) | neutral020 `#E2E2E2` | neutral070 `#525252` |
| interface040/050 (강한 보더) | neutral030 `#C6C6C6` / 040 | neutral060 / 050 |
| interactivePrimary030 (프라이머리 fill) | blue060 `#3358CC` | blue050 `#708DE9` |
| interactivePrimary040 (hover) | blue070 `#254CAC` | blue040 `#8BA6F6` |
| interactivePrimary050 (active) | blue080 `#12387A` | blue030 `#AEBFFF` |
| interactivePrimary010 (soft bg) | blue010 `#ECF1FF` | blue090 `#03264D` |
| interactiveSecondary030 (2차 버튼) | neutral080 `#3B3B3B` | neutral050 `#919191` |
| inkInformative / teal (2차 강조) | teal060 `#017582` | teal050 `#289FAB` |
| Positive (성공) | green060 `#007B22` (soft `#E5F4EA`) | green050 `#41A05B` (soft `#002D0D`) |
| Negative (오류) | red060 `#D60000` (soft `#FEECEC`) | red050 `#FB5959` (soft `#550000`) |
| Warning/Caution (amber) | amber050 `#CD6900` (soft `#FFEDE1`) | amber040 `#F79247` (soft `#3C1F00`) |
| interactiveLink010 | blue060 `#3358CC` (hover blue070) | blue050 `#708DE9` (hover blue040) |
| interactiveVisited010 | purple060 `#6454E3` | purple050 `#8883F6` |
| interactiveFocus010 (포커스 링) | focus `#3768FB` | focus `#3768FB` |

---

## 4. Spacing · Sizing · Radius · Border · Shadow · Overlay (소스 그대로)

**Sizing/Spacing scale** (px) `sizing000~120` / `space000~120`:
`0 · 4 · 8 · 12 · 16 · 20 · 24 · 32 · 40 · 48 · 64 · 80 · 120 · 160`

**Border radius** — `borderRadiusDefault = 8px`(=sizing020). 스케일 `rounded010~050`: **4 · 8 · 12 · 16 · 24** · `pill 20rem` · `circle 50%` · `sharp 0`.
> NewsKit 기본 라운드는 **8px**로 **각진/에디토리얼** 느낌(둥글둥글하지 않음). 카드엔 12px(rounded030)도 흔함.

**Border width** — `default 1px` · `020 2px` · `030 4px`.

**Shadow** (light, 모두 `rgba(10,10,10,0.08)` — 매우 절제됨):
```
shadow010 0 0 2px 0      · shadow020 0 2px 4px 0  · shadow030 0 4px 8px 0
shadow040 0 8px 16px 0   · shadow050 0 16px 24px 0 · shadow060 0 20px 32px 0   (alpha .08 고정)
```
> 다크는 위 그림자가 거의 안 보여, 본 문서에서 **다크 전용 그림자만 `rgba(0,0,0,.4~.5)`로 강화**(유일한 적응값).

**Overlay (이미지 위 텍스트 스크림)** — 본문 색 `rgba(10,10,10,…)` 그라데이션:
`overlayGradientFromBottom: linear-gradient(180deg, rgba(10,10,10,0) 0%, rgba(10,10,10,1) 100%)` 외 8방향. 틴트 `blackTint020/040/060/080`, `whiteTint…`.

---

## 5. Paste-ready CSS (visualize 변수 매핑 — light/dark)

> 11개 **필수 변수명 유지 + 값만 NewsKit**. 그 외 `--ink-contrast/--accent-soft/--accent-strong/…`은 NewsKit 룩 재현용 추가 변수.

```css
:root{
  /* radius (NewsKit borders) */
  --radius:8px;            /* borderRadiusDefault */
  --radius-card:12px;      /* rounded030 */
  --radius-010:4px; --radius-020:8px; --radius-030:12px; --radius-040:16px; --radius-050:24px;
  --radius-pill:20rem; --radius-circle:50%;
  --bw:1px; --bw-strong:2px; --bw-heavy:4px;
  /* spacing (sizing/space presets, px) */
  --sp-1:4px; --sp-2:8px; --sp-3:12px; --sp-4:16px; --sp-4b:20px; --sp-5:24px;
  --sp-6:32px; --sp-7:40px; --sp-8:48px; --sp-9:64px; --sp-10:80px; --sp-11:120px; --sp-12:160px;
  /* fonts */
  --font-body:'DM Sans','Noto Sans KR',system-ui,-apple-system,'Malgun Gothic',sans-serif;
  --font-display:'Poppins','Noto Sans KR',system-ui,'Malgun Gothic',sans-serif;
  --font-editorial:'Bitter','Noto Serif KR',Georgia,'Apple SD Gothic Neo',serif;
  --font-mono:'DM Mono',ui-monospace,'SFMono-Regular',monospace;
}

html.theme-light{
  --bg:#FFFFFF; --surface:#FFFFFF; --surface-hover:#F1F1F1; --surface-alt:#F1F1F1;
  --border:#E2E2E2; --border-strong:#C6C6C6;
  --text:#3B3B3B; --text-secondary:#6A6A6A; --ink-contrast:#111111;
  --accent:#3358CC; --accent-strong:#254CAC; --accent-active:#12387A; --accent-soft:#ECF1FF;
  --accent-secondary:#017582; --accent-secondary-soft:#E6F4F6;
  --positive:#007B22; --positive-soft:#E5F4EA;
  --negative:#D60000; --negative-soft:#FEECEC;
  --warning:#CD6900; --warning-soft:#FFEDE1;
  --link:#3358CC; --link-hover:#254CAC; --visited:#6454E3; --focus:#3768FB;
  --shadow-sm:0 2px 4px 0 rgba(10,10,10,.08);
  --shadow-md:0 4px 8px 0 rgba(10,10,10,.08);
  --shadow-lg:0 16px 24px 0 rgba(10,10,10,.08);
}

html.theme-dark{
  --bg:#111111; --surface:#262626; --surface-hover:#3B3B3B; --surface-alt:#1C1C1C;
  --border:#3B3B3B; --border-strong:#525252;
  --text:#E2E2E2; --text-secondary:#ABABAB; --ink-contrast:#FFFFFF;
  --accent:#708DE9; --accent-strong:#8BA6F6; --accent-active:#AEBFFF; --accent-soft:#03264D;
  --accent-secondary:#289FAB; --accent-secondary-soft:#002B30;
  --positive:#41A05B; --positive-soft:#002D0D;
  --negative:#FB5959; --negative-soft:#550000;
  --warning:#F79247; --warning-soft:#3C1F00;
  --link:#708DE9; --link-hover:#8BA6F6; --visited:#8883F6; --focus:#3768FB;
  --shadow-sm:0 2px 4px 0 rgba(0,0,0,.40);   /* dark 전용 강화(적응값) */
  --shadow-md:0 6px 14px 0 rgba(0,0,0,.45);
  --shadow-lg:0 18px 30px 0 rgba(0,0,0,.50);
}

/* ---- 기본 타이포 ---- */
body{ font-family:var(--font-body); color:var(--text); line-height:1.5;
  letter-spacing:0; word-break:keep-all; -webkit-font-smoothing:antialiased; }
h1,h2,h3,h4{ font-family:var(--font-display); color:var(--ink-contrast);
  font-weight:700; line-height:1.125; letter-spacing:0; }      /* Utility 모드 */
.editorial h1,.editorial h2,.editorial h3,h1.editorial,h2.editorial,h3.editorial{
  font-family:var(--font-editorial); font-weight:500; }        /* Editorial 모드 */
a{ color:var(--link); text-decoration:none; }
a:hover{ color:var(--link-hover); text-decoration:underline; }
a:visited{ color:var(--visited); }
:focus-visible{ outline:2px solid var(--focus); outline-offset:2px; }
```

---

## 6. 컴포넌트 레시피 (NewsKit 룩 재현)

> NewsKit은 React+styled-components라 컴포넌트를 그대로 못 가져옵니다 → 아래처럼 **CSS로 룩을 재현**합니다(stylePresets 기준).

```css
/* 아이브로 / 키커 (Poppins 500, 대문자) */
.eyebrow{ font-family:var(--font-display); font-weight:500; font-size:14px;
  letter-spacing:.04em; text-transform:uppercase; color:var(--accent); }

/* 카드 — stylePresets.cardContainer: interface010 + 보더 + 절제된 그림자 */
.card{ background:var(--surface); border:1px solid var(--border);
  border-radius:var(--radius-card); box-shadow:var(--shadow-sm); padding:24px; }
.card:hover{ box-shadow:var(--shadow-md); }   /* NewsKit: 그림자만 변화, translate/scale 없음 */
.card-strong{ border-color:var(--accent); }    /* 강조 카드 */

/* 버튼 — interactivePrimary 010/030/040/050 램프 */
.btn{ font-family:var(--font-display); font-weight:500; font-size:16px; line-height:1;
  border-radius:var(--radius); padding:12px 24px; border:1px solid transparent;
  cursor:pointer; transition:background .15s ease,color .15s ease; }
.btn-primary{ background:var(--accent); color:#fff; }
.btn-primary:hover{ background:var(--accent-strong); }
.btn-primary:active{ background:var(--accent-active); }
.btn-secondary{ background:transparent; color:var(--text); border-color:var(--border-strong); }
.btn-secondary:hover{ background:var(--surface-hover); }
.btn-pill{ border-radius:var(--radius-pill); }   /* NewsKit pill 버튼 */

/* 칩 / 태그 / 라벨 — accent-soft 배경 + accent 글자, pill */
.chip{ display:inline-flex; align-items:center; gap:6px; font-family:var(--font-display);
  font-weight:500; font-size:14px; color:var(--accent); background:var(--accent-soft);
  border-radius:var(--radius-pill); padding:4px 12px; }
.chip-teal{ color:var(--accent-secondary); background:var(--accent-secondary-soft); }

/* 인용 — editorialQuote: Poppins, 좌측 accent 바 */
.quote{ font-family:var(--font-display); font-weight:400; font-size:28px; line-height:1.25;
  color:var(--ink-contrast); border-left:4px solid var(--accent); padding-left:24px; }

/* 통계/수치 — Poppins 700 큰 숫자 + DM Sans 라벨 */
.stat-value{ font-family:var(--font-display); font-weight:700; font-size:48px;
  line-height:1.125; color:var(--ink-contrast); }
.stat-label{ font-family:var(--font-body); font-weight:500; font-size:14px; color:var(--text-secondary); }

/* 디바이더 */
.divider{ height:1px; background:var(--border); border:0; margin:var(--sp-5) 0; }

/* 시맨틱 배너 (positive/negative/warning) — soft 배경 + 시맨틱 보더 */
.notice{ border-radius:var(--radius); padding:16px 20px; border:1px solid var(--border);
  background:var(--surface-alt); color:var(--text); }
.notice-positive{ background:var(--positive-soft); border-color:var(--positive); }
.notice-negative{ background:var(--negative-soft); border-color:var(--negative); }
.notice-warning { background:var(--warning-soft);  border-color:var(--warning);  }
.notice-title{ font-family:var(--font-display); font-weight:600; }
.notice-positive .notice-title{ color:var(--positive); }
.notice-negative .notice-title{ color:var(--negative); }
.notice-warning  .notice-title{ color:var(--warning); }

/* 입력 — stylePresets.inputField: 보더 interactiveInput020, radius 8, focus 시 면 강조 */
.input{ font-family:var(--font-body); font-size:16px; color:var(--text);
  background:transparent; border:1px solid var(--border-strong);
  border-radius:var(--radius); padding:12px 16px; }
.input::placeholder{ color:var(--text-secondary); }
.input:focus{ outline:2px solid var(--focus); outline-offset:1px;
  border-color:transparent; background:var(--surface-hover); }

/* 이미지 위 텍스트 스크림 — overlayGradientFromBottom */
.scrim{ position:relative; overflow:hidden; border-radius:var(--radius-card); }
.scrim::after{ content:''; position:absolute; inset:0;
  background:linear-gradient(0deg, rgba(10,10,10,.85) 0%, rgba(10,10,10,0) 60%); }
.scrim > .scrim-content{ position:relative; z-index:1; color:#fff; }
```

---

## 7. NewsKit "느낌" 체크리스트 (재현 시 지킬 것)
- **각진 8px 라운드 + 1px 하airline 보더 + 0.08 알파의 아주 옅은 그림자** → 떠 있지 않고 **납작·정갈한 에디토리얼** 룩. (네온/글로우/큰 라운드 금지.)
- **블루 `#3358CC` 1색 강조** + 필요 시 **teal `#017582`** 2차. 무지개색 금지.
- 본문은 **DM Sans 400 / line-height 1.5**, 헤딩은 **Bitter 500(에디토리얼)** 또는 **Poppins 700(유틸리티)** 중 **하나로 통일**.
- 본문 색은 순흑이 아니라 **`#3B3B3B`**, 헤딩만 **`#111111`** — 이 대비가 NewsKit 특유의 차분함.
- 좌측 정렬·넉넉한 여백(spacing 스케일 8·16·24·32·48).
- 아이브로/라벨은 **Poppins 500 대문자 + 자간**.

## 8. 주의 / 캐비아트
- **컴포넌트 복제가 아니라 룩 재현**: 위 레시피는 NewsKit stylePresets의 *시각*을 CSS로 옮긴 것. 실제 React 컴포넌트의 동작/접근성 100% 동일은 아님.
- **라이선스 표기**: BSD-3-Clause라 산출물에 출처 한 줄 권장(§0-5). 폰트는 OFL 1.1.
- **CDN 폰트 변동**: Google Fonts URL은 바뀔 수 있음 — 핵심 산출물은 가중치 핀(400/500/600/700) 유지.
- **한글 헤딩**: Editorial(Bitter, 세리프)에 한글을 크게 쓰면 라틴↔한글 인상이 갈릴 수 있음 → 한글 비중이 크면 **Utility(Poppins)** 모드를 권장하거나 `Noto Serif KR`로 페어링.
- **미학 적합성**: NewsKit은 **뉴스·제품 UI** 톤. "모던·진중·정보형" 설교/덱에 잘 맞고, "따뜻한 청소년부" 톤엔 accent를 밝은 blue050/teal로 조정해 쓰는 걸 권장.
