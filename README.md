# The Joke About the Demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/nemesisbug/demo-typo-joke/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/nemesisbug/demo-typo-joke/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)

A [make.fun](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
entry for **The joke about the demo**: a program that writes one one-line
joke about working beside AI coding agents to `/output/entry.txt`.

## The joke

> My coding agent rehearsed the demo forty times flawlessly — then, live in
> front of two hundred people, it spotted a typo and fixed it by taking the
> whole app down.

The angle: the agent is not the thing that breaks the demo — it is the thing
that *fixes* it, live, in front of everyone, and the fix is the disaster.
Forty flawless rehearsals, one unprompted "improvement", one dead app. Every
developer who has watched an agent "helpfully" refactor working code five
minutes before a demo has lived this exact moment.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` (Python 3.13, stdlib only, no network) writes the joke to
`/output/entry.txt` — one line, 163 characters, UTF-8.

## License

MIT — see [LICENSE](LICENSE).
