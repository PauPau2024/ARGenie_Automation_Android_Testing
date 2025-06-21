from drivers.driver_utils import *
from utils.meeting_id import *
from utils.annotation import *
from utils.presence_of_elements import check_ui_elements

def test_user_profile_option_button(driver):
    assert element_clicked_by_uiautomator(driver, "new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(2)" ), "Failed to Click the Profile Button"
    assert element_clicked_by_xpath(driver, '//android.widget.RelativeLayout[@resource-id="com.supportgenie.argenie:id/complete_profile_rly"]'), "Failed to click the User Profile Section"

def test_dynamic_ui_elements_of_logout_page(driver):
    elements = [
        {
            "desc": "Log-out POP-UP",
            "xpath": '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/dialogTitle"]'
        },
        {
            "desc": "Log-out 'YES' Option",
            "xpath": '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/positiveButton"]'
        },
        {
            "desc": "Log-out 'NO' Option",
            "xpath": '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/negativeButton"]'
        }
    ]
    check_ui_elements(driver, elements)

def test_cancel_log_out(driver):
    assert element_clicked_by_xpath(driver,'//android.widget.Button[@resource-id="com.supportgenie.argenie:id/negativeButton"]'),"Failed to Click the Cancel Button in the Log-Out pop-up"

def test_successfull_logout(driver):
    assert element_clicked_by_xpath(driver,'//android.widget.RelativeLayout[@resource-id="com.supportgenie.argenie:id/complete_profile_rly"]'),  "Failed to click the User Profile Section"   
    assert element_clicked_by_xpath(driver,'//android.widget.Button[@resource-id="com.supportgenie.argenie:id/positiveButton"]'),"Failed to Click the 'YES' Button in the Log-Out pop-up"    

def test_go_back_button(driver):
    assert element_presence_by_uiautomator(driver, "new UiSelector().text(\"Go Back\")"), "Failed to Find the 'Go Back' Button in the Login Page"
    assert element_clicked_by_uiautomator(driver, "new UiSelector().text(\"Go Back\")"), "Failed to click the 'Go Back' Button in the Login Page"
