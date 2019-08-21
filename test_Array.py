import numpy as np
from Array import Array
import pytest

number_list_a = [6,2,5,3,4,8,7,9,7,1]
number_list_b = [3,8,5,1,7,4,9,2,0,2]
number_list_c = number_list_a + number_list_b

array_a = Array(number_list_a)
array_b = Array(number_list_b)
array_c = Array(number_list_c)

def test___eq__():
	assert not array_a == array_b
	assert array_b == Array(number_list_b)

def test___add__():
	assert array_a + array_b == Array(number_list_c)

def test___len__():
	assert len(array_a) == 10
	assert len(array_c) == 20
	
def test___contains__():
	assert 7 in array_a
	assert not 10 in array_c

def test_find():
	assert array_a.find(7) == [6,8]
	assert array_b.find(3) == [0]
	assert array_c.find(7) == [6,8,14]

def test_count_equal_than():
	assert array_a.count_equal_to(7) == 2
	assert array_a.count_equal_to(9) == 1
	assert array_c.count_equal_to(0) == 1
	
def test_count_lower_than():
	assert array_a.count_lower_than(7)[0] == 6
	assert array_a.count_lower_than(9)[0] == 9
	assert array_c.count_lower_than(0)[0] == 0
	
def test_count_higher_than():
	assert array_a.count_higher_than(7)[0] == 2
	assert array_a.count_higher_than(9)[0] == 0
	assert array_c.count_higher_than(0)[0] == 19
	
def test_is_empty():
	assert not array_a.is_empty()
	assert Array([]).is_empty()

def test_remove_value():
	assert array_a.remove_value(4) == Array([6,2,5,3,8,7,9,7,1])
	assert array_a.remove_value(10) == Array([6,2,5,3,4,8,7,9,7,1])
	assert len(array_c.remove_value(7)) == 17
	
def test_remove_at():
	assert array_a.remove_at(3) == Array([6,2,5,4,8,7,9,7,1])
	assert array_b.remove_at(9) == Array([3,8,5,1,7,4,9,2,0])
	assert array_c.remove_at(20) == None