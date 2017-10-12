#!/usr/bin/python3

import curses
import title, clean, top, body, end, diff, colum, after, size, write
import time, thread

#start window
win = curses.initscr()
curses.start_color()
curses.noecho()
curses.cbreak()
win.keypad(1)

write.clear()

fin = False
while (fin == False):

	#initializes all variables

	#initialize colours
	curses.use_default_colors()
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_GREEN)

	#run difficulty
	clean.clear(win)
	#return chosen difficulty
	dif = diff.choice(win)

	#clear screen
	clean.clear(win)

	''' ADD THREAD FOR INTRO AND REGISTERS '''
	'''
		will run a thread for the word generation as well as the intro scene
		safe variable is for checking if both threads are done
	'''
	#start intro
	def start_thread(c):
		global safe
		if c == 1:
			title.start(win)
			safe = safe + 1
		if c == 2:
			body.start(win,dif)
			safe = safe + 1		
	
	#define variable
	safe = 0
	#start threads
	thread.start_new_thread(start_thread,(1,))
	thread.start_new_thread(start_thread,(2,))
	while (safe != 2):
		ch = win.getch()

	#initial print
	clean.clear(win)
	top.title(win,0.02)
	body.printer(win,0.02)

	#check attempts
	final = False
	x = 0
	y = 0
	#if flip = 1, then other side
	flip = 0
	way = 'left'
	while (final == False):
		clean.clear_top(win)
		top.title(win,0)
		
		result = False
		while (result == False):
			clean.clear_left(win)
			body.printer(win,0)		
			body.printCurrent(win,x,y,flip,way)
			ch = win.getch()
			
			#if left
			if(ch == curses.KEY_LEFT):
				y = y - 1
				way = 'left'
				#check on which colum
				if ((y < 0) and (flip == 0)):
					y = 0
					flip = 0
				if ((y < 0) and (flip == 1)):
					flip = 0
					y = (len(body.getArray(x,flip)))-1
			
			#if right
			if(ch == curses.KEY_RIGHT):
				y = y + 1
				way = 'right'
				if ((y >= len(body.getArray(x,flip))) and (flip == 0)):
					flip = 1
					y = 0
				if ((y >= len(body.getArray(x,flip))) and (flip == 1)):
					flip = 1
					y = len(body.getArray(x,flip))-1
					
			#if up
			if(ch == curses.KEY_UP):
				x = x - 1
				way = 'up'
				if (x < 0):
					x = 0
					way = ''
				if ((y >= len(body.getArray(x,flip))) and (flip == 0)):
					flip = 1
					y = 0
				if ((y >= len(body.getArray(x,flip))) and (flip == 1)):
					flip = 1
					y = len(body.getArray(x,flip))-1
					
			#if down
			if(ch == curses.KEY_DOWN):
				x = x + 1
				way = 'down'
				if (x > 16):
					x = 16
					way = ''
				if ((y >= len(body.getArray(x,flip))) and (flip == 0)):
					flip = 1
					y = 0
				if ((y >= len(body.getArray(x,flip))) and (flip == 1)):
					flip = 1
					y = len(body.getArray(x,flip))-1
					
			#if enter is pressed		
			if (ch == 10):
				result = True

		
		final, score = colum.printer(win)
		
		top.lessAttempts(1)
		i = top.getAttempts()
		if (i <= 0 and final != True):
			final = True
		
	if (score == True):
		time.sleep(1.5)
		fin = True
	else:
		clean.clear(win)
		end.end(win)
		fin = end.trap(win)
		top.setAttempts(4)

	
clean.clear(win)
master = body.getMaster()

def end_lock(w,m):
	global safe
	
	end.good(w,m)
	safe = safe + 1

#define variable
safe = 0
#start threads
thread.start_new_thread(end_lock,(win,master,))
while (safe != 1):
	ch = win.getch()

clean.clear(win)
top.defaultTop(win)
after.menu(win)

win.getch()



#end windows
curses.nocbreak()
win.keypad(0)
curses.echo()
curses.endwin()
