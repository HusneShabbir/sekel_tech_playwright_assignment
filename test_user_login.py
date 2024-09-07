from playwright.sync_api import Page, expect
from pageobjects.userlogin import *


def test_user_login(page: Page) -> None:
    userlogin(page, 'Admin', 'admin123')
    invalid_creds = page.get_by_text("Invalid credentials")
    # locator of user-specific element
    dashboard_loc = page.get_by_role("heading", name="Dashboard")
    # Ensure the page is loaded
    page.wait_for_load_state('networkidle')
    # Negative scenario
    if invalid_creds.is_visible():
        print("Please re-check your credentials and Try again.")
    else:
        # Step 4: Verify successful login by checking the presence of a user-specific element
        expect(dashboard_loc).to_be_visible()
        expect(dashboard_loc).to_have_text("Dashboard")
        print("You have successfully Logged-in")

