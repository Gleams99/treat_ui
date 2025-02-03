import pytest
import chromedriver_autoinstaller
from loguru import logger
from treat_ui.config.browsers import init_driver, DEFAULT_CONFIGURATION


@pytest.fixture
def ensure_latest_chromedriver():
    logger.debug("Ensuring chromedriver is correct version")
    chromedriver_autoinstaller.install()


@pytest.fixture
def driver(request, ensure_latest_chromedriver):
    """Yield a prepared web driver instance based on provided browser configuration."""
    cfg = request.config.option.brw_cfg or DEFAULT_CONFIGURATION
    driver = init_driver(config_key=cfg, test_name=request.node.nodeid)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    """Add support to pytest for specifying browser configuration via commandline argument."""
    group = parser.getgroup('drivercfg', 'Driver Configuration')
    group.addoption(
        '--brw-cfg', default=DEFAULT_CONFIGURATION, action='store',
        help='Specify browser cfg')
