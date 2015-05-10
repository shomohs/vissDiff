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
