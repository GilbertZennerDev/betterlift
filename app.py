'''
this project attempts to write a better lift script than our crappy glass lifts got
'''
import random as r
import time as t

class BetterLift:
	def __init__(self, liftcount):
		self.queue = []
		self.liftcount = liftcount
		self.lifts = [''] * liftcount
	def printLifts(self):
		print(self.lifts)
	def updateQueue(self):
		print('Updating Queue...')
		print(self.queue)
		self.printLifts()
	def getShortestQueue(self):
		qLengths = [len(lift.split(';')) for lift in self.lifts]
		index = qLengths.index(min(qLengths))
		#print(f'qLength: {qLengths} and index {index}')
		return index
	def addLevel(self, level):
		liftindex = r.randint(0, self.liftcount - 1)
		liftindex = self.getShortestQueue()
		self.lifts[liftindex] += f";{level}"
		self.printLifts()
	def main(self):
		for i in range(6):
			newlevel = r.randint(-10, 10)
			self.addLevel(newlevel)
			t.sleep(.5)

if __name__ == '__main__':
	bl = BetterLift(4)
	bl.main()
