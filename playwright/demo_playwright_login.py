""" Simple Playwright demo by Rob Marchetti
    It fills out a dummy Registration Form

"""

from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('http://the-internet.herokuapp.com/login')
        page.wait_for_timeout(2000)
        #  login
        page.fill('input[name="username"]', 'tomsmith')
        page.fill('input[name="password"]', 'SuperSecretPassword!')

        #class ="fa fa-2x fa-sign-in"
        # verify






if __name__ == '__main__':
    main()
