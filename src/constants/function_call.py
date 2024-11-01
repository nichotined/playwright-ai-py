functions = [
    {
        "name": "get_locator",
        "description": "Get the locator for a specified element ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to fetch the locator for.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locate_element",
        "description": "Locates element using a CSS selector and returns elementId. This element ID can be used with other functions to perform actions on the element.",
        "parameters": {
            "type": "object",
            "properties": {
                "css_selector": {
                    "type": "string",
                    "description": "The CSS selector for the element to be located.",
                },
            },
            "required": ["css_selector"],
        },
    },
    {
        "name": "locator_evaluate",
        "description": "Execute JavaScript code in the page, taking the matching element as an argument.",
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
            "required": ["element_id", "page_function"],
        },
    },
    {
        "name": "locator_get_attribute",
        "description": "Returns the matching element's attribute value.",
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
            "required": ["element_id", "attribute_name"],
        },
    },
    {
        "name": "locator_inner_html",
        "description": "Returns the element.innerHTML.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to retrieve inner HTML from.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_inner_text",
        "description": "Returns the element.innerText.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to retrieve inner text from.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_text_content",
        "description": "Returns the node.textContent.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to retrieve text content from.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_input_value",
        "description": "Returns input.value for the selected <input> or <textarea> or <select> element.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to retrieve input value from.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_blur",
        "description": "Removes keyboard focus from the current element.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to remove focus from.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_bounding_box",
        "description": "Returns the bounding box of the element matching the locator, or null if not visible.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to get the bounding box for.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_check",
        "description": "Ensure that checkbox or radio element is checked.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the checkbox or radio element to check.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_uncheck",
        "description": "Ensure that checkbox or radio element is unchecked.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the checkbox or radio element to uncheck.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_is_checked",
        "description": "Returns whether the element is checked.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to check if it is checked.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_is_editable",
        "description": "Returns whether the element is editable.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to check if it is editable.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_is_enabled",
        "description": "Returns whether the element is enabled.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to check if it is enabled.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_is_visible",
        "description": "Returns whether the element is visible.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to check if it is visible.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_clear",
        "description": "Clear the input field.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the input field to clear.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_click",
        "description": "Click an element.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the element to click.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_count",
        "description": "Returns the number of elements matching the locator.",
        "parameters": {
            "type": "object",
            "properties": {
                "element_id": {
                    "type": "string",
                    "description": "The ID of the locator to count elements for.",
                },
            },
            "required": ["element_id"],
        },
    },
    {
        "name": "locator_fill",
        "description": "Set a value to the input field.",
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
            "required": ["element_id", "value"],
        },
    },
    {
        "name": "page_goto",
        "description": "Navigate to a specified URL.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The URL to navigate to.",
                },
            },
            "required": ["url"],
        },
    },
    {
        "name": "expect_to_be",
        "description": "Asserts that the actual value is equal to the expected value.",
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
            "required": ["actual", "expected"],
        },
    },
    {
        "name": "expect_not_to_be",
        "description": "Asserts that the actual value is not equal to the expected value.",
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
            "required": ["actual", "expected"],
        },
    },
    {
        "name": "result_assertion",
        "description": "Called when asserting something; returns the assertion result.",
        "parameters": {
            "type": "object",
            "properties": {
                "assertion": {
                    "type": "boolean",
                    "description": "The result of the assertion.",
                },
            },
            "required": ["assertion"],
        },
    },
    {
        "name": "result_query",
        "description": "Called to extract data; returns the extracted data.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The extracted data value.",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "result_action",
        "description": "Called to perform an action.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
    {
        "name": "result_error",
        "description": "Used to produce the final response if instructions cannot be completed.",
        "parameters": {
            "type": "object",
            "properties": {
                "error_message": {
                    "type": "string",
                    "description": "The error message to return.",
                },
            },
            "required": ["error_message"],
        },
    },
]
