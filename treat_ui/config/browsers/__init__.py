from loguru import logger
from pydantic import BaseModel, ConfigDict, Field
from strenum import StrEnum
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


class BrowserNamesEnum(StrEnum):
    Chrome = "chrome"
    Firefox = "firefox"


class BrowserLocationEnum(StrEnum):
    Local = "local"
    Remote = "remote"


class BrowserOptions(BaseModel):
    model_config = ConfigDict(extra='allow', use_enum_values=True)

    window_height: int = 1000
    window_width: int = 600


class BrowserConfiguration(BaseModel):
    model_config = ConfigDict(extra='allow', use_enum_values=True)

    browser_name: str
    location: BrowserLocationEnum = Field(default_factory=BrowserLocationEnum)
    options: BrowserOptions = Field(default_factory=BrowserOptions)
    capabilities: dict = {}


DEFAULT_CONFIGURATION = "local_chrome_1"
BROWSER_CONFIGURATIONS = {
    "local-chrome-1": BrowserConfiguration(
        browser_name=BrowserNamesEnum.Chrome,
        location=BrowserLocationEnum.Local,
        capabiliities={}
    ),
    "local-firefox-1": BrowserConfiguration(
        browser_name=BrowserNamesEnum.Firefox,
        location=BrowserLocationEnum.Local,
    ),
    "remote-chrome-1": BrowserConfiguration(
        browser_name=BrowserNamesEnum.Chrome,
        location=BrowserLocationEnum.Remote,
        capabiliities={}
    ),
}


def init_driver(*, config_key: str | None = None, test_name: str | None):
    use_config = config_key if config_key in BROWSER_CONFIGURATIONS else DEFAULT_CONFIGURATION
    test_name = test_name if test_name else "test"

    logger.info(f"Using driver configuration: {use_config}")
    config = BROWSER_CONFIGURATIONS[use_config]
    driver = None
    if config.browser_name == BrowserNamesEnum.Chrome:
        if config.location == BrowserLocationEnum.Local:
            opts = webdriver.ChromeOptions()
            opts.add_argument("--disable-extensions")
            opts.add_argument("--disable-gpu")
            opts.add_argument("--no-sandbox")  # linux only
            opts.add_argument("--headless=new")
            opts.add_argument("--window-size=800,600")
            driver = webdriver.Chrome(options=opts)
        elif config.location == BrowserLocationEnum.Remote:
            options = ChromeOptions()
            options.set_capability('se:name', test_name)
            driver = webdriver.Remote(options=options, command_executor="http://localhost:4444")

    elif config.browser_name == BrowserNamesEnum.Firefox:
        driver = webdriver.Firefox()

    if driver:
        return driver


__all__ = ["init_driver", "BROWSER_CONFIGURATIONS", "DEFAULT_CONFIGURATION"]
