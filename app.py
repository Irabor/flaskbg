#!/usr/bin/env python
from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def home():
    my_db = sqlite3.connect('post.db')
    try:
        my_db.execute('CREATE TABLE anons(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, posts TEXT NOT NULL);')
        my_db.commit()
    except sqlite3.OperationalError:
        pass
    cursor = my_db.cursor()
    if request.method == 'POST':
        post = request.form['body']
        my_db.execute('INSERT INTO anons(posts) VALUES( ?)', (post,))
        my_db.commit()
        entry = cursor.execute('SELECT ID, posts FROM anons')
        return render_template('index.html', posts = entry)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
