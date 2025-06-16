from utils.presence_of_elements import check_ui_elements
from drivers.driver_utils import element_clicked_by_uiautomator


def test_dynamic_ui_elements_of_session_page(driver):
    assert element_clicked_by_uiautomator(driver, "new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(1)" ), "Failed to Click the Session Button"
    elements = [
        {"desc": "Home Button",
         "xpath": '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[1]'},
        {"desc": "Profile Button",
         "xpath": '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[3]'},
        {"desc": "Login‑required title",
         "xpath": '//android.widget.TextView[@text="Log In Required"]'},
        {"desc": "Login‑required subtitle",
         "xpath": '//android.widget.TextView[@text="Please log in to access session features."]'},
        {"desc": "Login Button",
         "xpath": '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/login_btn"]'}
    ]
    check_ui_elements(driver, elements)
    