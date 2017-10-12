import curses
import size

#-----
#clear screen
def clear(win):
	string = ''
	
	i = 0
	while (i < size.getWidth()-1):
		string = string + ' '
		i = i + 1

	i = 0
	while (i < size.getHeight()-1):	
		win.addstr(i,0,string, curses.color_pair(1))
		i = i + 1
	win.refresh()

#-----
#clear top rows of screen	
def clear_top(win):
	string = ''
	
	i = 0
	while (i < size.getWidth()-1):
		string = string + ' '
		i = i + 1

	i = 0
	while (i < 5):	
		win.addstr(i,0,string, curses.color_pair(1))
		i = i + 1
	win.refresh()
	
#-----
#clear bottom of screen	
def clear_bottom(win):
	string = ''
	
	i = 0
	while (i < size.getWidth()-1):
		string = string + ' '
		i = i + 1

	i = 6
	while (i < size.getHeight()-1):	
		win.addstr(i,0,string, curses.color_pair(1))
		i = i + 1
	win.refresh()
	
#-----
#clear left colum of screen	
def clear_left(win):
	string = ''
	
	i = 0
	while (i < 40):
		string = string + ' '
		i = i + 1

	i = 6
	while (i < size.getHeight()-1):	
		win.addstr(i,0,string, curses.color_pair(1))
		i = i + 1
	win.refresh()

#-----
#clear right colum of screen	
def clear_right(win):
	string = ''
	
	i = 0
	while (i < 20):
		string = string + ' '
		i = i + 1

	i = 6
	while (i < 22):	
		win.addstr(i,41,string, curses.color_pair(1))
		i = i + 1
	win.refresh()