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

def element_presence_by_xpath(driver, xpath, timeout=10):
    try:
        # Wait for the element to be present within the specified timeout
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((AppiumBy.XPATH, xpath))
        )
        return True  # Element found
    except Exception as e:
        return False  # Element not found

def element_clicked_by_xpath(driver, xpath, timeout=10):
    try:
        # Wait for the element to be present within the specified timeout
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, xpath))
        ).click()
        return True  # Element found
    except Exception as e:
        return False  # Element not found    

def element_presence_by_accessibility(driver, accessibility, timeout=10):
    try:
        # Wait for the element to be present within the specified timeout
        WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((AppiumBy.ACCESSIBILITY_ID, accessibility))
        )
        return True  # Element found
    except Exception as e:
        return False  # Element not found        

def element_clicked_by_accessibility(driver, accessibility, timeout=10):
    try:
        # Wait for the element to be present within the specified timeout
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, accessibility))
        ).click()
        return True  # Element found
    except Exception as e:
        return False  # Element not found        

def perform_swipe(driver,start_x, start_y, end_x, end_y):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    
def element_clicked_by_uiautomator(driver, uiautomator, timeout=10):
    try:
        # Wait for the element to be present within the specified timeout
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, uiautomator))
        ).click()
        return True  # Element found
    except Exception as e:
        return False  # Element not found          
    
def element_clicked_by_id(driver, id, timeout=10):
    try:
        # Wait for the element to be present within the specified timeout
        WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((AppiumBy.ID, id ))
        ).click()
        return True  # Element found
    except Exception as e:
        return False  # Element not found     

def element_presence_by_uiautomator(driver, uiautomator, timeout=10):
    try:
        # Wait for the element to be present within the specified timeout
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, uiautomator))
        )
        return True  # Element found
    except Exception as e:
        return False  # Element not found
    
def element_presence_by_id(driver, id, timeout=10):
    try:
        # Wait for the element to be present within the specified timeout
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((AppiumBy.ID, id ))
        )
        return True  # Element found
    except Exception as e:
        return False  # Element not found  