import os
import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Rachael Glazner in 3308'

@app.route("/db_test")
def db_test():
    DATABASE_URL = os.environ.get("DATABASE_URL")
    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()

@app.route("/db_create")
def creating():
    DATABASE_URL = os.environ.get("DATABASE_URL")
    conn = psycopg2.connect(DATABASE_URL)

    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball (
    First varchar(255),
    Last varchar(255),
    City varahcar(255),
    Name varchar(255),
    Number int
    );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"
@app.route("/db_insert")
def creating():
    DATABASE_URL = os.environ.get("DATABASE_URL")
    conn = psycopg2.connect(DATABASE_URL)

    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    VALUES
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
    ('Rachael', 'Glazner', 'CU Boulder', 'Buffs', 3308)
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"