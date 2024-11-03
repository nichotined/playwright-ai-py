from src.open_ai_client import OpenAIClient
from playwright.sync_api import sync_playwright

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=200,
        )
        page = browser.new_page(
            viewport={"width": 1366, "height": 720},
        )
        page.goto("https://youtube.com/")

        client = OpenAIClient(
            api_key="sk-proj-",
            model="gpt-4o-mini",
        )
        client.run_completion(
            page=page, prompt="On the search bar, search for 'DOTA 2'"
        )
        client.run_completion(
            page=page, prompt="Click on search icon"
        )
        client.run_completion(page=page, prompt="Click on the first result")
        client.run_completion(page=page, prompt="Get the title of the video")

        browser.close()
