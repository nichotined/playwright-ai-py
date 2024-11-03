import json
import pprint
import openai

from openai.types.chat import ChatCompletion
from src import action, helper
from playwright.sync_api import Page
from src.constants.function_call import functions


class OpenAIClient:
    def __init__(self, api_key, model="gpt-4o"):
        self.model = model
        self.client = openai.OpenAI(api_key=api_key)

    def get_client(self) -> openai.OpenAI:
        return self.client

    def run_completion(self, page: Page, prompt: str) -> ChatCompletion:
        pw = action.LocatorActions(page)

        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"""This is your task: {prompt}
                            * You have capabilities to locate elements using CSS selectors and XPath selectors. Ensure they are unique and specific enough to select only one element, even if there are multiple elements of the same type (like multiple h1 elements).
                            * You must use XPath when the need is to use text content or inner text.
                            * Avoid using generic tags like 'h1' alone. Instead, combine them with other attributes or structural relationships to form a unique selector.
                            * You must not derive data from the page if you are able to do so by using one of the provided functions, e.g. locator_evaluate.

                            Webpage snapshot:
                            
                            \\\\\\
                            {helper.get_snapshot(page)}
                            \\\\\\
                            """,
                    },
                ],
            }
        ]
        temperature = 0
        top_p = 0

        tools = [{"type": "function", "function": item} for item in functions]

        opr = self.client.beta.chat.completions.parse(
            model=self.model,
            messages=messages,
            tools=tools,
            tool_choice="auto",
            temperature=temperature,
            top_p=top_p,
        )
        print(opr.usage)

        while opr.choices[0].finish_reason == "tool_calls":
            print("##### TOOL CALLS #####")

            messages.append(opr.choices[0].message.to_dict())
            # print("##### AFTER #####")
            # pprint.pp(messages)

            for tool in opr.choices[0].message.tool_calls:
                execute_tool_result = self.execute_tool(
                    pw, tool.function.name, tool.function.parsed_arguments
                )
                pprint(execute_tool_result)
                messages.append(
                    {
                        "tool_call_id": tool.id,
                        "role": "tool",
                        "content": json.dumps(execute_tool_result),
                    }
                )
            opr = self.client.beta.chat.completions.parse(
                model=self.model,
                messages=messages,
                tools=tools,
                tool_choice="auto",
                temperature=temperature,
                top_p=top_p,
            )
            print(opr.usage)
            print("##### DONE #####")

        pprint.pp(messages)
        return opr

    def execute_tool(self, action: action.LocatorActions, tool_name, parsed_arguments):
        print(f"{tool_name} : {parsed_arguments}")
        match tool_name:
            case "locate_element_css":
                return action.locate_element_css(parsed_arguments["css_selector"])
            case "locate_element_xpath":
                return action.locate_element_xpath(parsed_arguments["xpath_selector"])
            case "locator_count":
                return action.locator_count(parsed_arguments["element_id"])
            case "locator_click":
                return action.locator_click(parsed_arguments["element_id"])
            case "locator_is_visible":
                return action.locator_is_visible(parsed_arguments["element_id"])
            case "locator_is_editable":
                return action.locator_is_editable(parsed_arguments["element_id"])
            case "locator_is_enabled":
                return action.locator_is_enabled(parsed_arguments["element_id"])
            case "locator_is_checked":
                return action.locator_is_checked(parsed_arguments["element_id"])
            case "locator_get_attribute":
                return action.locator_get_attribute(
                    parsed_arguments["element_id"], parsed_arguments["attribute_name"]
                )
            case "locator_inner_html":
                return action.locator_inner_html(parsed_arguments["element_id"])
            case "locator_inner_text":
                return action.locator_inner_text(parsed_arguments["element_id"])
            case "locator_text_content":
                return action.locator_text_content(parsed_arguments["element_id"])
            case "locator_input_value":
                return action.locator_input_value(parsed_arguments["element_id"])
            case "locator_blur":
                return action.locator_blur(parsed_arguments["element_id"])
            case "locator_bounding_box":
                return action.locator_bounding_box(parsed_arguments["element_id"])
            case "locator_check":
                return action.locator_check(parsed_arguments["element_id"])
            case "locator_uncheck":
                return action.locator_uncheck(parsed_arguments["element_id"])
            case "locator_clear":
                return action.locator_clear(parsed_arguments["element_id"])
            case "locator_fill":
                return action.locator_fill(
                    parsed_arguments["element_id"], parsed_arguments["value"]
                )
            case "page_goto":
                return action.page_goto(parsed_arguments["url"])
            case "expect_to_be":
                return action.expect_to_be(
                    parsed_arguments["actual"], parsed_arguments["expected"]
                )
            case "expect_not_to_be":
                return action.expect_not_to_be(
                    parsed_arguments["actual"], parsed_arguments["expected"]
                )
            case "send_key":
                return action.send_key(parsed_arguments["value"])
            case "result_assertion":
                return action.result_assertion(parsed_arguments["assertion"])
            case "result_query":
                return action.result_query(parsed_arguments["query"])
            case "result_action":
                return action.result_action()
            case "result_error":
                return action.result_error(parsed_arguments["error_message"])
            case _:
                raise NotImplementedError(f"Not Implemented tool: {tool_name}")
