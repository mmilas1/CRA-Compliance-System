from django import template
from django.utils.html import format_html
import re

register = template.Library()

KEYWORDS = [
    "SBOM", "CVE","EU Declaration of Conformity", "current cryptographic standards",
    "risk assessment", "external interfaces", "data at rest", "DoS", "foreseeable cybersecurity risks"
]

@register.filter
def link_keywords(text):
    def replace_keyword(match):
        keyword = match.group(0)
        query_url = f"https://you.com/search?q=What+is+{keyword.replace(' ', '+')}"
        return f'<a href="{query_url}" target="_blank">{keyword}</a>'

    pattern = re.compile(r'\b(' + '|'.join(re.escape(k) for k in KEYWORDS) + r')\b', re.IGNORECASE)
    return format_html(pattern.sub(replace_keyword, text))
