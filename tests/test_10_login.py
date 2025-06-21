from drivers.driver_utils import element_clicked_by_uiautomator,element_presence_by_id,element_clicked_by_xpath,element_clicked_by_id,element_presence_by_uiautomator,element_presence_by_xpath
from utils.presence_of_elements import check_ui_elements
from utils.login import login
import time

def  test_clicking_login_button_under_session_section(driver):
    assert element_clicked_by_uiautomator(driver, "new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(1)" ), "Failed to Click the Session Button"
    assert element_clicked_by_id(driver,"com.supportgenie.argenie:id/login_btn"), "Failed to Click the 'Login Button' from the Session Page"

def test_dynamic_ui_elements_of_login_page(driver):
    elements = [
        {
            "desc": "Email Field",
            "xpath": '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/username"]'
        },
        {
            "desc": "Password Field",
            "xpath": '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/user_password"]'
        },
        {
            "desc": "Forgot Password Option",
            "xpath": '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/forgetPwdBtn"]'
        },
        {
            "desc": "Show Password Icon",
            "xpath": '//android.widget.ImageButton[@content-desc="Show password"]'
        },
        {
            "desc": "Create Account Option",
            "xpath": '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/create_account_btn"]'
        },
        {
            "desc": "Join as Guest Option",
            "xpath": '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/guestBtn"]'
        },
        {
            "desc": "Login Button",
            "xpath": '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/login_btn"]'
        }
    ]
    check_ui_elements(driver, elements)

def test_go_back_button(driver):
    assert element_presence_by_uiautomator(driver, "new UiSelector().text(\"Go Back\")"), "Failed to Find the 'Go Back' Button in the Login Page"
    assert element_clicked_by_uiautomator(driver, "new UiSelector().text(\"Go Back\")"), "Failed to click the 'Go Back' Button in the Login Page"

def test_create_account_button(driver):
    assert element_clicked_by_uiautomator(driver, "new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(1)" ), "Failed to Click the Session Button"
    assert element_clicked_by_id(driver,"com.supportgenie.argenie:id/login_btn"), "Failed to Click the 'Login Button' from the Session Page"
    assert element_presence_by_id(driver,"com.supportgenie.argenie:id/create_account_btn"), "Failed to Find the 'Create Account' Button"
    assert element_clicked_by_uiautomator(driver, "new UiSelector().text(\"Go Back\")"), "Failed to click the 'Go Back' Button in the Login Page"

def test_forgot_password_button(driver):
    assert element_clicked_by_id(driver,"com.supportgenie.argenie:id/login_btn"), "Failed to Click the 'Login Button' from the Session Page"
    assert element_presence_by_xpath(driver, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/forgetPwdBtn"]') , "Failed to Find the 'Forgot Password' Button"
    assert element_clicked_by_uiautomator(driver, "new UiSelector().text(\"Go Back\")"), "Failed to click the 'Go Back' Button in the Login Page"

def test_guest_account_button(driver):    
    assert element_clicked_by_id(driver,"com.supportgenie.argenie:id/login_btn"), "Failed to Click the 'Login Button' from the Session Page"
    assert element_presence_by_xpath(driver,'//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/guestBtn"]' ), "Failed to Find the 'Guest Account' Button"
    #assert element_clicked_by_xpath(driver,'//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/guestBtn"]' ),"Failed to Click the 'Guest Account' Button"

def test_wrong_email_wrong_password(driver):
    assert login(driver, "test@test.com", "password"), "Failed to Login with Wrong Email and Wrong Password"

def test_correct_email_wrong_password(driver):    
    assert login(driver, "sujal@staging.com", "password"), "Failed to Login with Correct Email and Wrong Password"

def test_wrong_email_correct_password(driver):    
    assert login(driver, "test@test.com", "Kingfisher@123"), "Failed to Login with Wrong Email and Correct Password"
     
def test_correct_email_correct_password(driver):    
    assert login(driver, "sujal@staging.com", "Kingfisher@123"), "Failed to Login with Wrong Email and Correct Password"
    time.sleep(5)
    assert element_clicked_by_uiautomator(driver, "new UiSelector().text(\"Go Back\")"), "Failed to click the 'Go Back' Button in the Login Page"
 
     