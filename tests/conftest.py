import os

import pytest
from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

load_dotenv(find_dotenv())


@pytest.fixture
def open_browser():
    options = ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    web_url = os.environ.get('WEB_URL')
    if web_url is None:
        raise ValueError("The environment variable 'WEB_URL' is not set.")
    driver.get(web_url)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()
