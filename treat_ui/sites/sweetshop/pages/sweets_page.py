from treat_ui.sites.base.pages import BaseUIPage


class SweetsPage(BaseUIPage):
    def __init__(self, *, site):
        page_url = "sweets"
        super().__init__(site=site, page_url=page_url)
