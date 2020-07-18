import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="session")
def setup(request):
    global driver
    caps = ""
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        #caps = DesiredCapabilities.CHROME
        driver = webdriver.Chrome(executable_path="E:\\san_latest_2020\\grid\\chromedriver.exe")
        #driver = webdriver.Remote(command_executor="http://localhost:4547/wd/hub", desired_capabilities=caps)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="E:\\san_latest_2020\\grid\\geckodriver.exe")
        #caps = DesiredCapabilities.FIREFOX
        #driver = webdriver.Remote(command_executor="http://localhost:4546/wd/hub", desired_capabilities=caps)
    driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    yield
    #driver.close()
