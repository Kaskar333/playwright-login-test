from playwright.sync_api import sync_playwright, expect

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://login-form-theta-five.vercel.app/")

        page.fill("#email", "kaskar@gmail.com")
        page.fill("#password", "445566")
        page.click("#loginBtn")

        expect(page.locator("h1")).to_have_text("Welcome Back")

        browser.close()

def test_login_fail():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://login-form-theta-five.vercel.app/")

        page.fill("#email", "kaskar23@gmail.com")
        page.fill("#password", "445566")
        page.click("#loginBtn")

        expect(page.locator("div#passErr")).to_have_text("Incorrect password. Please try again.")


        browser.close()
