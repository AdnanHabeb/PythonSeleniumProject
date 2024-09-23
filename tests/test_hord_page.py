import os

import allure
import pytest

from hord_page import HordPage
from tests.conftest import open_browser


class TestHordPage:
    os.environ["WEB_URL"] = os.environ["HORD_URL"]

    @pytest.fixture(autouse=True)
    def open_hord_page(self, open_browser):
        pass

    @allure.title("test_sidebar_state -Test Hord Page-")
    def test_sidebar_state(self, open_browser):
        # This test Perform :->
        # validate if sidebar is opened
        # validate is sidebar attribute is expanded
        # close the sidebar
        # validate sidebar collapse
        # scroll down to EOP
        # open all the FAQ
        # getting the message and validate that the message is not None
        driver = open_browser
        hord_page = HordPage(driver)
        assert hord_page.is_side_bar_opened(), "Sidebar should be opened."
        assert hord_page.is_side_bar_expanded(), "Sidebar should be expanded."
        hord_page.close_side_bar()
        assert hord_page.is_side_bar_expanded() is False, 'should be collapsing'
        hord_page.scroll_dwon()
        faq_messages = [hord_page.click_and_get_faq_messages(num) for num in range(10)]
        for mess in faq_messages:
            assert mess is not None, 'message is not displayed'
