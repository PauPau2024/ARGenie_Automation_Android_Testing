from drivers.driver_utils import *
from utils.meeting_id import *
from utils.annotation import *


def test_dynamic_ui_elements_session_section(driver):
    assert element_clicked_by_uiautomator(driver, "new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(1)" ), "Failed to Click the Session Button"
    assert element_presence_by_xpath(driver, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/user_name_tv"]'),"Failed to find the Username of the User in the Session Section"
    assert element_presence_by_xpath(driver, '//android.widget.TextView[@text="Active Sessions"]'), "Failed to Find the 'Active Session'"
    assert element_presence_by_xpath(driver, '(//android.widget.LinearLayout[@resource-id="com.supportgenie.argenie:id/session_card"])[1]'), "Failed to Find the 'Session Card'"
    assert element_presence_by_xpath(driver, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/participant_iv"])[1]'), "Failed to Find the 'Participants icon'"
    assert element_presence_by_xpath(driver, '(//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_btn"])[1]'), "Failed to Find the 'Join Session of the 1st Session'"
    