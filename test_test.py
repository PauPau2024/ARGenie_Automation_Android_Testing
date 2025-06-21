from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
import time
import pytest

options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",  # Ensure this matches your device
    "appium:deviceName": "emulator-5554",
    "appium:automationName": "UIAutomator2",
    "appium:ensureWebviewsHavePages": True,
    "appium:nativeWebScreenshot": True,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True,
    "appium:autoGrantPermissions": True,
    "appium:app": "D:/Device_Farm/Stagging Application/Remote Assist-stagingV4.0.4.apk"
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 10)  # Global wait instance

def perform_swipe(start_x, start_y, end_x, end_y):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

def perform_draw(start_x, start_y, pause):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.pause(pause)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

def test_app_start_up():
    try:
       button = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/skipBtn"]')))
       print("App opened successfully, 'Skip' button found!")
    except Exception as e:
        print(f"Failed to open the app or find the button: {e}")
        assert False

def test_slide():
    try:
        button = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/imageView1"]')))
        print("First Page Successfull Presented")
        perform_swipe(858, 1071, 511, 1071)
        button = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/imageView2"]')))
        print("Second Page Successfull Presented")
        perform_swipe(858, 1071, 511, 1071)
        button = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/imageView1"]')))
        print("Third Page Successfull Presented")
        perform_swipe(858, 1071, 511, 1071)
        button = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/imageView2"]')))
        print("Fourth Page Successfull Presented")
        perform_swipe(858, 1071, 511, 1071)
    except Exception as e:
        print(f"Failed to to Load Slide Page: {e}")
        assert False

def test_GET_STARTED_button(): 
    try:
       button = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/skipBtn"]')))
       print("GET STARTED button found")
       try :
           wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/skipBtn"]'))).click()
           print("GET STARTED Button clicked Successfully")
       except Exception as e:
           print(f"GET STARTED BUTTON click Failed : {e}")
           assert False    

    except Exception as e:
        print(f"Failed to find the GET STARTED button: {e}")
        assert False

def test_skipping_DND_permission():
    try :    
        wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Navigate up")))
        print("Do Not Disturb Permission Section is Present")
        try:
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Navigate up"))).click()
            print("Successfully Skipped the DND Permission")
        except Exception as e:
            print(f"DND Permission Errror : {e}")    
    except Exception as e:
        print(f"Failed to find the GET STARTED button: {e}")
        assert False 

def test_GET_STARTED_CLICK():
    try:
       button = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/skipBtn"]')))
       print("GET STARTED button found")
       try :
           wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/skipBtn"]'))).click()
           print("GET STARTED Button clicked Successfully")
       except Exception as e:
           print(f"GET STARTED BUTTON click Failed : {e}")
           assert False    

    except Exception as e:
        print(f"Failed to find the GET STARTED button: {e}")
        assert False

def test_home_page():
    try: 
        home = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[1]')))
        print(f"Home Button is Present")
        try:
               wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[1]'))).click()
               print("Clicked the HOME button Successfully")        
        except Exception as e:
               print(f"Failed to click HOME button: {e}")
               assert False
        session = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Session"]')))
        print(f"Session Button is Present")       
        profile = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[3]')))
        print(f"Profile Button is Present")
        name = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/user_name"]')))
        print(f"Hey, {name.text} is Present")
        welcome = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Welcome to AR Genie!"]')))
        print(f"{welcome.text} is Present")
        empower = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Empower Your Work"]')))
        print(f"{empower.text} is Present")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Spinner[@resource-id="com.supportgenie.argenie:id/lang_spinner"]')))
        print("Language Changer is Present")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_btn"]')))
        print("Join Session Button is Present")
        network = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/network_status_text"]')))
        print(f"Network Status is Present: {network.text}")


    except Exception as e:
        print(f"Home Section Error : {e}")
        assert False

def test_session_page():
    try:
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Session"]')))
        print(f"Session Button is Present")
        try:
                wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(1)"))).click()
                print("Clicked the Session button Successfully")        
        except Exception as e:
               print(f"Failed to click Session button: {e}")
               assert False 
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[1]')))
        print(f"Home Button is Present")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[3]')))
        print(f"Profile Button is Present")
        login_req = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Log In Required"]')))
        print(f"{login_req.text} text  is Present")
        login_text = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Please log in to access session features."]')))
        print(f"{login_text.text} text  is Present")
        login_button = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/login_btn"]')))
        print(f"{login_button.text} Button is Present")
    except Exception as e:   
        print(f"Session Section Error : {e}")
        assert False

def test_profile_page():
    try:
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[3]')))
        print(f"Profile Button is Present")
        try:
                wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(2)"))).click()
                print("Clicked the Profile button Successfully")        
        except Exception as e:
               print(f"Failed to click Profile button: {e}")
               assert False 
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[1]')))
        print(f"Home Button is Present")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Session"]')))
        print(f"Session Button is Present")

        login_button = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.RelativeLayout[@resource-id="com.supportgenie.argenie:id/complete_profile_rly"]')))
        print(f"{login_button.text} Button is Present")
        faq = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/faq_btn"]')))
        print(f"{faq.text} Button  is Present")
        demo = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/create_rec_btn"]')))
        print(f"{demo.text} Button is Present")
    except Exception as e:   
        print(f"Session Section Error : {e}")
        assert False      

def test_session_login_button():
    try:
       wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(1)"))).click()
       wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/login_btn")))
       print("Login Button in Session Section is Present")
       try:
           wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/login_btn"))).click()
           print("Clicked Login Button Successfully")
           wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/username"]')))
           print("Email Param is Present")
           wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/user_password"]')))
           print("Password Param is Present")
           wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/forgetPwdBtn"]')))
           print("forgot password option is Present")
           wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Show password"]')))
           print("Show password option is Present")
           wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/create_account_btn"]')))
           print("Create Account option is Present")
           wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/guestBtn"]')))
           print("Join as Guest option is Present")
           wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/login_btn"]')))
           print("Login Button is Present")
           wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")")))
           print("Go Back Button is Present")
           wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")"))).click()
           print("Clicked GO BACK button")
       except Exception as e:
           print(f"Login Button Errors in Session Section: {e}")   
    except Exception as e:
        print(f"Failed at Login Session: {e}")
        assert False 

def test_create_account_and_forget_password():
    try:
        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(1)"))).click()
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/login_btn")))
        print("Login Button in Session Section is Present")

        wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/login_btn"))).click()
        print("Clicked Login Button Successfully")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/forgetPwdBtn"]')))    
        print("Forgot Password Button is Present")
        
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/create_account_btn")))    
        print("Create Account Button is Present")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/guestBtn"]')))    
        print("Guest Account Button is Present")
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/guestBtn"]'))).click()    
        print("Guest Account Button is Clicked Succesfully")
    
    except Exception as e:
        print(f"Failed at Creating Account & Forget Password : {e}")
        assert False 

def test_no_login_Join_Session():
    try:
       wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(0)"))).click()
       time.sleep(2)
       wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_btn"]')))
       print("Join Session Button is Present")
       try :
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/join_btn"))).click()
            print('Join Session Button Clicked Successfully')
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="com.supportgenie.argenie:id/control_panel"]')))
            print("Meeting ID Control Panel is Present")
            id = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/link_id"]')))
            print(f"{id.text} is Present")
            back = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")")))
            print(f"{back.text} button is Present")
            join = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/btn_join_link"]')))
            print(f"{join.text} button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")"))).click()
            print("Clicked GO BACK button")
       except Exception as e:   
            print(f"Join Session Button Internal Errors: {e}")
            assert False 
    except Exception as e:
        print(f"Failed at JOIN SESSION button: {e}")
        assert False




def test_no_login_Join_Session_id():
    try:
       wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(0)"))).click()
       wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_btn"]')))
       print("Join Session Button is Present")
       try :
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/join_btn"))).click()
            print('Join Session Button Clicked Successfully')
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="com.supportgenie.argenie:id/control_panel"]')))
            print("Meeting ID Control Panel is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/link_id"]'))).send_keys("067-159-746")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/btn_join_link"))).click()
            print(f'Correct Metting ID input')
            time.sleep(10)
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.FrameLayout\").instance(12)")))
            print("Video of the User is Present")
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Me\")")))
            print("Video User Name is Present")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/mic_iv")))
            print("Mic Button is Present")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/audio_output_option_iv")))
            print("Audio Device Change Button is Present")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/video_iv")))
            print("Video Button is Present")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/chat_lly")))
            print("Chat Button is Present")           

            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/mic_iv"))).click()
            print("Mic Button is Clicked Successfully")
            #wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/audio_output_option_iv"))).click()
            #print("Audio Device Change Button is Clicked Successfully")
            #perform_draw(858, 1071, 0.1)
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/video_iv"))).click()
            print("Video Button is Clicked Successfully")
            time.sleep(10)
            #Console Check
            #Draw arrows
            
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotation Menu is Clicked Successfully")
            wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Arrow')))
            print("Annotation Arrow is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Arrow'))).click()
            print("Annotation Arrow is Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotation Menu Open is Clicked Successfully")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors')))
            print("Remove Achor Button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors'))).click()
            print("Remove Achor Button is Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
            print("Okay Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu_open'))).click()
            print("Clicked the Closed of Annotation")
            #Draw
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotationn Menu Clicked")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Draw'))).click()
            print("Clicked the Draw Annotation Button Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotation Menu Open is Clicked Successfully")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors')))
            print("Remove Achor Button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors'))).click()
            print("Remove Achor Button is Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
            print("Okay Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu_open'))).click()
            print("Clicked the Closed of Annotation")

            #Draw Circle
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotationn Menu Clicked")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Circle'))).click()
            print("Circle Annotation Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotation Menu Open is Clicked Successfully")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors')))
            print("Remove Achor Button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors'))).click()
            print("Remove Achor Button is Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
            print("Okay Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu_open'))).click()
            print("Clicked the Closed of Annotation")
            
            #Draw Text
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotationn Menu Clicked")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_text_iv')))
            print("AR Text Button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_text_iv'))).click()
            print("AR Text Button is Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, 'android.widget.EditText'))).send_keys("test")
            print("Test Text Send to the Text Box")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
            print("Okay button clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotation Menu Open is Clicked Successfully")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors')))
            print("Remove Achor Button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors'))).click()
            print("Remove Achor Button is Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
            print("Okay Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu_open'))).click()
            print("Clicked the Closed of Annotation")
            
            #Colour Selections    
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotation Menu Open is Clicked Successfully")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_color_selection_iv')))
            print("Colour Annotation button is present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_color_selection_iv'))).click()
            print("Colour Annotation Button Clicked Successfully")
            perform_draw(784, 1300,0.1)
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
            print("Okay Button Clicked Successfully")
            print("colour selection done")
            
            #AR Arrow Direction
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Menu Close Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_options_iv'))).click()
            print("AR Options Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_arrow_up_iv'))).click()
            print("Arrow Up Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_arrow_right_iv'))).click()
            print("Arrow Right Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_arrow_left_iv'))).click()
            print("Arrow Left Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'ar_anchor_setting_close'))).click()
            print("Anchor Setting Close Button Clicked Successfully")
            print("Arrow Direction  Done")

            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Menu Open Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors'))).click()
            print("Remove Anchors Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
            print("Confirmation OK Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu_open'))).click()
            print("Menu Closed Button Clicked Successfully")

            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")")))
            print("Go back Button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")"))).click()
            print("Clicked GO BACK button")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/chat_lly"))).click()
            print("Chat Button is Clicked Successfully") 
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/message_textview"))).send_keys("Automation_Testing")
            print("Text Send to the Text Box") 
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "TODO"))).click()
            print("Send Button Clicked for the Text Box")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/chat_back_btn_iv"))).click()
            print("Chat Back Button Clicked")
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/leave_room_btn"]')))
            print(f"Leave Metting Button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/leave_room_btn"]'))).click()
            print(f'Clicked Leave Metting Button Successfully')
            time.sleep(5)
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")"))).click()
            print("Clicked GO BACK button")
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")"))).click()
            print("Clicked GO BACK button")
       except Exception as e:   
            print(f"Join Session Button Internal Errors: {e}")
    except Exception as e:
        print(f"Failed at JOIN SESSION button: {e}")
        assert False


def test_login_session():
    try:
       wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"com.supportgenie.argenie:id/navigation_bar_item_icon_container\").instance(1)"))).click()
       wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/login_btn")))
       print("Login Button in Session Section is Present")
       try:
           wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/login_btn"))).click()
           print("Clicked Login Button Successfully")
           
           wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/username"]'))).send_keys("test@test.com")
           wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/user_password"]'))).send_keys("password")
           wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Show password"]')))
           wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Show password"]'))).click()
           print("Show Password Option Clicked Successfully")
           wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Show password"]')))
           wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Show password"]'))).click()
           print("Hide Password Option Clicked Succesfully")
           wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/login_btn"))).click()
           error = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Toast[@text="Incorrect username or password"]')))
           print(f"Wrong Email & Wrong Password Login Result : {error.text}")
           
           wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/username"]'))).send_keys("sujal@staging.com")
           wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/user_password"]'))).send_keys("password")
           wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/login_btn"))).click()
           error = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Toast[@text="Incorrect username or password"]')))
           print(f"Correct Email & Wrong Password Login Result : {error.text}")

           wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/username"]'))).send_keys("test@test.com")
           wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/user_password"]'))).send_keys("Kingfisher@123")
           wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/login_btn"))).click()
           error = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Toast[@text="Incorrect username or password"]')))
           print(f"wrong Email & Correct Password Login Result : {error.text}")           
           
           
           wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/username"]'))).send_keys("sujal@staging.com")
           wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/user_password"]'))).send_keys("Kingfisher@123")
           wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/login_btn"))).click()
           print(f"Correct Email & Correct Password Login: Success")           
           wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")"))).click()
           print("Go Back Button is Present")
           time.sleep(5)
           wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")"))).click()
           print("Clicked GO BACK button")
       except Exception as e:
           print(f"Login Button Errors in Session Section: {e}")   
    except Exception as e:
        print(f"Failed at Login Session: {e}")
        assert False  


def test_session_section_after_login():
    try: 
        name = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/user_name_tv"]')))
        print(f"Username : {name.text}")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Active Sessions"]')))
        print(f"Active Session Header is Present")
        try:
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.supportgenie.argenie:id/session_card"])[1]')))
            print(f"First Active Session is Avaliable")
            session_name = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.supportgenie.argenie:id/session_card"])[1]')))
            print(f"Active Session Name: {session_name.text}")
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/participant_iv"])[1]')))
            print("Participants Icon is visible")
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_btn"])[1]')))
            print("Join Session Button is Present")
        except Exception as e:
            print("Active Session was not Found")    
    except Exception as e:
        print(f"Failed at SESSION Section After Login: {e}")
        assert False    
def test_join_button_session_session():
    try:
       wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_btn"])[2]')))
       print("Join Session Button in the Session Section is Present")
       try :
            wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_btn"])[2]'))).click()
            print('Join Session Button Clicked Successfully')
            time.sleep(10)
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.FrameLayout\").instance(12)")))
            print("Video of the User is Present")
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Me\")")))
            print("Video User Name is Present")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/mic_iv")))
            print("Mic Button is Present")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/audio_output_option_iv")))
            print("Audio Device Change Button is Present")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/video_iv")))
            print("Video Button is Present")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/chat_lly")))
            print("Chat Button is Present")           

            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/video_iv"))).click()
            print("Video Button is Clicked Successfully")
            time.sleep(10)
            #Console Check
            
            #Draw arrows
            
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotation Menu is Clicked Successfully")
            wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Arrow')))
            print("Annotation Arrow is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Arrow'))).click()
            print("Annotation Arrow is Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotation Menu Open is Clicked Successfully")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors')))
            print("Remove Achor Button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors'))).click()
            print("Remove Achor Button is Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
            print("Okay Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu_open'))).click()
            print("Clicked the Closed of Annotation")
            #Draw
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotationn Menu Clicked")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Draw'))).click()
            print("Clicked the Draw Annotation Button Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotation Menu Open is Clicked Successfully")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors')))
            print("Remove Achor Button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors'))).click()
            print("Remove Achor Button is Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
            print("Okay Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu_open'))).click()
            print("Clicked the Closed of Annotation")

            #Draw Circle
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotationn Menu Clicked")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Circle'))).click()
            print("Circle Annotation Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotation Menu Open is Clicked Successfully")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors')))
            print("Remove Achor Button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors'))).click()
            print("Remove Achor Button is Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
            print("Okay Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu_open'))).click()
            print("Clicked the Closed of Annotation")
            
            #Draw Text
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotationn Menu Clicked")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_text_iv')))
            print("AR Text Button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_text_iv'))).click()
            print("AR Text Button is Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, 'android.widget.EditText'))).send_keys("test")
            print("Test Text Send to the Text Box")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
            print("Okay button clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotation Menu Open is Clicked Successfully")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors')))
            print("Remove Achor Button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors'))).click()
            print("Remove Achor Button is Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
            print("Okay Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu_open'))).click()
            print("Clicked the Closed of Annotation")
            
            #Colour Selections    
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Annotation Menu Open is Clicked Successfully")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_color_selection_iv')))
            print("Colour Annotation button is present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_color_selection_iv'))).click()
            print("Colour Annotation Button Clicked Successfully")
            perform_draw(784, 1300,0.1)
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
            print("Okay Button Clicked Successfully")
            print("colour selection done")
            
            #AR Arrow Direction
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Menu Close Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_options_iv'))).click()
            print("AR Options Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_arrow_up_iv'))).click()
            print("Arrow Up Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_arrow_right_iv'))).click()
            print("Arrow Right Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/ar_arrow_left_iv'))).click()
            print("Arrow Left Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'ar_anchor_setting_close'))).click()
            print("Anchor Setting Close Button Clicked Successfully")
            print("Arrow Direction  Done")

            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu close'))).click()
            print("Menu Open Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.supportgenie.argenie:id/remove_anchors'))).click()
            print("Remove Anchors Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
            print("Confirmation OK Button Clicked Successfully")
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Menu_open'))).click()
            print("Menu Closed Button Clicked Successfully")

            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")")))
            print("Go back Button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")"))).click()
            print("Clicked GO BACK button")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/chat_lly"))).click()
            print("Chat Button is Clicked Successfully") 
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/message_textview"))).send_keys("Automation_Testing")
            print("Text Send to the Text Box") 
            wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "TODO"))).click()
            print("Send Button Clicked for the Text Box")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/chat_back_btn_iv"))).click()
            print("Chat Back Button Clicked")
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/leave_room_btn"]')))
            print(f"Leave Metting Button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/leave_room_btn"]'))).click()
            print(f'Clicked Leave Metting Button Successfully')
            time.sleep(5)
            
            
       except Exception as e:   
            print(f"Join Session Button in Session Section Internal Errors: {e}")
            assert False 
    except Exception as e:
        print(f"Failed at JOIN SESSION button: {e}")
        assert False

def test_home_page_after_login():
    try:
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.supportgenie.argenie:id/navigation_bar_item_icon_view").instance(0)')))
        print("Home Button is Present")
        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.supportgenie.argenie:id/navigation_bar_item_icon_view").instance(0)'))).click()
        print("Clicked the HOME button Successfully")
        name = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/user_name"]')))
        print(f"Hey, {name.text} is Present")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_btn"]')))
        print("Join Session Button is Present")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/host_btn"]')))
        print("Create Session Button is Present")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Spinner[@resource-id="com.supportgenie.argenie:id/lang_spinner"]')))
        print("Language Changer is Present")
        network = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/network_status_text"]')))
        print(f"Network Status is Present: {network.text}")

    except Exception as e:
        print(f"Home Section Error : {e}")
        assert False

def test_join_session_after_login():
    try:
       wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_btn"]')))
       print("Join Session Button is Present")
       try :
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/join_btn"))).click()
            print('Join Session Button Clicked Successfully')
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="com.supportgenie.argenie:id/control_panel"]')))
            print("Meeting ID Control Panel is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/link_id"]'))).send_keys("000-000-000")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/btn_join_link"))).click()
            wrong_id = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/info_text"]')))
            print(f"Wrong Mettign ID input : {wrong_id.text}")
            wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.supportgenie.argenie:id/link_id"]'))).send_keys("067-159-746")
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/btn_join_link"))).click()
            print(f'Correct Metting ID input')
            time.sleep(10)
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.FrameLayout\").instance(12)")))
            print("Video of the User is Present")
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Me\")")))
            print("Video User Name is Present")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/mic_iv")))
            print("Mic Button is Present")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/audio_output_option_iv")))
            print("Audio Device Change Button is Present")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/video_iv")))
            print("Video Button is Present")
            wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/chat_lly")))
            print("Chat Button is Present")           
            wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.supportgenie.argenie:id/mic_iv"))).click()
            print("Mic Button is ON")
            wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/leave_room_btn"]')))
            print(f"Leave Metting Button is Present")
            wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/leave_room_btn"]'))).click()
            print(f'Clicked Leave Metting Button Successfully')
            wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")")))
            print("Go back Button is Present")
            time.sleep(5)
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")"))).click()
            print("Clicked GO BACK button")
            wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")"))).click()
            print("Clicked GO BACK button")
       except Exception as e:   
            print(f"Join Session Button Internal Errors: {e}")
            assert False 
    except Exception as e:
        print(f"Failed at JOIN SESSION button: {e}")
        assert False     

def test_profile_section():
    try: 
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[3]')))
        print("Profle Section Button is Present")
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[3]'))).click()
        print("Profile Section Button Clicked Successfully")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.RelativeLayout[@resource-id="com.supportgenie.argenie:id/complete_profile_rly"]')))
        print("User Profle Section Layout is Present")
        name = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/profile_name_tv"]')))
        print(f"User Profle Section Name : {name.text}")
        faq = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/faq_btn"]')))
        print(f"{faq.text} Button  is Present")
        demo = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/create_rec_btn"]')))
        print(f"{demo.text} Button is Present")
    except Exception as e:
        print(f"Failed at Profile Section: {e}")
        assert False    

def test_create_session():
    try:
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[1]')))
        print("Home Section Button is Present")
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[1]'))).click()
        print("Home Section Button Clicked Successfully")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/host_btn"]')))
        print("Create Session Button is Present")
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/host_btn"]'))).click()
        print("Create Session Button Clicked Successfully")
        time.sleep(10)
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/title_tv"]')))
        print("Session ID Title text is Present")
        code = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/link_code_tv"]')))
        print(f"Session Code Generated : {code.text}")
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.supportgenie.argenie:id/share_btn")')))
        print("Share Session ID is Present")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/title_tv"]')))
        print("Session ID Title text is Present")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_meeting_btn"]')))
        print("Join Session Button is Present")
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")")))
        print("Go back Button is Present")
        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")"))).click()
        print("Clicked GO BACK button")
    except Exception as e:
        print(f"Failed at Create SESSION button: {e}")
        assert False         

def test_home_page_after_session_creation():
    try:
        wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.supportgenie.argenie:id/navigation_bar_item_icon_view").instance(0)')))
        print("Home Button is Present")
        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.supportgenie.argenie:id/navigation_bar_item_icon_view").instance(0)'))).click()
        print("Clicked the HOME button Successfully")
        name = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/user_name"]')))
        print(f"Hey, {name.text} is Present")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_btn"]')))
        print("Join Session Button is Present")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/host_btn"]')))
        print("Create Session Button is Present")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Spinner[@resource-id="com.supportgenie.argenie:id/lang_spinner"]')))
        print("Language Changer is Present")
        network = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/network_status_text"]')))
        print(f"Network Status is Present: {network.text}")

    except Exception as e:
        print(f"Home Section Error : {e}")
        assert False

def test_profile_after_session_creation():
    try: 
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[3]')))
        print("Profle Section Button is Present")
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[3]'))).click()
        print("Profile Section Button Clicked Successfully")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.RelativeLayout[@resource-id="com.supportgenie.argenie:id/complete_profile_rly"]')))
        print("User Profle Section Layout is Present")
        name = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/profile_name_tv"]')))
        print(f"User Profle Section Name : {name.text}")
        faq = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/faq_btn"]')))
        print(f"{faq.text} Button  is Present")
        demo = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/create_rec_btn"]')))
        print(f"{demo.text} Button is Present")
    except Exception as e:
        print(f"Failed at Profile Section: {e}")
        assert False    

def test_LOG_OUT():
    try: 
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[3]')))
        print("Profle Section Button is Present")
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[3]'))).click()
        print("Profile Section Button Clicked Successfully")
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.RelativeLayout[@resource-id="com.supportgenie.argenie:id/complete_profile_rly"]')))
        print("User Profle Section Layout is Present")
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.RelativeLayout[@resource-id="com.supportgenie.argenie:id/complete_profile_rly"]'))).click()
        print("User Profle Section Layout Clicked Successfully")
        
        popup = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/dialogTitle"]')))
        print(f"Log Out POP-UP : {popup.text}")
        yes = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/positiveButton"]')))
        print(f"Log Out Option: {yes.text}")
        cancel = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/negativeButton"]')))
        print(f"Log Out option : {cancel.text}")
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/negativeButton"]'))).click()
        print("Log-out Cancelled Successfully")
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.RelativeLayout[@resource-id="com.supportgenie.argenie:id/complete_profile_rly"]'))).click()
        print("Profile Section Button Clicked Successfully")
        popup2 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/dialogTitle"]')))
        print(f"Log Out POP-UP : {popup2.text}")
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.supportgenie.argenie:id/positiveButton"]'))).click()
        print("Log-out Clicked YES Successfully")
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/login_btn")))
        print("Redirected to Login Page")
        wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Go Back\")"))).click()
        print("Clicked GO BACK button")
        
    except Exception as e:
        print(f"Failed at LOG_OUT : {e}")
        assert False 
        
def test_log_out_cross_check():
    try: 
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[1]')))
        print("Home Section Button is Present")
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[1]'))).click()
        print("Home Section Button Clicked Successfully")
        name1 = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/user_name"]')))
        if name1.text == "Guest":
            print("Log-out at Home Section was Successfull")
        else :
            print("Log-out at Home Section Failed")

        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[2]')))
        print("Session Section Button is Present")
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[2]'))).click()
        print("Session Section Button is Clicked SuccessFully")
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.supportgenie.argenie:id/login_btn")))
        print("Log-Out at Session Section was Successfull")

        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[3]')))
        print("Profile Section Button is Present")
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.supportgenie.argenie:id/navigation_bar_item_icon_view"])[3]'))).click()
        print("Profile Section Button Clicked Successfully")
        name = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.supportgenie.argenie:id/profile_name_tv"]')))
        if name.text == "Login to your Account":
            print("Log-Out at Profile Section was Successfull")    
        else:
            print("Log-out at Profile Section Failed")   
    except Exception as e:
        print(f"Failed at LOG_OUT : {e}")
        assert False     


   




  