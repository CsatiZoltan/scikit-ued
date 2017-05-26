# -*- coding: utf-8 -*-
"""
Plotting utilities, including color manipulation. This is especially useful when
plotting time-series.
"""
from collections import Iterable
from colorsys import hsv_to_rgb
from functools import partial

def spectrum_colors(num_colors):
	"""
	Generates a set of RGB colors corresponding to the visible spectrum (i.e. the rainbox). 
	These colors can be used by Matplotlib, PyQtGraph, Qt, and other plotting/graphics libraries.
    
	Parameters
	----------
	num_colors : int or iterable
		Number of colors to generate. Alternatively, if `num_colors` is an iterable, 
		then the number of colors is deduced with specific spacing.
    
	Yields
	------
	color : (R,G,B) tuple.
		R, G, B values in a tuple, from 0.0 to 1.0.
	"""
	if isinstance(num_colors, int):
		# Hue values from 0 to 1 with equal spacing
		hue_values = reversed([i/num_colors for i in range(num_colors)])

	elif isinstance(num_colors, Iterable):
		num_colors = list(num_colors)
		
		# Scale iterable to be between 0 and 1
		mi = min(num_colors)
		ma = max(num_colors) - mi
		hue_values = reversed([(n - mi)/ma for n in num_colors])

	# Scale so that the maximum is 'purple' (hue = 0.8)
	# otherwise plots don't look as good
	yield from map(lambda hue: hsv_to_rgb(0.8*hue, s = 0.7, v = 0.9), hue_values)