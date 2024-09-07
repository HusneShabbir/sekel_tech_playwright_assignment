from playwright.sync_api import Page, expect
from pageobjects.userlogin import *
from pageobjects.user_management_search import *


def test_user_management_search(page: Page) -> None:
    userlogin(page, 'Admin', 'admin123')
    # Enter valid user name
    user = 'Bhuvaneshwar'
    userManagementSearch(page, user)
    # Verify that search results are displayed and contain the search keyword
    name_loc = page.get_by_text(user)
    expect(name_loc).to_be_visible()
    expect(name_loc).to_have_text(user)
    # print statement
    print(f"Search results are displayed and contain the search keyword :: {user}")

