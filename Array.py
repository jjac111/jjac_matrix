import numpy as np
import .utils

class Array(utils):
	'''Class for 1D numerical array manipulation. Uses numpy arrays for faster processing
		
		Attributes:
			data (numpy.array): containing the sequence of numbers
			
	'''
	
	def __init__(self, data):
		'''Initializer of the Array instance
			
			Args:
				data (array-like): container of initializing data
		'''
		self.data = np.array(data)
		
	def __add__(self, values):
		'''Appends the values to the data list
			
			Args:
				values (iterable): numerical elements to add to the data list
				
			Returns:
				self: reference to the calling object
		'''
		
		self.data = self.data.append(values)
		
		return self
		
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
			return new_array[:idx-1].append(values).append(new_array[idx:])
			
	def remove_value(self, value):
		'''Removes the specified value from the data, if it exists, and shrinks the data array
			
			Args:
				value (numerical): the value to be looked for in the data
				
			Returns:
				float: the value found and removed in the data, or None if the value was not found
				
		'''
		
		if not value in self.data:
			return None
		else:
			removed = value
			removed_idx = self.find(value)
			
			if(removed_idx == 0):	#if its the first element
				self.data = self.data[1:]
				
			elif(removed_idx == len(self.data)-1):	#if its the last element
				self.data = self.data[:-1]
				
			else:	#if element is in between
				self.data = self.data[:removed_idx] + self.data[removed_idx+1:]
			
	def remove_at(self, idx):
		'''Removes the specified value from the data, if it exists, and shrinks the data array
			
			Args:
				idx (int): the index of the value to be looked for and removed from the data
				
			Returns:
				float: the value found and removed in the data, or None if the index is out of bounds
				
		'''
		
		removed = None
		
		try:
			removed = self.data[idx]
		except:
			return None
		
		if(idx == 0):	#if its the first element
				self.data = self.data[1:]
				
			elif(idx == len(self.data)-1):	#if its the last element
				self.data = self.data[:-1]
				
			else:	#if element is in between
				self.data = self.data[:idx] + self.data[idx+1:]
	