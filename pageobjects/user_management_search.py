def userManagementSearch(page, name):
    page.get_by_placeholder("Search").fill("Admin")
    page.get_by_role("link", name="Admin").click()
    page.get_by_role("textbox").nth(1).fill(name)
    page.get_by_role("button", name="Search").click()
