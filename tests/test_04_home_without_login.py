from utils.presence_of_elements import check_ui_elements

def test_dynamic_ui_elements_of_home_page(driver):
    elements = [
        {"desc": "Session Button", "xpath": '//android.widget.FrameLayout[@content-desc="Session"]'},
        {"desc": "Profile Button", "xpath": '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[3]'},
        {"desc": "User Name", "xpath": '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/user_name"]'},
        {"desc": "Welcome Text", "xpath": '//android.widget.TextView[@text="Welcome to AR Genie!"]'},
        {"desc": "Empower Text", "xpath": '//android.widget.TextView[@text="Empower Your Work"]'},
        {"desc": "Language Changer Spinner", "xpath": '//android.widget.Spinner[@resource-id="com.supportgenie.argenie:id/lang_spinner"]'},
        {"desc": "Join Session Button", "xpath": '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_btn"]'}
    ]
    check_ui_elements(driver, elements)

