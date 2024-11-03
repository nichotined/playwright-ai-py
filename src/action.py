import uuid
from playwright.sync_api import Page


class LocatorActions:
    def __init__(self, page: Page):
        self.page = page
        self.locator_map = {}

    def get_locator(self, element_id: str):
        locator = self.locator_map.get(element_id)
        if locator is None:
            raise ValueError(f'Unknown elementId "{element_id}"')
        return locator

    def locate_element_css(self, css_selector: str):
        """Locates an element using a CSS selector and returns elementId."""
        locator = self.page.locator(css_selector).first
        element_id = str(uuid.uuid4())
        self.locator_map[element_id] = locator
        return {"elementId": element_id}

    def locate_element_xpath(self, xpath_selector: str):
        """Locates an element using a XPath selector and returns elementId."""
        locator = self.page.locator(f"xpath={xpath_selector}").first
        element_id = str(uuid.uuid4())
        self.locator_map[element_id] = locator
        return {"elementId": element_id}

    def locator_evaluate(self, element_id: str, page_function: str):
        """Execute JavaScript code in the page, taking the matching element as an argument."""
        return {"result": self.get_locator(element_id).evaluate(page_function)}

    def locator_get_attribute(self, element_id: str, attribute_name: str):
        """Returns the matching element's attribute value."""
        return {
            "attributeValue": self.get_locator(element_id).get_attribute(attribute_name)
        }

    def locator_inner_html(self, element_id: str):
        """Returns the element.innerHTML."""
        return {"innerHTML": self.get_locator(element_id).inner_html()}

    def locator_inner_text(self, element_id: str):
        """Returns the element.innerText."""
        return {"innerText": self.get_locator(element_id).inner_text()}

    def locator_text_content(self, element_id: str):
        """Returns the node.textContent."""
        return {"textContent": self.get_locator(element_id).text_content()}

    def locator_input_value(self, element_id: str):
        """Returns input.value for the selected <input> or <textarea> or <select> element."""
        return {"inputValue": self.get_locator(element_id).input_value()}

    def locator_blur(self, element_id: str):
        """Removes keyboard focus from the current element."""
        self.get_locator(element_id).blur()
        return {"success": True}

    def locator_bounding_box(self, element_id: str):
        """Returns the bounding box of the element matching the locator, or null if not visible."""
        return self.get_locator(element_id).bounding_box()

    def locator_check(self, element_id: str):
        """Ensure that checkbox or radio element is checked."""
        self.get_locator(element_id).check()
        return {"success": True}

    def locator_uncheck(self, element_id: str):
        """Ensure that checkbox or radio element is unchecked."""
        self.get_locator(element_id).uncheck()
        return {"success": True}

    def locator_is_checked(self, element_id: str):
        """Returns whether the element is checked."""
        return {"isChecked": self.get_locator(element_id).is_checked()}

    def locator_is_editable(self, element_id: str):
        """Returns whether the element is editable."""
        return {"isEditable": self.get_locator(element_id).is_editable()}

    def locator_is_enabled(self, element_id: str):
        """Returns whether the element is enabled."""
        return {"isEnabled": self.get_locator(element_id).is_enabled()}

    def locator_is_visible(self, element_id: str):
        """Returns whether the element is visible."""
        return {"isVisible": self.get_locator(element_id).is_visible()}

    def locator_clear(self, element_id: str):
        """Clear the input field."""
        self.get_locator(element_id).clear()
        return {"success": True}

    def locator_click(self, element_id: str):
        """Click an element."""
        self.get_locator(element_id).click()
        return {"success": True}

    def locator_count(self, element_id: str):
        """Returns the number of elements matching the locator."""
        return {"elementCount": self.get_locator(element_id).count()}

    def locator_fill(self, element_id: str, value: str):
        """Set a value to the input field."""
        self.get_locator(element_id).fill(value)
        return {"success": True}

    def send_key(self, value: str):
        """Send key to the input field."""
        self.page.keyboard.press(value)

    def page_goto(self, url: str):
        """Navigate to a specified URL."""
        return {"url": self.page.goto(url)}

    def expect_to_be(self, actual: str, expected: str):
        """Asserts that the actual value is equal to the expected value."""
        return {"actual": actual, "expected": expected, "success": actual == expected}

    def expect_not_to_be(self, actual: str, expected: str):
        """Asserts that the actual value is not equal to the expected value."""
        return {"actual": actual, "expected": expected, "success": actual != expected}

    def result_assertion(self, assertion: bool):
        """Called when asserting something; returns the assertion result."""
        return {"assertion": assertion}

    def result_query(self, query: str):
        """Called to extract data; returns the extracted data."""
        return {"query": query}

    def result_action(self):
        """Called to perform an action."""
        return None

    def result_error(self, error_message: str):
        """Used to produce the final response if instructions cannot be completed."""
        return {"errorMessage": error_message}
