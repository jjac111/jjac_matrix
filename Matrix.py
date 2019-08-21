import numpy as np
from utils import utils

class Matrix(utils):
	'''Class for 2D numerical array manipulation. Uses numpy arrays for faster processing
		
		Attributes:
			data (numpy.ndarray): containing the two-dimentional sequence of numbers
			
	'''
	
	def __init__(self, data, shape=None):
		'''Initializer of the Array instance
			
			Args:
				data (array-like): container of initializing data. Takes the shape specified by the shape kwarg if data is non-bidimentional
				shape (tuple): shape of the matrix, if specified. Must have the form (m, n) for m rows and n columns
		'''
		if shape:
			self.data = np.ndarray(data, shape)
		else:
			self.data = np.ndarray(data, data.shape)
		
	def __add__(self, values):
		'''Concatenates the values to the data container. 
			
			Args:
				values (iterable): numerical elements to add to the data container
				
			Returns:
				self: reference to the calling object
		'''
		
		pass
	
	def remove_value(self, value):
		pass
			
	def remove_at(self, idx):
		pass
	
	
			
	
	