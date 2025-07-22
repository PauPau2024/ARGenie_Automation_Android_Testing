
# Android Automation Testing Framework

## Overview

This project provides an automated testing framework for Android applications using **Appium** and **Python (pytest)**. It allows developers and QA teams to write and run UI tests across real devices or emulators to ensure application quality.

## Tech Stack

* **Language:** Python 3.x
* **Framework:** Pytest
* **Automation Tool:** Appium
* **Device Support:** Android Emulators, Physical Devices, AWS Device Farm 
* **Dependency Manager:** pip

## Project Structure

```
APPPIUM-ANDROID-TEST-AUTOMATION/
├── config/                     # Configuration files (e.g., Appium capabilities)
├── drivers/                    # Driver setup and initialization
│   └── android_driver.py
├── driver_utils.py             # Utility functions for driver management
├── reports/                    # Test execution reports
│   └── logs/
├── resources/                  # Test data and assets
│   └── app/                    # APKs or app references
│   └── screenshots/            # Screenshots captured during test runs
├── tests/                      # Organized test cases
│   ├── test_01_start_up.py
│   ├── test_02_intro_slides.py
│   ├── ...
│   └── test_20_logout.py
├── utils/                      # Helper modules and utilities
├── conftest.py                 # Pytest fixture definitions
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
├── pytest.ini                  # Pytest configuration
```

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/PauPau2024/ARGenie_Automation_IOS_Testing.git
   cd android-automation
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Appium**

   * Via npm:

     ```bash
     npm install -g appium
     ```
   * Start the Appium server:

     ```bash
     appium
     ```

4. **Set up Android Environment**

   * Android Studio with SDK tools
   * Enable USB debugging on your Android device or emulator

5. **Verify setup**

   ```bash
   adb devices
   ```

## Running the Tests

### Locally:

```bash
pytest -v tests/ --html=reports/report.html
```

## Test Cases Explaination

| **Test File**                                 | **Purpose / Description**                                                                                     |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `test_01_start_up.py`                         | Verifies that the app starts correctly and the splash or launch screen behaves as expected.                   |
| `test_02_intro_slides.py`                     | Tests the introduction/onboarding slides shown to the user during the first app launch.                       |
| `test_03_get_started_button.py`               | Checks the functionality of the "Get Started" button, ensuring it navigates as expected.                      |
| `test_04_home_without_login.py`               | Verifies access control: attempts to access the home screen without login and ensures redirection or warning. |
| `test_05_session_without_login.py`            | Tests whether starting a session without login is blocked or redirected correctly.                            |
| `test_06_profile_without_login.py`            | Ensures that users cannot access or edit the profile screen without logging in.                               |
| `test_07_login_on_session_page.py`            | Tests login from the session page context (i.e., clicking “login” when trying to start a session).            |
| `test_08_join_session_button.py`              | Validates that the “Join Session” button works and navigates to the correct screen.                           |
| `test_09_join_session_without_login.py`       | Ensures users cannot join sessions unless authenticated.                                                      |
| `test_10_create_session_button.py`            | Tests the “Create Session” button and whether it allows access only after login.                              |
| `test_11_home_page_after_login.py`            | Confirms that home page elements load correctly after a successful login.                                     |
| `test_12_join_session_after_login.py`         | Ensures a logged-in user can successfully join an existing session.                                           |
| `test_13_create_session_after_login.py`       | Verifies that logged-in users can create new sessions properly.                                               |
| `test_14_join_the_created_session.py`         | Simulates joining a session that was just created and checks correctness.                                     |
| `test_15_session_section_after_login.py`      | Tests the display and interactivity of the “Session” section after login.                                     |
| `test_16_join_session_from_session_screen.py` | Tests in-app navigation and session joining from within the session list/screen.                              |
| `test_17_profile_section_after_login.py`      | Checks that profile settings, info, or actions are visible after login.                                       |
| `test_18_AR_demo.py`                          | Possibly a demo test for AR (Augmented Reality) functionality, if supported by the app.                       |
| `test_19_FAQ.py`                              | Verifies that the FAQ/help section loads correctly and is accessible.                                         |
| `test_20_logout.py`                           | Tests the logout functionality and ensures the session ends, redirecting to login/home.                       |


## Reporting

The Reports of the test cases on the devices will be stored within the reports/report.html section within the files.
