from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'fadzni'
DB_HOST = 'localhost' 
DB_PORT = '5432'

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/hello/<name>')
def hello(name):
    # return f'Hello {name}!'
    return render_template('hello.html', name=name)

@app.route('/list_customer')
def list_customer():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()
    cur.execute('SELECT * from customer;')
    data = cur.fetchall()
    cur.close()
    # return version
    return render_template('display.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)