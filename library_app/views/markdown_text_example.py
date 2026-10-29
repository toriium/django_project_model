from pathlib import Path

from django.shortcuts import render

from components.markdown_text import build_markdown_text_context


def markdown_text_example(request):
    text = (Path(__file__).parent / "markdown_text_example.md").read_text()

    context = {
        "markdown_text": build_markdown_text_context(text=text),
    }
    return render(request, "library_app/markdown_text_example.html", context)
