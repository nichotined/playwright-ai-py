from playwright.sync_api import Page

from html_sanitizer import Sanitizer


def sanitize_html(html: str):
    sanitizer = Sanitizer()
    return sanitizer.sanitize(html)


def get_snapshot(page: Page):
    return {
        "dom": sanitize_html(page.content()),
    }
