# PPT 제작 에이전트 (ppt_making_agents)

예배 설교 PPT를 자동으로 만드는 Claude Code 에이전트 파이프라인과, 그 산출물 예시를 담은 저장소입니다.

## 에이전트 파이프라인 (`.claude/agents`)

설교 원고 → 스토리라인 → (형식 골격 +) 디자인(16:9 HTML 슬라이드)으로 이어지는 단계별 서브에이전트. 최종 산출물은 그대로 투사·발표하는 HTML 아트보드입니다:

| 단계 | 에이전트 | 역할 |
|---|---|---|
| 2 | `sermon-storyline-architect` | 원고를 받아 슬라이드 스토리라인 작성 |
| 3 | `storyline-reviewer` | 스토리라인을 원고와 대조해 신학적 충실성·구조 감수 |
| 4 | `slide-visual-designer` | 스토리라인을 16:9 HTML 슬라이드 아트보드로 디자인 (visualize 스킬) |
| 5 | `design-reviewer` | 아트보드를 실제 렌더해 투사 가독성·일관성·줄바꿈·정렬 감수 (최종 QA) |

## 세컨드 브레인 (`knowledge/user-brain.md`)

파이프라인은 사용자 선호를 누적하는 **공유 세컨드 브레인** `knowledge/user-brain.md`를 둔다. 중요도(필수/중요/선호/실험 + 0–100 점수)와 성숙도(provisional/established)로 취향을 규칙화하며, **사용자가 컨펌한 피드백에서만** 제안형으로 학습한다(미검토 산출물은 시드에서 제외). 파일 쓰기 주체는 `sermon-storyline-architect` 1명(storyline·global 직접 + design은 디자이너 제안분 대리 커밋)이고, `slide-visual-designer`는 읽기·적용 + design 규칙 후보 제안을 맡는다. scope는 `storyline`·`design`·`global`이다.

## 산출물 예시 (`test/output/`)

| 파일 | 설명 |
|---|---|
| `하나님은-누구신가-스토리라인.md` | 「하나님은 누구신가?」(교리설교 ②·송도청소년1부) 19슬라이드 스토리라인 — 줄바꿈·시각 컴포넌트·디자인 요청 반영 |
| `하나님은-누구신가-v3.html` | 위 스토리라인을 Montage 스타일로 구현한 16:9 슬라이드 덱 |
| `styles/` | 같은 슬라이드에 5가지 디자인 스타일을 입혀 비교 (`index.html`에서 열람): 진중 세리프 · 파스텔 팝 · 코스믹 나이트 · 리소그래프 팝 · 두들 저널 |

## 디자인 시스템 · 스타일

디자인 톤·스타일·폰트는 **사용자 요청과 대상**(예: 대예배 = 경건·절제, 청소년부 = 명쾌·명랑)에 맞춰 자유롭게 고릅니다. `test/output/styles/`가 한 설교를 5가지 스타일로 풀어낸 예시입니다.

자주 쓰는 레퍼런스 중 하나가 [Wanted Montage](https://github.com/wanteddev/montage-web)(Wanted Sans · 브랜드 블루 `#0066FF` · cool-neutral)이며, 토큰 매핑은 `design/montage-web.md`를 참고하세요.

## 형식(Format) 시스템

슬라이드의 **구조(골격)**를 정하는 **도메인 중립 재사용층**입니다(디자인이 *룩*을 고르듯, 형식은 *구조*를 고름). 설교뿐 아니라 **행사 안내·순서 요약·주제 강의 등 모든 토픽**에 재사용됩니다. 레지스트리는 `format/README.md`, 형식별 골격 사양은 `format/<type>.md`(현재 `lecture-deck` 1종 — 다단원 교육·강의형). 형식은 2단계에서 선택·구조화되고 4단계에서 렌더, 3·5단계에서 골격 충실도가 감수됩니다.
