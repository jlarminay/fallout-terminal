
#just a test file for writing text to a file
#this is really useful to see if certain parts are running
#or what some variables are

file = "_file.txt"

def clear():
	global file
	
	target = open(file, "w")
	target.write("")
	target.close()

def draw(word):
	global file
	
	target = open(file, "a")
	target.write(word)
	target.write("\n")
	target.close()