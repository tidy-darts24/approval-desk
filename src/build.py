"""Builds approval-desk.html from src.html: inlines the GT America web fonts, both logo colourways, the whitepaper visual and the physical card."""
import base64
import re
import zipfile
from pathlib import Path

root = Path(__file__).parent
assets = root / "assets"

src = (root / "src.html").read_text(encoding="utf-8")
b64 = lambda name: base64.b64encode((assets / name).read_bytes()).decode()

logo = (assets / "corpay-logo.svg").read_text(encoding="utf-8")
inner = re.search(r"<svg[^>]*>(.*)</svg>", logo, re.S).group(1).strip()

out = (
    src.replace("{{FONT_REG}}", b64("GT-America-Standard-Regular.f9f8deee.woff2"))
    .replace("{{FONT_MED}}", b64("GT-America-Standard-Medium.69df7c4a.woff2"))
    .replace("{{LOGO_WHITE}}", inner.replace('fill="black"', 'fill="#FFFFFF"'))  # Two-Tone White
    .replace("{{LOGO_DARK}}", inner.replace('fill="black"', 'fill="#231F20"'))  # Two-Tone Black, on the ghost card
    .replace("{{COVER}}", b64("whitepaper-book@2x.webp"))  # exported from Figma Web/Whitepaper visual (1016:8687) at 2x
    .replace("{{CARD}}", b64("physical-card@2x.webp"))
    .replace("{{BANNER_CARD}}", b64("banner-card.webp"))  # card mockup from the 44-days ad (1516:10173)
    .replace("{{BANNER_BOOK}}", b64("banner-book.webp"))  # whitepaper book from CTA · Book (793:9105)
    .replace("{{SCENE_TREE}}", b64("scene-tree.webp"))  # Won's Figma front (2142:8525): Christmas tree, desk and hamper cut-outs
    .replace("{{SCENE_DESK}}", b64("scene-desk.webp"))
    .replace("{{SCENE_PHONE}}", b64("scene-phone.webp"))  # Won's mobile front scene (2156:8601, Front props 1)
    .replace("{{SCENE_TREE_PHONE}}", b64("scene-tree-phone.webp"))
    .replace("{{SCENE_HAMPER}}", b64("scene-hamper.webp"))  # Fortnum & Mason product photo: use needs their OK  # exported from Figma Card/flat-front (41:6782) at 2x, shadow cropped off
)
assert "{{" not in out, "unreplaced placeholder"
(root / "approval-desk.html").write_text(out, encoding="utf-8")
print(f"wrote approval-desk.html ({len(out) // 1024} KB)")

# Standalone copy for people without Claude: the same skeleton the artifact host wraps the page in
# (charset, phone viewport), with the title and styles moved into <head>. Also used for local testing.
head, body = out.split("</style>\n", 1)
standalone = (
    '<!doctype html>\n<html lang="en-GB">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    "<style>:root{padding:env(safe-area-inset-top,0px) 0 env(safe-area-inset-bottom,0px)}"
    "body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"
    f"{head}</style>\n</head>\n<body>\n{body}</body>\n</html>\n"
)
share = root / "share"
share.mkdir(exist_ok=True)
page = share / "PaymentsChallenge.html"
page.write_text(standalone, encoding="utf-8")
with zipfile.ZipFile(share / "PaymentsChallenge.zip", "w", zipfile.ZIP_DEFLATED) as z:
    z.write(page, page.name)
print(f"wrote share/{page.name} and share/PaymentsChallenge.zip")

# The repo's index.html is the same standalone page, so GitHub Pages and reviewers always see the latest build
(root.parent / "index.html").write_text(standalone, encoding="utf-8")
print("wrote ../index.html")
