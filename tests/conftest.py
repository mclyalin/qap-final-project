import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def web_browser():
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1400,1000")
    # options.add_argument('--headless')
    # options.add_argument("--no-sandbox")
    # options.add_argument('--log-level=DEBUG')
    browser = webdriver.Chrome(options=options, service=service)

    # Return browser instance to test case:
    yield browser

    browser.quit()


def get_test_case_docstring(item):
    """ This function gets doc string from test case and format it
        to show this docstring instead of the test case name in reports.
    """

    full_name = ''

    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Generate the list of parameters for parametrized test cases:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Create List based on Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Add dict with all parameters to the name of test case:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ This function modifies names of test cases "on the fly"
        during the execution of test cases.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ This function modified names of test cases "on the fly"
        when we are using --collect-only parameter for pytest
        (to get the full list of all existing test cases).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # If test case has a doc string we need to modify it's name to
            # it's doc string to show human-readable reports and to
            # automatically import test cases to test management system.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')
