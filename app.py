'''
this project attempts to write a better lift script than our crappy glass lifts got
the code is done for serving queues given at the start
now real-time adding would be neat
I need an interface where I can add stuff. And I need the lifts to run in the background
I need to have runLifts run synchro in the background and take input every x seconds.
'''
import random as r
import time as t

class BetterLift:
	def __init__(self, liftcount, traveltime):
		self.queue = []
		self.liftcount = liftcount
		self.traveltime = traveltime
		self.lifts = [{'current_level': 0, 'queue': []} for i in range(liftcount)]
 
	def printLifts(self):
		for lift in self.lifts:
			print(f'current_level: {lift["current_level"]} levels:lift["queue"]')
	def interface(self):
		try: self.addLevel(int(input("Enter your target level:\n")))
		except Exception as e: print(e);
	def getShortestQueue(self):
		qLengths = [len(lift['queue']) for lift in self.lifts]
		return (qLengths.index(min(qLengths)))
	def addLevel(self, level):
		liftindex = self.getShortestQueue()
		self.lifts[liftindex]['queue'].append(level)
		self.lifts[liftindex]['queue'] = sorted(self.lifts[liftindex]['queue'])
		#self.printLifts()
	def getAllQueuesEmpty(self):
		allqlengths = [len(lift['queue']) for lift in self.lifts]
		return (sum(allqlengths) == 0)
	def runLifts(self):
		arrivals = 0
		while not self.getAllQueuesEmpty():
			t.sleep(self.traveltime)
			for i, lift in enumerate(self.lifts):
				if not len(lift['queue']): continue
				if lift['queue'][0] < lift['current_level']:
					self.lifts[i]['current_level'] -= 1
					print(f'Moving Lift #{i} down to {self.lifts[i]["current_level"]}')
				elif lift['queue'][0] > lift['current_level']:
					self.lifts[i]['current_level'] += 1
					print(f'Moving Lift #{i} up to {self.lifts[i]["current_level"]}')
				else:
					arrivals += 1
					self.lifts[i]['queue'].pop(0)
					print(f'Lift #{i} has arrived at', self.lifts[i]['current_level'], f'arrival #{arrivals}')

	def main(self):
		self.interface()
		#for i in range(100):
		#	newlevel = r.randint(-10, 30)
		#	self.addLevel(newlevel)
		self.runLifts()
		

if __name__ == '__main__':
	bl = BetterLift(4, .05)
	bl.main()
