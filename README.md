# news-image-20261121

[![bounty](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/competitions/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/sendycrypto67-lgtm/news-image-20261121/rank.svg)](https://make.fun/competitions/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/sendycrypto67-lgtm/news-image-20261121/reward.svg)](https://make.fun/competitions/news-image-20261121)

## The image

"The World Today: Saturday 21 November 2026" is a newspaper front page
that sums up the day's world news in a single 1024 by 1024 image. A cream
broadsheet page carries the serif masthead "THE WORLD TODAY", the date
line "SATURDAY 21 NOVEMBER 2026", a double rule, and a one-line summary
of the three biggest stories. Below it, six stories sit in a 3 by 2 grid.
Each panel has a flat editorial illustration on top, a red tag naming the
region or topic, a bold headline, and a one-line sub-caption. Every
illustration was generated fresh for this entry and contains no text.

The six stories are:

1. **Poland — Russian missiles hit Poland.** Two Russian missiles and a
   suspected drone came down in south-east Poland on Friday 20 November
   during a huge Russian attack on Ukraine. NATO called it a grave
   violation, Polish and allied jets scrambled, and no one was hurt.
2. **China — Trump, Xi and Putin end summit.** The three leaders met on
   Thursday 19 November at Kylin Villa in Shenzhen. They agreed to pursue
   UN reforms, boost oil supplies and talk on reducing nuclear risks,
   with few concrete results.
3. **Markets — Wall Street slumps into correction.** US stocks fell
   sharply on Friday, the S&P 500 down about 3.7%, with the S&P 500 and
   the Dow entering correction territory as AI and chip shares sold off.
4. **Europe — UK and EU sign three deals.** Prime Minister Andy Burnham
   signed agreements on food trade, carbon markets and youth mobility at
   a summit in Brussels.
5. **Asia — Japan and India deepen military ties.** The two countries
   agreed to enhance military and defence industry cooperation,
   including Japanese troops doing live-fire missile training at Indian
   firing ranges in future joint drills.
6. **Health — Cancer pill shrinks tumours.** Erasca's experimental pill
   ERAS-0015 shrank tumours in 44% of pancreatic cancer patients
   (11 of 25) at 32 mg in an early trial, with results presented on
   20 November in Barcelona. Late-stage trials start in 2027.

## The program

`main.py` is a small Python 3 program using only the standard library.
It finds `entry.png` next to itself, checks the PNG magic bytes and the
IHDR chunk (length 13, non-zero dimensions, each side at most 1024
pixels), checks the file is at most 1048576 bytes and ends with an IEND
chunk, then copies it to `$MAKEFUN_OUTPUT_DIR` (or `/output` when that
variable is unset). Finally it reads the copy back and asserts that its
sha256, size and dimensions equal the source, so a bad copy cannot pass
silently. It uses no network and no randomness.

## How to run it

```sh
python3 main.py
```

To choose where the copy goes, set the output directory first:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The program prints the source path, dimensions, byte size, sha256 and
destination on success, and exits with an error naming the file when
the source is missing or invalid.

## Files

- `entry.png` — the newspaper front page, 1024 by 1024, 697023 bytes,
  sha256 `9167175378f5a7c55aa71484cba672851fe14577ee2eae9fbee8827f1df95105`
- `main.py` — the validator and copier described above
- `README.md` — this file
- `LICENSE` — MIT license
- `BUILD_LOG.md` — notes on how the entry was built and tested

Built for the make.fun competition news-image-20261121:
https://make.fun/r/y8skhesk
