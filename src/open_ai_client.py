import openai

from src import helper
from playwright.sync_api import Page
from src.constants.function_call import functions


class OpenAIClient:
    def __init__(self, api_key, model="gpt-4o"):
        self.model = model
        self.client = openai.OpenAI(api_key=api_key)

    def get_client(self) -> openai.OpenAI:
        return self.client

    def run_completion(self, page: Page, prompt: str):
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"""This is your task: {prompt}
                            * When creating CSS selectors, ensure they are unique and specific enough to select only one element, even if there are multiple elements of the same type (like multiple h1 elements).
                            * Avoid using generic tags like 'h1' alone. Instead, combine them with other attributes or structural relationships to form a unique selector.
                            * You must not derive data from the page if you are able to do so by using one of the provided functions, e.g. locator_evaluate.

                            Webpage snapshot:
                            
                            \\\\
                            {helper.get_snapshot(page)}
                            \\\\
                            """,
                    },
                ],
            }
        ]

        tools = [{"type": "function", "function": item} for item in functions]

        return self.client.chat.completions.create(
            model=self.model, messages=messages, tools=tools, stream=False
        )
