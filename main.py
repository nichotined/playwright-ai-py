from src.open_ai_client import OpenAIClient
from playwright.sync_api import sync_playwright

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://playwright.dev")

        client = OpenAIClient(
            api_key="sk-proj-###",
            model="gpt-4o",
        )
        print(client.run_completion(page=page, prompt="get the header text"))

        # Sample output:
        # ChatCompletion(id='chatcmpl-AOp2W7E2u9DX70Zgsyatz88Zh1Osv',
        # choices=[Choice(finish_reason='tool_calls',
        # index=0,
        # logprobs=None,
        # message=ChatCompletionMessage(content=None, refusal=None, role='assistant',
        # audio=None, function_call=None,
        # tool_calls=[ChatCompletionMessageToolCall(id='call_vxy2ldSZYWJWTTAVp3kw9AaT',
        # function=Function(arguments='{"css_selector":"h1"}',
        # name='locate_element'),
        # type='function')]))],
        # created=1730479432, model='gpt-4o-2024-08-06',
        # object='chat.completion',
        # service_tier=None,
        # system_fingerprint='fp_159d8341cc',
        # usage=CompletionUsage(completion_tokens=17, prompt_tokens=2900, total_tokens=2917,
        # completion_tokens_details=CompletionTokensDetails(audio_tokens=None, reasoning_tokens=0),
        # prompt_tokens_details=PromptTokensDetails(audio_tokens=None, cached_tokens=0)))

        browser.close()
