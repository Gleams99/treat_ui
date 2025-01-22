from treat_ui.sites.base.pages import BaseUIPage


class BasketPage(BaseUIPage):
    def __init__(self, *, site):
        page_url = "basket"
        super().__init__(site=site, page_url=page_url)
