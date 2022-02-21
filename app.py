
from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    connection = sqlite3.connect('database.db') #mi connetto al database
    connection.row_factory = sqlite3.Row #database organizzato in righe cosi
    posts= connection.execute('SELECT * FROM posts').fetchall() #serve per prendere tutte le righe dalla tabella posts e fetchall organizza le righe in lista
    connection.close()
    return render_template('index.html', posts = posts)

@app.route('/<int:idx>/delete', methods=('POST',))
def delete(idx): #i parametri devono essere uguali
    connection = sqlite3.connect('database.db') #mi connetto al database
    connection.row_factory = sqlite3.Row #database organizzato in rig
    connection.execute('DELETE FROM posts WHERE id=?', (idx,)) #eseguo la cancellazione
    connection.commit()
    connection.close()
    return redirect('/')

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        titolo= request.form['titolo']
        info = request.form['info']
        connection = sqlite3.connect('database.db') #mi connetto al database
        connection.row_factory = sqlite3.Row #database organizzato in rig
        connection.execute(
            'INSERT INTO posts (titolo, info) VALUES (?, ?)',
            (titolo, info)
        )
        connection.commit()
        connection.close()
        return redirect ('/')
    return render_template('create.html')

