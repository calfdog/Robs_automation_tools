""" Simple Playwright demo by Rob Marchetti
    It fills out a dummy Registration Form

"""

from playwright.sync_api import sync_playwright
from misc_utils import name_gen


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://way2automation.com/way2auto_jquery/index.php')
        page.wait_for_timeout(2000)

        # Bring in the name
        name = name_gen.get_name().split(' ')

        # ---- Fill out Dummy Registration form ----
        # First Name
        page.wait_for_selector('input[name="name"]')
        page.fill('input[name="name"]', name[0] + " " + name[1])
        # phone
        page.fill('input[name="phone"]', '978-467-0098')
        # Email
        page.fill('input[name="email"]', name[1] + name[0] + '@gmail.com')
        # Country'
        page.select_option("//*[@id='load_form']/fieldset[4]/select", "United States")
        # City
        page.fill("//*[@id='load_form']/fieldset[5]/input", 'Tampa')
        # user Name
        page.fill("//*[@id='load_form']/fieldset[6]/input", value='TampaBay')
        # pass
        page.fill("//*[@id='load_form']/fieldset[7]/input", 'SecretPass')

        # Submit
        page.click("//div/div/form/div[1]/div[2]/input")

        page.wait_for_timeout(15000)


if __name__ == '__main__':
    main()
