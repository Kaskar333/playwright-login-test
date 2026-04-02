from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("file:///c:/Users/user/Desktop/cicd/index.html")

        page.fill("#email", "kaskar@gmail.com")
        page.fill("#password", "445566")
        page.click("#loginBtn")

        assert page.locator("h1").inner_text() == "Welcome Back"


        browser.close()