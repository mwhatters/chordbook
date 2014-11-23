###IMPORTS/NECESSARYLISTS###
from collections import deque

flatnotes = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
sharpnotes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
flats = ['Bb', 'Db', 'Eb', 'Gb']

#rootscalelist = []

#chords = ['Minor Triad', 'Major Triad', 'Diminished Triad', 'Augmented Triad']

###INIT FUNTION###


###CHORD DATABASE###

"""class ChordPrinter:

	def __init__(self, rootscalelist):
		self.rootscalelist = rootscalelist"""

class Triad:

	numberofnotes = 3

	def __init__(self, root, third, fifth):
		self.root = root
		self.third = third
		self.fifth = fifth

	def __len__(self, root):
		pass

	def __repr__(self):
		return "%s is the root\n%s is the third\n%s is the fifth" % (self.root, self.third, self.fifth)


class Tertian:

	numberofnotes = 4

	def __init__(self, root, third, fifth, seventh):
		self.root = root
		self.third = third
		self.fifth = fifth
		self.seventh = seventh

	def __repr__(self):
		return "%s is the root\n%s is the third\n%s is the fifth\n%s is the seventh" % (self.root, self.third, self.fifth, self.seventh)

###CONTINUE PROGRAM###
def continueProgram(rootscalelist, firstenry = True):

	if firstenry == True:
		print "would you like to take a look at other chords? (Y/N)"

	answer = raw_input("> ")

	if answer.upper() == "Y":
		menu(rootscalelist)
	elif answer.upper() == "N":
		print "Goodbyeeee"
		pass
	else:
		"Y or N?"
		continueProgram(False)


###CREATE CUSTOM CHORD###
def numberOfNotesCustomChord(rootscalelist, is_valid = False):

	print "Create a custom chord from the root!"

	print "How many notes?"

	if is_valid == False:
        	try:
         		num = int(raw_input("How many notes in this chord?: "))
         		createCustomChord(rootscalelist, num)

                
    		except ValueError, e:
            		print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
            		createCustomChord(False)

def createCustomChord(rootscalelist, num):
	pass


###CHORD TYPES###
def chordTypeTriadSelection(rootscalelist, firstenry = True):

	if firstenry == True:
		print "what kind of Triad would you like to take a look at?\
		\n\t1: Major Triad\
		\n\t2: Minor Triad\
		\n\t3: Diminished Triad\
		\n\t4: Augmented Triad"

	triadtype = raw_input("> ")

	if triadtype == "1": #Major Triad: (0-4-7)
		majortriad = Triad(rootscalelist[0], rootscalelist[4], rootscalelist[7])
		print "Here is your " + str(rootscalelist[0]) + " Major Triad:"
		print majortriad

	elif triadtype == "2": #Minor Triad: (0-3-7)
		minortriad = Triad(rootscalelist[0], rootscalelist[3], rootscalelist[7])
		print "Here is your " + str(rootscalelist[0]) + " Minor Triad:"
		print minortriad

	elif triadtype == "3": #Diminished Triad: (0-3-6)
		diminishedtriad = Triad(rootscalelist[0], rootscalelist[3], rootscalelist[6])
		print "Here is your " + str(rootscalelist[0]) + " Diminished Triad:"
		print diminishedtriad

	elif triadtype == "4": #Augmented Triad: (0-4-8)
		augmentedtriad = Triad(rootscalelist[0], rootscalelist[4], rootscalelist[8])
		print "Here is your " + str(rootscalelist[0]) + " Augmented Triad:"
		print augmentedtriad

	else:
		print "Not a proper chord type!"
		chordTypeTriadSelection(rootscalelist, False)

	continueProgram(rootscalelist)

def chordTypeTertianSelection(rootscalelist, firstenry = True):
#Make this function less fatty. Take the two bottom printing lines of each if variable and refactor it
	if firstenry == True:
		print "What kind of Tertian would you like to take a look at?\
		\n\t1: Major Seventh\
		\n\t2: Minor Seventh\
		\n\t3: Minor Major Seventh\
		\n\t4: Dominant Seventh\
		\n\t5: Diminished Seventh\
		\n\t6: Half Diminished Seventh\
		\n\t7: Augmented Seventh\
		\n\t8: Augmented Major Seventh\
		\n\t9: Seventh Flat Five"

	tertiantype = raw_input("> ")

	if tertiantype == "1": #Major Seventh: (0-4-7-11)
		majorseventh = Tertian(rootscalelist[0], rootscalelist[4], rootscalelist[7], rootscalelist[11])
		print "Here is your " + str(rootscalelist[0]) + " Major Seventh Chord:"
		print majorseventh

	elif tertiantype == "2": #Minor Seventh: (0-3-7-10)
		minorseventh = Tertian(rootscalelist[0], rootscalelist[4], rootscalelist[7], rootscalelist[10])
		print "Here is your " + str(rootscalelist[0]) + " Minor Seventh Chord:"
		print minorseventh

	elif tertiantype == "3": #Minor Major Seventh: (0-3-7-11)
		minormajorseventh = Tertian(rootscalelist[0], rootscalelist[3], rootscalelist[7], rootscalelist[11])
		print "Here is your " + str(rootscalelist[0]) + " Minor Seventh Chord:"
		print minormajorseventh

	elif tertiantype == "4": #Dominant Seventh: (0-4-7-10)
		dominantseventh = Tertian(rootscalelist[0], rootscalelist[4], rootscalelist[7], rootscalelist[10])
		print "Here is your " + str(rootscalelist[0]) + " Dominant Sevneth Chord:"
		print dominantseventh

	elif tertiantype == "5": #Diminished Seventh: (0-3-6-9)
		diminishedseventh = Tertian(rootscalelist[0], rootscalelist[3], rootscalelist[6], rootscalelist[9])
		print "Here is your " + str(rootscalelist[0]) + " Diminished Seventh:"
		print diminishedseventh

	elif tertiantype == "6": #Half Diminished Seventh: (0-3-6-10)
		halfdiminishedseventh = Tertian(rootscalelist[0], rootscalelist[3], rootscalelist[6], rootscalelist[10])
		print "Here is your " + str(rootscalelist[0]) + " Half Diminished Seventh:"
		print halfdiminishedseventh

	elif tertiantype == "7": #Augmented Seventh: (0-4-8-10)
		augmentedseventh = Tertian(rootscalelist[0], rootscalelist[4], rootscalelist[8], rootscalelist[10])
		print "Here is your " + str(rootscalelist[0]) + " Augmented Seventh:"
		print augmentedseventh

	elif tertiantype == "8": #Augmented Major Seventh: (0-4-8-11)
		augmentedmajorseventh = Tertian(rootscalelist[0], rootscalelist[4], rootscalelist[8], rootscalelist[11])
		print "Here is your " + str(rootscalelist[0]) + " Augmented Major Seventh:"
		print augmentedmajorseventh

	elif tertiantype == "9": #Seventh Flat Five: (0-4-6-10)
		seventhflatfive = Tertian(rootscalelist[0], rootscalelist[4], rootscalelist[6], rootscalelist[10])
		print "Here is your " + str(rootscalelist[0]) + " Seventh Flat Five:"
		print seventhflatfive

	else:
		print "Not a proper input, shall we try again?"
		chordTypeTertianSelection(rootscalelist, False)

	continueProgram(rootscalelist)

def chordTypeExtendedSelection(rootscalelist, firstenry = True):

	if firstenry == True:
		print "What kind of Extended Chord would you like to take a look at?\n\t1: 9th Chords\n\t2: 11th Chords\n\t3: 13th Chords"

	tertiantype = raw_input("> ")
	pass


###CHOOSE A CHORD TYPE###
#the menu function takes an input from ignorant users, which in turn points to the next function.
def menu(rootscalelist):
	print "Root: " + rootscalelist[0]
	print "what kind of chord would you like to take a look at?\
	\n\t1: Triad\
	\n\t2: Tertian\
	\n\t3: Extended Chords\
	\n\t4: Altered Chords\
	\n\t5: Added Tone Chords\
	\n\t6: Sus Chords \
	\n\t7: **Change Root**\
	\n\t 8: **Create Custom Chord**"


	chordtype = raw_input("> ")

	if chordtype == "1":
		chordTypeTriadSelection(rootscalelist)
	elif chordtype == "2": 
		chordTypeTertianSelection(rootscalelist)
	elif chordtype == "3" or chordtype == "4" or chordtype == "5" or chordtype == "6":
		print "Apologies, not yet available"
		chooseChordType(rootscalelist)
	elif chordtype == "7":
		print "Okay, lets choose a new root!"
		main(False)
	elif chordtype == "8":
		print "Okay, let's create a custom chord!"
		numberOfNotesCustomChord(rootscalelist, False)
	else:
		print "Make sure to choose a number."
		chooseChordType(rootscalelist)


###CHOOSE A ROOT###
#Must make this a working function
def main(firstenry = True):

	if firstenry == True:
		print "Choose your root (Eg. A#, B, G)"

	root = raw_input("> ")
	rootscale = None

	if root.upper() in sharpnotes:
		root = root.upper()
		rootscale = deque(sharpnotes)

	elif root.title() in flats:
		root = root.title()
		rootscale = deque(flatnotes)

	else:
		print "not a proper note (currently), let's try again"
		chooseRoot(False)

	while rootscale[0] != str(root):
		rootscale.rotate(-1)
	rootscalelist = list(rootscale)

	#printer = ChordPrinter(rootscalelist)

	#print printer.rootscalelist

	menu(rootscalelist)


main()


#create a member variable for the rootscalelist

#For funtions, ADD COMMENTS!:
#This takes x parameter
#It returns y value
#this is what it does


#Format the program in a way that other users will be able to read. 
#REFORMAT











###PLAY DAT CHORD###
