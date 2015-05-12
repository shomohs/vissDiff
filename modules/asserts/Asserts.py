#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Abhinav CHADHA
Module: Custom assertions
"""


class Asserts(object):
	def __init__(self):
		pass

	@classmethod
	def assert_equals(cls, expected, actual, error="Values Unequal"):
		"""
		Asserts if two values are equal

		Args:
			expected: The expected value
			actual: The actual value
			error: The error message to be displayed

		Returns:
			None

		Raises:
			AssertionError
		"""
		try:
			assert expected == actual
		except AssertionError:
			print "{0}\nExpected: {1}\nActual: {2}".format(error, expected, actual)
			raise 

	@classmethod
	def assert_type_equals(cls, expected, actual, error="Type Unequal"):
		try:
			assert type(expected) == type(actual)
		except AssertionError:
			print "{0}\nExpected: {1}\nActual: {2}".format(error, type(expected).__name__, type(actual).__name__)
			raise 
