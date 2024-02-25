from selenium.webdriver.common.by import By

from pages.base_page import BasePage

import time


class LoginPage(BasePage):
    LOGIN_PAGE_URL = "https://flip.ro/autentifica-te/"
    EMAIL_INPUT = (By.ID, "login-email")
    PASSWORD_INPUT = (By.ID, "login-password")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='w-100 reactangle large-btn primary']")
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

    def is_main_error_message_displayed(self, expected_error_message):
        try:
           error_message_text = self.driver.find_element(*self.ERROR_LOGIN_MESSAGE).text.replace("ș", "s").replace("ă", "a")
        except:
            pass
        assert self.is_element_displayed(self.ERROR_LOGIN_MESSAGE) == True

        assert expected_error_message == error_message_text, f"expected message {expected_error_message}, actual error message {error_message_text}"

    def get_error_message_text(self):
        return self.get_text(self.ERROR_LOGIN_MESSAGE)