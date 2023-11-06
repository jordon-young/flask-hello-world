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
    # cur = conn.cursor()
    # cur.execute('''
    # CREATE TABLE IF NOT EXISTS Basketball(
    #     First varchar(255),
    #     Last varchar(255),
    #     City varchar(255),
    #     Name varchar(255),
    #     Number int
    # );
    # ''')
    # cur.commit()
    conn.close()
    return "Basketball Table Successfully Created"


