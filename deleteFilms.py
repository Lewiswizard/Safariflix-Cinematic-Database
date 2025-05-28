#Deletefilms
from connect import *
from readFilms import read
from time import sleep
# DELETE FROM films WHERE SongID = "id"

def delete():
	read()
	sure = False
	# while loop validation
	while sure == False:
		givenID = input("\nEnter the ID of the Film you'd Like to delete:\n")
		print(f"You've selected film of ID {givenID}.")
		confirm = input(f"Are you sure you want to Delete film {givenID}?\n")
		if confirm == "yes" or confirm == "y" or confirm == "Y":
			sure = True

	cursor.execute(f"DELETE FROM films WHERE FilmID = {givenID}")
	conn.commit()

	print(f"The film of ID {givenID} has been deleted.")
	sleep(2)
	read()

if __name__ == "__main__":
	delete()