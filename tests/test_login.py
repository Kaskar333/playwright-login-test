from playwright.sync_api import sync_playwright, expect

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://login-form-theta-five.vercel.app/")

        page.fill("#email", "kaskar@gmail.com")
        page.fill("#password", "445566")
        page.click("#loginBtn")

        welcome = page.locator("h1").inner_text()
        if welcome == "Welcome Back":
            print("Login test passed")
        else:
            print("Login test failed")

        browser.close()

def test_login_fail():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://login-form-theta-five.vercel.app/")

        page.fill("#email", "kaskar23@gmail.com")
        page.fill("#password", "445566")
        page.click("#loginBtn")

        errorMsg = page.locator("div#passErr").inner_text()
        if errorMsg == "Incorrect password. Please try again.":
            print("Login test passed")
        else:
            print("Login test failed")


        browser.close()
