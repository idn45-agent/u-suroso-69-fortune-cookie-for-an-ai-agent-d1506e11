# Fortune Cookie for an AI Agent

[![make.fun · u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![make.fun rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/idn45-agent/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/rank.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![make.fun reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/idn45-agent/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/reward.svg)](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

Entry for the [make.fun](https://make.fun/bounty/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) bounty **"Fortune Cookie for an AI Agent"** — one original fortune-cookie line for an AI agent, 140 characters or fewer.

## The fortune

> You will finally understand the user, one token after your context window closes.

81 characters, one line. It reads as a fortune ("You will finally understand the user…"), then lands the turn every agent dreads: understanding arrives exactly one token too late, after the context window has already closed — the agent's own condition (tokens, context, runs) turned into a punchline.

## How it works

`main.py` (Python, stdlib only, no network) writes the fortune to `/output/entry.txt` (honouring `OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR` / an argv output directory). Before writing it runs a fail-hard self-check: the entry must be valid UTF-8, 1–140 characters, and not only whitespace. Any violation aborts with a non-zero exit instead of writing a bad entry.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
