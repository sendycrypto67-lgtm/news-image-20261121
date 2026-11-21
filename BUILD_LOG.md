# Build log — news-image-20261121

## The six stories

Built from the supplied verified facts for Saturday 21 November 2026,
with no casualty figures anywhere in the image and no speculative claim
shown as fact:

1. Poland — Russian missiles hit Poland; NATO calls it a grave violation,
   jets scrambled, no one hurt.
2. China — Trump, Xi and Putin end their Shenzhen summit with few
   concrete results.
3. Markets — Wall Street slumps into correction; S&P 500 falls 3.7%.
4. Europe — UK and EU sign three deals on food, carbon and youth
   mobility in Brussels.
5. Asia — Japan and India deepen military ties; live-fire missile
   training at Indian ranges agreed.
6. Health — Erasca pill ERAS-0015 shrinks tumours in 44% of pancreatic
   cancer patients in an early trial.

## Generation notes

Six flat editorial illustrations were generated fresh for this entry,
one per story, each prompted with no text, no words, no letters and no
numbers. All six were read back visually. Five were right first time.
The first summit image was regenerated because its flags were wrong
(they showed other countries); the replacement shows the Chinese,
American and Russian flags correctly, with three leaders shaking hands
at a round table in a Chinese villa hall. No other illustration needed
a second attempt.

## Compose notes

The page was composed with Python and Pillow in a script kept at
`/tmp/news-image-20261121-compose.py`. It draws a cream 1024 by 1024
page, a serif masthead "THE WORLD TODAY", the date line "SATURDAY
21 NOVEMBER 2026", a double rule, a one-line summary deck, and a 3 by
2 grid of panels. Each panel centre-crops its illustration, then adds
a red region tag, a bold headline and a one-line sub-caption, all in
DejaVu fonts. Headline and sub-caption sizes are adaptive and shared:
the script steps down from 26 pt (headline) and 14 pt (sub) until every
headline fits two lines and every sub fits one line, and asserts that
no panel overflows. Final sizes were headline 22 pt and sub 10 pt.

## Self-review notes

Defects found on visual read-back, and how each was fixed:

- Summit flags wrong in the first illustration (other countries shown).
  Fixed by regenerating with explicit flag descriptions; the new image
  shows the correct three flags.
- Large empty gap at the bottom of every panel in the first compose
  (about 90 px of blank panel). Fixed by adding a summary deck line
  under the masthead and a footer line at the bottom of the page, and
  by raising the illustration height from 246 to 256 px.
- Centre-cropping cut the Indian flag to a sliver in the Asia panel and
  cut the small shrinking tumour in half in the Health panel. Fixed by
  adding a per-image horizontal focal offset, shifting the Asia crop
  fully right and the Health crop mostly right, so both flags and both
  tumour shapes are fully visible.
- The first draft of the IEND check in main.py used the wrong byte
  offsets (it would have rejected every valid PNG). Caught while
  re-reading the code before testing and fixed to check the length
  bytes and the IEND type bytes in their correct positions.

Final read-back: every headline and sub-caption is spelled exactly,
nothing is garbled or cut off, nothing overflows, every illustration
matches its caption, and there are no large empty gaps.

## main.py description

`main.py` uses only the Python standard library. It validates
`entry.png` (PNG magic bytes, IHDR chunk with length 13 and non-zero
dimensions, each side at most 1024, file at most 1048576 bytes, IEND
chunk present), copies it to `$MAKEFUN_OUTPUT_DIR` or `/output`, then
re-reads the output file's own PNG header and asserts its sha256, size
and dimensions equal the source. No network, no randomness.

## Test results

- `python3 -m py_compile main.py`: passed.
- `main.py` run twice to two separate output dirs: both runs printed
  1024x1024, 697023 bytes, sha256
  `9167175378f5a7c55aa71484cba672851fe14577ee2eae9fbee8827f1df95105`;
  `cmp` of the two outputs was clean and both sha256 values equal the
  source.
- Output confirmed 1024x1024 PNG and under 1 MiB (697023 bytes).
- Negative test, non-PNG file: rejected, exit code 1, error naming the
  file ("invalid PNG in /tmp/negtest/entry.png: file too short").
- Negative test, 1200x1200 PNG: rejected, exit code 1, error naming the
  file ("invalid PNG in /tmp/negtest/entry.png: 1200x1200 exceeds
  1024x1024").

## Cleanup

The `assets/` directory (generated illustrations, build-time only) and
the compose script were removed from the repo. The repo holds exactly
five files: `entry.png`, `main.py`, `README.md`, `LICENSE`,
`BUILD_LOG.md`. Nothing was committed, pushed or submitted.
