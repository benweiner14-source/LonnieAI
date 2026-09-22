#!/usr/bin/env python3
"""Pull the transcript/captions text from a YouTube video link.

Usage:
    python3 transcript.py "<youtube url or video id>" [--timestamps] [--lang en] [--out FILE]

Defaults to clean paragraph text (no timestamps). Uses YouTube's existing
caption track via youtube-transcript-api (no download, no API cost).
Falls back to yt-dlp auto-subs if the API can't fetch them.
"""
import argparse
import re
import subprocess
import sys
import tempfile
import os


def extract_video_id(s: str) -> str:
    s = s.strip()
    # Already a bare 11-char id
    if re.fullmatch(r"[0-9A-Za-z_-]{11}", s):
        return s
    patterns = [
        r"(?:v=|/shorts/|/embed/|youtu\.be/|/v/)([0-9A-Za-z_-]{11})",
    ]
    for p in patterns:
        m = re.search(p, s)
        if m:
            return m.group(1)
    raise ValueError(f"Could not extract a video id from: {s}")


def via_api(video_id: str, lang: str):
    from youtube_transcript_api import YouTubeTranscriptApi
    api = YouTubeTranscriptApi()
    fetched = api.fetch(video_id, languages=[lang, "en"])
    # fetched is iterable of snippets with .text, .start, .duration
    return [(snip.text, snip.start) for snip in fetched]


def via_ytdlp(url: str, lang: str):
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, "sub")
        subprocess.run([
            "yt-dlp", "--skip-download", "--write-auto-subs", "--write-subs",
            "--sub-langs", f"{lang},en", "--sub-format", "vtt",
            "-o", out, url,
        ], check=True, capture_output=True)
        vtt = next((os.path.join(tmp, f) for f in os.listdir(tmp) if f.endswith(".vtt")), None)
        if not vtt:
            raise RuntimeError("yt-dlp produced no subtitle file")
        text = []
        seen = set()
        for line in open(vtt, encoding="utf-8"):
            line = line.strip()
            if not line or line.startswith(("WEBVTT", "Kind:", "Language:")) or "-->" in line:
                continue
            line = re.sub(r"<[^>]+>", "", line)
            if line and line not in seen:
                seen.add(line)
                text.append((line, None))
        return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--timestamps", action="store_true", help="prefix each line with [mm:ss]")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--out", help="write to file instead of stdout")
    args = ap.parse_args()

    try:
        vid = extract_video_id(args.url)
        try:
            segments = via_api(vid, args.lang)
        except Exception as e:
            print(f"[api failed: {e}; falling back to yt-dlp]", file=sys.stderr)
            segments = via_ytdlp(args.url, args.lang)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    lines = []
    for text, start in segments:
        text = text.replace("\n", " ").strip()
        if not text:
            continue
        if args.timestamps and start is not None:
            ts = f"[{int(start)//60:02d}:{int(start)%60:02d}] "
            lines.append(ts + text)
        else:
            lines.append(text)

    output = "\n".join(lines) if args.timestamps else " ".join(lines)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(output + "\n")
        print(f"Wrote {len(lines)} segments to {args.out}")
    else:
        print(output)


if __name__ == "__main__":
    main()
