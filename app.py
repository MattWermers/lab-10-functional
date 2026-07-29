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

@app.route('/db_create')
def db_create():
    try:
        conn = psycopg.connect(database_conn)
        cur = conn.cursor()

        cur.execute('''
            CREATE TABLE IF NOT EXISTS Basketball (
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
        ''')

        conn.commit()
        conn.close()

        return "Basketball table created"
    except Exception as e:
        return f"Creation of Basketball table failed {e}"
    finally:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close()

@app.route('/db_insert')
def pop_basketball():
    try:
        conn = psycopg.connect(database_conn)
        cur = conn.cursor()

        cur.execute('''
            INSERT INTO Basketball (First, Last, City, Name, Number)
            SELECT * FROM (
                VALUES
                    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
                    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
                    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
                    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
                    ('Matt', 'Wermers', 'CU Boulder', 'CSPB', 3308)
                ) AS v(First, Last, City, Name, Number)
                EXCEPT
                SELECT First, Last, City, Name, Number FROM Basketball;
        ''')

        return "Basketball table populated"
    except Exception as e:
        return f"Population of Basketball table failed {e}"
    finally:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close()

@app.route('/db_select')
def selecting():
    try:
        conn = psycopg.connect(database_conn)
        cur = conn.cursor()

        cur.execute('''
            SELECT * FROM Basketball;
            ''')

        records = cur.fetchall()
        output = "<!DOCTYPE html><html><body><table border='1'><tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"
        output_row = ""
        for row in records:
            output_row += "<tr>"
            for attribute in row:
                output_row += f"<td>{attribute}</td>"
            output += output_row + "</tr>"
        output += "</table></body></html>"
        return output + "wth"
    except Exception as e:
        return f"Selecting from Basketball table failed {e}"
    finally:
        if conn is not None:
            conn.close()
        if cur is not None:
            cur.close()
