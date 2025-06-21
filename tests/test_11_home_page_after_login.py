from utils.presence_of_elements import check_ui_elements
from drivers.driver_utils import element_clicked_by_uiautomator
from utils.username import username

def test_home_page_button_after_login(driver):
        assert element_clicked_by_uiautomator(driver, "new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(0)" ), "Failed to Click the 'Home' Button"

def test_dynamic_ui_elements_of_home_page(driver):
    elements = [
        {"desc": "Session Button", "xpath": '//android.widget.FrameLayout[@content-desc="Session"]'},
        {"desc": "Profile Button", "xpath": '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[3]'},
        {"desc": "User Name", "xpath": '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/user_name"]'},
        {"desc": "Empower Text", "xpath": '//android.widget.TextView[@text="Empower Your Work"]'},
        {"desc": "Language Changer Spinner", "xpath": '//android.widget.Spinner[@resource-id="com.supportgenie.argenie:id/lang_spinner"]'},
        {"desc": "Join Session Button", "xpath": '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_btn"]'}
    ]
    check_ui_elements(driver, elements)

def test_home_page_username(driver):
    assert username(driver,"Sujal"), "Failed to Find the Username of the user after Login"
