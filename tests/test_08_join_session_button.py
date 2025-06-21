from drivers.driver_utils import *

def test_click_join_session_button(driver):
     assert element_clicked_by_uiautomator(driver,"new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(0)"),"Failed to Click the Home Button"
     assert element_presence_by_xpath(driver,'//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_btn"]'),"Failed to Find the Join Session Button"

def test_dynamic_ui_elements_of_join_session_page(driver):
     #assert element_presence_by_xpath(driver,'//android.widget.LinearLayout[@resource-id="com.supportgenie.argenie:id/control_panel"]' ),"Failed to find the Metting ID Control Panel Text"
     #assert element_presence_by_xpath(driver,'//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/link_id"]'), "Failed to Find the Metting ID Text"
     assert element_presence_by_xpath(driver,'//android.widget.Button[@resource-id="com.supportgenie.argenie:id/btn_join_link"]'), "Failed to Find the Join Button"
     assert element_clicked_by_xpath(driver,"new UiSelector().text(\"Go Back\")"), "Failed to find the Go Back Button"

     assert element_clicked_by_id(driver,"com.supportgenie.argenie:id/join_btn"),"Failed to Click the Join Session Button"
     assert element_clicked_by_uiautomator(driver, "new UiSelector().text(\"Go Back\")"), "Failed to click the 'Go Back' Button in the Login Page"
     
