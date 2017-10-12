import curses
import size
import time

#print end segment once beaten

#-----
#bad end
def end(win):
	i = 0
	string = 'TERMINAL LOCKED' 
	array = list(string)
	lingth = len(string)
	pos = ((size.getWidth()-lingth) / 2) - 1
	while (i < (len(array))):
		win.addstr(3,i+pos,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.02)
		i = i + 1
	
	i = 0
	string = 'PLEASE CONTACT AN ADMINISTRATOR' 
	array = list(string)
	lingth = len(string)
	pos = ((size.getWidth()-lingth) / 2) - 1
	while (i < (len(array))):
		win.addstr(4,i+pos,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.02)
		i = i + 1

#-----
#good end
def good(win,master):
	i = 0
	string = 'WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK' 
	array = list(string)
	while (i < (len(array))):
		win.addstr(0,i,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.02)
		i = i + 1
	
	win.addstr(1,0,'>',curses.color_pair(1))
	win.refresh()
	time.sleep(1.0)
	
	i = 0
	string = 'LOGON ADMIN'
	array = list(string)
	while (i < (len(array))):
		win.addstr(1,i+1,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.07)
		i = i + 1
	
	i = 0
	string = 'ENTER PASSWORD NOW' 
	array = list(string)
	while (i < (len(array))):
		win.addstr(3,i,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.02)
		i = i + 1

	
	win.addstr(4,0,'>',curses.color_pair(1))
	win.refresh()
	time.sleep(1.0)
	
	i = 0
	string = ''
	while (i < len(master)):
		string = string + '*'
		i = i + 1
	
	i = 0
	array = list(string)
	while (i < (len(array))):
		win.addstr(4,i+1,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.07)
		i = i + 1
	
	time.sleep(1.0)
	
	i = 0
	string = 'PRESS ANY KEY TO CONTINUE <'
	array = list(string)
	while (i < (len(array))):
		win.addstr(6,i,array[i],curses.color_pair(1))
		win.refresh()
		time.sleep(0.02)
		i = i + 1
	
	time.sleep(1.0)

#-----
#originaly a lock that only continued when password is entered, but for the moment just skips	
def trap(win):
	fin = True
	ch = win.getch()
	return fin