from playwright.sync_api import Page, expect
from pageobjects.userlogin import *


def test_user_login(page: Page) -> None:
    userlogin(page, 'Admin', 'admin123')
    invalid_creds = page.get_by_text("Invalid credentials")
    dashboard_loc = page.get_by_role("heading", name="Dashboard")
    page.wait_for_load_state('networkidle')
    if invalid_creds.is_visible():
        print("Please re-check your credentials and Try again.")
    else:
        expect(dashboard_loc).to_be_visible()
        expect(dashboard_loc).to_have_text("Dashboard")
        print("You have successfully Logged-in")

