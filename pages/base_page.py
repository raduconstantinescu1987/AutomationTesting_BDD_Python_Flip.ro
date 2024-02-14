from selenium.webdriver.common.by import By

from driver import Browser


class BasePage(Browser):
    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        return self.find(locator).click()

    def type(self, locator, text):
        return self.find(locator).send_keys(text)

    def is_element_displayed(self, locator):
        return self.find(locator).is_displayed()

    def get_text(self, locator):
        return self.find(locator).text




