#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Abhinav CHADHA
Module: logging module
"""

import logging

FORMAT = "%(asctime)s %(process)s %(thread)s: %(message)s"

class logger(object):
	def __init__(self, level=1, format=FORMAT):
		levels = {
		0: logging.DEBUG,
		1: logging.INFO,
		2: logging.WARNING,
		3: logging.ERROR,
		4: logging.critical
		}
		return logging.basicConfig(level=levels[level], format=FORMAT)

	def debug(self, debug_message):
		"""
		Logs the messages with levels DEBUG and upwards

		Args:
			debug_message: The message to be logged

		Returns:
			The logged message

		Raises:
			None
		"""
		return logging.debug(debug_message)

	def info(self, info_message):
		"""
		Logs the messages with levels INFO and upwards

		Args:
			info_message: The message to be logged

		Returns:
			The logged message

		Raises:
			None
		"""
		return logging.info(info_message)

	def warning(self, warning_message):
		"""
		Logs the messages with levels WARNING and upwards

		Args:
			warning_message: The message to be logged

		Returns:
			The logged message

		Raises:
			None
		"""
		return logging.warning(warning_message)

	def error(self, error_message):
		"""
		Logs the messages with levels ERROR and upwards

		Args:
			error_message: The message to be logged

		Returns:
			The logged message

		Raises:
			None
		"""
		return logging.error(error_message)

	def critical(self, critical_message):
		"""
		Logs the messages with levels CRITICAL and upwards

		Args:
			critical_message: The message to be logged

		Returns:
			The logged message

		Raises:
			None
		"""
		return logging.critical(critical_message)
