"""Rebuild local badges with Python and requests: python scripts/generate_badges.py."""
from concurrent.futures import ThreadPoolExecutor
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

import requests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "badges"
# Pin the source so rebuilding preserves the same logos and license.
DEVICON_REF = "7330accdbc47e2dc0c19789a48533c4a3c50fe58"
BASE = f"https://raw.githubusercontent.com/devicons/devicon/{DEVICON_REF}"
SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)

BADGES = [
    ("html", "HTML5", "html5", "html5-original.svg", "#f47b50", 115),
    ("css", "CSS3", "css3", "css3-original.svg", "#6bbaff", 105),
    ("javascript", "JavaScript", "javascript", "javascript-original.svg", "#f7df1e", 150),
    ("php", "PHP", "php", "php-original.svg", "#b4a1ff", 100),
    ("csharp", "C#", "csharp", "csharp-original.svg", "#b795ed", 92),
    ("python", "Python", "python", "python-original.svg", "#78b9ec", 125),
    ("sql", "SQL", None, None, "#6ee7f7", 100),
]


def fetch(path):
    response = requests.get(f"{BASE}/{path}", timeout=30)
    response.raise_for_status()
    return response.text


def make_badge(spec):
    slug, label, folder, filename, color, width = spec
    if folder:
        icon = ET.fromstring(fetch(f"icons/{folder}/{filename}"))
        icon.attrib.update(x="14", y="9", width="22", height="22")
        icon.attrib.pop("class", None)
        logo = ET.tostring(icon, encoding="unicode")
    else:
        logo = '<g transform="translate(13 8)" fill="none" stroke="#6ee7f7" stroke-width="1.7"><ellipse cx="12" cy="5" rx="9" ry="3.5"/><path d="M3 5v15c0 4.7 18 4.7 18 0V5M3 12c0 4.7 18 4.7 18 0"/></g>'
    markup = (
        f'<svg xmlns="{SVG}" width="{width}" height="40" viewBox="0 0 {width} 40" role="img" aria-label="{escape(label)}">'
        f'<title>{escape(label)}</title>'
        f'<rect x=".5" y=".5" width="{width-1}" height="39" rx="9" fill="#101828" stroke="#33435a"/>'
        f'<path d="M13 39h{width-26}" stroke="{color}" stroke-width="1.5"/>'
        f'{logo}<text x="46" y="26" fill="#edf5ff" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="600">{escape(label)}</text>'
        '</svg>'
    )
    ET.fromstring(markup)
    return slug, markup


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=6) as pool:
        badges = list(pool.map(make_badge, BADGES))
    license_text = fetch("LICENSE")
    for slug, markup in badges:
        (OUT / f"{slug}.svg").write_text(markup + chr(10), encoding="utf-8")
    (OUT / "DEVICON-LICENSE.txt").write_text(license_text, encoding="utf-8")
    print(f"Generated {len(badges)} standalone SVG badges.")


if __name__ == "__main__":
    main()
