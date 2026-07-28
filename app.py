import psycopg2
import os
from flask import Flask
app = Flask(__name__)

database_conn = os.environ.get("DATABASE_URL")
# conn = psycopg2.connect(database_conn)

@app.route('/')
def index():
    return 'Matthew Wermers: Render flask app for Software Dev'

@app.route('/db_test')
def db_test():
    try:
        conn = psycopg2.connect(database_conn)
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()

def try_function( function , data ):
    try:
        db_conn = psycopg2.connect(database_conn)
        cur = db_conn.cursor()

        #call function with data

        return "Function processed sucessfully"
    except Exception as e:
        if db_conn is not None:
            db_conn.rollback()
        return (f"Error {e}")
    finally:
        if cur is not None:
            cur.close()
        if db_conn is not None:
            db_conn.close()
