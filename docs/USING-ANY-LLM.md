# Using these skills with any model: closed, open-weight, or local

The skills here are plain markdown, so the knowledge is model-agnostic. What differs is how a
given setup loads a skill at the right moment. There are three paths, from most built-in to
least.

## 1. Skill-aware harnesses (closed models, zero setup)

Claude Code and Codex read skills automatically. Install the package (see the main README) and
the assistant loads the right skill when your question matches. This is the smoothest path and
uses the strongest hosted models.

## 2. Model-agnostic agent frameworks (any model, including open-weight and local)

Several open agent frameworks run any model, hosted or local, and read external instructions.
Point them at this repository's `skills/` folder as their rules or context. Frameworks in this
category include Goose, OpenCode, Cline, Continue, and aider. The skills are portable markdown,
so they drop in as reusable instructions. Each framework configures custom instructions
differently, so follow its own docs for where to put them.

## 3. Any model directly, including a local one (the bundled router)

For a raw model with no skill harness, use `tools/skill_router.py`. It routes your question to
the most relevant skill and either prints a ready-to-paste prompt or sends it to any
OpenAI-compatible chat endpoint. That covers a local server (Ollama, LM Studio, vLLM) and a
hosted one (OpenAI, OpenRouter, Together, Groq). Standard library only, nothing to install.

```bash
# see what is available
python3 tools/skill_router.py --list

# which skill answers this?
python3 tools/skill_router.py --match "why is my DV360 line item not spending"

# print a prompt to paste into any model
python3 tools/skill_router.py --build "which bid strategy for a new conversion campaign"

# ask a LOCAL model (Ollama on its default port)
python3 tools/skill_router.py --ask "why is my DV360 line item not spending" \
    --base-url http://localhost:11434/v1 --model llama3.1

# ask a LOCAL model (LM Studio default port)
python3 tools/skill_router.py --ask "plan a CTV reach campaign" \
    --base-url http://localhost:1234/v1 --model your-local-model

# ask a HOSTED model
SKILL_ROUTER_API_KEY=sk-... python3 tools/skill_router.py --ask "set up consent mode" \
    --base-url https://api.openai.com/v1 --model gpt-4o-mini
```

For a cross-platform or ambiguous question, add `--top 2` to include the next-best skill too.

## Honest limits

- The router's matching is keyword-based. It is good for most questions and it shows its picks, but it is not as smart as a skill-aware harness. Name the platform or the intent ("deduplicated reach", "which DSP") for the cleanest match, or use `--match` to choose.
- The router is single-shot: one question, the right skill, one answer. It is not a multi-step agent with tool-calling. For agentic loops on any model, use a framework from path 2.
- A smaller local model gives weaker answers than a frontier model, but the skill content levels it up a lot, because the model follows the playbook instead of guessing.
- Credentials never enter the repo or a prompt. The router talks only to the endpoint you point it at.

## The principle

The value is the knowledge, and the knowledge is markdown. Closed, open-weight, and local
models can all use it. The only thing that changes is the loader, and this folder gives you one
that works everywhere.
