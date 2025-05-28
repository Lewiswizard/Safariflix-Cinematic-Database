#updateFilms
from connect import *
from readFilms import read
from time import sleep


def update():
    # Taken the ID
    givenID = input("Enter the ID of the Film you'd like to update:\n")
    title = input("Enter new title: ")
    year = input("Enter new Year: ")
    rating = input("Enter new Film Rating: ")
    duration = input("Enter new Film Duration: ")
    genre = input("Enter new Genre: ")

    # Update SQL Statement
    cursor.execute(
        f"""
		UPDATE film
		SET Title = "{title}", Year = "{year}", Rating = "{rating}", Duration = "{duration}", Genre = "{genre}"
		WHERE FilmID = {givenID}
		;
		"""

    )
    conn.commit()

    print(f"Film ID {givenID} has been successfully updated.")
    sleep(2)
    read()


if __name__ == "__main__":
    update()
