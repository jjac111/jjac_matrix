class utils:
	'''Class for shared utility functions
	'''
	def count_equal_to(self, value):
		'''Count all numbers equal to the specified value
			Args:
				value (numerical): the value to compare with all the elements in the data
				
			Returns:
				int: number of equal ocurrences
		'''
		
		return len(self.data[self.data == value])
		
	def count_lower_than(self, value):
		'''Count all numbers lower than to the specified value
			Args:
				value (numerical): the value to compare with all the elements in the data
				
			Returns:
				tuple (int, list): [0]:number of ocurrences, [1]:list containing all ocurrences in the data
		'''
		
		count = len(self.data[self.data < value])
		list = self.data[self.data < value].tolist()
		
		return (count, list)
	
	def count_higher_than(self, value):
		'''Count all numbers higher than the specified value
			Args:
				value (numerical): the value to compare with all the elements in the data
				
			Returns:
				tuple (int, list): [0]:number of ocurrences, [1]:list containing all ocurrences in the data
		'''
		
		count = len(self.data[self.data > value])
		list = self.data[self.data > value].tolist()
		
		return (count, list)
		
	def sort(self):
		'''Sort the data container in-place

			Args:
				none
			
			Returns:
				a reference to the calling object with sorted data
		'''
		
		self.data.sort()
		
		return self
		
	def sum(self):
		'''Calculates the sum of all elements in the matrix.
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
		'''Calculates the mean of all elements in the matrix.
			Args:
				none
				
			Returns:
				float: the mean of all the elements in the array, or None if the array is empty.
		'''
		
		if self.is_empty():
			return None
		else:
			return self.data.mean()
			
	def find(self, value):
		'''Finds the given value and returns it's position in the matrix.
		
			Args: 
				value (numerical): value to be looked for inside the data
				
			Returns:
				list (int): the positional indices of all ocurences of the value, or None if no ocurrence was found
		'''
		if not value in self.data:
			return None
		
		return self.data.where(arr == value).tolist()
	
	def __len__(self):
		'''Returns the size of this Matrix
		'''
		
		return len(self.data)
	
	def __str__(self):
		'''String representation of the Array object
		
			Args:
				none
			Returns:
				string: printable representation of this object
		'''
		return str(self.data)
			
	def __contains__(self, value):
		'''Implementation of 'in' keyword
		
			Args: value to check within data
			
			Returns: 
				True or False, whether the value is contained the in the data 
		'''
		return value in self.data
	
	def is_empty(self):
		'''Checks wether the data container is empty or not
		
			Args:
				none
			
			Returns:
				boolean: True if the data is empty or False otherwise
		'''
		
		return len(self.data) == 0
		