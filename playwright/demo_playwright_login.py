""" Simple Playwright demo by Rob Marchetti
    It fills in login and click login button then validates
    secure page

"""

from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        # Navigate to login page
        page.goto('http://the-internet.herokuapp.com/login')
        #  login
        # Enter username
        page.fill('input[id="username"]', 'tomsmith')
        # Enter password
        page.fill('input[id="password"]', 'SuperSecretPassword!')
        # Click login button
        page.locator("button").click()

        # TO DO: Validate Text on next page - http://the-internet.herokuapp.com/secure


if __name__ == '__main__':
    main()
