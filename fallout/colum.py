import curses
import body, clean, top, size
import random, time

final_array = []
current = ""
master = ""
master_array = []
cheat_array = []
choiceF = []

picks = []

ystart = 42
xstart = 22

#-----
#static print that waits for choice
def show(win,cur):
	global current
	global master
	global master_array
	global cheat_array
	global choiceF
	
	current = cur
	master = body.getMaster()
	master_array = body.getMasterArray()
	cheat_array = body.getCheatArray()
	choiceF = body.getChoiceF()
	
	win.addstr(xstart,ystart,">            ",curses.color_pair(1))
	win.addstr(xstart,ystart,">" + current,curses.color_pair(1))
	win.refresh()

#-----
#function that runs the other functions that allow for prints and replacer
def printer(win):

	final = False
	score = False
	
	picks.append(current)

	if (current == master):
		final = True
		score = True
	if ((current in master_array) or (current in cheat_array)):
		replacer(win,'null')
		addColum(win)
		printColum(win)
		
	return final, score
	
#-----
#replaces the chosen word with periods
def replacer(win,choice):
	global choiceF
	
	if (choice == 'null'):
		choice = current
	
	if ((choice in master_array) or (choice in cheat_array)):
		i = 0
		while (i < len(choiceF)):
			array = choiceF[i]
			if (choice in array):
				j = 0
				while (choice != array[j]):
					j = j + 1
				length = len(array[j])
				string = ''
				k = 0
				while (k < length):
					string = string + '.'
					k = k + 1
				array[j] = string
				choiceF[i] = array
			i = i + 1
			
	body.setChoiceF(choiceF)

#-----
#add a line of text to the colum	
def addColum(win):
	global final_array
	
	tmp_array = []
	
	#if correct
	if (current == master):
		tmp_array.append(current)
		tmp_array.append("Exact match!")
		tmp_array.append("Please wait");
		tmp_array.append("while system");
		tmp_array.append("is accessed");
	
	#if wrong but close
	elif (current in master_array):
		tmp_array.append(current)
		tmp_array.append("Entry denied")
		length = len(current)
		current_list = list(current)
		master_list = list(master)
		
		i = 0
		num_same = 0
		while (i < length-1):
			one = current_list[i]
			two = master_list[i]
			if (one == two):
				num_same = num_same + 1
			i = i + 1
		tmp_array.append(str(num_same) + "/" + str(length) + " correct")
	
	#if in cheat
	elif (current in cheat_array):
		nat = random.randint(0,1)
		if (nat == 0):
			tmp_array.append(current)
			tmp_array.append("Allowance")
			tmp_array.append("replenished")
			top.setAttempts(5)
		if (nat == 1):
			tmp_array.append(current)
			tmp_array.append("Dud removed")
			top.setAttempts(top.getAttempts() + 1)
			p = 0
			while (p == 0):
				choice = random.choice(master_array)
				
				if(choice in picks):
					p = 0
				elif(choice == master):
					p = 0
				else:
					p = 1
					
				
				'''
				if (choice in picks):
					p = 0
				else:
					if (choice != master):
						p = 1
					else:
						choice = 'null'
						p = 0
				'''
			replacer(win,choice)
	
	final_array.append(tmp_array)
	
#-----
#print cloum to screen
def printColum(win):
	clean.clear_right(win)
	max = 5
	xcount = 0
	length = len(final_array)
	i = 0
	while ((i < 5) and (i < length)):
	
		win.addstr(0,0,str(length))
		win.refresh()
	
		arruy = final_array[length-1-i]
		linght = len(arruy)
		j = 0
		while (j < linght):
			string = arruy[linght-1-j]
			win.addstr(xstart-xcount-2,ystart,">" + string,curses.color_pair(1))
			win.refresh()
			j = j + 1
			xcount = xcount + 1
		i = i + 1