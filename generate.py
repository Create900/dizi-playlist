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

def get_stream(video_id):
    try:
        cmd = ["yt-dlp", "-g", "--no-warnings", "--no-playlist", f"https://www.youtube.com/watch?v={video_id}"]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout.strip().split("\n")[0]
    except Exception as e:
        print(f"Error {video_id}: {e}")
    
    # Fallback kesintisiz canlı link
    return f"https://invidious.nerdvpn.de/latest_version?id={video_id}&itag=96"

m3u_lines = ["#EXTM3U"]

for name, video_id in channels:
    print(f"Processing {name}...")
    url = get_stream(video_id)
    m3u_lines.append(f'#EXTINF:-1 group-title="7/24 Canlı Diziler", {name} 7/24 Canlı')
    m3u_lines.append(url)

with open("diziler.m3u", "w", encoding="utf-8") as f:
    f.write("\n".join(m3u_lines) + "\n")

print("Generated diziler.m3u successfully!")
