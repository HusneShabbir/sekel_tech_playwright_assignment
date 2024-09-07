def add_new_user(page, username):
    # Click on "Add" button to open the "Add User" form
    page.get_by_role("button", name=" Add").click()
    # Fill in the form to add a new user
    # Enter employee name
    page.get_by_role("textbox").nth(2).fill(username)
    # Select user role
    page.locator("form i").first.click()
    page.get_by_role("option", name="Admin").click()
    # Enter Employee Name
    page.get_by_placeholder("Type for hints...").fill("name")
    page.get_by_role("option", name="Qwerty Qwerty LName").click()
    # Select status
    page.locator("form i").nth(1).click()
    page.get_by_role("option", name="Enabled").click()
    # Enter password and confirm password
    page.locator("(//input[@type='password'])[1]").fill("Qwerty@123")
    page.locator("(//input[@type='password'])[2]").fill("Qwerty@123")
