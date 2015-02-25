from nose.tools import *
import yam as y
from yamexcept import * 
from scoresheet import *
from player import *

def test_throw_dices():
	assert_equal(5, len(throwDices(5)))
	assert_equal(4, len(throwDices(4)))
	assert_equal(3, len(throwDices(3)))

def test_player():
	p = Player()

	assert_equal( type(p.turn()).__name__ , 'function')


def test_scoring():
	game = y.Game()
	# 2 pair seche
	assert_equal({'sec': True, 'pair': 2}, game.score(([1,1,2,2,3], 1)))
	# Brelan
	assert_equal({'pair':1, 'brelan':1}, game.score(([1,1,1,2,3], 2)))
	# Full
	assert_equal({'full': 1, 'brelan': 1, 'pair': 2}, game.score(([1,1,1,2,2],2)))
	# carre
	assert_equal({'full': 1, 'carre': 1, 'brelan': 1, 'pair': 2}, game.score(([1,1,1,1,2],3)))
	# Yam
	assert_equal({'sec': True, 'carre': 1, 'yam': 1, 'brelan': 1, 'pair': 2}, game.score(([1,1,1,1,1],1)))
	#suite
	assert_equal({'suite': 1},game.score(([1,2,3,4,5],2)))
	#rien
	assert_equal({},game.score(([1,3,4,5,6],3)))