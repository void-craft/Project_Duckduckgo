import json
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json", help="Path to the configuration file.")


@pytest.fixture(scope='session')
def config(request):
    # Read the file specified in the command line options
    config_file_path = request.config.getoption("--config")
    with open(config_file_path) as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    supported_browsers = ['Firefox', 'Chrome', 'Headless Chrome']
    assert config['browser'] in supported_browsers, f"Invalid browser value. Supported browsers: {supported_browsers}"
    assert isinstance(config['implicit_wait'], int), "Implicit wait must be an integer."
    assert config['implicit_wait'] > 0, "Implicit wait must be greater than 0."

    # Return config so it can be used
    return config


@pytest.fixture
def browser(request, config):
    # Initialize the WebDriver instance based on the configuration
    if config['browser'] == 'Firefox':
        b = webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        b = webdriver.Chrome(options=options)
    else:
        raise ValueError(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
