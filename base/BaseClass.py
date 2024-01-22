from traceback import print_stack

from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec

import utilities.CustomLogger as cl

class BaseClass:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def launchWebPage(self, url):
        try:
            self.driver.get(url)
            self.log.info("Web Page Launched with URL : " + url)
        except:
            self.log.info("Web Page not Launched with URL : " + url)


    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("Locator Type : " + locatorType + " entered is not found")
        return False

    def waitForElement(self, locatorValue, locatorType):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            webElement = wait.until(ec.presence_of_element_located((locatorByType, locatorValue)))
            self.log.info("WebElement found with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "WebElement not found with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            #self.takeScreenshot(locatorType)
            assert False
        return webElement

    def clickOnElement(self, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.click()
            self.log.info(
                "Clicked on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "Unable to Click on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            #self.takeScreenshot(locatorType)
            assert False