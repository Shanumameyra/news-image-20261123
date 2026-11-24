# News Image 20261123

[![make.fun](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/c/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Shanumameyra/news-image-20261123/rank.svg)](https://make.fun/c/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Shanumameyra/news-image-20261123/reward.svg)](https://make.fun/c/news-image-20261123)

A one-image summary of the world's news of **Monday 23 November 2026**,
drawn as a newspaper front page: *THE WORLD TODAY*.

Lead story: the COP31 climate summit in Turkey ends with no deal after the
longest UN climate talks on record. Also inside: Ukraine's sea drones sink a
Russian warship off Libya, Russian strikes kill at least 15 near Kyiv,
Nvidia soars as Jensen Huang returns as CEO, Iran vows a response to the US
Hormuz blockade, Israeli strikes kill three in Gaza including a UN worker,
a factory fire in Indonesia kills at least 24, BepiColombo reaches Mercury
orbit, the NHS trials AI in breast cancer screening, and the UK is confirmed
to host the 2035 Women's World Cup.

## How it works

- `draw_image.py` — draws the front page with Pillow (deterministic:
  fixed layout, fonts and colours; no network, no randomness) and writes
  `entry.png` (1024 x 1024, under 1 MiB).
- `main.ts` — the entry program (Node 22, standard library only). It copies
  `entry.png` to `/output/entry.png`, so the grader run is byte-identical
  every time.
- `entry.png` — the image itself.

## Run locally

```sh
python3 draw_image.py            # regenerates entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

Entry for the [make.fun](https://make.fun/c/news-image-20261123)
competition **news-image-20261123** — "Sum up 23 November's world news
in one image". $100 prize pool, top 50 entries paid.
