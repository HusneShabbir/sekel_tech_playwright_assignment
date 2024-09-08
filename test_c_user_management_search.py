import pytest
from playwright.sync_api import Page, expect
from pageobjects.userlogin import *
from pageobjects.user_management_search import *
from pageobjects.screenshot_on_failure import *


@pytest.mark.UI
@pytest.mark.all
def test_user_management_search(page: Page) -> None:
    userlogin(page, 'Admin', 'admin123')
    # Enter valid user name
    user = 'Bhuvaneshwar'
    userManagementSearch(page, user)
    screenshot_on_failure(page, 'search_results')
    # Verify that search results are displayed and contain the search keyword
    name_loc = page.get_by_text(user)
    test_condition = name_loc.is_visible()
    if test_condition:
        # Verify that the user search results contain the search keyword.
        expect(name_loc).to_have_text(user)
        # print statement
        print(f"Search results are displayed and contain the search keyword :: {user}")
    else:
        # Negative scenario
        print(f"Search results are displayed and Does not contain the search keyword :: {user}")