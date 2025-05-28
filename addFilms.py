#addFilms
from connect import *
from readFilms import read
from time import sleep


def insertFilms():		
    myFilm = []
    title = input("Enter a Film Title: ")
    year = input("Enter a Film Year: ")
    rating = input("Enter a Film Rating: ")
    duration = input("Enter a Film Duration: ")
    genre = input("Enter the Genre of the film: ")

    myFilm.append(title)
    myFilm.append(year)
    myFilm.append(rating)
    myFilm.append(duration)
    myFilm.append(genre)

    print(myFilm)
    cursor.execute(
        f"""
	INSERT INTO film VALUES(NULL, "{myFilm[0]}", "{myFilm[1]}", "{myFilm[2]}", "{myFilm[3]}", "{myFilm[4]}")
	"""
    )
    conn.commit()
    print(f"{title}, has been added successfully to the database.")
    sleep(3)
    read()


if __name__ == "__main__":
    insertFilms()
