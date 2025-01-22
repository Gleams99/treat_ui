from treat_ui.sites.base.pages import BaseUIPage, Locator, ByLocatorEnum


class LoginPage(BaseUIPage):
    LOCATORS = {
        "email_field": Locator(identifier="exampleInputEmail", by=ByLocatorEnum.ID),
        "password_field": Locator(identifier="exampleInputPassword", by=ByLocatorEnum.ID),
        "login_btn": Locator(identifier="//button[contains(text(), 'Login')]", by=ByLocatorEnum.XPATH),
    }

    def __init__(self, *, site):
        page_url = "login"
        super().__init__(site=site, page_url=page_url)

    def attempt_login(self, *, email: str, password: str):
        self.site.driver.find_element(*self.locators["email_field"].element).send_keys(email)
        self.site.driver.find_element(*self.locators["password_field"].element).send_keys(password)
        self.site.driver.find_element(*self.locators["login_btn"].element).click()
