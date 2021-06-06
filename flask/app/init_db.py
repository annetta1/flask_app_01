import mysql.connector

conn  = mysql.connector.connect(
  host="localhost",
  user="root",
  password="_Pr0j3cT_"
)
#  database="db_posts"
cursor = conn.cursor()
cursor.execute("DROP database IF EXISTS db_posts")
cursor.execute("CREATE DATABASE db_posts")

conn.close()

conn  = mysql.connector.connect(
  host="localhost",
  user="root",
  password="_Pr0j3cT_", 
  database="db_posts"
)
cursor = conn.cursor()

def executeScriptsFromFile(filename):
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except IOError as msg:
            print ("Command skipped: ", msg)

executeScriptsFromFile('./app/schema.sql')




cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)",
            ('First Post', 'Content for the first post', ))

cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)",
            ('Second Post', 'Content for the second post', ))


conn.commit()
conn.close()


'''
import sqlite3
connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

connection.commit()
connection.close()
'''
