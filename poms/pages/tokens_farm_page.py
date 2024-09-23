from selenium.webdriver.chrome.webdriver import WebDriver

from gui_base.base_element import BaseElement

from selenium.webdriver.common.by import By


class TokenFarmPage(BaseElement):
    token_symbol_locator = (By.ID, "symbol")
    project_name_locator = (By.ID, "project_name")
    project_description_locator = (By.ID, "project_description")
    website_link_locator = (By.ID, "website_link")
    telegram_link_locator = (By.ID, "telegram_link")
    discord_link_locator = (By.ID, "discord_link")
    twitter_link_locator = (By.ID, "twitter_link")
    dark_mode_checkbox_locator = (By.ID, "dark_mode")
    # BY (ID ,XPATH,CSS_SELECTOR)
    select_placeholder_dropdown_locator = (By.ID, "react-select-2-placeholder")
    select_placeholder_dropdown_locator_Xpath = (By.XPATH, "//div[@id='react-select-2-placeholder']")
    select_placeholder_dropdown_locator_css_selector = (By.CSS_SELECTOR, "#react-select-2-placeholder")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
