#!/usr/bin/env python
# Copyright 2014 CryptoFinancial Strategies LLC
# & yungcrypt
#import requests
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib 
import datetime
import pytz
import time
import matplotlib.animation as anim

#create the instance of a graph
fig=plt.figure()
rect = fig.patch
ax1 = fig.add_subplot(1,1,1, axisbg='black') #height x Width x chart#
rect.set_facecolor('black')

#set timezone
est=pytz.timezone('US/Eastern')

# axis ticker colors
ax1.tick_params(axis='x', colors='red')
ax1.tick_params(axis='y', colors='red')


def graph_animate(i):
	read_file = open('mcxlist.txt', 'r')
	sep_file = read_file.read().split('\n')
	x = []
	y = []

	for pair in sep_file:
		XY = pair.split(' ')
		if len(XY) > 1: 
			x.append(float(XY[0]))
			y.append(float(XY[1]))

	ax1.clear()

	x = np.array(x)
	y = np.array(y)
	read_file.close()
	
	#rotates timestamps 
	plt.setp(plt.xticks()[1], rotation=30)

	#shows grid
	ax1.grid(b=True, which='major', color='r')
	plt.title('CFS Betagraph V0.0.1', color='w')
	#plt x, and y cords
	ax1.plot_date(md.epoch2num(x), y,'r',tz=est,linewidth=2,xdate=True,marker='o')

# Auto update function for the graph... interval in ms
ani = anim.FuncAnimation(fig,graph_animate, interval=10000)

plt.show()
