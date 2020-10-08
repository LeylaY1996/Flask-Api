from flask import Flask, request
from flask_mysqldb import MySQL
from flask import jsonify,json # <- `jsonify` instead of `json`


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'python_api'

mysql = MySQL(app)

@app.route('/add_user' , methods=['POST'])

def add_user():

   details = request.form
   firstname = details['firstname']
   lastname = details['lastname']
   email = details['email']
   cur = mysql.connection.cursor()
   cur.execute("INSERT INTO users(firstname,lastname,email) VALUES (%s,%s,%s)",(firstname,lastname,email))
   mysql.connection.commit()
   cur.close()

   return 'Kullanıcı Eklendi'

@app.route('/get_users', methods=['GET'])

def get_users():

   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM users")
   rows = jsonify(cur.fetchall())
   return rows

@app.route('/get_user/<id>')
def get_user(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id=%s", id)
    rows = jsonify(cur.fetchone())
    return rows

@app.route('/update_user', methods=['POST'])
def update_user():
   
   details = request.form
   _id = details['id']
   firstname = details['firstname']
   lastname = details['lastname']
   email = details['email']
   cur = mysql.connection.cursor()
   cur.execute("UPDATE users(firstname,lastname,email) VALUES (%s,%s,%s)",(firstname,lastname,email))
   mysql.connection.commit()
   cur.close()
