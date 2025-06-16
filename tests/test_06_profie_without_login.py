from utils.presence_of_elements import check_ui_elements
from drivers.driver_utils import element_clicked_by_uiautomator


def test_dynamic_ui_elements_of_profile_page(driver):
    assert element_clicked_by_uiautomator(driver, "new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(2)" ), "Failed to Click the Profile Button"
    elements = [
        {
            "desc": "Home Button",
            "xpath": '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[1]'
        },
        {
            "desc": "Session Button",
            "xpath": '//android.widget.FrameLayout[@content-desc="Session"]'
        },
        {
            "desc": "Complete Profile Button",
            "xpath": '//android.widget.RelativeLayout[@resource-id="com.supportgenie.argenie:id/complete_profile_rly"]'
        },
        {
            "desc": "FAQ Button",
            "xpath": '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/faq_btn"]'
        },
        {
            "desc": "Create Demo Recording Button",
            "xpath": '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/create_rec_btn"]'
        }
    ]
    check_ui_elements(driver, elements)
    