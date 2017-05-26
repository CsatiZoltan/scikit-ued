# -*- coding: utf-8 -*-
import unittest
from .. import spectrum_colors

class TestSpectrumColors(unittest.TestCase):

	def test_on_ints(self):
		""" Test spectrum_colors on an int """
		colors = spectrum_colors(10)
		self.assertEqual(len(list(colors)), 10)

	def test_on_sized_iterable(self):
		""" Test on iterable that has a __len__ attribute: list, tuple, etc. """
		colors = spectrum_colors( [1,2,3,4,5] )
		self.assertEqual(len(list(colors)), 5)

	def test_on_unsized_iterable(self):
		""" Test spectrum_colors on unsized_iterable (e.g. generator) """
		colors = spectrum_colors( range(0, 10) )
		self.assertEqual(len(list(colors)), 10)

if __name__ == '__main__':
	unittest.main()