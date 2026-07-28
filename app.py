import psycopg
import os
from flask import Flask
app = Flask(__name__)

database_conn = os.environ.get("DATABASE_URL")
# conn = psycopg.connect(database_conn)

@app.route('/')
def index():
    return 'Matthew Wermers: Render flask app for Software Dev'

@app.route('/db_test')
def db_test():
    try:
        conn = psycopg.connect(database_conn)
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()
