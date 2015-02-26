#/usr/bin/python
# -*- coding : utf-8 -*-

from yamexcept import *
from helper import log

# COLUMN = ("1", "2", "3", "4", "5", "6","Mini", "Maxi", "Two pairs" , "Brelan" , "Full" , "Carre", "Suite", "Yam" )
POINTS = ('1', '2', '3', '4', '5', '6')
SUMS = ("Mini", "Maxi")
HEADS = ("Two pairs" , "Brelan" , "Full" , "Carre", "Suite", "Yam" )
COLUMN = POINTS + SUMS + HEADS
BONUS = { 63 : 30, 70 : 40, 80 : 50, 99 : 100}



class ScoringSheet(object):
	def __init__(self):
		self._up = []
		self._down = []
		self._free = {}
		self._straight = {}

		for comb in COLUMN:
			self._free[comb] = None
			self._straight[comb] = None


	def __score_head(self, head):
		return (HEADS.index(head) + 2) * 10 

	def __score_points(self, point, dices):
		log('scoring', 'dices %r do %r '%(dices ,dices.count(int(point)) * int(point) ))
		return dices.count(int(point)) * int(point)

	def __score_sums(self, dices):
		return reduce(lambda x, y: x+y, dices)

	def up(self, combo, dices=[]):
		if combo in COLUMN:
			log('up', '_up : %r'%self._up)
			log('up', combo+' is in COLUMS')
			log('up', 'next combo is '+COLUMN[len(self._up)])
			score = 0
			

			if combo == COLUMN[len(self._up)]:
				if combo in POINTS:
					self._up.append(self.__score_points(combo, dices))
					

				if combo in SUMS:
						
					score = self.__score_sums(dices)
					# maxi
					if combo == SUMS[1]:
						if score > self._up[-1]:
							self._up.append(score)
						else :
							raise MinOrMaxError, "Maximum should be superior to minimum"
					else :
						self._up.append(score)

				if combo in HEADS:
					self._up.append(self.__score_head(combo))

			else :
				raise IntervalError

		elif combo == 'cross':
			self._up.append(0)


		else :
			raise NoComboLikeThis 

		return self._up


	def down(self, combo, dices=[]):
		log('down', ' combo : %r dices : %r '%(combo, dices))
		log("down", self._down)
		log('down', "next interval %r "% COLUMN[ len(COLUMN) - len(self._down) - 1 ])

		if combo in COLUMN:

			if combo == COLUMN[ len(COLUMN) - len(self._down) - 1 ] :
				if combo in POINTS:
					self._down.append(self.__score_points(combo, dices))

				elif combo in SUMS :
					
					score = self.__score_sums(dices)

					if combo == SUMS[0] :

						if self._down[-1] > score :
							self._down.append(score)
						else :
							raise MinOrMAxError, "Minimum should be strictly inferior to maximum."
					else :
						self._down.append(score)

				elif combo in HEADS :
					
					self._down.append(self.__score_head(combo))
				
			else :
				raise IntervalError

		elif combo == 'cross':
			self._down.append(0)

		else:
			raise NoComboLikeThis


		return self._down

	def free(self, combo, dices = [], pos_to_cross = None):

		if combo in COLUMN:

			if self._free[combo] != None :
				raise AlreadyAttributed

			if combo in POINTS:
				self._free[combo] = self.__score_points(combo, dices)

			elif combo in SUMS :
				
				score = self.__score_sums(dices)

				if self._free[SUMS[0]] == None and self._free[SUMS[1]] == None :
					self._free[combo] = score
				else :
					if combo == SUMS[0]:
						if self._free[SUMS[1]] > score or self_free[SUMS[1]] == None:
							self._free[SUMS[0]] = score
						else :
							raise MinOrMaxError, 'Maximum should be strictly superior from Minimum'
					else:
						if self._free[SUMS[0]] < score or self._free[SUMS[0]] == None:
							self._free[SUMS[1]] = score
						else:
							raise MinOrMaxError, 'Minimum should be strictly inferior from Maximum'

			elif combo in HEADS :
				self._free[combo] = self.__score_head(combo)

		elif combo == 'cross':
			if self._free[pos_to_cross] != None:
				raise AlreadyAttributed

			self._free[pos_to_cross] = 0

		else :
			raise NoComboLikeThis

		clean_free = {}
		for k in self._free.keys():
			if self._free[k] != None:
				clean_free[k] = self._free[k]

		return clean_free

	def straight(self, combo, dices = [], pos_to_cross=None):
		if combo != 'cross' and self._straight[combo] != None :
			raise AlreadyAttributed
		elif pos_to_cross != None and self._straight[pos_to_cross] != None :
			raise AlreadyAttributed

		if combo in COLUMN:

			if self._straight[combo] != None : 
				raise AlreadyAttributed

			if combo in POINTS :
				self._straight[combo] = self.__score_points(combo, dices)

			elif combo in SUMS :
				score = self.__score_sums(dices)

				if self._straight[SUMS[0]] == None and self._straight[SUMS[1]] == None:
					
					if self._straight[SUMS[1]] > score :
						self._straight[combo] = score
					else :
						raise MinOrMaxError

				else :
					if self._straight[SUMS[0]] < score :
						self._straight[combo] = score
					else :
						raise MinOrMaxError


			elif combo in HEADS :
				self._straight[combo] = self.__score_head(combo)

		elif combo == 'cross':
			self._straight[pos_to_cross] = 0

		else:
			raise NoComboLikeThis

		cleaned_straight = {}
		for k in self._straight.keys() :
			if self._straight[k] != None:
				cleaned_straight[k] = self._straight[k]

		return cleaned_straight









