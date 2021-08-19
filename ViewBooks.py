from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

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

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#7E6551")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="black", bd=1)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Book list", bg='#466362', fg='white', font=('Times New Roman', 15))

    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s %-40s %-30s %-20s" % ('ID', 'Title', 'Author', 'Type'),
          bg='black', fg='white', font=('Times New Roman', 11)).place(relx=0.05, rely=0.1)

    Label(labelFrame, text="-------------------------------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from " + bookTable
    try:
        current.execute(getBooks)
        con.commit()

        for i in current:
            # i[0] = book id, i[1] = title, i[2] = author, i[3] = type
            Label(labelFrame, text="%-10s %-40s %-30s %-20s" % (i[0], i[1], i[2], i[3]), bg='black', fg='white',
                  font=('Times New Roman', 11)).place(relx=0.05, rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quitBtn = Button(root, text="QUIT", bg='#466362', fg='white', relief='raised', command=root.destroy, font=('Times New Roman', 10))
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
