"""
Author: Abhinav CHADHA
Module: Visual Diff Main
"""

import os
import requests
import json
import logging

FORMAT = "%(asctime)s %(process)s %(thread)s: %(message)s"

class logObject(object):
	def __init__(self, level=1, format=FORMAT):
		levels = {
		0: logging.DEBUG,
		1: logging.INFO,
		2: logging.WARNING,
		3: logging.ERROR,
		4: logging.critical
		}
		return logging.basicConfig(level=levels[level], format=FORMAT)

	def info(self, info_message):
		return logging.info(info_message)

	def debug(self, debug_message):
		return logging.debug(debug_message)

	def warning(self, warning_message):
		return logging.warning(warning_message)

	def error(self, error_message):
		return logging.error(error_message)

	def critical(self, critical_message):
		return logging.critical(critical_message)

class getResources(object):
	def __init__(self):
		self.request_formatter = lambda verb, res: "{0} on {1}".format(verb, res)
		self.request_logger = logObject(1)

	def get(self, res):
		self.request_logger.info(self.request_formatter("GET", res))
		try:
			requests.get(res)
		except requests.exceptions.MissingSchema:
			requests.get("http://" + res)

