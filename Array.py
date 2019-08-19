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
	
	def __contains__(self, value):
		'''Implementation of 'in' keyword
		
			Args: value to check within data
			
			Returns: 
				True or False, whether the value is contained the in the data 
		'''
		return value in self.data
	
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
			
	def find(self, value):
		'''Finds the given value and returns it's position in the array.
		
			Args: 
				value (numerical): value to be looked for inside the data
				
			Returns:
				list (int): the positional indices of all ocurences of the value, or None if no ocurrence was found
		'''
		if not value in self.data:
			return None
		
		return self.data.where(arr == value).tolist()
	
	def is_empty(self):
		'''Checks wether the data container is empty or not
		
			Args:
				none
			
			Returns:
				boolean: True if the data is empty or Fal
		'''
		
		if len(self.data) == 0:
			return True
		else:
			return False
		
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
	
	
	def sum(self):
		'''Calculates the sum of all elements in the array.
			Args:
				none
				
			Returns:
				float: the sum of all the elements in the array, or None if the array is empty.
		'''
		
		if self.is_empty():
			return None
		else:
			return self.data.sum()
	
	def mean(self):
		'''Calculates the mean of all elements in the array.
			Args:
				none
				
			Returns:
				float: the mean of all the elements in the array, or None if the array is empty.
		'''
		
		if self.is_empty():
			return None
		else:
			return self.data.mean()