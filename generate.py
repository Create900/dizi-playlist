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

m3u_lines = ["#EXTM3U"]

for name, video_id in channels:
    url = f"https://www.youtube.com/watch?v={video_id}"
    print(f"Fetching {name}...")
    try:
        cmd = ["yt-dlp", "-g", "--no-warnings", "--extractor-args", "youtube:player_client=android,web", url]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0 and res.stdout.strip():
            stream_url = res.stdout.strip().split("\n")[0]
            m3u_lines.append(f'#EXTINF:-1 group-title="7/24 Canlı Diziler", {name} 7/24 Canlı')
            m3u_lines.append(stream_url)
            print(f"OK: {name}")
        else:
            print(f"FAIL {name}: {res.stderr}")
    except Exception as e:
        print(f"ERROR {name}: {e}")

with open("diziler.m3u", "w", encoding="utf-8") as f:
    f.write("\n".join(m3u_lines) + "\n")

print("Playlist generated successfully!")
