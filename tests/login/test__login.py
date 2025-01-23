import time
import pytest
from treat_ui.sites.sweetshop import SweetShopSite


pytestmark = [pytest.mark.ui, pytest.mark.login]


def test__login(driver):
    """
    Attempt to login to SweetShop site then browse sweets and view the basket.

    Steps:
    1. Attempt to Login to Sweetshop site
    2. Go to Sweets page
    3. Go to Basket page
    """
    sweet_shop = SweetShopSite(driver=driver)
    sweet_shop.login_as(email="Dean Winchester", password="Pie")
    time.sleep(1)
    sweet_shop.browse_sweet()
    time.sleep(1)
    sweet_shop.view_basket()
    time.sleep(1)
