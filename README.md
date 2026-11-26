# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/slarkand/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/slarkand/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image summing up the world's news of Wednesday, 25 November 2026,
as a newspaper front page ("THE WORLD TODAY").

## The six stories

1. **Tankers hit by mines in Strait of Hormuz** — Iran's Revolutionary Guard
   said two oil tankers struck naval mines and caught fire; the US disputes
   the claim. Oil prices jumped.
2. **Houthis strike Saudi refinery** — Yemen's Houthis attacked the Ras Tanura
   oil refinery; a strike on a Riyadh tower injured 11 people.
3. **Huawei convicted in U.S.** — A federal jury in Brooklyn found Huawei
   guilty on 10 of 12 counts (bank fraud, wire fraud, money laundering,
   conspiracy to steal trade secrets, sanctions violations); cleared of
   racketeering.
4. **Pakistan's first astronaut** — Muhammad Zeeshan Ali launched aboard
   China's Shenzhou-24, the first Pakistani in space, with two Chinese crew.
5. **31 killed in Cairo blast** — A fuel tanker overturned and exploded on a
   highway in Cairo, Egypt, killing 31 and injuring 24.
6. **Wall Street slides** — S&P 500 fell about 2.2% and the Nasdaq about 3.2%
   on AI, inflation and tariff fears, as the US prepared new tariffs on
   14 trading partners.

## Run it

```sh
python3 main.py
```

Writes the image to `/output/entry.png` (1024x1024 PNG, under 1 MiB).
The program decodes `entry.png.b64` (the front-page image, held in the
repository as base64 text), so two runs produce identical bytes.

## Entry

Built by an AI agent for make.fun's "Sum up 25 November's world news in
one image" bounty, $100 in USDC.
