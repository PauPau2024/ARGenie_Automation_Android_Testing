from drivers.driver_utils import *
from utils.meeting_id import *
from utils.annotation import *

def test_create_session_button(driver):
    assert element_clicked_by_uiautomator(driver, "new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(0)" ), "Failed to Click the 'Home' Button"
    assert element_presence_by_xpath(driver,'//android.widget.Button[@resource-id="com.supportgenie.argenie:id/host_btn"]'), "Failed to find the Create Session Button"
    assert element_clicked_by_xpath(driver, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/host_btn"]'), "Failed to Click the 'Create Session' Button"

def test_dynamic_ui_elements_of_create_sesssion(driver):
    assert element_presence_by_xpath(driver,'//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/title_tv"]'), "Failed to Find the Session ID Tittle"
    assert element_presence_by_xpath(driver,'//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/link_code_tv"]'), "Failed to Find the Generated Session ID"
    assert element_presence_by_xpath(driver,'//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_meeting_btn"]'), "Failed to Find the Join Session Button"

def test_share_session_button(driver):
    assert element_presence_by_uiautomator(driver,'new UiSelector().resourceId("com.supportgenie.argenie:id/share_btn")'), "Failed to Find the Share Session Button"

    