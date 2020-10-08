from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'python_api'

mysql = MySQL(app)

@app.route('/add_users' , methods=['POST'])
def add_users():
   
   details = request.form
   firstname = details['firstname']
   lastname = details['lastname']
   email = details['email']
   cur = mysql.connection.cursor()
   cur.execute("INSERT INTO users(firstname,lastname,email) VALUES (%s,%s,%s)",(firstname,lastname,email))
   mysql.connection.commit()
   cur.close()

   return 'Kullanıcı Eklendi'

