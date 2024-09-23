import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base_element import BaseElement


class RevenueShare(BaseElement):
    connect_button = (By.XPATH, "//button[contains(@class,'connect-button')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step
    def is_pop_up_displayed(self):
        """
            verify that popup is opened
        """
        shadow_host = self.driver.find_element(By.CSS_SELECTOR, ".dynamic-shadow-dom")
        shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", shadow_host)
        shadow_element = shadow_root.find_element(By.CSS_SELECTOR, ".wallet-list__search-container")
        return shadow_element.is_displayed()

    @allure.step
    def is_all_items_displayed(self):
        """
            after opening the popup
            we get into the shadow root
            then returned all the items by text
        """
        shadow_host = self.driver.find_element(By.CSS_SELECTOR, ".dynamic-shadow-dom")
        shadow_root = self.driver.execute_script("return arguments[0].shadowRoot", shadow_host)
        item = shadow_root.find_element(By.CSS_SELECTOR, ".wallet-list__container")
        return item.text.split("\n")

    @allure.step
    def click_on_connect_button(self):
        """
            wait for the button to displayed and then click on it
        """
        self.wait_for_visibility(self.connect_button)
        self.click(self.connect_button)
