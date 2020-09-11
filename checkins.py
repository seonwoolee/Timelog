#!/usr/bin/env python
import os

with open(os.environ.get('TIMELOG'), 'r') as f:
	sorted_lines = []

	for line in f:
		sorted_lines.append(line[2:22]+line[0:1]+line[21:-1])

	sorted_lines.sort()
	checkins = []

	for line in sorted_lines:
		task = line[22:].partition(' ')[0]
		
		if(line[20]=='i'):
			checkins.append(task)
		elif(line[20]=='o'):
			try:
				checkins.remove(task)
			except ValueError:
				print(line+" not in checkins")
		else:
			print('invalid checkin/checkout')

	for task in checkins:
		print('checked into '+task)
