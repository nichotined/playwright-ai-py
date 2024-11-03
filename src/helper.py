import lxml_html_clean
from playwright.sync_api import Page
from html_sanitizer import Sanitizer


def sanitize_html(html: str):
    sanitizer = Sanitizer()
    return sanitizer.sanitize(html)


def clean_html(html: str):
    return lxml_html_clean.Cleaner(
        page_structure=False,
        scripts=True,
        style=True,
        javascript=True,
        inline_style=True,
        comments=True,
        forms=False,
        meta=True,
        safe_attrs=["id", "type", "role", "name", "value", "title"],
        remove_unknown_tags=False,
        remove_tags=["img", "svg", "yt-icon", "iron-iconset-svg"],
    ).clean_html(html)


def get_snapshot(page: Page):
    page.wait_for_load_state(state="load")
    page_content = page.content()
    html = clean_html(page_content)
    print(html)
    return {
        "dom": html,
    }
