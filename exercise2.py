import sqlite3

file_path = r"D:\exercise2\stephen_king_adaptations.txt"
stephen_king_adaptations_list = []

with open(file_path, "r") as file:
    for line in file:
        movie_info = line.strip().split(",")
        stephen_king_adaptations_list.append(movie_info)

# Connect to a SQLite database
conn = sqlite3.connect("stephen_king_adaptations.db")
cursor = conn.cursor()

# Create the table
cursor.execute("CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (movieID TEXT, movieName TEXT, movieYear INTEGER, imdbRating REAL)")
for movie in stephen_king_adaptations_list:
    cursor.execute("INSERT INTO stephen_king_adaptations_table (movieID, movieName, movieYear, imdbRating) VALUES (?, ?, ?, ?)", movie)

conn.commit()


while True:
    print("What do you want to search for movies based on? Here are some options:")
    print("1. Movie name")
    print("2. Movie year")
    print("3. Movie rating")
    print("4. STOP")
    selection = input("Please enter your selection: ")

    if selection == "1":
        movie_name = input("Please enter the movie name you want to search for: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName=?", (movie_name,))
        result = cursor.fetchall()
        if result:
            for movie in result:
                print("movieID:", movie[1])
                print("movieYear:", movie[2])
                print("imdbRating:", movie[3])
        else:
            print("No such movie exists in our database")

    elif selection == "2":
        movie_year = input("Please enter the movie year you want to search for: ")
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear=?", (movie_year,))
        result = cursor.fetchall()
        if result:
            for movie in result:
                print("movieID:", movie[1])
                print("movieYear:", movie[2])
                print("imdbRating:", movie[3])
        else:
            print("No movies were found for that year in our database.")

    elif selection == "3":
        movie_rating = float(input("Please enter the rating of the movie you want to search for: "))
        cursor.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating>=?", (movie_rating,))
        result = cursor.fetchall()
        if result:
            for movie in result:
                print("movieID:", movie[1])
                print("movieYear:", movie[2])
                print("imdbRating:", movie[3])
        else:
            print("No movies at or above that rating were found in the database.")

    elif selection == "4":
        break

# Close the database Connection
conn.close()