from drivers.driver_utils import element_presence_by_xpath
from tests.conftest import driver


def test_app_is_in_foreground(driver):
    current_package = driver.current_package
    assert current_package == "com.supportgenie.argenie", f"Expected app not in foreground. Found: {current_package}"

def test_app_start_up(driver):
    assert element_presence_by_xpath(driver,'//android.widget.Button[@resource-id="com.supportgenie.argenie:id/skipBtn"]'), "Failed to Start the App"
