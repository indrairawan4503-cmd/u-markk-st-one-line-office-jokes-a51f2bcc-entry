# NOTES — One-Line Office Jokes, variant A (reply-all disaster)

Concept: one click, whole company, the apology email also goes reply-all.
One concept iterated v1→v8; the best version was submitted.

## Iterations (chars / bytes)

- v1 (102 / 102): I hit reply-all to complain about my boss, then hit reply-all again to apologise to the whole company.
  - Works, but "the whole company" is vague and "complain" is flat.
- v2 (91 / 91): I meant to vent about my boss to one colleague, but hit reply-all, so all 400 of us got it.
  - Specific number helps, but the punchline ("got it") lands soft and the apology twist is missing.
- v3 (114 / 114): I hit reply-all to call my boss a nightmare, then sent a reply-all apology that reached the exact same 400 people.
  - Good escalation, but "reached the exact same 400 people" explains the joke instead of landing it.
- v4 (99 / 99): My private rant about my boss went to all 400 colleagues with one reply-all, and so did my apology.
  - Tight, but "and so did my apology" is a summary, not a beat.
- v5 (117 / 117): I accidentally reply-all'd my rant about the boss to all 400 colleagues, then reply-all'd my apology to the same 400.
  - "reply-all'd" twice is clunky; reads like a tongue-twister, not a joke.
- v6 (109 / 109): One reply-all sent my "my boss is a nightmare" rant to all 400 colleagues, and my apology went reply-all too.
  - Quoted rant is strong; ending "went reply-all too" is decent but the sentence sags in the middle.
- v7 (117 / 117): I hit reply-all and told all 400 colleagues my boss is a nightmare, then hit reply-all again to apologise to all 400.
  - Clean parallel structure, but the ending repeats the setup instead of twisting it.
- v8 (115 / 117) — FINAL: I hit reply-all and told all 400 colleagues my boss is a nightmare, then apologised to all 400 — also by reply-all.

## Why v8 won

- Real detail: reply-all, a named audience of "all 400 colleagues", a boss rant — concrete office life, not generic work talk.
- The laugh lands in the last few words: "— also by reply-all" is the second disaster, delivered as an afterthought, which is the twist.
- One clear reading, no setup needed; fresh wording (no copied internet joke).
- Parallel structure (rant → apology, both reply-all) makes the escalation feel inevitable and funny.
- 115 chars / 117 bytes — inside the 1–199 char gate, near the useful length for a joke.

## Final line (verbatim)

I hit reply-all and told all 400 colleagues my boss is a nightmare, then apologised to all 400 — also by reply-all.

Chars: 115. Bytes: 117. No trailing newline.

## Validation

- main.py run 1 sha256 (/output/entry.txt): 4d9f5394af7f330b7d1a02be834aaf8dd6b01d59ab203b6f80e5371813260295
- main.py run 2 sha256 (/output/entry.txt): 4d9f5394af7f330b7d1a02be834aaf8dd6b01d59ab203b6f80e5371813260295
- Byte-identical across both runs; entry.txt in repo matches /output/entry.txt (same sha256).
- Read-only grader simulation (copy to /tmp, chmod -R a-w, run main.py): exit 0, /output/entry.txt sha256 4d9f5394af7f330b7d1a02be834aaf8dd6b01d59ab203b6f80e5371813260295.
- Gate check: 115 chars, 1–199, UTF-8, not whitespace-only — PASS.
