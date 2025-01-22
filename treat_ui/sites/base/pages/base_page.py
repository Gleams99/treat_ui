from strenum import LowercaseStrEnum
from enum import auto
from dataclasses import dataclass


class ByLocatorEnum(LowercaseStrEnum):
    ID = auto()
    XPATH = auto()


class BaseUIPage:
    LOCATORS = {}

    def __init__(self, *, site, page_url):
        self.page_url = page_url
        self.site = site
        self.locators = self.LOCATORS

    def goto_page(self):
        if self.page_url:
            self.site.driver.get(f"{self.site.site_url}/{self.page_url}")


@dataclass
class Locator:
    by: ByLocatorEnum
    identifier: str

    @property
    def element(self):
        return self.by, self.identifier
