#!/usr/bin/env python3
"""Use these skills with any model: closed, open-weight, or local.

The skills in this repository are plain markdown, so the knowledge is model-agnostic.
Skill-aware harnesses (Claude Code, Codex) load them automatically. This router lets you
use the same skills with any other model through one OpenAI-compatible interface: a local
server (Ollama, LM Studio, vLLM) or a hosted one (OpenAI, OpenRouter, Together, Groq).

It routes a question to the most relevant skill and either prints an assembled prompt or
sends it to a model. It is a reference loader for single-shot, skill-grounded answers, not a
full multi-step agent. For agentic loops on any model, use a framework that reads these skills
(see docs/USING-ANY-LLM.md).

Modes:
  --list                 List every skill (name and description).
  --match "QUESTION"     Show the skills that best match the question.
  --build "QUESTION"     Print an assembled prompt (system instruction plus matched skills)
                         that you can paste into any model.
  --ask "QUESTION"       Send the assembled prompt to an OpenAI-compatible chat endpoint and
                         print the answer.

Endpoint options for --ask (flags or environment):
  --base-url URL   default http://localhost:11434/v1 (Ollama).  Env SKILL_ROUTER_BASE_URL
  --model NAME     default llama3.1.                            Env SKILL_ROUTER_MODEL
  --api-key KEY    optional for local servers.   Env SKILL_ROUTER_API_KEY or OPENAI_API_KEY
  --top N          how many matched skills to include (default 1).
  --skills-dir D   where the skills live (default: the skills folder next to this script).

Examples:
  python3 tools/skill_router.py --list
  python3 tools/skill_router.py --match "why is my DV360 line item not spending"
  python3 tools/skill_router.py --build "which bid strategy for a new conversion campaign"
  python3 tools/skill_router.py --ask "why is my DV360 line item not spending" \
      --base-url http://localhost:11434/v1 --model llama3.1
  SKILL_ROUTER_API_KEY=sk-... python3 tools/skill_router.py --ask "plan a CTV campaign" \
      --base-url https://api.openai.com/v1 --model gpt-4o-mini

Standard library only. No third-party packages.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

STOPWORDS = {
    "the", "a", "an", "is", "are", "do", "does", "my", "to", "for", "of", "in", "on",
    "and", "or", "i", "we", "how", "what", "which", "why", "should", "with", "this",
    "that", "it", "be", "can", "me", "you", "your", "not", "no", "at", "as", "by",
}

PLATFORM_HINTS = {
    "dv360": "dv360-", "display & video 360": "dv360-", "display and video 360": "dv360-",
    "google ads": "google-ads-", "adwords": "google-ads-", "shopping": "google-ads-",
    "performance max": "google-ads-", "pmax": "google-ads-",
    "amazon": "amazon-", "amazon dsp": "amazon-dsp-", "amc": "amazon-marketing-cloud",
    "stackadapt": "stackadapt-",
    "trade desk": "ttd-", "the trade desk": "ttd-", "ttd": "ttd-", "kokai": "ttd-",
    "uid2": "ttd-identity", "youtube": "dv360-youtube",
}

INTENT_BOOST = {
    "reach-and-frequency-planning": ["deduplicated reach", "effective frequency", "reach curve", "reach and frequency", "co-viewing", "frequency cap"],
    "incrementality-and-experimentation": ["incremental", "lift test", "holdout", "geo lift", "conversion lift", "is it incremental"],
    "dsp-selection": ["which dsp", "which platform", "platform selection", "best dsp", "best platform"],
    "marketing-mix-modeling": ["marketing mix", "media mix", "mmm"],
    "path-to-conversion-analysis": ["path to conversion", "touchpoints to convert", "assisted conversion"],
    "privacy-and-consent": ["consent mode", "gdpr", "ccpa", "cpra", "privacy sandbox", "cookieless"],
    "brand-safety-and-suitability": ["made for advertising", "sellers.json", "ads.txt", "invalid traffic", "supply path"],
    "discrepancy-and-reconciliation": ["discrepancy", "reconciliation", "make good", "ad server vs"],
    "value-based-bidding": ["value-based bidding", "value based bidding", "ltv bidding", "conversion value"],
    "data-quality-and-reconciliation": ["data quality", "anomaly detection", "numbers do not match"],
}

SYSTEM_INSTRUCTION = (
    "You are a programmatic advertising specialist (trader, analyst, and ad-operations). "
    "Answer using the skill playbook(s) below, following their decision rules, checklists, and "
    "steps. Do not invent platform specifics: where a skill says to verify a value in the "
    "platform, say so rather than guessing. You advise and recommend; you never imply you have "
    "changed a live account. Do not use em dashes."
)


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", text.lower())


def tokenize(text: str) -> list[str]:
    return [t for t in normalize(text).split() if t not in STOPWORDS and len(t) > 1]


def parse_skill(path: str):
    """Return (name, description, body) for a SKILL.md, or None if unparseable."""
    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None
    name, description, key, buf = "", "", None, []
    for raw in lines[1:end]:
        match = re.match(r"^([A-Za-z0-9_-]+):\s?(.*)$", raw)
        if match and not raw.startswith((" ", "\t")):
            if key == "description":
                description = "\n".join(buf).strip().strip('"').strip("'").strip()
            key = match.group(1)
            value = match.group(2).strip()
            if key == "name":
                name = value
            buf = [] if value in (">", "|", ">-", "|-") else [value]
        elif key == "description":
            buf.append(raw.strip())
    if key == "description" and not description:
        description = "\n".join(buf).strip()
    body = "\n".join(lines[end + 1:]).strip()
    return name, description, body


def load_skills(skills_dir: str):
    skills = []
    for entry in sorted(os.listdir(skills_dir)):
        path = os.path.join(skills_dir, entry, "SKILL.md")
        if os.path.isfile(path):
            parsed = parse_skill(path)
            if parsed and parsed[0]:
                name, description, body = parsed
                skills.append({"name": name, "description": description, "body": body})
    return skills


def score_skill(query: str, skill: dict) -> int:
    q_tokens = set(tokenize(query))
    if not q_tokens:
        return 0
    name_tokens = set(tokenize(skill["name"]))
    desc_tokens = set(tokenize(skill["name"] + " " + skill["description"]))
    score = 4 * len(q_tokens & name_tokens) + len(q_tokens & desc_tokens)
    norm_q = normalize(query)
    norm_desc = normalize(skill["name"] + " " + skill["description"])
    q_words = norm_q.split()
    for i in range(len(q_words) - 1):
        bigram = q_words[i] + " " + q_words[i + 1]
        if len(bigram) > 5 and bigram in norm_desc:
            score += 2
    for hint, prefix in PLATFORM_HINTS.items():
        if hint in norm_q and skill["name"].startswith(prefix):
            score += 1
    for phrase in INTENT_BOOST.get(skill["name"], []):
        if phrase in norm_q:
            score += 5
    return score


def rank(query: str, skills: list, top: int):
    scored = [(score_skill(query, s), s) for s in skills]
    scored = [(sc, s) for sc, s in scored if sc > 0]
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return scored[:top]


def build_prompt(matches: list) -> str:
    blocks = [f"# Skill: {s['name']}\n\n{s['body']}" for _, s in matches]
    return SYSTEM_INSTRUCTION + "\n\n" + "\n\n---\n\n".join(blocks)


def call_endpoint(base_url, model, api_key, system, user):
    url = base_url.rstrip("/") + "/chat/completions"
    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": 0.2,
        "stream": False,
    }).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    request = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    with urllib.request.urlopen(request, timeout=180) as response:
        data = json.load(response)
    return data["choices"][0]["message"]["content"]


def default_skills_dir() -> str:
    return os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "skills")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Route a programmatic question to the right skill and use it with any model.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--list", action="store_true", help="list every skill")
    group.add_argument("--match", metavar="QUESTION", help="show the best-matching skills")
    group.add_argument("--build", metavar="QUESTION", help="print an assembled prompt for any model")
    group.add_argument("--ask", metavar="QUESTION", help="send the prompt to an OpenAI-compatible endpoint")
    parser.add_argument("--top", type=int, default=1, help="matched skills to include (default 1)")
    parser.add_argument("--skills-dir", default=default_skills_dir(), help="path to the skills folder")
    parser.add_argument("--base-url", default=os.environ.get("SKILL_ROUTER_BASE_URL", "http://localhost:11434/v1"))
    parser.add_argument("--model", default=os.environ.get("SKILL_ROUTER_MODEL", "llama3.1"))
    parser.add_argument("--api-key", default=os.environ.get("SKILL_ROUTER_API_KEY") or os.environ.get("OPENAI_API_KEY"))
    return parser


def main(argv: list[str]) -> int:
    parser = build_parser()
    if not argv:
        parser.print_help()
        return 0
    args = parser.parse_args(argv)

    if not os.path.isdir(args.skills_dir):
        print(f"error: no skills folder at {args.skills_dir}. Pass --skills-dir.", file=sys.stderr)
        return 2
    skills = load_skills(args.skills_dir)
    if not skills:
        print(f"error: no skills found in {args.skills_dir}.", file=sys.stderr)
        return 2

    if args.list:
        for skill in skills:
            summary = skill["description"].replace("\n", " ")
            if len(summary) > 110:
                summary = summary[:107] + "..."
            print(f"{skill['name']}\n    {summary}")
        print(f"\n{len(skills)} skills.")
        return 0

    query = args.match or args.build or args.ask
    if not query:
        parser.print_help()
        return 0

    matches = rank(query, skills, max(1, args.top))
    if not matches:
        print("No skill matched. Try --list to see what is available, or rephrase.", file=sys.stderr)
        return 1

    if args.match:
        print(f"Best matches for: {query}\n")
        for score, skill in matches:
            print(f"  {skill['name']}  (score {score})")
        return 0

    prompt = build_prompt(matches)
    if args.build:
        print(prompt)
        return 0

    # --ask
    print(f"Using skill(s): {', '.join(s['name'] for _, s in matches)}", file=sys.stderr)
    print(f"Endpoint: {args.base_url}  model: {args.model}", file=sys.stderr)
    try:
        answer = call_endpoint(args.base_url, args.model, args.api_key, prompt, query)
    except urllib.error.HTTPError as error:
        print(f"error: the endpoint returned HTTP {error.code}. Check the model name and the API key.", file=sys.stderr)
        return 2
    except urllib.error.URLError as error:
        print(f"error: could not reach {args.base_url} ({error.reason}). Is the local server running?", file=sys.stderr)
        return 2
    except (KeyError, ValueError):
        print("error: the endpoint did not return an OpenAI-compatible chat response.", file=sys.stderr)
        return 2
    print(answer)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
