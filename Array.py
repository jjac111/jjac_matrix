import numpy as np
from utils import utils

class Array(utils):
	'''Class for 1D numerical array manipulation. Uses numpy arrays for faster processing
		
		Attributes:
			data (numpy.array): containing the sequence of numbers
			
	'''
	
	def __init__(self, data=None):
		'''Initializer of the Array instance
			
			Args:
				data (array-like): container of initializing data
		'''
		self.data = np.array(data)
		
	def __add__(self, other):
		'''Appends the other's data to this instance data list
			
			Args:
				other (Array): another instance of Array
				
			Returns:
				new: reference a new Array instance
		'''
		 
		new_data = np.hstack([self.data, other.data])
		
		new = Array(new_data)
		
		return new
		
	def add_at_index(self, values, idx):
		'''Inserts the sequence of values at the idx position and returns it as a new Array. Elements already at position idx 
			and forward are displaced to make space for the new values.
			
			Args:
				values (iterable): numerical elements to insert to the data list
				idx (int): index at which values will be inserted
				
			Returns:
				Array: numpy array containing previous and added elements
		'''
		
		new_array = Array(self.data)
		
		#if idx is the next out-of-bound index for the contained data, the values are appended
		if(idx == len(new_array)):
			return new_array.append(values)
		else:
			return new_array[:idx-1].append(values).append(new_array[idx:])
			
	def remove_value(self, value):
		'''Removes all ocurrences of the specified value from the data, if it exists, and shrinks the data array
			
			Args:
				value (numerical): the value to be looked for in the data
				
			Returns:
				Array: Another instance of Array with the value removed
				
		'''
		
		new_array = Array(self.data)
		
		if not value in self.data:
			return self
		
		else:
			removed_idices = new_array.find(value)
			
			for removed_idx in removed_idices:
				if(removed_idx == 0):	#if its the first element
					new_array.data = new_array.data[1:]
					
				elif(removed_idx == len(new_array.data)-1):	#if its the last element
					new_array.data = new_array.data[:-1]
					
				else:	#if element is in between
					new_array.data = np.hstack([new_array.data[:removed_idx], new_array.data[removed_idx+1:]])
			
			return new_array
		
	def remove_at(self, idx):
		'''Removes the specified value from the data, if it exists, and shrinks the data array
			
			Args:
				idx (int): the index of the value to be looked for and removed from the data
				
			Returns:
				Array: Another instance of Array with the value removed, or None if the index is out of bounds
				
		'''
		
		removed = None
		new_array = Array(self.data)
		
		try:
			removed = new_array.data[idx]
		except:
			return None
		
		if(idx == 0):	#if its the first element
			new_array.data = new_array.data[1:]
				
		elif(idx == len(new_array.data)-1):	#if its the last element
			new_array.data = new_array.data[:-1]
				
		else:	#if element is in between
			new_array.data = np.hstack([new_array.data[:idx] , new_array.data[idx+1:]])
			
		return new_array
	
	def find(self, value):
		'''Finds the given value and returns it's position in the matrix.
		
			Args: 
				value (numerical): value to be looked for inside the data
				
			Returns:
				list (int): the positional indices of all ocurences of the value, or None if no ocurrence was found
		'''
		if not value in self.data:
			return None
		
		indices = [i for i in range(len(self.data)) if self.data[i] == value]
		
		return indices