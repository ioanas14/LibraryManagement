from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


def bookRegister():
    bid = bookID.get()
    title = bookTitle.get()
    author = bookAuthor.get()
    type = bookType.get()

    insertBooks = "insert into " + bookTable + " values('" + bid + "','" + title + "','" + author + "','" + type + "')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    print(bid)
    print(title)
    print(author)
    print(type)

    root.destroy()


def addBook():
    global bookID, bookTitle, bookAuthor, bookType, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.maxsize(width=800, height=800)
    root.geometry("800x800")

    # Add your own database name and password here to reflect in the code
    mypass = "Soare141225"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books"  # Book Table

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add a new book", bg='black', fg='white', font=('Times New Roman', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white', font=('Times New Roman', 10))
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    bookID = Entry(labelFrame)
    bookID.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Title
    lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white', font=('Times New Roman', 10))
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookTitle = Entry(labelFrame)
    bookTitle.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Book Author
    lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white', font=('Times New Roman', 10))
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    bookAuthor = Entry(labelFrame)
    bookAuthor.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Book Status
    lb4 = Label(labelFrame, text="Type (hardback/paperback): ", bg='black', fg='white', font=('Times New Roman', 10))
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    bookType = Entry(labelFrame)
    bookType.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=bookRegister, font=('Times New Roman', 10))
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy, font=('Times New Roman', 10))
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()