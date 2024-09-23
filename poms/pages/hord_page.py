import os

import allure
from dotenv import load_dotenv
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from base_element import BaseElement

load_dotenv(dotenv_path='.env')


class HordPage(BaseElement):
    side_bar_locator = (By.CSS_SELECTOR, "div.duf-aside-container")
    side_bar_toggle_locator = (By.XPATH, "(//div[@class='sidebar-toggle-wrapper'])[2]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step
    def is_side_bar_opened(self) -> bool:
        return self.wait.until(expected_conditions.visibility_of_element_located(self.side_bar_locator))

    @allure.step
    def is_side_bar_expanded(self) -> bool:
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.side_bar_locator))
        return "expanded" in element.get_attribute("class")

    @allure.step
    def scroll_dwon(self):
        down_locator = (By.TAG_NAME, "body")
        elem = self.wait.until(expected_conditions.visibility_of_element_located(down_locator))
        elem.send_keys(Keys.PAGE_DOWN)

    @allure.step
    def close_side_bar(self):
        element = self.wait.until(expected_conditions.visibility_of_element_located(self.side_bar_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.click(self.side_bar_toggle_locator)

    @allure.step
    def click_and_get_faq_messages(self, number):
        faq_locator = (By.XPATH, f"//div[@id='{number}']")
        try:
            element = self.wait.until(expected_conditions.element_to_be_clickable(faq_locator))
            element.click()
            return element.text
        except TimeoutException:
            print(f"Element with ID '{number}' not found or not clickable.")
            return ""

    @allure.step
    def get_all_faq_messages(self) -> list:
        faq = (By.XPATH, "//div[@class='d-flex gap-6 md-gap-0 md-flex-column']")
        element = self.wait.until(expected_conditions.element_to_be_clickable(faq))
        return element.text.split("\n")

    @allure.step
    def wait_for_sidebar_to_expand(self) -> None:
        self.wait.until(lambda driver: "expanded" in self.get_element_attribute(self.side_bar_locator, "class"))

    @allure.step
    def get_element_attribute(self, by_locator, attribute_name):
        try:
            element = self.wait.until(expected_conditions.visibility_of_element_located(by_locator))
            return element.get_attribute(attribute_name)
        except TimeoutException:
            return None
