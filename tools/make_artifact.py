"""Turn index.html (the master copy) into a page for a Claude artifact.

Claude artifacts can't embed YouTube, so each embedded video becomes a
link button; .m4a audio sources are dropped (the .mp3 copies remain); and the
document wrapper is removed (the artifact adds its own).

Usage: python3 tools/make_artifact.py index.html artifact.html
"""
import re, sys

src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()

# embedded players -> link buttons
s, n = re.subn(
    r'<div class="video-embed"><iframe src="https://www\.youtube-nocookie\.com/embed/([\w-]+)".*?</iframe>'
    r'<a class="video-fallback"[^>]*>.*?</a></div>',
    r'<a class="video-link" href="https://www.youtube.com/watch?v=\1" target="_blank" rel="noopener"><span>Open this video on YouTube ↗</span></a>',
    s, flags=re.S)
s = re.sub(r'  \.video-embed \{.*?\n  \.video-fallback \{[^\n]*\n', '', s, flags=re.S)

# Claude artifacts don't serve .m4a, so keep only the .mp3 audio sources
s = re.sub(r'<source src="audio/[^"]+\.m4a" type="audio/mp4">', '', s)

# strip the document wrapper
# Artifacts block downloads, so link the PDF guides to the copies on GitHub Pages instead.
s = re.sub(r'href="guides/([\w.-]+\.pdf)" download="[^"]*"', r'href="https://mcahalane.github.io/e-commerce-lesson/guides/\1" target="_blank" rel="noopener"', s)
s = s[s.index('<title>'):]
s = s.replace('</head>\n<body>\n', '', 1)
s = s[:s.rindex('</body>')].rstrip('\n') + '\n'
open(out, 'w', encoding='utf-8').write(s)
print(f'{n} videos converted -> {out}')
