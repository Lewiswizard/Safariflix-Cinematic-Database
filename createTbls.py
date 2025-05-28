#createTbls
from connect import *

cursor.execute(
"""
CREATE TABLE "film"(
	"FilmID"	INTEGER NOT NULL UNIQUE,
	"Title" TEXT,
	"Year" INT,
	"Rating" TEXT,
	"Duration" INT,
	"Genre" TEXT,
	PRIMARY KEY("FilmID" AUTOINCREMENT)
)
"""
)

