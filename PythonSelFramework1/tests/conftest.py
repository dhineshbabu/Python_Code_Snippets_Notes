import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = None
# code to choose browser from command line
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="To choose browser from command line"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    global driver
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\lenovo\Desktop\\My Projects\Code\\Python\\Selenium_python_Udemy\\chromedriver_win32\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            executable_path="C:\\Users\\lenovo\\Desktop\\My Projects\\Code\\Python\\Selenium_python_Udemy\\geckodriver.exe")
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    elif browser_name == "ie":
        driver = webdriver.Ie(
            executable_path="C:\\Users\\lenovo\\Desktop\\My Projects\\Code\\Python\\Selenium_python_Udemy\\IEDriverServer.exe")
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)