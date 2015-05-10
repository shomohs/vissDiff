"""
Author: Abhinav CHADHA
Module: Visual Diff Main
"""

import os
import requests
import json
import logging

class infoLog(object):
	def __init__(self, level=1):
		levels = {
		0: logging.DEBUG,
		1: logging.INFO,
		2: logging.WARNING,
		3: loggin.ERROR
		}