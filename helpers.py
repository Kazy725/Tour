import sqlite3
con = sqlite3.connect("tours.db", check_same_thread=False)
cur = con.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS tours (
id INTEGER PRIMARY KEY AUTOINCREMENT , 
name TEXT,
price INTEGER,   
description TEXT,
country TEXT,
category TEXT,
days INTEGER,
rate INTEGER
);''')
con.commit()

def get_tours():
    cur.execute('SELECT * FROM tours')
    return cur.fetchall()

def get_tour_covers():
    cur.execute('SELECT id, name FROM tours')
    return cur.fetchall()

def get_cover_by_id(tour_id):
    cur.execute(f'SELECT id, name FROM tours WHERE id = {tour_id}')
    return cur.fetchone()

def get_tour_by_id(tour_id):
    cur.execute(f'SELECT * FROM tours WHERE id = {tour_id}')
    return cur.fetchone()