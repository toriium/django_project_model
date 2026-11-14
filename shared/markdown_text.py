from django.utils.safestring import mark_safe
from django.utils.text import slugify
from markdown_it import MarkdownIt
from markdown_it.token import Token

# Raw HTML inside the markdown is rendered as text instead of being passed through, to avoid XSS
md = MarkdownIt("commonmark", {"html": False}).enable(["table", "strikethrough"])

# Heading levels that get an entry in the table of contents (h5/h6 are left out)
TOC_LEVELS = {"h1", "h2", "h3", "h4"}


def build_toc(tokens: list[Token]) -> list[dict]:
    """Gives every heading a unique id (so it can be linked to) and returns the table of contents.

    Changes the heading tokens in place.
    toc entries: {"id": "infos", "title": "Infos", "level": 2}
    """
    toc = []
    used_ids: dict[str, int] = {}

    for i, token in enumerate(tokens):
        if token.type != "heading_open":
            continue
        # The heading text lives in the inline token right after heading_open
        # Only keep the plain text, so "**Bold** `code`" becomes "Bold code"
        inline = tokens[i + 1]
        title = "".join(
            child.content for child in inline.children or [] if child.type in ("text", "code_inline")
        ).strip() or inline.content
        base_id = slugify(title) or "section"
        count = used_ids.get(base_id, 0)
        used_ids[base_id] = count + 1
        heading_id = base_id if count == 0 else f"{base_id}-{count}"
        token.attrSet("id", heading_id)

        if token.tag in TOC_LEVELS:
            toc.append({"id": heading_id, "title": title, "level": int(token.tag[1])})

    return toc


def build_markdown_text_context(text: str) -> dict:
    tokens = md.parse(text)
    toc = build_toc(tokens)
    return {
        "html": mark_safe(md.renderer.render(tokens, md.options, {})),
        "toc": toc,
    }
