# PPT 제작 에이전트 (ppt_making_agents)

예배 설교 PPT를 자동으로 만드는 Claude Code 에이전트 파이프라인과, 그 산출물 예시를 담은 저장소입니다.

## 에이전트 파이프라인 (`.claude/agents`)

설교 원고 → 스토리라인 → 디자인 → PPTX로 이어지는 단계별 서브에이전트:

| 단계 | 에이전트 | 역할 |
|---|---|---|
| 2 | `sermon-storyline-architect` | 원고를 받아 슬라이드 스토리라인 작성 |
| 3 | `storyline-reviewer` | 스토리라인을 원고와 대조해 신학적 충실성·구조 감수 |
| 4 | `slide-visual-designer` | 스토리라인을 16:9 HTML 슬라이드 아트보드로 디자인 (visualize 스킬) |
| 5 | `design-reviewer` | 아트보드를 실제 렌더해 투사 가독성·일관성 감수 |
| 6 | `pptx-builder` | 승인된 HTML을 PowerPoint(.pptx)로 변환 |

## 산출물 예시

| 파일 | 설명 |
|---|---|
| `하나님은-누구신가-v2.html` | 「하나님은 누구신가?」 13장 설교 슬라이드 덱 (Montage 디자인 적용) |
| `하나님은-누구신가.html` | 동일 덱 v1 (경건체/세리프 버전) |
| `하나님은-누구신가-image.pptx` | v2를 이미지 기반으로 변환 (폰트 고정, 픽셀 일치) |
| `하나님은-누구신가-editable.pptx` | v2를 편집 가능한 네이티브 도형으로 변환 |
| `하나님은_누구신가_PPT_스토리보드.md` | 원본 스토리보드 |
| `montage-web.md` | 적용한 Montage(Wanted) 디자인 시스템 토큰 레퍼런스 |
| `claude-code-deck.html` | Claude Code 소개 데모 덱 |

## 디자인 시스템

슬라이드는 [Wanted Montage](https://github.com/wanteddev/montage-web) 디자인 시스템(Wanted Sans · 브랜드 블루 `#0066FF` · cool-neutral)을 따릅니다. 토큰 매핑은 `montage-web.md` 참고.
