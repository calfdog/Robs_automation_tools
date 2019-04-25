""" This Python file contains the classes for the main_page Locators
    and for the main_page methods to control the locator objects

    Scripted by: Rob Marchetti
    Date: July 3, 2018
    Version: 1.0
    Updated by:
    Update date:
"""

from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """ Locators mapped to Main page """
    NAME_TXBX       = (By.NAME, 'name')
    PHONE_TXBX      = (By.NAME, 'phone')
    EMAIL_TXBX      = (By.NAME, 'email')
    DEALERSHIP_TXBX = (By.NAME, 'dealership')
    HOW_TXBX        = (By.NAME, 'dealership')
    SUBMIT_BTN      = (By.CSS_SELECTOR, 'button.btn')


class MainPage(object):
    """ Main Page methods"""

    # initialize driver
    def __init__(self, driver):
        self.driver = driver

    def login(self, sName=None,sPhone=None, sEmail=None, sDealership=None, sHow=None):
        self.set_name(sName)
        self.set_phone_txbx(sPhone)
        self.set_email_txbx(sEmail)
        self.set_dealership_txbx(sDealership)
        self.set_how_txbx(sHow)
        self.click_submit_btn()

    def set_name(self, sName):
        name_txbx = self.driver.find_element(*MainPageLocators.NAME_TXBX)
        name_txbx.send_keys(sName)

    def set_phone_txbx(self, sPhone):
        phone_txbx = self.driver.find_element(*MainPageLocators.PHONE_TXBX)
        phone_txbx.send_keys(sPhone)

    def set_email_txbx(self, sEmail):
        email_txbx = self.driver.find_element(*MainPageLocators.EMAIL_TXBX)
        email_txbx.send_keys(sEmail)

    def set_dealership_txbx(self, sDealership):
        dealership_txbx = self.driver.find_element(*MainPageLocators.DEALERSHIP_TXBX)
        dealership_txbx.send_keys(sDealership)

    def set_how_txbx(self, sHow):
        how_txbx = self.driver.find_element(*MainPageLocators.HOW_TXBX)
        how_txbx.send_keys(sHow)

    def click_submit_btn(self):
        submit_btn = self.driver.find_element(*MainPageLocators.SUBMIT_BTN)
        submit_btn.click()
