# utils.py
import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='adminelias',
        password='elias220',
        database='david'
    )
    return conn