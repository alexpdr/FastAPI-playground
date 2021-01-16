"""
Module contains application settings
"""
import json
from pathlib import Path

SETTINGS: dict = {}

# Load settings into SETTINGS
for file in Path('api/settings/store').absolute().iterdir():
    with open(file, 'r') as config:
        SETTINGS[str(file.name).split('.')[0].upper()] = json.load(config)
