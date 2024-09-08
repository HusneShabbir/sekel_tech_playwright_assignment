import pytest
from playwright.sync_api import Page, expect
from pageobjects.userlogin import *
from pageobjects.add_new_user import *
from pageobjects.screenshot_on_failure import *


@pytest.mark.UI
@pytest.mark.all
def test_add_new_user(page: Page) -> None:
    userlogin(page, 'Admin', 'admin123')
    # Navigate to the User Management page
    page.get_by_role("link", name="Admin").click()
    count_locator = page.locator("(//span[@class='oxd-text oxd-text--span'])[1]")
    initial_no_of_records = count_locator.inner_text()

    add_new_user(page, 'Bhuvaneshwar')

    already_exists = page.get_by_text("Already exists").is_visible(timeout=1000)
    if already_exists:
        screenshot_on_failure(page, 'username_already_exists')
        print('Please Enter a Non-existing Username')
    else:
        screenshot_on_failure(page, 'added_new_user')
        # Click the "Save" button
        page.get_by_role("button", name="Save").click()
        final_no_of_records = count_locator.inner_text()
        if final_no_of_records > initial_no_of_records:
            # Verify the new user has been added
            assert (final_no_of_records > initial_no_of_records)
            print("you have successfully created a new user")
        else:
            # Negative scenario
            print('Something went Wrong!! please try again')
