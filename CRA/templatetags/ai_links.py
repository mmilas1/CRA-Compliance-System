from django import template
from django.utils.html import format_html
import re

register = template.Library()

# Define keywords you want to link
KEYWORDS = {
    "SBOM": "https://www.google.com/search?q=SBOM",
    "CVE": "https://www.google.com/search?q=CVE",
    "vulnerability": "https://www.google.com/search?q=vulnerability"
}

@register.filter
def link_keywords(text):
    def replacer(match):
        word = match.group(0)
        url = KEYWORDS.get(word)
        return format_html(f'<a href="{url}" target="_blank">{word}</a>') if url else word

    pattern = r'\b(' + '|'.join(map(re.escape, KEYWORDS.keys())) + r')\b'
    return re.sub(pattern, replacer, text)
