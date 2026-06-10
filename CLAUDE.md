# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 이 저장소는 무엇인가

예배 설교 PPT를 **16:9 HTML 슬라이드**로 만드는 5단계 서브에이전트 파이프라인이다. **메인 세션(너)이 오케스트레이터**로서 단계별 에이전트를 순서대로 호출하고, 두 번의 사용자 컨펌 게이트를 통과시킨다. 별도 오케스트레이터 파일은 없다 — 네가 그 역할이다.

- 최종 산출물 = `sermons/<id>/03-slides/`의 **정적 16:9 HTML 아트보드**. 그대로 투사·발표한다.
- **PPTX 변환 단계는 없다.** (과거 pptx-builder 에이전트는 폐기됨 — PPTX를 만들려 하지 마라.)
- 일반적 의미의 빌드·린트·테스트가 없는 **콘텐츠/HTML 파이프라인**이다.

## 파이프라인 (오케스트레이터가 조율)

| 단계 | 담당 | 입력 → 출력 | 게이트 |
|---|---|---|---|
| 1 인제스트 | 오케스트레이터 직접 | 원고(docx/pdf) → `01-script.md` | — |
| 2 스토리라인 | `sermon-storyline-architect` | `01-script.md` → `02-storyline.md` | — |
| 3 콘텐츠 감수 | `storyline-reviewer` | → `02-storyline.review.md` | **사용자 컨펌#1** |
| 4 비주얼 | `slide-visual-designer` | `02-storyline.md` → `03-slides/` (visualize 스킬) | — |
| 5 디자인 감수 | `design-reviewer` | 실제 렌더(Playwright) → `03-slides.review.md` | **사용자 컨펌#2** → 최종 |

- **생성자/비평가 분리:** 리뷰어(3·5단계)는 **리포트만** 내고 직접 수정하지 않는다. 수정은 생성자(2·4단계)가 한다.
- 리뷰 판정 심각도: 🔴 필수 / 🟡 권장 / 🟢 선택. **🔴가 하나라도 있으면 ✅통과 불가** → 생성자가 재작업.
- **두 게이트는 사용자가 통과시킨다.** 사용자 컨펌 없이 다음 단계로 진행하지 마라.
- **형식(Format) 적용:** 오케스트레이터가 킥오프 때 **형식**을 결정(사용자 지정 > 덱 성격 추천 > 지정 없음)해 아키텍트에 전달한다(디자인 요청과 같은 결). 2단계가 슬롯 구조화 → 4단계가 골격 렌더 → 3·5단계가 구조·골격 충실도 감수. 상세는 아래 `## 형식(Format)`.

## 작업 폴더 규약

설교 하나당 `sermons/<날짜-제목>/` 폴더:

```
sermons/<id>/
  01-script.md              # 입력 원고 (오케스트레이터가 인제스트)
  02-storyline.md           # 2단계 산출 / 4단계 입력
  02-storyline.review.md    # 3단계 리포트
  03-slides/
    slide-NN.html           # 슬라이드당 1개 독립 HTML
    index.html              # 미리보기 그리드
    assets/slide-NN.png     # AI 이미지(선택)
  03-slides.review.md       # 5단계 리포트
```

## 절대 불변식 (어떤 단계에서도 위반 금지)

- **원고 충실성 최우선.** 원고에 있는 메시지·교리만 옮긴다. 해석을 임의로 더하거나 바꾸지 않는다. 세컨드 브레인의 학습된 취향도 이 원칙을 **넘지 못한다**(충돌 시 원고 우선 + 플래그). 불확실하면 `[확인필요]`로 표시.
- **예배 순서는 범위 밖.** 찬양·기도·봉헌·광고·축도·성찬 등은 슬라이드로 만들지 않는다 — 원고에 섞여 있어도 제외하고 **설교 본문만** 슬라이드화한다. (`전환·구분` 슬라이드 유형은 설교 내부의 대지 전환에만 쓴다.)
- **형식은 구조 골격일 뿐.** 형식(`format/`)은 슬라이드 구조를 정하지만 **원고 충실성·예배 순서 범위를 넘지 못한다**(위 두 불변식·세컨드 브레인 가드와 동일 계층). 충돌 시 콘텐츠 우선.
- **AI 이미지 신학 가드(중도).** 하나님·삼위일체의 형상이나 예수의 얼굴은 묘사하지 않는다(성경 장면·사물·인물은 허용). `scripts/generate_image.py`의 `POLICY` 블록이 강제하지만, 디렉티브를 만들 때 너도 인지한다.

## 세컨드 브레인 (`knowledge/user-brain.md`)

전 에이전트가 공유하는 **사용자 선호 지식베이스**(취향). 솔루션 KB(`docs/solutions/`)와는 별개다.

- **scope:** `storyline` / `design` / `global`. 각 에이전트는 **자기 scope + global**만 적용·수정한다. (형식 구조 선호는 `storyline` scope — 아키텍트 소유.)
- **쓰기/읽기:** `sermon-storyline-architect`가 쓰기·커밋(storyline·global), `slide-visual-designer`는 읽기·적용만(design·global).
- **컨펌된 피드백만 규칙화한다(제안형).** 미검토 산출물은 시드/가중치에서 제외. 일회성 지시는 규칙으로 만들지 않는다.
- **커밋 흐름:** architect가 핸드오프에 `🧠 규칙 후보`를 제시 → 사용자가 승인/수정 → **오케스트레이터가 architect를 "커밋 모드"로 재호출**해 `user-brain.md`(규칙표 + 선호 프로파일 + 변경 로그)를 갱신한다.
- **적용 우선순위:** 원고 충실성[절대] > 필수 > 중요 > 선호 > 실험. (중요도 점수와 성숙도 상태 provisional/established/retired는 분리.)

## 디자인

- **톤 결정 우선순위:** 사용자 지정 > 대상·절기(대예배=절제 / 청소년·캠프=명랑) > 세컨드 브레인 > 절제된 기본.
- **공통 규칙:** 좌측 정렬 기본(중앙은 의도적 예외), `word-break: keep-all`, 본문 ≥28px급 고대비, 줄바꿈은 의미 단위(어절·구)에만.
- **재사용 토큰 레퍼런스:** `design/montage-web.md`(Montage — Wanted Sans·브랜드 블루 `#0066FF`·light-first), `design/newskit.md`(NewsKit — BSD-3, OFL 폰트). 5가지 스타일 비교 예시는 `test/output/styles/index.html`.

## 형식(Format)

슬라이드의 **구조(골격)**를 정하는 **도메인 중립 재사용층** — 디자인이 *룩*을 고르듯 형식은 *구조*를 고른다. 설교뿐 아니라 행사·강의 등 **모든 토픽**에 쓰인다(설교 파이프라인이 첫 소비자).

- **레지스트리:** `format/README.md`(사용 가능 형식·트리거·선택 규칙) + `format/<type>.md`(형식별 골격 — 슬롯·순서·헤더 해부·chrome·필수/선택 슬롯·네이티브 베이스·DOM 계약). 현재 `lecture-deck` 1종.
- **3층:** 내용 > **형식** > 디자인. 적용 우선순위 **콘텐츠 진실성[절대] > 형식 > 디자인**.
- **선택:** 사용자 지정 > 덱 성격 추천 > `지정 없음(자유 구조=현행)`. 미지정이면 형식 골격 미적용(전 단계 현행 동작 — 하위호환).
- **슬롯 직교:** 형식 슬롯(표지/목표/아젠다/단원구분/번호본문/마무리)은 내용유형(대지/예화/봉독…)과 **직교** — 내용유형은 유지하고 슬롯을 추가 태깅한다.
- **생명주기:** 오케스트레이터 선택 → 2단계 슬롯 구조화·태깅 → 4단계 골격 렌더(`data-fmt` 부착) → 3·5단계 구조·골격 감수. **렌더(4)·검증(5)은 내용 무관이라 다른 토픽도 재사용**(콘텐츠→슬롯 어댑터만 교체).

## 명령

```powershell
# AI 이미지 생성 (4단계, GPT-5.5 → gpt-image-2). 실패 시 종료코드 2(설정)/3(생성) → 디자이너가 SVG 폴백
py scripts/generate_image.py --intent "<이미지 묘사>" --context "<헤드라인+대상·절기·톤>" --out "sermons/<id>/03-slides/assets/slide-NN.png"

# 이미지 생성 의존성 + 키 (.env는 git 제외)
py -m pip install openai python-dotenv      # 루트 .env에 OPENAI_API_KEY=sk-...

# 슬라이드 미리보기
Start-Process "sermons/<id>/03-slides/index.html"
```

- **1단계 인제스트는 스크래치다.** `workspace/extract.py`·`assemble.py`는 docx/pdf → 텍스트 → `01-script.md` 변환 예시이며 특정 세션에 하드코딩됐다(`pypdf` 필요). 재사용 도구가 아니라 패턴 참고용 — 새 설교마다 맞게 쓴다.
- `scripts/`·`workspace/`는 현재 **untracked**(개발 중).

## 세션 학습 기록

`/reflect`로 세션 교훈을 `docs/solutions/<category>/sol-YYYYMMDD-NNN.md` + `index.json`에 적재한다. 카테고리: `bug-fix` / `architecture` / `workflow` / `tool-usage` / `pattern`. (이건 해결책 KB로, 사용자 취향 KB인 `user-brain.md`와 구분된다.)
