def userlogin(page, username, password):
    # Step 1: Navigate to the login page
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Step 2: Enter a valid username and password
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    # Step 3: Click on the "Login" button
    page.get_by_role("button", name="Login").click()
