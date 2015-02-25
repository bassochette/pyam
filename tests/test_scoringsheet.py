#!/usr/bin/python
# -*- coding : utf-8 -*-

from nose.tools import *
from yamexcept import *
from scoresheet import *


s = ScoringSheet()

def test_ScoringSheet():
	s = ScoringSheet()

	assert_equal(None, s._straight['Yam'])
	assert_equal(None, s._free['Brelan'])

	# missing : attributing things with a yam becaus yam is has the secret power to be converted in anything at is maximum value except for min and max. They must be mulptiple of 5
	
def test_up():
	# up
	s.up('1', [1,1,1,1,1])
	assert_equal( [5, 4] , s.up('2', [1,1,1,2,2])) # ok
	# assert_raise( IntervalError , s.up('5', [5,5,5,5,5])) # bad interval
	# assert_raise( AlreadyAttributed , s.up('2', [2,3,2,2,2])) # Already done
	assert_equal( [5, 4, 0] , s.up('cross')) # cross
	
	s._up = [1, 2, 3, 4, 5, 6, 15]
	# assert_raise( MinOrMaxError , s.up('Maxi', [1,2,1,1,1]))	# set max with max < min
	s._up = [1,2,3,4,5,6, 10]
	assert_equal([1,2,3,4,5,6,10,15], s.up('Maxi', [3,3,4,2,3]))	# set max with max > min
	s._up = [1, 2, 3, 4, 5, 6, 10]

	# assert_raise( MinOrMaxError, s.up('Maxi', [1,2,3,2,2]))	# set max with max == min

	# down
def test_down():
	s.down('Yam', [1,1,1,1,1])

	assert_equal( [70, 60] , s.down('Suite')) # ok
	# assert_raise( IntervalError , s.down('Brelan')) # bad interval
	# assert_raise( AlreadyAttributed, s.down('Suite')) # already done\
	assert_equal( [70, 60, 0] , s.down('cross')) # cross

	s._down = [70, 60, 50, 0, 30, 0, 15]
	assert_equal([70, 60, 50, 0, 30, 0, 15, 10], s.down('Mini', [1,2,3,2,2]))	# set min with max > min
	s._down = [70, 60, 50, 0, 30, 0, 15]
	# assert_raise( MinOrMaxError, s.down('Mini', [6,5,6,5,6]))	# set min with min > max
	s._down = [70, 60, 50, 0, 30, 0, 15, 10, 36]
	assert_equal([70, 60, 50, 0, 30, 0, 15, 10, 36, 20], s.down('5', [5,5,5,5,6]))
	# assert_raise( MinOrMaxError, s.down('Mini', [3,2,4,3,3]))	# set min with min == max
	
	

def test_free():	

	# free
	s.free('Yam', [6,6,6,6,6])
	s.free('6', [6,6,6,6,6])
	assert_equal({'Yam': 70, '6' : 36, 'Brelan': 30}, s.free('Brelan', [])) # ok
	# assert_raise( AlreadyAttributed, s.free('Yam', [1,1,1,1,1])) # already done
	assert_equal( {'Yam': 70, '6' : 36, 'Brelan': 30, 'Mini': 0} , s.free('cross', [4,2,5,6,1], 'mini')) # cross
	# assert_raise( AlreadyAttributed, s.free('cross', [1,2,3,4,6], 'mini')) # cross already done
	s._free = { 'Mini': 10}	

	
	# assert_raise( MinOrMaxError, s.free('Maxi', [1,2,1,1,2])) 		# set max with min > max
	s._free = { 'Mini' : 10}
	assert_equal({ 'Mini' : 10, 'Maxi': 15}, s.free('Maxi', [3,4,2,4,2]))		# set max with max > min
	s._free = { 'Maxi': 36}
	assert_equal( {'Maxi': 36, 'Mini': 15}, s.free('Mini', [3,4,2,5,1]))		# set min with max > min
	s._free = { 'Maxi': 15}
	# assert_raise( MinOrMaxError, s.free('Mini', [6,6,5,4,6]))		# set min with min > max
	# assert_raise( MinOrMaxError, s.free('Mini', [3,4,2,5,1]))		# set min with min == max
	s._free = { 'Mini': 15}
	# assert_raise (MinOrMaxError, s.free('Maxi', [6,3,1,1,1]))		# set max with max == min

	

def test_straight():	

	# straight
	s.straight('Yam', [6,6,6,6,6])
	s.straight('6', [6,6,6,6,6])
	assert_equal({'Yam': 70, '6' : 36, 'Brelan': 30}, s.straight('Brelan', [])) # ok
	# assert_raise( AlreadyAttributed, s.free('Yam', [1,1,1,1,1])) # already done
	assert_equal( {'Yam': 70, '6' : 36, 'Brelan': 30, 'mini': 0} , s.straight('cross', [4,2,5,6,1], 'mini')) # cross
	# assert_raise( AlreadyAttributed, s.straight('cross', [1,2,3,4,6], 'mini')) # cross already done
 	s._straight = { 'Mini': 10}		
 	
 	# assert_raise( MinOrMaxError, s.straight('Maxi', [1,2,1,1,2])) 		# set max with min > max
 	s._straight = { 'Mini' : 10}
 	assert_equal({ 'Mini' : 10, 'Maxi': 15}, s.straight('Maxi', [3,4,2,4,2]))		# set max with max > min
 	s._straight = { 'Maxi': 36}
 	assert_equal( {'Maxi': 36, 'Mini': 15}, s.straight('Mini', [3,4,2,5,1]))		# set min with max > min
 	s._straight = { 'Maxi': 15}
 	# assert_raise( MinOrMaxError, s.straight('Mini', [6,6,5,4,6]))		# set min with min > max
 	# assert_raise( MinOrMaxError, s.straight('Mini', [3,4,2,5,1]))		# set min with min == max
 	s._straight = { 'Mini': 15}
 	# assert_raise (MinOrMaxError, s.straight('Maxi', [6,3,1,1,1]))	
