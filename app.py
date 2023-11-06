import psycopg2

from flask import Flask
app = Flask(__name__)

DATABASE_URL = 'postgres://flask_hello_world_fnxg_user:SqJ6U11VXSvKXrrYBAwNy1CZDYuwEo3x@dpg-cl42172uuipc738p5qk0-a/flask_hello_world_fnxg'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect(DATABASE_URL)
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
    );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Populated"

@app.route('/db_select')
def db_select():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Basketball;')
    data = cur.fetchall()
    conn.commit()
    conn.close()
    
     # Generate an HTML table
    table_html = "<table border='1'>"
    table_html += "<tr><th>First</th><th>Last</th><th>City</th><th>Name</th><th>Number</th></tr>"

    for row in data:
        table_html += "<tr>"
        for value in row:
            table_html += f"<td>{value}</td>"
        table_html += "</tr>"

    table_html += "</table>"
    return table_html

@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute('DROP TABLE Basketball;')
    conn.commit()
    conn.close()
    return "Basketball Table Dropped"