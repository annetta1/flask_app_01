from app import app
from flask_mysqldb import MySQL 
import MySQLdb.cursors
#import sqlite3
import os.path
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

mysql = MySQL(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'roott' #'_Pr0j3cT_'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_DB'] = 'db_posts'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_PORT'] = 3306

def get_db_connection():
    conn = mysql.connection.cursor()
    return conn


def get_post(post_id):
    cursor = get_db_connection()
    cursor.execute("SELECT * FROM posts WHERE id = %s",(post_id,))
    post = cursor.fetchone()
    cursor.close()

    if post is None:
        abort(404)
    return post


@app.route('/')
def index():
    cursor = get_db_connection()
    cursor.execute('SELECT * FROM posts')
    posts = cursor.fetchall()
    cursor.close()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            cursor = get_db_connection()
            cursor.execute('INSERT INTO posts (title, content) VALUES (%s, %s)', (title, content, ))
            mysql.connection.commit()          
            cursor.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            cursor = get_db_connection()
            cursor.execute('UPDATE posts SET title = %s, content = %s'
                         ' WHERE id = %s',(title, content, id, ))
            mysql.connection.commit()           
            cursor.close()
            
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    cursor = get_db_connection()   
    cursor.execute('DELETE FROM posts WHERE id = %s', (id,))
    mysql.connection.commit()           
    cursor.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

