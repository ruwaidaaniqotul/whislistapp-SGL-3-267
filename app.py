import sqlite3 as lite
from flask import Flask, render_template, url_for, redirect, request, session

app = Flask(__name__)

@app.route("/")
def main():
    #return "Welcome!"
    return render_template('index.html')

@app.route('/carlist')
def carlist():
    con = lite.connect("app4.db")
    con.row_factory=lite.Row

    cur = con.cursor()
    cur.execute( "select * from Cars")

    rows = cur.fetchall();
    con.close()
    return render_template('carlist.html', rows = rows)

@app.route('/insertcar')
def insertcar():
    return render_template('insertcar.html')

@app.route('/showsignin')
def showsignin():
    return render_template('signin.html')

@app.route('/savecar', methods=['GET' , 'POST'])
def savecar():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        price = request.form['price']

        con = lite.connect('app4.db')

        with con:

            cur = con.cursor()
            cur.execute("INSERT INTO Users VALUES(?, ?, ?)",(id,name,price))
            con.commit()

    return redirect(url_for('carlist'))

@app.route('/deletecar')
def deletecar():
    con = lite.connect("app4.db")
    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("select id from Cars")

    rows = cur.fetchall();
    con.close()
    return render_template("deletecar.html",rows = rows)

@app.route('/deluser/<int:idcar>', methods=['GET' , 'POST'])
def deluser(idcar):
    try:
        idcar = str(idcar)
        con = lite.connect('app4.db')
        cur = con.cursor()

        with con:
            cur.execute("DELETE FROM  Cars WHERE Id=(?)",[idcar])
            con.commit()

        return redirect(url_for('carlist'))

    except:
        return redirect(url_for('carlist'))


@app.route('/username')
def username():
    con = lite.connect("app4.db")
    con.row_factory=lite.Row

    cur = con.cursor()
    cur.execute( "select * from Users")

    rows = cur.fetchall();
    con.close()
    return render_template('user1.html', rows = rows)

@app.route('/insertuser')
def insertuser():
        return render_template('insertuser.html')

@app.route('/saveuser', methods=['GET' , 'POST'])
def saveuser():
    if request.method == 'POST':
        id = request.form['id']
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        gender = request.form['gender']

        con = lite.connect('app4.db')

        with con:

            cur = con.cursor()
            cur.execute("INSERT INTO Users VALUES(?, ?, ?, ?, ?, ?, ?)",(id,username,password,first_name,last_name,email,gender))
            con.commit()

    return redirect(url_for('username'))

@app.route('/deleteuser')
def deleteuser():
    con = lite.connect("app4.db")
    con.row_factory = lite.Row

    cur = con.cursor()
    cur.execute("select id from Users")

    rows = cur.fetchall();
    con.close()
    return render_template("deleteuser.html",rows = rows)

@app.route('/delete', methods=['GET' , 'POST'])
def delete():
    if request.method == 'POST':
        id = request.form['id']

        con = lite.connect('app4.db')
        cur = con.cursor()

        with con:
            cur.execute("DELETE FROM  Users WHERE Id=(?)",[id])
            con.commit()

    return redirect(url_for('username'))

@app.route("/")
def main():
    if 'username' in seassion:
        username_session = session['username']
        #print(session['username'], file=sys.stderr)
        return render_template('home.html', session_user_name=username_session)
    else:
        return render_template('index.html')

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('main'))

@app.route("/gosignin/", methods=['GET','POST'])
def gosignin():
    Error=""
    if request.method =='POST':
        username_form = request.form['username']
        password_form = request.form['password']

        con = lite,connect('app4.db')
        cur = con.cursor()
        cur.execute("SELECT CONT(1) FROM Users where usernaame = (?)", [username_form])
        if cur.fetchone()[0]:
            cur.execute("SELECT password FROM Users where username(?)", [username_form])
            for row in cur.fetchall():
                if password_form == row[0]:
                    session['username'] = request.form['username']
                    print(request.form['username'], file=sys.stderr)
                    print(session['username'],file=sys.stderr)

                    #return redirect(url_for('main'))
                    return redirect(url_for('index')) #study? uncoment here
                else:
                    error ="Invalid Credential"
        else:
            error ="Invalid Credential"
    return render_template('signin.html', error=error)

app.secret_key ='aidapao'

if __name__ == "__main__":
    app.run(debug="True")
