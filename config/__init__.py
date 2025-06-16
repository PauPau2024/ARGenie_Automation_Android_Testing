# config/__init__.py

import json

def load_config(file_path):
    """Load a JSON configuration file."""
    with open(file_path, 'r') as f:
        return json.load(f)

appium_config = load_config("config/appium_config.json")
ios_capabilities = load_config("config/android_capabilities.json")
env_config = load_config("config/env_config.json")


