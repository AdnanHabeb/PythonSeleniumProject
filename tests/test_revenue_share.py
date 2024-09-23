import os
import pytest

from revenue_share import RevenueShare


class TestRevenueShare:
    os.environ["WEB_URL"] = os.environ["REVENUE_SHARE"]

    @pytest.fixture(autouse=True)
    def open_revenue_page(self, open_browser):
        pass

    def test_wallet_popup(self, open_browser):
        driver = open_browser
        rev_share = RevenueShare(driver)
        rev_share.click_on_connect_button()
        assert rev_share.is_pop_up_displayed(), 'popup is not opened '
        items = rev_share.is_all_items_displayed()
        expected_items = ['MetaMask', 'Coinbase', 'WalletConnect', 'Trust', 'Rainbow', "Don't see your wallet?",
                          'Try search instead']
        boolean_flag_list = [item for item in items if item in expected_items]
        assert False not in boolean_flag_list, 'expected all the items should be visible'
