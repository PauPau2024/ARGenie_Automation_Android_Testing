from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import pytest
import time

def click_element(wait, by, value, description="Element"):
    try:
        wait.until(EC.element_to_be_clickable((by, value))).click()
        print(f"{description} Clicked Successfully")
    except Exception as e:
        print(f"Failed to click {description}: {e}")
        raise

def check_presence(wait, by, value, description="Element"):
    try:
        wait.until(EC.presence_of_element_located((by, value)))
        print(f"{description} is Present")
    except Exception as e:
        print(f"{description} not found: {e}")
        raise

def remove_anchor(wait):
    check_presence(wait, AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors', "Remove Anchor Button")
    click_element(wait, AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors', "Remove Anchor Button")
    click_element(wait, AppiumBy.ID, 'android:id/button1', "Confirmation OK Button")

def annotation_arrow_flow(wait):
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Menu close', "Annotation Menu")
    check_presence(wait, AppiumBy.ACCESSIBILITY_ID, 'Arrow', "Annotation Arrow")
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Arrow', "Annotation Arrow")
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Menu close', "Annotation Menu Open")
    remove_anchor(wait)
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Menu_open', "Menu Close")

def annotation_draw_flow(wait):
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Menu close', "Annotation Menu")
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Draw', "Draw Annotation Button")
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Menu close', "Annotation Menu Open")
    remove_anchor(wait)
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Menu_open', "Menu Close")

def annotation_circle_flow(wait):
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Menu close', "Annotation Menu")
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Circle', "Circle Annotation Button")
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Menu close', "Annotation Menu Open")
    remove_anchor(wait)
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Menu_open', "Menu Close")

def annotation_text_flow(wait):
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Menu close', "Annotation Menu")
    check_presence(wait, AppiumBy.ID, 'com.supportgenie.argenie:id/ar_text_iv', "AR Text Button")
    click_element(wait, AppiumBy.ID, 'com.supportgenie.argenie:id/ar_text_iv', "AR Text Button")
    wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, 'android.widget.EditText'))).send_keys("test")
    print("Text entered in Text Box")
    click_element(wait, AppiumBy.ID, 'android:id/button1', "Text OK Button")
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Menu close', "Annotation Menu Open")
    remove_anchor(wait)
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Menu_open', "Menu Close")

def annotation_colour_flow(wait, perform_draw):
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Menu close', "Annotation Menu")
    check_presence(wait, AppiumBy.ID, 'com.supportgenie.argenie:id/ar_color_selection_iv', "Color Annotation Button")
    click_element(wait, AppiumBy.ID, 'com.supportgenie.argenie:id/ar_color_selection_iv', "Color Annotation Button")
    perform_draw(784, 1300, 0.1)
    click_element(wait, AppiumBy.ID, 'android:id/button1', "OK Button")
    print("Color selection done")

def annotation_arrow_direction_flow(wait):
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, 'Menu close', "Menu Close Button")
    click_element(wait, AppiumBy.ID, 'com.supportgenie.argenie:id/ar_options_iv', "AR Options Button")
    click_element(wait, AppiumBy.ID, 'com.supportgenie.argenie:id/ar_arrow_up_iv', "Arrow Up")
    click_element(wait, AppiumBy.ID, 'com.supportgenie.argenie:id/ar_arrow_right_iv', "Arrow Right")
    click_element(wait, AppiumBy.ID, 'com.supportgenie.argenie:id/ar_arrow_left_iv', "Arrow Left")
    click_element(wait, AppiumBy.ID, 'ar_anchor_setting_close', "Anchor Setting Close")
    print("Arrow direction set")

def go_back_and_chat_flow(wait):
    check_presence(wait, AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")", "Go Back Button")
    click_element(wait, AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")", "Go Back Button")
    click_element(wait, AppiumBy.ID, "com.supportgenie.argenie:id/chat_lly", "Chat Button")
    wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/message_textview"))).send_keys("Automation_Testing")
    print("Text sent in chat")
    click_element(wait, AppiumBy.ACCESSIBILITY_ID, "TODO", "Send Button")
    click_element(wait, AppiumBy.ID, "com.supportgenie.argenie:id/chat_back_btn_iv", "Chat Back Button")

def leave_meeting_flow(wait):
    check_presence(wait, AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/leave_room_btn"]', "Leave Meeting Button")
    click_element(wait, AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/leave_room_btn"]', "Leave Meeting Button")
    time.sleep(5)
    click_element(wait, AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")", "Go Back Button")
    click_element(wait, AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")", "Go Back Button")
