---
name: 2k-yt-transcript
description: Pull the transcript/caption text out of a YouTube video link. Use when the user pastes a YouTube URL and wants the transcript, captions, subtitles, or spoken text — e.g. "get the transcript", "transcribe this video", "what does this video say", "pull captions from this link".
---

# YouTube Transcript Extractor

Extracts the text transcript from any YouTube video using its existing caption
track. No download, no API key, no Apify cost — runs locally and instantly.

## How to run

The script lives next to this file, at `.claude/skills/2k-yt-transcript/transcript.py`
relative to the repo root. Run it with the video URL or ID:

```bash
python3 .claude/skills/2k-yt-transcript/transcript.py "<youtube url>"
```

### Options
- `--timestamps` — one line per segment, prefixed `[mm:ss]` (good for finding a moment / chaptering)
- `--lang xx` — preferred caption language (default `en`; always falls back to en)
- `--out FILE` — write to a file instead of printing (use for long videos so you don't flood the chat)

### Examples
```bash
# Clean paragraph text to stdout
python3 .claude/skills/2k-yt-transcript/transcript.py "https://youtu.be/VIDEOID"

# With timestamps, saved to a file
python3 .claude/skills/2k-yt-transcript/transcript.py "https://www.youtube.com/watch?v=VIDEOID" --timestamps --out /tmp/transcript.txt
```

### Dependencies
Requires `youtube-transcript-api` and `yt-dlp` (`pip install youtube-transcript-api yt-dlp`).
Already installed in this environment; if running elsewhere and the script errors with
`ModuleNotFoundError`, install those two packages first.

## Behavior notes
- Accepts full URLs, `youtu.be` short links, `/shorts/` links, or a bare 11-char video ID.
- Primary path: `youtube-transcript-api`. If that fails (rare regional/anti-bot block), it auto-falls back to `yt-dlp --write-auto-subs`.
- A `NotOpenSSLWarning` may print to stderr — ignore it, the transcript prints to stdout.
- For long videos, prefer `--out` and then summarize/quote from the file rather than dumping the whole thing into chat.

## When NOT to use this
If the user wants *unattended/scheduled* transcription (e.g. auto-transcribe every new upload on a channel into a Google Sheet), build an n8n workflow instead — this skill is for on-demand, paste-a-link use.
