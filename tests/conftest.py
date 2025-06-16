import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Define the fixture for Appium driver setup and teardown
@pytest.fixture(scope="session")
def driver():
    # Load capabilities from a JSON file
    capabilities = load_capabilities_from_json("config/android_capabilities.json")
    
    # Initialize Appium options with the capabilities
    options = UiAutomator2Options()
    options.load_capabilities(capabilities)
    
    # Initialize the driver
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    
    # Give the driver some time to initialize and ensure it's ready for tests
    driver.implicitly_wait(10)
    
    yield driver  # This allows the test to use the driver

    # Quit the driver after the test finishes
    driver.quit()

# Helper function to load capabilities from JSON file
def load_capabilities_from_json(file_path):
    """
    Loads desired capabilities from a JSON file.
    """
    with open(file_path, 'r') as file:
        capabilities = json.load(file)
    return capabilities

