import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def remote():
    url = "http://localhost:4444/wd/hub"
    driver = webdriver.Remote(command_executor=url)
    yield driver
    driver.quit()
