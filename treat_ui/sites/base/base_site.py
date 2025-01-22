

class BaseUISite:
    def __init__(self, *, driver, site_url):
        self.driver = driver
        self.site_url = site_url

    # locators
