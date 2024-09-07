def userManagementSearch(page, name):
    # Validating that the user details page can be opened from the search results
    page.get_by_placeholder("Search").fill("Admin")
    page.get_by_role("link", name="Admin").click()
    # Enter search keyword and click search
    page.get_by_role("textbox").nth(1).fill(name)
    page.get_by_role("button", name="Search").click()
