from selenium.webdriver.common.by import By

from pages.base_page import BasePage

import time


class LoginPage(BasePage):
    LOGIN_PAGE_URL = "https://flip.ro/autentifica-te/"
    EMAIL_INPUT = (By.ID, "login-email")
    PASSWORD_INPUT = (By.ID, "login-password")
    LOGIN_BUTTON = (By.XPATH,
                    "/html/body/div[1]/div/section/section/section/section/div/div/div/div/div/div/div[2]/div[1]/form/fieldset[2]/div/button/span")
    ERROR_LOGIN_MESSAGE = (By.XPATH, "/html/body/div[2]/div")
    ACCEPT_COOKIE = (By.XPATH, "/html/body/div[3]/div[1]/div/div/div/div/button[1]/span")

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)
        self.driver.maximize_window()

    def accept_cookie(self):
        self.click(self.ACCEPT_COOKIE)

    def set_username(self, email):
        self.type(self.EMAIL_INPUT, email)

    def set_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def is_main_error_message_displayed(self):
        return self.is_element_displayed(self.ERROR_LOGIN_MESSAGE)

    def get_error_message_text(self):
        return self.get_text(self.ERROR_LOGIN_MESSAGE)
