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

m3u_content = "#EXTM3U\n\n"

for name, video_id in channels:
    m3u_content += f'#EXTINF:-1 group-title="7/24 Canlı Diziler", {name} 7/24 Canlı\n'
    m3u_content += f"https://invidious.nerdvpn.de/latest_version?id={video_id}&itag=96\n\n"

with open("diziler.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_content)

print("diziler.m3u olusturuldu!")
