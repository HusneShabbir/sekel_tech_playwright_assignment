# Add screenshot to allure report if the test failed
import allure


def screenshot_on_failure(page, use):
    screenshot_path = f"screenshots/{use}.png"
    page.screenshot(path=screenshot_path)
    allure.attach.file(screenshot_path, name=f"Screenshot_{use}", attachment_type=allure.attachment_type.PNG)

