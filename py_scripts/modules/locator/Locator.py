#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Abhinav CHADHA
Module: URI locators
"""

from modules.logger.Logger import Logger
import requests

class Locator(object):
	def __init__(self):
		self.request_formatter = lambda verb, res: "{0} on {1}".format(verb, res)
		self.request_logger = Logger(1)

	def get(self, res):
		"""
		Use the GET verb on a URI resource
		
		Args:
			res : The  resource on which the action is performed

		Returns:
			The result of the action on the resource

		Raises:
			Exception in case the status code of the response is not 200
		"""
		self.request_logger.info(self.request_formatter("GET", res))
		try:
			resp = requests.get(res)
		except requests.exceptions.MissingSchema:
			self.request_logger.debug("Missing Schema, adding http to the uri")
			resp = requests.get("http://" + res)
		request_logger.debug("Checking for response status code")
		assert resp.status_code == 200, "Error while processing request."
		return resp
