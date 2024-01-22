from base.BaseClass import BaseClass
from base.DriverClass import WebDriverClass

wd = WebDriverClass()
driver = wd.getWebDriver("chrome")

bc = BaseClass(driver)

bc.launchWebPage("https://petdiseasealerts.org/forecast-map#/")

driver.switch_to.frame(bc.waitForElement("//iframe[contains(@id,'map-instance')]", "xpath"))

ele = bc.waitForElement("Florida", "name")
driver.execute_script("arguments[0].click();", ele)

# bc.clickOnElement("Florida", "name")
