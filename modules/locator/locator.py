#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Abhinav CHADHA
Module: URI locators
"""

from modules.logger.logger import logger
import requests

class locator(object):
	def __init__(self):
		self.request_formatter = lambda verb, res: "{0} on {1}".format(verb, res)
		self.request_logger = logger(1)

	def get(self, res):
		self.request_logger.info(self.request_formatter("GET", res))
		try:
			resp = requests.get(res)
		except requests.exceptions.MissingSchema:
			resp = requests.get("http://" + res)
		assert resp.status_code == 200, "Error while processing request."
		return resp
