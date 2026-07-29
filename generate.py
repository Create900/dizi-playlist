#!/usr/bin/env python3
import time
import logging
from yt_dlp import YoutubeDL

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

channels = [
    ("Eşref Rüya", "jS4yNqXITBI"),
    ("Ezel", "9n-Du17MvQg"),
    ("Çocuklar Duymasın", "4SrvTqYmHvM"),
    ("Çukur", "rEhExHolYas"),
    ("Kurtlar Vadisi Pusu", "4QICVoMeA4s"),
    ("Cennet Mahallesi", "sIRnY47T9IU"),
    ("Türk Malı", "CZj3aXwxsXQ"),
    ("Sakarya Fırat", "LrXSGDCnmnQ")
]

ydl_opts = {
    "quiet": True,
    "skip_download": True,
    # Gerekirse cookiefile veya headers ekleyin:
    # "cookiefile": "cookies.txt",
}

def fetch_stream_url(url, retries=2, backoff=2):
    for attempt in range(1, retries + 2):
        try:
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
            if not info:
                raise ValueError("No info returned")
            if info.get("url"):
                return info["url"]
            formats = info.get("formats") or []
            if formats:
                return formats[-1].get("url")
            raise ValueError("No usable stream URL found")
        except Exception as e:
            logging.warning("Attempt %d failed for %s: %s", attempt, url, e)
            if attempt <= retries:
                time.sleep(backoff * attempt)
            else:
                return None

m3u_lines = ["#EXTM3U\n"]
failed = {}

for name, video_id in channels:
    url = f"https://www.youtube.com/watch?v={video_id}"
    stream_url = fetch_stream_url(url)
    if stream_url:
        m3u_lines.append(f'#EXTINF:-1 group-title="7/24 Canlı Diziler", {name} 7/24 Canlı')
        m3u_lines.append(f"{stream_url}\n")
        logging.info("Fetched: %s", name)
    else:
        logging.warning("Failed to fetch %s (%s)", name, url)
        failed[name] = url

with open("diziler.m3u", "w", encoding="utf-8") as f:
    f.write("\n".join(m3u_lines))

logging.info("Playlist updated successfully!")

if failed:
    logging.warning("Failed to fetch %d item(s):", len(failed))
    for k, v in failed.items():
        logging.warning("- %s : %s", k, v)
    # Eğer isterseniz burada non-zero exit ile job'un fail olmasını sağlayabilirsiniz:
    # raise SystemExit(1)
