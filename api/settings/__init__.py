"""
Module contains application settings
"""
import json
from logging import getLogger
from pathlib import Path

SETTINGS: dict = {}
logger = getLogger(__name__)

# Load settings into SETTINGS
for file in Path('api/settings/store').absolute().iterdir():
    try:
        with open(file, 'r') as config:
            SETTINGS[str(file.name).split('.')[0].upper()] = json.load(config)
    except json.decoder.JSONDecodeError:
        logger.warning(f'Could not decode: {file.name}')
