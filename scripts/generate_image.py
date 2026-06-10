# -*- coding: utf-8 -*-
"""슬라이드용 AI 이미지 생성 (파이프라인 4단계 보조 도구).

사용:  py scripts/generate_image.py --intent "<이미지 묘사>" --context "<헤드라인+대상·절기·톤>" --out "<png 경로>"
종료코드:  0 성공 / 2 설정 오류(키·의존성) / 3 생성 오류(API·정책 거부) → 디자이너는 2·3에서 SVG 폴백.
의존성:  py -m pip install openai python-dotenv   (루트 .env에 OPENAI_API_KEY=sk-...)
"""

import argparse
import base64
import json
import re
import sys
from pathlib import Path

# Windows cp949 콘솔에서 한글 메시지 깨짐 방지
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent

# 신학 이미지 가드(중도) — CLAUDE.md 절대 불변식. 프롬프트 정제 단계에 그대로 주입되어 강제된다.
POLICY = """\
[신학 이미지 가드 — 절대 규칙]
금지: 하나님(성부)·삼위일체의 시각적 형상화. 예수의 얼굴(정면이든 측면이든 식별 가능한 얼굴) 묘사.
허용: 성경 장면·사물·풍경·일반 인물, 비식별 실루엣·뒷모습, 상징(빛·길·문·십자가·물·빵·포도주 등).
적용: 금지 대상이 요청되면 상징·실루엣·풍경으로 대체해 의도를 보존한다. 대체가 불가능하면 거부한다.
거부 시에는 JSON의 refused를 true로 한다."""

# 금지 대상을 직접 요구하는 의도는 정제 모델에 '대체 필수'로 플래그
FORBIDDEN_RE = re.compile(r"(하나님|성부|삼위일체|예수)[^,.]{0,12}(얼굴|형상|모습|초상)")

PROMPT_MODEL = "gpt-5.5"     # 의도+맥락 → 이미지 프롬프트 정제 (POLICY 적용 주체)
IMAGE_MODEL = "gpt-image-2"
IMAGE_SIZE = "1536x1024"     # 16:9 아트보드용 가로형


def fail(code: int, msg: str):
    print(f"[generate_image] {msg}", file=sys.stderr)
    sys.exit(code)


def craft_prompt(client, intent: str, context: str) -> str:
    flagged = bool(FORBIDDEN_RE.search(intent + " " + context))
    instruction = (
        "너는 예배 설교 슬라이드의 배경/보조 이미지 프롬프트를 만드는 디렉터다.\n"
        f"{POLICY}\n"
        "아래 의도와 맥락을, 위 가드를 지키는 영어 이미지 프롬프트 한 문단으로 정제하라. "
        "텍스트·글자가 이미지에 들어가지 않게 하고, 슬라이드 배경으로 쓰기 좋게 과밀하지 않게.\n"
        + ("⚠ 의도에 금지 대상 묘사가 포함됨 — 반드시 상징·실루엣·풍경으로 대체하라.\n" if flagged else "")
        + 'JSON으로만 답하라: {"prompt": "<영어 프롬프트>", "refused": false} 또는 {"refused": true, "reason": "..."}'
    )
    resp = client.chat.completions.create(
        model=PROMPT_MODEL,
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": f"의도: {intent}\n맥락: {context}"},
        ],
        response_format={"type": "json_object"},
    )
    data = json.loads(resp.choices[0].message.content)
    if data.get("refused"):
        fail(3, f"정책 거부: {data.get('reason', '사유 미상')}")
    return data["prompt"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--intent", required=True, help="이미지 묘사(무엇을 그릴까)")
    ap.add_argument("--context", required=True, help="헤드라인+대상·절기·톤")
    ap.add_argument("--out", required=True, help="저장할 png 경로")
    args = ap.parse_args()

    try:
        from dotenv import load_dotenv
        from openai import OpenAI
    except ImportError as e:
        fail(2, f"의존성 누락({e.name}) — py -m pip install openai python-dotenv")

    load_dotenv(ROOT / ".env")
    import os
    if not os.environ.get("OPENAI_API_KEY"):
        fail(2, "OPENAI_API_KEY 없음 — 루트 .env에 설정하라")

    client = OpenAI()

    try:
        prompt = craft_prompt(client, args.intent, args.context)
    except SystemExit:
        raise
    except Exception as e:
        # 정제 실패는 치명적이지 않다 — POLICY를 포함한 로컬 조립으로 폴백
        print(f"[generate_image] 프롬프트 정제 실패({e}) → 로컬 조립 폴백", file=sys.stderr)
        if FORBIDDEN_RE.search(args.intent + " " + args.context):
            fail(3, "금지 대상 묘사 의도 — 정제 모델 없이 대체 불가, 거부")
        prompt = (
            f"{args.intent}. Context: {args.context}. "
            "Clean presentation slide background, no text, no letters. "
            "Never depict the face of Jesus or any visual form of God the Father or the Trinity."
        )

    try:
        img = client.images.generate(model=IMAGE_MODEL, prompt=prompt, size=IMAGE_SIZE)
        png = base64.b64decode(img.data[0].b64_json)
    except Exception as e:
        fail(3, f"이미지 생성 실패: {e}")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(png)
    print(f"[generate_image] 저장: {out} ({len(png)} bytes)")


if __name__ == "__main__":
    main()
