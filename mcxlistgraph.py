from mcxnowapi import McxNowSession
import requests
import numpy as np 
import datetime
import pytz
import time
import linecache


S = McxNowSession("","")
cur = raw_input('what currency are we working with?: ')
cur_history = S.GetCurrencyHistoryOrders(cur)
#Data is returned in lists [time,type,ammt,ammtbtc,price]

def write_hist_data():


	#opens the file for writing
	file_open = open('mcxlist.txt', 'w')
	file_open.truncate()
	cur_history.reverse()
	count = 0
	while count < 24:
		
			
		time = str(cur_history[count][0])
		price = str(cur_history[count][4])
		file_open.write(time)
		#file_open.write(amount)
		file_open.write(' ')
		file_open.write(price)
		
		if count < 23:
			newline = "\n"
			file_open.write(newline)
		count +=1


	file_open.close()


def update_trade_data(cur_history):

	while True:

		cur_history1 = S.GetCurrencyHistoryOrders(cur)

		#Data is returned in lists [time,type,ammt,ammtbtc,price]
		
		file_open = open('mcxlist.txt', 'r+')
		lines = file_open.readlines()
		cur_history.reverse()
		if cur_history1[0] != cur_history[0]:
			
			time1 = str(cur_history1[0][0])
			price1 = str(cur_history1[0][4])
			replacement = time1+" "+price1
			counted = 0
			

			print replacement
			
			lines.reverse()
			file_open.write('\n')
			file_open.write(replacement)
			lines.reverse()

			cur_history.reverse()
			cur_history.append(cur_history1[0])
			cur_history.reverse()
			print '.'
		time.sleep(2)

		
write_hist_data()
update_trade_data(cur_history)