from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
import tkinter as tk
import mysql.connector

mypass = "Soare141225"
mydatabase="db"

con = pymysql.connect( host="localhost",user="root",password=mypass,database=mydatabase)
current = con.cursor()

# Enter Table Names here
bookTable = "books"

def viewBooks():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.maxsize(width=800, height=800)
    root.geometry("800x800")
    root.resizable(False, False)

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#7E6551")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="black", bd=1)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Book list", bg='#466362', fg='white', font=('Times New Roman', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


    getBooks = "SELECT * FROM " + bookTable
    current.execute(getBooks)
    rows = current.fetchall()
    total = current.rowcount

    frm = Frame(root)
    frm.pack(side=tk.LEFT, padx=20, pady=20)
    frm.place(relx=0.18, rely=0.3)

    tv = ttk.Treeview(frm, columns=(1,2,3,4), show="headings", height="15")
    tv.pack()

    tv.heading(1, text="ID", anchor=CENTER)
    tv.heading(2, text="Name", anchor=CENTER)
    tv.heading(3, text="Author", anchor=CENTER)
    tv.heading(4, text="Type", anchor=CENTER)

    tv.column(1, width=30, anchor=CENTER)
    tv.column(2, width=200, anchor=CENTER)
    tv.column(3, width=170, anchor=CENTER)
    tv.column(4, width=100, anchor=CENTER)

    for i in rows:
        tv.insert('', 'end', values=i)

    quitBtn = Button(root, text="QUIT", bg='#466362', fg='white', relief='raised', command=root.destroy, font=('Times New Roman', 12))
    quitBtn.place(relx=0.4, rely=0.75, relwidth=0.18, relheight=0.08)

    root.mainloop()
