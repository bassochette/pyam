#!/usr/bin/python

import random
from sys import argv
import yamexcept
import player
import scoresheet

script = argv[0]
players = argv[1:]
print players

class Game(object):
	
	players = []
	def __init__(self):
		self.round = 0
		self.on = False
	
	def add_player(self, player):
		self.players.append(player)

	def start(self):
		
		self.on = True

		while self.on:
			for player in self.players:
				dices = player.turn()()
				print " Dices : ", dices
				print " score : ", self.score(dices)

	def score(self, data):
		
		## Check les identiques

		dict = {}
			
		result = {"pair": 0, "brelan":0,"carre":0,"yam":0,"full":0,"suite":0,"sec":0}

		dices, roll = data

		if roll == 1:
			result['sec'] = True

		for dice in dices :
			if dict.has_key(str(dice)) :
				dict[str(dice)] += 1
			else :
				dict[str(dice)] = 1

		for val in dict.itervalues():
			if val >= 2 :
				result["pair"] += 1
				if val >= 3:
					result["brelan"] += 1
					if val >= 4:
						result["carre"] += 1
						result["pair"] += 1
						if val == 5:
							result["yam"] += 1

		if result["pair"] == 2 and result["brelan"]== 1 and result["yam"] ==0:
			result["full"] += 1	
		
		if len(dict) == 5 :
			d = sorted(dict.keys())
			# print "d ",d
			possible_suites = (['1','2','3','4','5'], ['2','3','4','5','6'])
			if d in possible_suites:
				result["suite"] += 1
		
		# cleaning unused keys
		for k in result.keys():
			if result[k] == 0:
				del result[k]

		return result

game = Game()
for player in players:
	game.add_player(Player(player))
# game.start()
