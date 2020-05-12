from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#mysqlconnect
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'rivwox'
app.config['MYSQL_PASSWORD'] = 'pepe1pass'
app.config['MYSQL_DB'] = 'uss'

mydb = MySQL(app)

# settings
app.secret_key = 'mysecretkey'


@app.route('/')
def Index():
    cur = mydb.connection.cursor() #do the connection
    cur.execute('SELECT * FROM us1') #do the query
    dat = cur.fetchall() #excute ##obtener todo
    return render_template('index.html', data = dat)

@app.route('/add_contact', methods=['POST'])
def AddContact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        # print(fullname)
        # print(phone)
        # print(email)
        cur = mydb.connection.cursor() #do the connection
        #write data into table
        cur.execute('INSERT INTO us1 (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        #execute the query
        mydb.connection.commit()
        flash('Contact added')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mydb.connection.cursor()
    cur.execute('DELETE FROM us1 WHERE id = {0}'.format(id)) #borra de us1 el dato de id que te estoy pasando
    mydb.connection.commit() #execute
    flash('Contact deleted')
    return redirect(url_for('Index'))

@app.route('/edit/<id>')
def get_contact(id):
    cur = mydb.connection.cursor()
    cur.execute('SELECT * FROM us1 WHERE id = %s',(id))
    dat = cur.fetchall()
    return render_template('edit.html', data = dat[0])

@app.route('/update/<id>',methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mydb.connection.cursor()
        cur.execute(""" 
            UPDATE us1
            SET fullname = %s,
                phone = %s,
                email = %s
            WHERE id = %s
        """, (fullname,phone,email,id))
        mydb.connection.commit()
        flash('Contact updated')
        return redirect(url_for('Index'))
if __name__ == '__main__':
    app.run(port = 3000, debug = True)