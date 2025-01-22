from treat_ui.sites.base import BaseUISite
from treat_ui.sites.sweetshop.pages import AboutPage, BasketPage, LoginPage, SweetsPage


class SweetShopSite(BaseUISite):
    """Sweet Shop Site"""
    def __init__(self, *, driver):
        site_url = 'https://sweetshop.netlify.app/'
        super().__init__(driver=driver, site_url=site_url)

        self.about_page = AboutPage(site=self)
        self.basket_page = BasketPage(site=self)
        self.login_page = LoginPage(site=self)
        self.sweets_page = SweetsPage(site=self)

    # ----------------------------------------------
    #   Higher level business functions for better readability
    # ----------------------------------------------
    def login_as(self, *, email: str, password: str):
        self.login_page.goto_page()
        self.login_page.attempt_login(email=email, password=password)
        assert False

    def view_basket(self):
        self.basket_page.goto_page()

    def browse_sweet(self):
        self.sweets_page.goto_page()
