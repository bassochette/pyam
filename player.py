#/usr/bin/python
# -*- coding : utf-8 -*-

from yamexcept import *
from scoresheet import *
import random

# lancer les des
def throwDices(n=5):
	dices = []
	for i in range(1, (n+1)):
		dices.append(random.randint(1,6))
	return dices

##

positive = ('yes', 'y', 'oui', 'o', 'O', 'Y')
negative = ('no', 'n', 'non', 'N')

class Player(object):
	def __init__(self, name='toto'):
		self.name = name
		self.score = 0
		self.roll = 0
		self.keepedDices = []
		self.scoringScheet = ScoringSheet()
		dices = []

	def turn(self):
		
	
		def UI(self):
			
			print " Debut tour joueur " , self.name
			dices = []
			ok = True
			while self.roll < 3 and len(self.keepedDices) != 5 and ok == True:
				print " ############################### " 
				print " ## Lance #%d    %s         ## "%(self.roll, self.name)
				print " ############################### " 

				dices = throwDices(5-len(self.keepedDices))
				print " Dices :" , dices
				self.roll += 1
				print " roll : ", self.roll 
				for dice in dices:
					print "keeped dices : " , self.keepedDices
					print "Would you like to keep : ", dice
					keep = raw_input("oui , [non] :")
					if keep in positive :
						self.keepedDices.append(dice)		
				
				print " Une derniere verif pour la route " 
				
				endFlag = False
				while endFlag == False:
					
					print "keeped dices : ", self.keepedDices
					
					for d in self.keepedDices:
						
						print " conserve : " , d
						keep = raw_input("[oui] / non : ")
						if keep in positive:
							pass
						elif keep in negative:
							self.keepedDices.remove(d)

					i = True
					while i:		
						print " de conserve : ", self.keepedDices
						print " OK????? " 
						i = raw_input("oui / [non] :")
						if i in positive :
							endFlag = True
						if i in negative:
							i = False

				if len(self.keepedDices) == 5:
					ok = False
			if self.roll == 0 : 
				self.roll = random.randint(1,3)
				
			return self.keepedDices, self.roll 	
		return UI			
