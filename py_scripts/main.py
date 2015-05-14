#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Abhinav CHADHA
Module: Visual Diff Main
"""

from modules.locator.Locator import Locator
from modules.logger.Logger import Logger
import json
import os


class vissDiff(object):
	def __init__(self):
		self.diffLogger = Logger(1)

	def domCompare(self, uri1, uri2):
		"""
		Simple DOM comparison. Would check for coherence in the DOM level.
		External CSS are not compared. Scripts are overlooked.


		Args:
			uri1: The first uri
			uri2: The second uri

		Returns:
			Unmatched lines

		Raises:
			None
		"""
		resp1 = Locator().get(uri1)
		resp2 = Locator().get(uri2)