import markdown
from django.utils.safestring import mark_safe
from markdown.extensions import Extension


class EscapeHtmlExtension(Extension):
    # Raw HTML inside the markdown is rendered as text instead of being passed through, to avoid XSS
    def extendMarkdown(self, md):
        md.preprocessors.deregister("html_block")
        md.inlinePatterns.deregister("html")


def build_markdown_text_context(text: str) -> dict:
    html = markdown.markdown(text, extensions=["tables", "fenced_code", EscapeHtmlExtension()])
    return {
        "html": mark_safe(html),
    }
