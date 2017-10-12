import curses
import size
import time, random


#------
#this is the menu for once the program is properly hacked
def menu(win):
	
	string = 'MENU' 
	lingth = len(string)
	pos = ((size.getWidth()-lingth) / 2) - 1
	win.addstr(4,pos,string,curses.color_pair(1))
	
	ch = win.getch()
	#if enter, end
	if(ch == 10):
		end = True