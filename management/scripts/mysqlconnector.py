import mysql.connector
from mysql.connector import Error
import os


def sql_create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name, user=user_name, passwd=user_password
        )
        print("MYSQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def sql_create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name, user=user_name, passwd=user_password, database=db_name
        )
        print("MYSQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()

    try:
        print("Executing queries")
        cursor.execute(query)
        connection.commit()
        print("query successful")
    except Error as err:
        print(f"Error: {err}")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None

    try:
        print("Executing queries")
        cursor.execute(query)
        result = cursor.fetchall()
        print("query successful")
        return result
    except Error as err:
        print(f"Error: '{err}'")


def execute_list_query(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def print_outputfile(filename, data):
    print("Writing to outfile")

    filename = f"scripts/data/{filename}"
    file = open(f"{os.path.join(os.getcwd(), filename)}.txt", "w")
    for item in data:
        file.write(f"{item},\n")
    file.close()

    print("Success")
