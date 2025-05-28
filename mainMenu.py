#MainMenu
from time import sleep
from readFilms import read
from addFilms import insertFilms
from updateFilms import update
from deleteFilms import delete

def menuOptions(): # Function? Subroutine?
	menuUI = \
	"""
	SAFARIFLIX CINEMATIC DATABASE 🚥 📶

	CHOOSE YOUR ADVENTURE:
		1. Explore films Catalogue in the Database...
		2. Introduce a New Masterpiece to your Database...
		3. Update an existing film...
		4. Permanently Delete an existing film...
		5. Exit the Viewing Expirience...

	"""
	options = ["1", "2", "3", "4", "5"]
	choice = 0
	while choice not in options:
		print(menuUI)
		choice = input("Enter Select an Adventure from the menu: ")
		if choice not in options:
			print(choice, "is not a valid option, try another adventure.")
			sleep(1)
	return choice
	

mainProgram = True
while mainProgram:
	userChoice = menuOptions() # Choice is stored in userChoice
	if userChoice == "1":
		read()
	elif userChoice == "2":
		insertFilms()
	elif userChoice == "3":
		update()
	elif userChoice == "4":
		delete()
	else:
		mainProgram = False

input("Press Enter to Exit the Application.")
# Finished