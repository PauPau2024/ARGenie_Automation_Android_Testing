import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def username(driver,username,timeout=5):
    wait = WebDriverWait(driver, timeout)
    name = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/user_name"]')))
    if username == name.text:
        return True
    else :
        return False    