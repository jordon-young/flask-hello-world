import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://flask_hello_world_fnxg_user:SqJ6U11VXSvKXrrYBAwNy1CZDYuwEo3x@dpg-cl42172uuipc738p5qk0-a/flask_hello_world_fnxg")
    conn.close()
    return "Database Connection Successful"
