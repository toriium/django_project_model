from django.utils.safestring import mark_safe
from markdown_it import MarkdownIt

# Raw HTML inside the markdown is rendered as text instead of being passed through, to avoid XSS
md = MarkdownIt("commonmark", {"html": False}).enable(["table", "strikethrough"])


def build_markdown_text_context(text: str) -> dict:
    return {
        "html": mark_safe(md.render(text)),
    }
