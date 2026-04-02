from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://login-form-theta-five.vercel.app/")

        page.fill("#email", "kaskar@gmail.com")
        page.fill("#password", "123123")
        page.click("#loginBtn")

        successText = page.locator("h1")
        if successText.inner_text() == "Welcome Back":
            print("Login test passed")
        else:
            print("Login test failed")


        browser.close()
