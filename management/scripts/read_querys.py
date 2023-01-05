from mysqlconnector import sql_create_db_connection, read_query, print_outputfile
import pandas

extract_genre = """
SELECT * FROM movie_genre
"""

extract_movie = """
SELECT * FROM movie_movie
"""

extract_movieposter = """
SELECT * FROM movie_movieposter
"""

connection = sql_create_db_connection("localhost", "root", "Underw@ter", "vidly")


genres = read_query(connection, extract_genre)
movies = read_query(connection, extract_movie)
movie_posters = read_query(connection, extract_movieposter)


print_outputfile("genres", genres)
print_outputfile("movies", movies)
print_outputfile("movie_posters", movie_posters)
