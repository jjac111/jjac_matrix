import numpy as np

class Array:
	'''Class for numerical array manipulation. Uses numpy arrays for faster processing
		
		Attributes:
			data (list): list containing the sequence of numbers
			
	'''
	
	def __init__(self, data):
		
		self.data = np.array(data)
		
	def __add__(self, values):
		'''Appends the values to the data list
			
			Args:
				values (iterable): numerical elements to add to the data list
				
			Returns:
				Array: numpy array containing previous and added elements
		'''
		
		return self.data.append(values)
		
	def __len__(self):
		'''Returns the size of this Array
		'''
		
		return len(self.data)
		
	def add_at_index(self, values, idx):
		'''Inserts the sequence of values at the idx position and returns it as a new Array. Elements already at position idx 
			and forward are displaced to make space for the new values.
			
			Args:
				values (iterable): numerical elements to insert to the data list
				idx (int): index at which values will be inserted
				
			Returns:
				Array: numpy array containing previous and added elements
		'''
		
		new_array = self
		
		#if idx is the next out-of-bound index for the contained data, the values are appended
		if(idx == len(new_array)):
			return new_array.append(values)
		else:
			return new_array[:idx-1].append(values).append(idx:)
		