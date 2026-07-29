import os
import yt_dlp

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
    'quiet': True,
    'skip_download': True,
    'nocheckcertificate': True,
    'extractor_args': {'youtube': {'player_client': ['mweb', 'android']}}
}

def get_stream_url(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if info and 'url' in info and info['url']:
                return info['url']
            formats = info.get('formats') or []
            if formats:
                return formats[-1].get('url')
    except Exception as e:
        print(f"yt_dlp error for {video_id}: {e}")
    
    # Fallback kesintisiz canlı akış
    return f"https://invidious.nerdvpn.de/latest_version?id={video_id}&itag=96"

m3u_lines = ["#EXTM3U\n"]

for name, video_id in channels:
    print(f"Processing {name}...")
    stream_url = get_stream_url(video_id)
    m3u_lines.append(f'#EXTINF:-1 group-title="7/24 Canlı Diziler", {name} 7/24 Canlı')
    m3u_lines.append(f"{stream_url}\n")

with open("diziler.m3u", "w", encoding="utf-8") as f:
    f.write("\n".join(m3u_lines))

print("Playlist generated successfully!")
