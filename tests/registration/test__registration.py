import time
from treat_ui.sites.sweetshop import SweetShopSite


def test_login(driver):
    sweet_shop = SweetShopSite(driver=driver)
    sweet_shop.login_as(email="Dean Winchester", password="Pie")
    time.sleep(10)
    sweet_shop.browse_sweet()
    time.sleep(10)
    sweet_shop.view_basket()
    time.sleep(10)
