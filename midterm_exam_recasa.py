import tkinter as tk
from tkenter import tk,messagebox
import sqlite3

conn = sqliite3.connect ("artist.db")
cursor= conn=cursor()

cursor.execute ("""
CREATE TABLE IF NOT EXIST artist (
id INTEGER PRIMARY KEY AUTONCREMENT,
name TEXT NOT NULL,
age INTEGER NOT NULL,
genre TEXT NOT NULL,

)
""")

com.commit()

#CREATE
def add_artist();
name =name_entry.get()
age=age_entry.get()
genre=genre_entry.get()

 if name=="" or age=="" or genre==":
 messagebox.showwarning(
  "warning",
  "plese fill in all fields."

  )
  return

try:
age= int(age)
except valueError:
    messagebox.showerror(

        "error",
        "Age must be a number"
    )
    return

cursor.execute(
    "INSERT INTO artist (name,age,genre) VALUES (???)",
    (name,age,genre)

    )
com.commit()







        





