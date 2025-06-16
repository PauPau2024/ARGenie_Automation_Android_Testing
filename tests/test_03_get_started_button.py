from drivers.driver_utils import element_presence_by_xpath,perform_swipe,element_clicked_by_xpath,element_clicked_by_accessibility,element_presence_by_accessibility

def test_clicking_the_GET_STARTED_button(driver):
    assert element_clicked_by_xpath(driver,'//android.widget.Button[@resource-id="com.supportgenie.argenie:id/skipBtn"]'), "Failed to Click the 'GET STARTED' Button Before Giving DND Permission"

def test_setting_up_DND_permission(driver):
    assert element_presence_by_accessibility(driver,'Navigate up'), "Failed to redirect to the Settings for DND Permission"
    assert element_clicked_by_accessibility(driver,'Navigate up'), "Failed to Click the Back Button of Setting from DND Section"

def test_clicking_the_GET_STARTED_button_after_DND(driver):
    assert element_clicked_by_xpath(driver,'//android.widget.Button[@resource-id="com.supportgenie.argenie:id/skipBtn"]'), "Failed to Click the 'GET STARTED' Button After Giving DND Permission"
