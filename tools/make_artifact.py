"""Turn index.html (the master copy) into a page for a Claude artifact.

Claude artifacts can't embed YouTube, so each embedded video becomes a
link button, and the document wrapper is removed (the artifact adds its own).

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

# strip the document wrapper
s = s[s.index('<title>'):]
s = s.replace('</head>\n<body>\n', '', 1)
s = s[:s.rindex('</body>')].rstrip('\n') + '\n'
open(out, 'w', encoding='utf-8').write(s)
print(f'{n} videos converted -> {out}')
