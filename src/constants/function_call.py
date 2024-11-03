functions = [
    {
        "name": "locate_element_css",
        "description": "Locates element using a CSS selector and returns elementId. This element ID can be used with other functions to perform actions on the element.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "css_selector": {
                    "type": "string",
                    "description": "The CSS selector for the element to be located.",
                },
            },
            "additionalProperties": False,
            "required": ["css_selector"],
        },
    },
    {
        "name": "locate_element_xpath",
        "description": "Locates element using a XPath selector and returns elementId. This element ID can be used with other functions to perform actions on the element.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "xpath_selector": {
                    "type": "string",
                    "description": "The XPath selector for the element to be located.",
                },
            },
            "additionalProperties": False,
            "required": ["xpath_selector"],
        },
    },
    {
        "name": "locator_evaluate",
        "description": "Execute JavaScript code in the page, taking the matching element as an argument.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to evaluate the function on.",
                },
                "page_function": {
                    "type": "string",
                    "description": "Function to be evaluated in the page context, e.g. node => node.innerText",
                },
            },
            "additionalProperties": False,
            "required": ["element_id", "page_function"],
        },
    },
    {
        "name": "locator_get_attribute",
        "description": "Returns the matching element's attribute value.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to get the attribute from.",
                },
                "attribute_name": {
                    "type": "string",
                    "description": "The name of the attribute to retrieve.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id", "attribute_name"],
        },
    },
    {
        "name": "locator_inner_html",
        "description": "Returns the element.innerHTML.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to retrieve inner HTML from.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_inner_text",
        "description": "Returns the element.innerText.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to retrieve inner text from.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_text_content",
        "description": "Returns the node.textContent.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to retrieve text content from.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_input_value",
        "description": "Returns input.value for the selected <input> or <textarea> or <select> element.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to retrieve input value from.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_blur",
        "description": "Removes keyboard focus from the current element.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to remove focus from.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_bounding_box",
        "description": "Returns the bounding box of the element matching the locator, or null if not visible.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to get the bounding box for.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_check",
        "description": "Ensure that checkbox or radio element is checked.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the checkbox or radio element to check.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_uncheck",
        "description": "Ensure that checkbox or radio element is unchecked.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the checkbox or radio element to uncheck.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_is_checked",
        "description": "Returns whether the element is checked.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to check if it is checked.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_is_editable",
        "description": "Returns whether the element is editable.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to check if it is editable.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_is_enabled",
        "description": "Returns whether the element is enabled.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to check if it is enabled.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_is_visible",
        "description": "Returns whether the element is visible.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to check if it is visible.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_clear",
        "description": "Clear the input field.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the input field to clear.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_click",
        "description": "Click an element.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to click.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_count",
        "description": "Returns the number of elements matching the locator.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the locator to count elements for.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_fill",
        "description": "Set a value to the input field.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the input field to fill.",
                },
                "value": {
                    "type": "string",
                    "description": "The value to set in the input field.",
                },
            },
            "additionalProperties": False,
            "required": ["element_id", "value"],
        },
    },
    {
        "name": "page_goto",
        "description": "Navigate to a specified URL.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The URL to navigate to.",
                },
            },
            "additionalProperties": False,
            "required": ["url"],
        },
    },
    {
        "name": "expect_to_be",
        "description": "Asserts that the actual value is equal to the expected value.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "actual": {
                    "type": "string",
                    "description": "The actual value to check.",
                },
                "expected": {
                    "type": "string",
                    "description": "The expected value to compare against.",
                },
            },
            "additionalProperties": False,
            "required": ["actual", "expected"],
        },
    },
    {
        "name": "expect_not_to_be",
        "description": "Asserts that the actual value is not equal to the expected value.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "actual": {
                    "type": "string",
                    "description": "The actual value to check.",
                },
                "expected": {
                    "type": "string",
                    "description": "The expected value to compare against.",
                },
            },
            "additionalProperties": False,
            "required": ["actual", "expected"],
        },
    },
    {
        "name": "send_key",
        "description": "Called when needing to press a key on the keyboard.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "string",
                    "description": "The key to be pressed. Sample values: Enter, Escape, Delete, Tab, Home, etc.",
                },
            },
            "additionalProperties": False,
            "required": ["value"],
        },
    },
    {
        "name": "result_assertion",
        "description": "Called when asserting something; returns the assertion result.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "assertion": {
                    "type": "boolean",
                    "description": "The result of the assertion.",
                },
            },
            "additionalProperties": False,
            "required": ["assertion"],
        },
    },
    {
        "name": "result_query",
        "description": "Called to extract data; returns the extracted data.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The extracted data value.",
                },
            },
            "additionalProperties": False,
            "required": ["query"],
        },
    },
    {
        "name": "result_action",
        "description": "Called to perform an action.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
            "required": [],
        },
    },
    {
        "name": "result_error",
        "description": "Used to produce the final response if instructions cannot be completed.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "error_message": {
                    "type": "string",
                    "description": "The error message to return.",
                },
            },
            "additionalProperties": False,
            "required": ["error_message"],
        },
    },
]
