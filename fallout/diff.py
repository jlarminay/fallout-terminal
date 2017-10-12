import curses
import size
import time, random

def choice(win):
	difficulty = ['Very Easy','Easy','Average','Hard','Very Hard']
	
	'''
			Very Easy
				Skill 	- 15
				Len 	- 4-5
				w_count - (len + (len/2)) <-> (len * 2)
				c_count - 
			Easy
				Skill 	- 25
				Len 	- 6-7
				w_count - (len + (len/2)) <-> (len * 2)
				c_count - 
			Average
				Skill 	- 50
				Len 	- 8
				w_count - (len + (len/2)) <-> (len * 2)
				c_count - 
			Hard
				Skill 	- 75
				Len 	- 9-10
				w_count - (len + (len/2)) <-> (len * 2)
				c_count - 
			Very Hard
				Skill 	- 100
				Len 	- 11-12
				w_count - (len + (len/2)) <-> (len * 2)
				c_count - 
	'''
	
	y = 0
	end = False
	while end != True:
		
		#print options to screen
		win.addstr(1,3,'Select Difficulty',curses.color_pair(1))
		win.addstr(2,6,'1 - ' + difficulty[0],curses.color_pair(1))
		win.addstr(3,6,'2 - ' + difficulty[1],curses.color_pair(1))
		win.addstr(4,6,'3 - ' + difficulty[2],curses.color_pair(1))
		win.addstr(5,6,'4 - ' + difficulty[3],curses.color_pair(1))
		win.addstr(6,6,'5 - ' + difficulty[4],curses.color_pair(1))
		
		#highlight selected option
		win.addstr(y+2,10,difficulty[y],curses.A_STANDOUT | curses.color_pair(1))
		
		#get key press
		ch = win.getch()
		
		#if up, lower on list
		if(ch == curses.KEY_UP):
			y = y - 1
			if y < 0:
				y = 0
		
		#if down, raises on list
		if(ch == curses.KEY_DOWN):
			y = y + 1
			if y > 4:
				y = 4
		
		#if enter, end
		if(ch == 10):
			end = True
			
	return y
	
def getWords(dif):
	dif = int(dif)
	choiceW = ['--FAIL--']
	#duf_ary
	#odd word, odd cheat, w_count min, w_count max, c_count min, c_count max
	duf_ary = 	['','','','','','']
	if (dif == 0):
		#Very Easy
		pos = 	[	
					#4 letters
					['BATH','BECK','BLAH','BACK','BETH','REEF','RAFT','PIPE','RIPE','TAME'],
					#5 letters
					['SPIES','JOINS','TIRES','TRICK','TRIED','SKIES','TERMS','THIRD','FRIES','TRITE','TRIBE','TEXAS','PRICE'],
					
				]
		num = random.randint(0,len(pos)-1)
		choiceW = pos[num]
		duf_ary = [3,3,6,10,4,6]
	if (dif == 1):
		#Easy
		pos = 	[	
					#6 letters
					['BODIES','PERIAN','BURIED','BARELY','INDIAN',],
					#7 letters
					['esay','two'],
				]
		num = random.randint(0,len(pos)-1)
		choiceW = pos[num]
		duf_ary = [5,5,9,12,4,5]
	if (dif == 2):
		#Average
		pos = 	[	
					#8 letters
					['average','one'],
				]
		num = random.randint(0,len(pos)-1)
		choiceW = pos[num]
		duf_ary = [7,7,12,16,4,5]
	if (dif == 3):
		#Hard
		pos = 	[	
					#9 letters
					['hard','one'],
					#10 letters
					['hard','two'],
				]
		num = random.randint(0,len(pos)-1)
		choiceW = pos[num]
		duf_ary = [9,9,13,20,4,5]
	if (dif == 4):
		#Very Hard
		pos = 	[	
					#11 letters
					['very hard','one'],
					#12 letters
					['very hard','two'],
				]
		num = random.randint(0,len(pos)-1)
		choiceW = pos[num]
		duf_ary = [11,11,15,22,3,4]

	return choiceW, duf_ary