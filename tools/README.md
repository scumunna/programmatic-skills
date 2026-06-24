# Tools

Small, runnable helpers that go with the skills. They come in two kinds.

## Calculators (no setup, no credentials)

Pure arithmetic you can run on any machine with Python 3. They answer planning questions a
trader asks every day. Each prints usage with `--help` or no arguments.

| Tool | Answers | Example |
| --- | --- | --- |
| `ecpm_compare.py` | What is this buy worth on a common eCPM basis, so I can compare lines priced on CPM, CPC, CPA, or CPCV? | `python3 tools/ecpm_compare.py --model cpa --cpa 25 --ctr 0.002 --cvr 0.05` |
| `frequency_delivery_check.py` | Will my frequency cap and audience actually deliver the impressions I need? | `python3 tools/frequency_delivery_check.py --audience 500000 --freq-cap 10 --budget 30000 --cpm 6` |
| `budget_flight_planner.py` | Across this flight and CPM, what daily budget, impressions, and conversions should I expect? | `python3 tools/budget_flight_planner.py --budget 30000 --start 2026-07-01 --end 2026-07-31 --cpm 6 --ctr 0.002 --cvr 0.05` |

## Use the skills with any model

`skill_router.py` routes a question to the most relevant skill and uses it with any model: a
local server (Ollama, LM Studio, vLLM) or a hosted OpenAI-compatible endpoint. Standard library
only. See [../docs/USING-ANY-LLM.md](../docs/USING-ANY-LLM.md).

```
python3 tools/skill_router.py --list
python3 tools/skill_router.py --match "why is my DV360 line item not spending"
python3 tools/skill_router.py --ask "plan a CTV reach campaign" --base-url http://localhost:11434/v1 --model llama3.1
```

## Platform helpers (bring your own credentials)

Read-only report pullers bundled with the platform skills. They read from your own account
with your own credentials and never change anything.

| Tool | Platform | Where |
| --- | --- | --- |
| `dv360_report_puller.py` | DV360 (Bid Manager API) | `skills/dv360-api-and-sdf-automation/scripts/` |
| `sdf_template.py` | DV360 Structured Data Files | `skills/dv360-api-and-sdf-automation/scripts/` |
| `gaql_report_puller.py` | Google Ads (GAQL) | `skills/google-ads-api-and-bulk-operations/scripts/` |
| `pacing_calculator.py` | Any platform (in-flight pacing math) | `skills/dv360-pacing-and-optimization/scripts/` |

## The rule these tools follow

Read and recommend. Do not change live campaigns automatically. Every tool here either
computes something or reads a report. Anything that would spend money or change a campaign is
left to a person to review and apply. See [../docs/CONNECTING-TOOLS.md](../docs/CONNECTING-TOOLS.md)
for how to give an agent live platform access safely, and why writes stay behind a human.

## Requirements

The calculators need only Python 3. The platform helpers additionally need the Google API
client libraries and your own credentials, documented at the top of each script.
