from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
import tkinter as tk
import mysql.connector

mypass = "Soare141225"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
current = con.cursor()

# Enter Table Names here
bookTable = "books"


def view_books():
    root = Toplevel()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.maxsize(width=800, height=800)
    root.geometry("800x800")
    root.resizable(False, False)

    bg = ImageTk.PhotoImage(file="lib.jpg")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#7E6551")
    Canvas1.pack(expand=True, fill=BOTH)

    Canvas1.create_image(0, 0, image=bg, anchor="nw")

    headingFrame1 = Frame(root, bg="black", bd=1)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Book list", bg='#AE6832', fg='white', font=('Times New Roman', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


    try:
        getBooks = "SELECT * FROM " + bookTable
        current.execute(getBooks)
        rows = current.fetchall()
        total = current.rowcount

        frm = Frame(root)
        frm.pack(side=tk.LEFT, padx=20, pady=20)
        frm.place(relx=0.18, rely=0.3)

        style = ttk.Style()
        style.configure("Treeview",
                        background="#AE6832",
                        foreground="black",


                        )
        

        bookTree = ttk.Treeview(frm, columns=(1, 2, 3, 4), show="headings", height="15")
        bookTree.pack()

        bookTree.heading(1, text="ID", anchor=CENTER)
        bookTree.heading(2, text="Name", anchor=CENTER)
        bookTree.heading(3, text="Author", anchor=CENTER)
        bookTree.heading(4, text="Type", anchor=CENTER)

        bookTree.column(1, width=30, anchor=CENTER)
        bookTree.column(2, width=200, anchor=CENTER)
        bookTree.column(3, width=170, anchor=CENTER)
        bookTree.column(4, width=100, anchor=CENTER)

        for i in rows:
            bookTree.insert('', 'end', values=i)
    except:
        messagebox.showinfo("Couldn't fetch database information.")

    quitBtn = Button(root, text="QUIT", bg='#466362', fg='white', relief='raised', command=root.destroy,
                     font=('Times New Roman', 12))
    quitBtn.place(relx=0.4, rely=0.75, relwidth=0.18, relheight=0.08)

    root.mainloop()
