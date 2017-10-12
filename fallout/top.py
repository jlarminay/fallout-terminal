import curses
import size
import time, random

numAttempts = 4
numVisual =  ''

#-----
#on main screen, prints the very top bar
def title(win,wait):
	i = 0
	string = 'ROBCO INDUSRIES (TM) TERMLINK PROTOCOL'
	array = list(string)
	while (i < (len(array))):
		win.addstr(0,i,array[i],curses.color_pair(1))
		if (wait > 0):
			win.refresh()
			time.sleep(wait)
		i = i + 1
	
	attempts(win,wait)

#-----
#get string of available attempts
def attempts(win,wait):
	if (numAttempts > 1):
		i = 0
		string = 'ENTER PASSWORD NOW'
		array = list(string)
		while (i < (len(array))):
			win.addstr(1,i,array[i],curses.color_pair(1))
			if (wait > 0):
				win.refresh()
				time.sleep(wait)
			i = i + 1
	elif (numAttempts == 1):
		i = 0
		string = '!!! WARNING: LOCKOUT IMMINENT !!!'
		array = list(string)
		while (i < (len(array))):
			win.addstr(1,i,array[i],curses.color_pair(1))
			if (wait > 0):
				win.refresh()
				time.sleep(wait)
			i = i + 1
	visual(win,wait)

#-----
#print attempts string to screen	
def visual(win,wait):
	global numVisual
	numVisual = ''
	i = 0
	while (i < numAttempts):
		numVisual = numVisual + ' '
		i = i + 1

	i = 0
	string = '' + str(numAttempts) + ' ATTEMPT(S) LEFT: ' 
	array = list(string)
	while (i < (len(array))):
		win.addstr(3,i,array[i],curses.color_pair(1))
		if (wait > 0):
			win.refresh()
			time.sleep(wait)
		i = i + 1
	
	i = 0
	array = list(numVisual)
	while (i < (len(array))):
		win.addstr(3,19+(i*2),array[i],curses.A_STANDOUT | curses.color_pair(1))
		if (wait > 0):
			win.refresh()
			time.sleep(wait)
		i = i + 1

#-----
#minus attempts from global
def lessAttempts(num):
	global numAttempts
	numAttempts = numAttempts - num

#-----
#return global of attempts
def getAttempts():
	return numAttempts

#-----
#set global number of attempts
def setAttempts(num):
	global numAttempts
	numAttempts = num
	
#-----
#prints the default text at the top of the screen	
def defaultTop(win):
	string = 'ROBCO INDUSTRIES UNIFIED OPERATING SYSTEM' 
	lingth = len(string)
	pos = ((size.getWidth()-lingth) / 2) - 1
	win.addstr(0,pos,string,curses.color_pair(1))
	
	string = 'COPYRIGHT 2075-2077 ROBCO INDUSTRIES' 
	lingth = len(string)
	pos = ((size.getWidth()-lingth) / 2) - 1
	win.addstr(1,pos,string,curses.color_pair(1))
	
	string = ''
	i = 0
	while (i < size.getWidth()-1):
		string = string + '_'
		i = i + 1
	win.addstr(2,0,string,curses.color_pair(1))
	
	num = random.randint(1,9)
	string = '-SERVER ' + str(num) + '-' 
	lingth = len(string)
	pos = ((size.getWidth()-lingth) / 2) - 1
	win.addstr(2,pos,string,curses.color_pair(1)|curses.A_UNDERLINE)
	
	win.refresh()