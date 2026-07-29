import subprocess
import os

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

m3u_lines = ["#EXTM3U\n"]

for name, video_id in channels:
    url = f"https://www.youtube.com/watch?v={video_id}"
    try:
        stream_url = subprocess.check_output(
            ["yt-dlp", "-g", "--no-warnings", url],
            stderr=subprocess.DEVNULL
        ).decode("utf-8").strip()
        m3u_lines.append(f'#EXTINF:-1 group-title="7/24 Canlı Diziler", {name} 7/24 Canlı')
        m3u_lines.append(f"{stream_url}\n")
    except Exception as e:
        print(f"Error fetching {name}: {e}")

with open("diziler.m3u", "w", encoding="utf-8") as f:
    f.write("\n".join(m3u_lines))

print("Playlist updated successfully!")
