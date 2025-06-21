from drivers.driver_utils import *
from utils.meeting_id import *
from utils.annotation import *

def test_join_session_from_session_section(driver):
    assert element_presence_by_xpath(driver, '(//android.widget.LinearLayout[@resource-id="com.supportgenie.argenie:id/session_card"])[1]'), "Failed to Find the 'Session Card'"    
    assert element_presence_by_xpath(driver, '(//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_btn"])[1]'), "Failed to Find the 'Join Session of the 1st Session'"
    assert element_clicked_by_xpath(driver, '(//android.widget.Button[@resource-id="com.supportgenie.argenie:id/join_btn"])[1]'), "Failed to Click the 'Join Session of the 1st Session'"

def test_dynamic_ui_elements_of_meeting(driver):
     assert element_presence_by_uiautomator(driver,"new UiSelector().className(\"android.widget.FrameLayout\").instance(12)"), "Failed to Find the Video of the User"
     assert element_presence_by_uiautomator(driver, "new UiSelector().text(\"Me\")" ), "Failed to Find the Video Username of the User"
     assert element_presence_by_id(driver,"com.supportgenie.argenie:id/mic_iv"), "Failed to find the 'Mic' Button"     
     assert element_presence_by_id(driver,"com.supportgenie.argenie:id/audio_output_option_iv"), "Failed to find the 'Audio Output' Button" 
     assert element_presence_by_id(driver,"com.supportgenie.argenie:id/video_iv"), "Failed to find the 'Video' Button" 
     assert element_presence_by_id(driver,"com.supportgenie.argenie:id/chat_lly"), "Failed to find the 'Chat' Button"                

def test_turn_on_the_mic(driver):
     assert element_clicked_by_id(driver,"com.supportgenie.argenie:id/mic_iv"), "Failed to Click the 'Mic' Button"     

def test_turn_on_the_video(driver):
     assert element_clicked_by_id(driver,"com.supportgenie.argenie:id/video_iv"), "Failed to Click the 'Video' Button" 
     time.sleep(10)

def no_test_ar_annotation_before_login(driver):
    wait = WebDriverWait(driver, timeout=10)
    try:
        annotation_arrow_flow(wait)
        annotation_draw_flow(wait)
        annotation_circle_flow(wait)
        annotation_text_flow(wait)
        annotation_colour_flow(wait, perform_swipe)
        annotation_arrow_direction_flow(wait)
        remove_anchor(wait)
        go_back_and_chat_flow(wait)
        leave_meeting_flow(wait)
    except Exception as e:
        print(f"[ERROR] Annotation Test Flow Failed: {e}")
        assert False

