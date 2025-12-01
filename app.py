'''
this project attempts to write a better lift script than our crappy glass lifts got
'''
import random as r
import time as t

class BetterLift:
	def __init__(self, liftcount):
		self.queue = []
		self.liftcount = liftcount
		self.lifts = [{'current_level': 0, 'queue': []} for i in range(liftcount)] 
	def printLifts(self):
		for lift in self.lifts:
			print(f'current_level: {lift["current_level"]} levels:lift["queue"]')
	def getShortestQueue(self):
		qLengths = [len(lift['queue']) for lift in self.lifts]
		return (qLengths.index(min(qLengths)))
	def addLevel(self, level):
		liftindex = self.getShortestQueue()
		self.lifts[liftindex]['queue'].append(level)
		self.lifts[liftindex]['queue'] = sorted(self.lifts[liftindex]['queue'])
		#self.printLifts()
	def runLifts(self):
		for i, lift in enumerate(self.lifts):
			if not len(lift['queue']): continue
			if lift['queue'][0] < lift['current_level']:
				self.lifts[i]['current_level'] -= 1
				print(f'Moving Lift {i} down to {self.lifts[i]["current_level"]}')
			elif lift['queue'][0] > lift['current_level']:
				self.lifts[i]['current_level'] += 1
				print(f'Moving Lift {i} up to {self.lifts[i]["current_level"]}')
			else:
				self.lifts[i]['queue'].pop(0)
				print(f'Lift has arrived at', self.lifts[i]['current_level'])
	def main(self):
		for i in range(4):
			newlevel = r.randint(-10, 10)
			self.addLevel(newlevel)
			#t.sleep(.5)
		self.runLifts()
		
def tests():
	bl = BetterLift(4)
	print(bl.getShortestQueue())

if __name__ == '__main__':
	#tests()
	bl = BetterLift(4)
	bl.main()
