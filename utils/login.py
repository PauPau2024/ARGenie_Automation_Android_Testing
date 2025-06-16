from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import pytest

def login(driver, username: str, password: str, timeout: int = 10):
    """
    Fill the login form, optionally toggle “show password”, and tap the Login button.

    Parameters
    ----------
    driver : Appium WebDriver
        The active Appium session.
    username : str
        Email / username to enter.
    password : str
        Password to enter.
    timeout : int, optional
        Seconds to wait for each element (default = 10).
    """

    wait = WebDriverWait(driver, timeout)

    try:
        # --- username field ---
        user_field = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH,
                 '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/username"]')
            )
        )
        user_field.clear()
        user_field.send_keys(username)

        # --- password field ---
        pwd_field = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.XPATH,
                 '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/user_password"]')
            )
        )
        pwd_field.clear()
        pwd_field.send_keys(password)

        # --- toggle show / hide password (optional) ---
        eye_icon_xpath = '//android.widget.ImageButton[@content-desc="Show password"]'
        eye_icon = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, eye_icon_xpath)))

        # Show password
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, eye_icon_xpath))).click()
        print("Show‑password toggled ON")

        # Hide password again
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, eye_icon_xpath))).click()
        print("Show‑password toggled OFF")

        # --- tap Login button ---
        wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ID, 'com.supportgenie.argenie:id/login_btn')
            )
        ).click()
        return True

    except Exception as e:
        return False
        
