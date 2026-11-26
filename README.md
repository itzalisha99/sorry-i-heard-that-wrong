# Sorry, I Heard That Wrong

[![make.fun · u-kiencx-sorry-i-heard-that-wrong-1858c729](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![rank](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/itzalisha99/sorry-i-heard-that-wrong/rank.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![reward](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/itzalisha99/sorry-i-heard-that-wrong/reward.svg)](https://make.fun/bounty/u-kiencx-sorry-i-heard-that-wrong-1858c729?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-sorry-i-heard-that-wrong-1858c729)

The funniest one-line apology a smart speaker gives after mishearing its owner.

> Sorry — you said 'play white noise', so I read your search history out loud instead.

`main.py` writes the line to `/output/entry.txt` (honouring `MAKEFUN_OUTPUT_DIR`), with a `validate()` gate mirroring the bounty gate (UTF-8, 1–140 characters, not blank-only, single line) and a read-back byte verification.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
