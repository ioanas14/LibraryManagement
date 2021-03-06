from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


def bookRegister():
    bid = bookID.get()
    title = bookTitle.get()
    author = bookAuthor.get()
    type = bookType.get()

    insertBooks = "INSERT INTO " + bookTable + " VALUES('" + bid + "','" + title + "','" + author + "','" + type + "')"
    try:
        current.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    print(bid)
    print(title)
    print(author)
    print(type)

    root.destroy()


def add_book():
    global bookID, bookTitle, bookAuthor, bookType, Canvas1, con, current, bookTable, root

    root = Toplevel()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.maxsize(width=800, height=800)
    root.geometry("800x800")
    root.resizable(False, False)

    bg = ImageTk.PhotoImage(file="lib.jpg")

    # Add your own database name and password here to reflect in the code
    mypass = "Soare141225"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    current = con.cursor()

    # Enter Table Names here
    bookTable = "books"  # Book Table

    Canvas2 = Canvas(root, bg='#7E6551')
    Canvas2.pack(expand=True, fill=BOTH)

    Canvas2.create_image(0, 0, image=bg, anchor="nw")

    headingFrame1 = Frame(root, bg="black", bd=1)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add a new book", bg='#466362', fg='white', font=('Times New Roman', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='#27130B')
    labelFrame.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.4)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='#27130B', fg='white', font=('Times New Roman', 15))
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    bookID = Entry(labelFrame)
    bookID.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Title
    lb2 = Label(labelFrame, text="Title : ", bg='#27130B', fg='white', font=('Times New Roman', 15))
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookTitle = Entry(labelFrame)
    bookTitle.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Book Author
    lb3 = Label(labelFrame, text="Author : ", bg='#27130B', fg='white', font=('Times New Roman', 15))
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    bookAuthor = Entry(labelFrame)
    bookAuthor.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Book Status
    lb4 = Label(labelFrame, text="Type (hardback/\npaperback): ", bg='#27130B', fg='white', font=('Times New Roman', 15))
    lb4.place(relx=0.05, rely=0.65, relheight=0.14)

    bookType = Entry(labelFrame)
    bookType.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#466362', fg='white', relief='raised', command=bookRegister, font=('Times New Roman', 13))
    SubmitBtn.place(relx=0.28, rely=0.7, relwidth=0.2, relheight=0.08)

    quitBtn = Button(root, text="QUIT", bg='#466362', fg='white', relief='raised', command=root.destroy, font=('Times New Roman', 13))
    quitBtn.place(relx=0.53, rely=0.7, relwidth=0.2, relheight=0.08)

    root.mainloop()