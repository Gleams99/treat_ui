import pytest
from selenium import webdriver
import chromedriver_autoinstaller
from loguru import logger



@pytest.fixture
def ensure_latest_chromedriver():
    logger.debug("Ensuring chromedriver is correct version")
    chromedriver_autoinstaller.install()


@pytest.fixture
def driver(ensure_latest_chromedriver):
    driver = webdriver.Chrome()
    logger.debug("Yielding Chrome driver")
    yield driver
    driver.quit()
