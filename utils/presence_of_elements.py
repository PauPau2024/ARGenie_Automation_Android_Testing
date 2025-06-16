import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_ui_elements(driver, elements_to_check, timeout=10):
    wait = WebDriverWait(driver, timeout)

    for element in elements_to_check:
        try:
            el = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, element["xpath"])))
            if el.tag_name == "android.widget.TextView":
                print(f"{element['desc']} is Present with text: '{el.text}'")
            else:
                print(f"{element['desc']} is Present")
        except Exception as e:
            pytest.fail(f" {element['desc']} not found within {timeout} seconds.\nError: {str(e)}")
