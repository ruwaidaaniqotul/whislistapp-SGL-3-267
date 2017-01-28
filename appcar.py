import sqlite3 as lite
from flask import Flask, render_template, url_for, redirect, request

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

@app.route('/deluser', methods=['GET' , 'POST'])
def deluser():
    if request.method == 'POST':
        id = request.form['id']

        con = lite.connect('app4.db')
        cur = con.cursor()

        with con:
            cur.execute("DELETE FROM  Users WHERE Id=(?)",[id])
            con.commit()

    return redirect(url_for('carlist'))

if __name__ == "__main__":
    app.run(debug="True")
