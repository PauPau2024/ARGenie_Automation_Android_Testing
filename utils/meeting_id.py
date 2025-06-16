from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import pytest

def meeting_id_input(driver, xpath, meeting_id , timeout=10):
    try:
        # Wait for the element to be present within the specified timeout
        id = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((AppiumBy.XPATH, xpath))
        )
        id.clear()
        id.send_keys(meeting_id)
        return True  # Element found
    except Exception as e:
        return False  # Element not found