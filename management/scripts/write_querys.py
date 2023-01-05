from mysqlconnector import sql_create_db_connection, execute_query

connection = sql_create_db_connection("localhost", "root", "Underw@ter", "vidly")

query = """
INSERT INTO movie_movie (title, imdbRating, genre_id, description, releaseDate, promoted) VALUES
('Raya and the Last Dragon', 8.00, 2, 'Long ago, in the fantasy world of Kumandra, humans and dragons lived together in harmony. But when sinister monsters known as the Druun threatened the land, the dragons sacrificed themselves to save humanity. Now, 500 years later, those same monsters have returned and it’s up to a lone warrior, Raya, to track down the last dragon in order to finally stop the Druun for good. However, along her journey, she’ll learn that it’ll take more than dragon magic to save the world—it’s going to take trust as well.', '2021-4-9', 0)
"""

query1 = """
INSERT INTO movie_genre (name) VALUES
('Action')
"""

execute_query(connection, query)
