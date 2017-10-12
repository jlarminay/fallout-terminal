import curses
import size
import time

#-----
#scrript for printing the intro scene to the screen
def start(win):
	i = 0
	string = 'WELCOME TO ROBCO INDUSRIES (TM) TERMLINK'
	array = list(string)
	while (i < (len(array))):
		win.addstr(0,i,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.02)
		i = i + 1
	
	win.addstr(2,0,'>',curses.color_pair(1))
	win.refresh()
	time.sleep(1.0)

	i = 0
	string = 'SET TERMINAL/INQUIRE'
	array = list(string)
	while (i < (len(array))):
		win.addstr(2,i+1,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.07)
		i = i + 1
	
	i = 0
	string = 'RIT-V300'
	array = list(string)
	while (i < (len(array))):
		win.addstr(4,i,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.02)
		i = i + 1

	win.addstr(6,0,'>',curses.color_pair(1))
	win.refresh()
	time.sleep(1.0)
	
	i = 0
	string = 'SET FILE/PROTECTION-OWNER:RWED ACCOUNT.F'
	array = list(string)
	while (i < (len(array))):
		win.addstr(6,i+1,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.07)
		i = i + 1

	win.addstr(7,0,'>',curses.color_pair(1))
	win.refresh()
	time.sleep(1.0)
	
	i = 0
	string = 'SET HALT RESTART/MANT'
	array = list(string)
	while (i < (len(array))):
		win.addstr(7,i+1,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.07)
		i = i + 1

	i = 0
	string = 'Initializing Robco Industries(TM) MF Boot Agent v2.3.0'
	array = list(string)
	while (i < (len(array))):
		win.addstr(9,i,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.02)
		i = i + 1

	i = 0
	string = 'RETROS BIOS'
	array = list(string)
	while (i < (len(array))):
		win.addstr(10,i,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.02)
		i = i + 1

	i = 0
	string = 'RBIOS-4.02.08.00 52EE5.E7.E8'
	array = list(string)
	while (i < (len(array))):
		win.addstr(11,i,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.02)
		i = i + 1

	i = 0
	string = 'Copyright 2201-2203 Robco Ind.'
	array = list(string)
	while (i < (len(array))):
		win.addstr(12,i,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.02)
		i = i + 1

	i = 0
	string = 'Uppermem: 64 KB'
	array = list(string)
	while (i < (len(array))):
		win.addstr(13,i,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.02)
		i = i + 1

	i = 0
	string = 'Root (5A8)'
	array = list(string)
	while (i < (len(array))):
		win.addstr(14,i,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.02)
		i = i + 1

	i = 0
	string = 'Maintenance Mode'
	array = list(string)
	while (i < (len(array))):
		win.addstr(15,i,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.02)
		i = i + 1

	win.addstr(17,0,'>',curses.color_pair(1))
	win.refresh()
	time.sleep(1.0)

	i = 0
	string = 'RUN DEBUG/ACCOUNTS.F'
	array = list(string)
	while (i < (len(array))):
		win.addstr(17,i+1,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.07)
		i = i + 1
	
	time.sleep(1.0)
	
	i = 0
	string = 'PRESS ANY KEY TO CONTINUE <'
	array = list(string)
	while (i < (len(array))):
		win.addstr(19,i,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.02)
		i = i + 1
	
	time.sleep(1.0)