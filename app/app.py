from flask import Flask,render_template,redirect,request

import os
from flaskext.mysql import MySQL
import pymysql
from flask import jsonify

app = Flask(__name__)

mysql = MySQL()

mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ['MYSQL_DATABASE_HOST'] or  'localhost'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'student'
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_PORT']=int('3306')
mysql.init_app(app)


@app.route("/")
def welcome():
    
    return render_template('welcome.html')

    
@app.route('/check vaccination status', methods=['GET', 'POST'])
def check_status():
    if request.method == 'POST':
        # Fetch form data
        
        userDetails = request.form
        regno = userDetails['RegNo']
        search=request.form['RegNo']
        conn = mysql.connect()

        cursor = conn.cursor(pymysql.cursors.DictCursor)
        global rid

        rid=request.form.get("RegNo")
        cursor.execute("SELECT * FROM vacdetails where RegNo=%s",rid)
    
        dets= cursor.fetchone()
        
        res=[]
        res.append(dets)
        
       
        
        return redirect('/show result')
    return render_template('index.html')


@app.route('/read from database')
def read():
    conn = mysql.connect()

    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM vacdetails ")
    row = cursor.fetchone()
    result = []
    while row is not None:
      row = cursor.fetchone()
      result.append(row)

      return ','.join(str(result)[1:-1])
    #   for column in row:
    #       result.append(column)
     
      
    cursor.close()
    conn.close()
    
    # return ','.join(','.join(map(str, l)) for l in result)
    return ",".join(result)

@app.route('/show result')
def result():
    conn = mysql.connect()
    

    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM vacdetails where RegNo=%s",rid)

    rows = cursor.fetchall()

    resp = jsonify(rows)
    resp.status_code = 200
    cursor.close()
    conn.close()

    return render_template('details.html',rows=rows)

@app.route('/all users')
def users():
    conn = mysql.connect()

    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM vacdetails")

    rows = cursor.fetchall()

    allusers = jsonify(rows)
    allusers.status_code = 200
    cursor.close()
    conn.close()

    return render_template('details.html',rows=rows)
if __name__ == "__main__":
        app.run(debug=True,host='0.0.0.0')

