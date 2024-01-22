from base.BaseClass import BaseClass
from base.DriverClass import WebDriverClass


wd = WebDriverClass()
driver = wd.getWebDriver("chrome")

bc = BaseClass(driver)