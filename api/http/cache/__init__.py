"""Module contains API cache"""
from cachy import CacheManager
from api.settings import SETTINGS

# Creating instance
CACHE = CacheManager(**SETTINGS['cache'])
