import psycopg2
from config import DATABASE_NAME, DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT


conn = psycopg2.connect(f"dbname={DATABASE_NAME} user={DATABASE_USER} host={DATABASE_HOST} password={DATABASE_PASSWORD}")
cur = conn.cursor()
