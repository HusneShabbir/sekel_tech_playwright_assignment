from playwright.sync_api import Page, expect
from pageobjects.userlogin import *
from pageobjects.add_new_user import *


def test_example(page: Page) -> None:
    userlogin(page, 'Admin', 'admin123')
    # Navigate to the User Management page
    page.get_by_role("link", name="Admin").click()
    count_locator = page.locator("(//span[@class='oxd-text oxd-text--span'])[1]")
    initial_no_of_records = count_locator.inner_text()

    add_new_user(page, 'Bhuvaneshwar')

    already_exists = page.get_by_text("Already exists").is_visible(timeout=1000)
    if already_exists:
        print('Please Enter a Non-existing Username')
    else:
        # Click the "Save" button
        page.get_by_role("button", name="Save").click()
        # Verify the new user has been added
        final_no_of_records = count_locator.inner_text()
        if final_no_of_records > initial_no_of_records:
            print("you have successfully created a new user")
        else:
            print('Something went Wrong!! please try again')