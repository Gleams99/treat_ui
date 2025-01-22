from treat_ui.sites.base.pages import BaseUIPage


class AboutPage(BaseUIPage):
    def __init__(self, *, site):
        page_url = "about"
        super().__init__(site=site, page_url=page_url)
