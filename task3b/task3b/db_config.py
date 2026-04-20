import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="feedback_user",
        password="veera8432",
        database="feedback_db"
    )