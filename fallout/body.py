import curses
import diff, colum, size, write
import time, random
import numpy as np

lon = 24
hig = 36

master = ''
master_array = []
cheat_array = []

#cheat choices
choiceC = [	'<.>','(-!)','[.,]','{~.}','<-!*$>',
                '{#..}','(-_%)','[(]','<>'
		]
		
#symbol choices
choiceS = [	'!','"','$','%','^','&','*','+','`',
		':','@','<','>','?',';',',','-','/',
		'#','~','=','_','|',
		]
		
#brackets choices
choiceB_c = ['[',']']
choiceB_t = ['<','>']
choiceB_s = ['{','}']
choiceB_r = ['(',')']
choiceF = []

#array of register numbers
choiceR = []

matrixF = []

current = ''

i = 0 
while (i<(hig/2)):
	matrixF.append([])
	i = i + 1

def start(win,dif):
	#generate registers points
	registers()
	#generate arrays
	arrays(win,dif)	

def registers():
	global choiceR
	
	#create register points
	num = random.randint(61440,65000)
	i = 1
	while (i<hig):
		n = hex(num)
		choiceR.append(n)
		i = i + 1
		num = num + (lon/2)

def arrays(win,dif):
	global choiceS
	global choiceC
	global choiceF
	global master
	global master_array
	global cheat_array
	
	choiceW,duf_ary = diff.getWords(dif)
	master_array = []
	
	#duf_ary
	#odd word, odd cheat, w_count min, w_count max, c_count min, c_count max
	#duf_ary defines what the random limits are such as min and max counts
	w_odd = duf_ary[0]
	c_odd = duf_ary[1] + duf_ary[0]
	w_c_min = duf_ary[2]
	w_c_max = duf_ary[3]
	c_c_min = duf_ary[4]
	c_c_max = duf_ary[5]
	
	safe = False
	while (safe != True):
		i = 1
		w_count = 0
		c_count = 0
		
		random.shuffle(choiceW)
		random.shuffle(choiceC)
		
		while (i < hig):
			tot = 0
			array = []
			
			choiceB_c_count = True
			choiceB_t_count = True
			choiceB_s_count = True
			choiceB_r_count = True
				
			w = False
			c = False
			while (tot < (lon/2)):
				t = 'false'
				while (t == 'false'):
					inti = random.randint(0,100)
					if ((inti < w_odd) and (w != True) and (w_count < len(choiceW)) and (w_count < w_c_max)):
						#choice for word
						choice = choiceW[w_count]
						master_array.append(choice)
						w_count = w_count + 1
						w = True
					elif ((inti < c_odd) and (c != True) and (c_count < len(choiceC)) and (c_count < c_c_max)):
						#choice for cheat
						choice = choiceC[c_count]
						cheat_array.append(choice)
						c_count = c_count + 1
						c = True
					else:
						yip = False
						while (yip == False):
							#choice for symbol
							sub = random.randint(0,100)
							if (sub < 20):
								#choice for left bracket
								if (sub < 25):
									choice = choiceB_c[0]
									choiceB_c_count = False
									yip = True
								elif (sub < 50):
									choice = choiceB_t[0]
									choiceB_t_count = False
									yip = True
								elif (sub < 75):
									choice = choiceB_s[0]
									choiceB_s_count = False
									yip = True
								else:
									choice = choiceB_r[0]
									choiceB_r_count = False
									yip = True
							elif (sub < 50):
								#choice for right bracket
								if (sub < 25 and choiceB_c_count == True):
									choice = choiceB_c[1]
									yip = True
								elif (sub < 50 and choiceB_t_count == True):
									choice = choiceB_t[1]
									yip = True
								elif (sub < 75 and choiceB_s_count == True):
									choice = choiceB_s[1]
									yip = True
								elif (sub < 100 and choiceB_r_count == True):
									choice = choiceB_r[1]
									yip = True
							else:
								#remaining symbol
								choice = random.choice(choiceS)
								yip = True
							
					if (len(choice) <= ((lon/2)-tot)):
						t = 'true'
					if (tot == (lon/2)):
						t = 'true'
				tot = tot + (len(choice))
				array.append(choice)
			choiceF.append(array)
			i = i + 1
		if ((w_count > w_c_min) or (w_count < w_c_max)):
			safe = True
		if ((c_count > c_c_min) or (c_count < c_c_max)):
			safe = True
	
	master = random.choice(master_array)
	write.draw("master: " + master)
	write.draw("-----------------------")
	for w in master_array:
		write.draw(w)
	write.draw("-----------------------")


def printer(win,wait):
	i = 0
	
	while (i < (len(choiceR))/2):
		win.addstr(6+i,0,choiceR[i],curses.color_pair(1))
		if (wait > 0):
			win.refresh()		
		
		tot = 0
		j = 0
		array = list(choiceF[i])
		while (j < len(array)):
			win.addstr(6+i,7+tot,array[j],curses.color_pair(1))
			tot = tot + len(array[j])
			j = j + 1
			if (wait > 0):
				win.refresh()
	
		win.addstr(6+i,21,choiceR[i+16],curses.color_pair(1))
		if (wait > 0):
				win.refresh()
		
		tot = 0
		j = 0
		array = list(choiceF[i+16])
		while (j < len(array)):
			win.addstr(6+i,28+tot,array[j],curses.color_pair(1))
			tot = tot + len(array[j])
			j = j + 1
			if (wait > 0):
				win.refresh()
			
		if (wait > 0):
			win.refresh()
			time.sleep(wait)
		i = i + 1
	win.refresh()
	
def printCurrent(win,x,y,flip,way):
	global current
	
	if (flip == 0):
		array = choiceF[x]
		xfirst = 6
		yfirst = 7
		
		space = 0
		
		i = 0
		while (i < y):
			tmp = len(array[i])
			space = space + tmp
			i = i + 1
			
		current = array[y]
			
		xfinal = xfirst + x
		yfinal = yfirst + space
		#win.addstr(xfinal,yfinal+len(current),current,curses.A_STANDOUT | curses.color_pair(1))			
		
		if (way == 'up'):
			#start
			'''			
			c_array = choiceF[x]
			o_array = choiceF[x+1]
						
			o_y = y
			o_len = 0
			o_pos = 0
			o_i = 0
			while (o_i <= o_y-1):
				o_len = o_len + len(o_array[o_i])
				o_i = o_i + 1
			o_pos = o_len + 1
						
			c_y = 0
			c_len = 0
			c_pos = 0
			c_i = 0
			while (c_len <= o_pos):
				c_len = c_len + len(c_array[c_i])
				c_i = c_i + 1
			c_y = c_i - 1
						
			current = c_array[c_y]
			yfinal = yfirst + c_y
			#'''
			#end
		
		if (way == 'down'):
			#start
			'''			
			c_array = choiceF[x]
			o_array = choiceF[x-1]
						
			o_y = y
			o_len = 0
			o_pos = 0
			o_i = 0
			while (o_i < o_y-1):
				o_len = o_len + len(o_array[o_i])
				o_i = o_i + 1
			o_pos = o_len + 1
						
			c_y = 0
			c_len = 0
			c_pos = 0
			c_i = 0
			while (c_len <= o_pos):
				c_len = c_len + len(c_array[c_i])
				c_i = c_i + 1
			c_y = c_i - 1
						
			current = c_array[c_y]
			yfinal = yfirst + c_y
			#'''
			#end
		
		win.addstr(xfinal,yfinal,current,curses.A_STANDOUT | curses.color_pair(1))
		win.refresh()
		
	if (flip == 1):
		
		x = x + (hig/2) - 1
		array = choiceF[x-1]
		xfirst = 6
		yfirst = 7
		
		space = 0
		
		i = 0
		while (i < y):
			tmp = len(array[i])
			space = space + tmp
			i = i + 1

			if(y > len(array)-1):
					y = len(array)-1
                
		current = array[y]
			
		xfinal = xfirst + x - (hig/2) + 1
		yfinal = yfirst + space + 21
		#win.addstr(xfinal,yfinal+len(current),current,curses.A_STANDOUT | curses.color_pair(1))
		
		if (way == 'up'):
			good = 1
		
		if (way == 'down'):
			good = 1		
		
		win.addstr(xfinal,yfinal,current,curses.A_STANDOUT | curses.color_pair(1))
		win.refresh()
		
	colum.show(win,current)
	
def getCurrent():
	return current
	
def getArray(x,flip):
	if (flip == 0):
		array = choiceF[x]
	else:
		x = x + (hig/2) - 1
		array = choiceF[x]
	return array
	
def getLenArray(x,y):
	array = choiceF[x]
	return array

def getLon():
	return lon
	
def getHig():
	return hig
	
def getPosX(x):
	pos = 0
	return pos
	
def getMaster():
	return master
	
def getMasterArray():
	return master_array
	
def getCheatArray():
	return cheat_array
	
def getChoiceF():
	return choiceF
	
def setChoiceF(new):
	global choiceF
	choiceF = new
