from drivers.driver_utils import element_presence_by_xpath,perform_swipe,element_clicked_by_xpath

def test_presence_of_skip_button(driver):
    assert element_presence_by_xpath(driver,'//android.widget.Button[@resource-id="com.supportgenie.argenie:id/skipBtn"]'), "Failed to find the 'Skip Button'"

def test_presence_of_first_into_page(driver):
    assert element_presence_by_xpath(driver, '//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/imageView1"]'), "Failed to find the First Page"
    perform_swipe(driver,858, 1071, 511, 1071)

def test_presence_of_second_into_page(driver):
    assert element_presence_by_xpath(driver, '//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/imageView2"]'), "Failed to find the Second Page"
    perform_swipe(driver,858, 1071, 511, 1071)

def test_presence_of_third_into_page(driver):
    assert element_presence_by_xpath(driver, '//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/imageView1"]'), "Failed to find the Third Page"
    perform_swipe(driver,858, 1071, 511, 1071)

def test_presence_of_fourth_into_page(driver):
    assert element_presence_by_xpath(driver, '//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/imageView2"]'), "Failed to find the Fourth Page"
    perform_swipe(driver,858, 1071, 511, 1071)

def test_presence_of_GET_STARTED_button(driver):
    assert element_presence_by_xpath(driver, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/skipBtn"]'), "Failed to find the GET STARTED Button"
    