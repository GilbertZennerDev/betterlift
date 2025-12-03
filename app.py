'''
this project attempts to write a better lift script than our crappy glass lifts got
the code is done for serving queues given at the start
now real-time adding would be neat
I need an interface where I can add stuff. And I need the lifts to run in the background
I need to have runLifts run synchro in the background and take input every x seconds.

I change my problem:
BetterLift just runs all its queue. Only when Queue empty, new Levels

LiftManager keeps taking orders for new levels. Passes the entire queue on if BetterLift is finished with everything.
'''
import random as r
import time as t

class BetterLift:
	def __init__(self, conn, liftcount, traveltime):
		self.conn = conn
		self.queue = []
		self.liftcount = liftcount
		self.traveltime = traveltime
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
	def addQueue(self, queue):
		for level in queue: self.addLevel(level)
	def getAllQueuesEmpty(self):
		allqlengths = [len(lift['queue']) for lift in self.lifts]
		return (sum(allqlengths) == 0)
	def runLifts(self):
		if not self.getAllQueuesEmpty(): self.runQueue(); self.conn.send('busy');
		else: 
			self.conn.send('give_queue');
			queue = self.conn.recv()
			self.addQueue(queue)
		
	def runQueue(self):
		arrivals = 0
		while not self.getAllQueuesEmpty():
			t.sleep(self.traveltime)
			for i, lift in enumerate(self.lifts):
				print("Doing Lift", i)
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

import multiprocessing
import os

def childProcess(conn):
	bl = BetterLift(conn, 4, 2)
	while 1: bl.runLifts()
	conn.close()

def interface():
	newlevel = input("Enter your target level:\n")
	if newlevel != 'exit':
		try: return (int(newlevel))
		except Exception as e: print(e); interface()
	#return 'exit'

def LiftManager():
	parent_conn, child_conn = multiprocessing.Pipe()
	
	p = multiprocessing.Process(target=childProcess, args = (child_conn,))
	p.start()
	queue = []
	while 1:
		newlevel = interface()
		if newlevel == 'exit': return
		if newlevel not in queue: queue.append(newlevel)
		child_state = parent_conn.recv()
		if child_state == 'give_queue': parent_conn.send(queue); queue = []
	p.join()
	parent_conn.close()

if __name__ == '__main__':
	LiftManager()
